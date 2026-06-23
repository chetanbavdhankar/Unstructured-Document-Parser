"""Merge engine — upserts parsed fragments into ModelDossier instances.

All intelligence about *how models relate across files* lives here.
Parsers are source-specific and dumb; they only produce fragments keyed by id.
"""

from __future__ import annotations

import logging

from pipeline.models import Metric, ChangeRequest, ModelDossier
from pipeline.id_resolver import IDResolver

logger = logging.getLogger(__name__)

# Maps Excel domain names to the ModelDossier attribute they populate
DOMAIN_TO_ATTRIBUTE = {
    "performance": "performance_kpis",
    "backtesting": "backtesting_kpis",
    "data_quality": "data_quality_kpis",
    "coverage":    "coverage_kpis",
    "governance":  "governance_kpis",
}

# Sheets that populate special lists (from Issue_Tracking/DQ_Issue_Log)
ISSUE_SHEET_MAP = {
    "Issue_Tracking":        "mrm_issues",
    "DQ_Issue_Log":          "dq_issues",
    "Tuning_Recommendations": "tuning_recommendations",
}


class MergeEngine:
    """Merges all parsed fragments into a dict of ModelDossier instances."""

    def __init__(self, resolver: IDResolver) -> None:
        self.resolver = resolver
        self.dossiers: dict[str, ModelDossier] = {}

    def _get_or_create(self, model_id: str) -> ModelDossier:
        """Fetch or create a dossier for the given canonical model_id."""
        if model_id not in self.dossiers:
            metadata = self.resolver.get_metadata(model_id)
            self.dossiers[model_id] = ModelDossier(
                model_id=model_id,
                model_code=metadata.get("model_code", ""),
            )
        return self.dossiers[model_id]

    # ── Structured metrics ────────────────────────────────────────────────

    def upsert_metrics(
        self,
        domain: str,
        fragments: dict[str, list[Metric]],
    ) -> None:
        """Upsert structured metric fragments from an Excel domain.

        Args:
            domain: one of "performance", "backtesting", "data_quality",
                    "coverage", "governance"
            fragments: dict of raw_model_id → list[Metric]
        """
        attr_name = DOMAIN_TO_ATTRIBUTE.get(domain)
        if not attr_name:
            logger.warning("Unknown domain '%s', skipping", domain)
            return

        resolved = 0
        failed = 0

        for raw_id, metrics in fragments.items():
            try:
                canonical = self.resolver.resolve(raw_id)
            except Exception as e:
                logger.warning("Skipping unresolvable ID '%s': %s", raw_id, e)
                failed += 1
                continue

            dossier = self._get_or_create(canonical)
            target_list: list[Metric] = getattr(dossier, attr_name)
            target_list.extend(metrics)
            resolved += 1

        logger.info("Upserted domain '%s': %d models resolved, %d failed",
                    domain, resolved, failed)

    # ── Issue / recommendation metrics (from mixed sheets) ────────────────

    def upsert_issues(
        self,
        sheet_name: str,
        issues: list[dict],
    ) -> None:
        """Upsert model-level issues from Issue_Tracking or DQ_Issue_Log sheets.

        Args:
            sheet_name: the sheet name (used to route to the right attribute)
            issues: list of dicts with at minimum a 'model' key
        """
        attr_name = ISSUE_SHEET_MAP.get(sheet_name)
        if not attr_name:
            logger.warning("Unknown issue sheet '%s', skipping", sheet_name)
            return

        source_tag = sheet_name
        for issue in issues:
            raw_model_id = issue.get("model", "")
            try:
                canonical = self.resolver.resolve(raw_model_id)
            except Exception:
                # This issue doesn't map to a model — it's estate-level
                continue

            dossier = self._get_or_create(canonical)
            target_list: list[Metric] = getattr(dossier, attr_name)

            # Serialize issue dict as a Metric for uniform handling
            description = " | ".join(
                f"{k}: {v}" for k, v in issue.items() if k != "model"
            )
            target_list.append(
                Metric(name=sheet_name, value=description, source=source_tag)
            )

    # ── Prose: FRD sections ───────────────────────────────────────────────

    def upsert_frd_sections(self, sections: dict[str, str]) -> None:
        """Upsert FRD/BRD prose sections.

        Args:
            sections: dict of "Model N" → verbatim prose content
        """
        for raw_id, prose in sections.items():
            try:
                canonical = self.resolver.resolve(raw_id)
            except Exception as e:
                logger.warning("Skipping FRD section for '%s': %s", raw_id, e)
                continue

            dossier = self._get_or_create(canonical)
            dossier.functional_requirements = prose

        logger.info("Upserted FRD sections for %d models", len(sections))

    # ── Prose: Change Requests ────────────────────────────────────────────

    def upsert_change_requests(
        self,
        model_crs: dict[str, list[ChangeRequest]],
    ) -> None:
        """Upsert Change Request prose.

        Args:
            model_crs: dict of "Model N" → list[ChangeRequest]
        """
        for raw_id, crs in model_crs.items():
            try:
                canonical = self.resolver.resolve(raw_id)
            except Exception as e:
                logger.warning("Skipping CRs for '%s': %s", raw_id, e)
                continue

            dossier = self._get_or_create(canonical)
            dossier.change_requests.extend(crs)

        total = sum(len(v) for v in model_crs.values())
        logger.info("Upserted %d CRs across %d models", total, len(model_crs))

    # ── Estate context per model ──────────────────────────────────────────

    def attach_sampling_methodology(
        self,
        family_methods: dict[str, str],
    ) -> None:
        """Attach family-level sampling methodology to each model in that family.

        Args:
            family_methods: dict of family_name → methodology description
        """
        for model_id in self.resolver.all_model_ids():
            family = self.resolver.get_family(model_id)
            if family in family_methods:
                dossier = self._get_or_create(model_id)
                dossier.sampling_methodology = family_methods[family]

    def attach_coverage_gaps(
        self,
        gaps: list[dict],
    ) -> None:
        """Attach relevant coverage gaps to models based on typology/segment/family match."""
        for model_id in self.resolver.all_model_ids():
            metadata = self.resolver.get_metadata(model_id)
            family = metadata.get("family", "")
            typology = metadata.get("typology", "")

            dossier = self._get_or_create(model_id)
            for gap in gaps:
                gap_text = str(gap.get("typology_segment", "")).lower()
                gap_desc = str(gap.get("description", "")).lower()
                combined = gap_text + " " + gap_desc

                if (family.lower() in combined or
                    typology.lower() in combined):
                    dossier.relevant_coverage_gaps.append(gap)

    # ── Finalize: explicit absence markers ────────────────────────────────

    def finalize(self) -> None:
        """Post-merge pass: ensure every model in the registry has a dossier,
        and mark explicit absence where data is missing.

        Silent omission invites hallucination; an explicit null suppresses it.
        """
        for model_id in self.resolver.all_model_ids():
            dossier = self._get_or_create(model_id)

            # Prose fields already default to "<not provided>"
            # Change requests: if none, leave empty list (serializer will note absence)

        logger.info("Finalized %d dossiers", len(self.dossiers))

    def get_all_dossiers(self) -> dict[str, ModelDossier]:
        """Return all dossiers keyed by canonical model_id."""
        return dict(sorted(
            self.dossiers.items(),
            key=lambda x: int(x[0].split()[-1])
        ))
