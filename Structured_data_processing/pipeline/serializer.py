"""Serializer — converts ModelDossier into LLM-ready text.

Serializes each dossier so the LLM can distinguish hard metrics from
subjective text.  Structured blocks and prose blocks are wrapped in
clearly labelled, separable XML-style tags.

The tagging is what lets the insight prompt reason over "the numbers"
and "the design intent" as distinct things.
"""

from __future__ import annotations

import json
import logging
from pathlib import Path

from pipeline.models import ModelDossier, Metric, EstateDossier

logger = logging.getLogger(__name__)


def _metrics_to_table(metrics: list[Metric]) -> str:
    """Render a list of Metrics as a markdown table."""
    if not metrics:
        return "    No data available.\n"

    lines = [
        "    | Metric | Value | Source |",
        "    |--------|-------|--------|",
    ]
    for m in metrics:
        val = m.value if m.value is not None else "—"
        lines.append(f"    | {m.name} | {val} | {m.source} |")

    return "\n".join(lines) + "\n"


def serialize_dossier_xml(dossier: ModelDossier) -> str:
    """Serialize a single ModelDossier to XML-tagged format.

    This is the primary serialization for LLM consumption.
    One serialized dossier = one LLM call's user content.
    """
    parts: list[str] = []

    # Header
    parts.append(f'<model id="{dossier.model_id}" code="{dossier.model_code}">')
    parts.append("")

    # ── Structured metrics ────────────────────────────────────────────────
    parts.append("<structured_metrics>")

    for domain_name, metrics in dossier.all_metric_domains().items():
        if not metrics:
            continue
        parts.append(f'  <domain name="{domain_name}">')
        parts.append(_metrics_to_table(metrics))
        parts.append("  </domain>")
        parts.append("")

    parts.append("</structured_metrics>")
    parts.append("")

    # ── Functional requirements (prose — verbatim) ────────────────────────
    parts.append("<functional_requirements>")
    parts.append(dossier.functional_requirements)
    parts.append("</functional_requirements>")
    parts.append("")

    # ── Change requests (prose — verbatim) ────────────────────────────────
    parts.append("<change_requests>")
    if dossier.change_requests:
        for cr in dossier.change_requests:
            parts.append(f'  <cr id="{cr.cr_id}" source="{cr.source}">')
            parts.append(cr.prose)
            parts.append("  </cr>")
            parts.append("")
    else:
        parts.append("  <not provided>")
    parts.append("</change_requests>")
    parts.append("")

    # ── Estate context ────────────────────────────────────────────────────
    parts.append("<estate_context>")

    parts.append("  <sampling_methodology>")
    parts.append(f"    {dossier.sampling_methodology}")
    parts.append("  </sampling_methodology>")
    parts.append("")

    if dossier.relevant_coverage_gaps:
        parts.append("  <relevant_coverage_gaps>")
        for gap in dossier.relevant_coverage_gaps:
            gap_str = " | ".join(f"{k}: {v}" for k, v in gap.items())
            parts.append(f"    - {gap_str}")
        parts.append("  </relevant_coverage_gaps>")
    else:
        parts.append("  <relevant_coverage_gaps>None identified</relevant_coverage_gaps>")
    parts.append("")

    parts.append("</estate_context>")
    parts.append("")

    parts.append("</model>")

    return "\n".join(parts)


def serialize_estate_dossier(estate: EstateDossier) -> str:
    """Serialize the estate-wide dossier for LLM estate-level context."""
    parts: list[str] = []

    parts.append("<estate_dossier>")
    parts.append("")

    # Coverage gaps
    parts.append("<coverage_gaps>")
    if estate.coverage_gaps:
        parts.append("  | Gap ID | Typology/Segment | Description | Severity | Owner |")
        parts.append("  |--------|------------------|-------------|----------|-------|")
        for gap in estate.coverage_gaps:
            parts.append(
                f"  | {gap.get('gap_id', '—')} "
                f"| {gap.get('typology_segment', gap.get('typology_/_segment', '—'))} "
                f"| {gap.get('description', gap.get('gap_description', '—'))} "
                f"| {gap.get('severity', '—')} "
                f"| {gap.get('remediation_owner', '—')} |"
            )
    else:
        parts.append("  No coverage gaps identified.")
    parts.append("</coverage_gaps>")
    parts.append("")

    # Sampling methodology
    parts.append("<sampling_methodology>")
    for sm in estate.sampling_methodology:
        parts.append(f"  - {sm.get('family', '—')}: {sm.get('methodology', '—')}")
    parts.append("</sampling_methodology>")
    parts.append("")

    # Unrouted issues
    if estate.unrouted_dq_issues:
        parts.append("<unrouted_dq_issues>")
        for issue in estate.unrouted_dq_issues:
            parts.append(f"  - {issue}")
        parts.append("</unrouted_dq_issues>")
        parts.append("")

    if estate.unrouted_mrm_issues:
        parts.append("<unrouted_mrm_issues>")
        for issue in estate.unrouted_mrm_issues:
            parts.append(f"  - {issue}")
        parts.append("</unrouted_mrm_issues>")
        parts.append("")

    # Generic references
    parts.append("<generic_references>")
    for ref in estate.generic_references:
        parts.append(f'  <reference filename="{ref["filename"]}" size="{ref["size_bytes"]}B">')
        parts.append(f"    {ref['content_preview']}")
        parts.append("  </reference>")
    parts.append("</generic_references>")
    parts.append("")

    parts.append("</estate_dossier>")

    return "\n".join(parts)


def write_dossiers(
    dossiers: dict[str, ModelDossier],
    estate: EstateDossier,
    output_dir: Path,
    *,
    per_file: bool = True,
) -> None:
    """Write serialized dossiers to disk.

    Args:
        dossiers: dict of model_id → ModelDossier
        estate: the estate-wide dossier
        output_dir: directory to write to
        per_file: if True, one file per model; if False, single combined file
    """
    output_dir.mkdir(parents=True, exist_ok=True)

    if per_file:
        # One file per model
        models_dir = output_dir / "per_model"
        models_dir.mkdir(exist_ok=True)

        for model_id, dossier in dossiers.items():
            safe_name = model_id.lower().replace(" ", "_")
            filepath = models_dir / f"{safe_name}_dossier.md"
            content = serialize_dossier_xml(dossier)
            filepath.write_text(content, encoding="utf-8")

        logger.info("Wrote %d per-model dossier files to %s", len(dossiers), models_dir)
    else:
        # Single combined file
        combined_path = output_dir / "all_dossiers.md"
        parts = []
        for model_id, dossier in dossiers.items():
            parts.append(serialize_dossier_xml(dossier))
            parts.append("\n" + "=" * 80 + "\n")
        combined_path.write_text("\n".join(parts), encoding="utf-8")
        logger.info("Wrote combined dossier file: %s", combined_path)

    # Always write the estate dossier
    estate_path = output_dir / "estate_dossier.md"
    estate_path.write_text(serialize_estate_dossier(estate), encoding="utf-8")
    logger.info("Wrote estate dossier: %s", estate_path)

    # Also write a JSON summary for programmatic access
    summary = {
        "total_models": len(dossiers),
        "models": [],
    }
    for model_id, dossier in dossiers.items():
        model_summary = {
            "model_id": model_id,
            "model_code": dossier.model_code,
            "metrics_count": sum(len(m) for m in dossier.all_metric_domains().values()),
            "has_frd": dossier.functional_requirements != "<not provided>",
            "change_requests": [cr.cr_id for cr in dossier.change_requests],
            "has_sampling_methodology": dossier.sampling_methodology != "<not provided>",
            "coverage_gaps_count": len(dossier.relevant_coverage_gaps),
        }
        summary["models"].append(model_summary)

    summary_path = output_dir / "pipeline_summary.json"
    summary_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    logger.info("Wrote pipeline summary: %s", summary_path)
