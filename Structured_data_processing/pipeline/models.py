"""Core data models — the dossier abstraction.

One ModelDossier per model.  Structured stays structured, prose stays prose.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class Metric:
    """A single named measurement with provenance.

    Provenance is critical in a governance/AML context — every datum must
    be traceable to its source file and sheet.
    """
    name: str
    value: Any          # numeric, string, date, or formula result
    source: str         # e.g. "Model_Performance_Metrics.xlsx/Confusion_Matrix"

    def to_dict(self) -> dict:
        return {"name": self.name, "value": self.value, "source": self.source}


@dataclass
class ChangeRequest:
    """A change request attached to one or more models."""
    cr_id: str
    prose: str          # full verbatim CR content
    source: str         # source filename

    def to_dict(self) -> dict:
        return {"cr_id": self.cr_id, "prose": self.prose, "source": self.source}


@dataclass
class ModelDossier:
    """The merge target — one per canonical model_id.

    Inviolable rule: structured stays structured, prose stays prose.
    Numeric KPI/KRI data is held as typed Metric fields;
    functional requirements and design are held as verbatim text.
    """
    model_id: str                           # canonical: "Model 1"
    model_code: str = ""                    # e.g. "TM-STR-001"

    # ── Structured metrics (lists of Metric, grouped by domain) ───────────
    performance_kpis: list[Metric] = field(default_factory=list)
    alert_kpis: list[Metric] = field(default_factory=list)
    backtesting_kpis: list[Metric] = field(default_factory=list)
    data_quality_kpis: list[Metric] = field(default_factory=list)
    coverage_kpis: list[Metric] = field(default_factory=list)
    governance_kpis: list[Metric] = field(default_factory=list)

    # ── Unstructured prose (verbatim — never parsed into fields) ──────────
    functional_requirements: str = "<not provided>"
    change_requests: list[ChangeRequest] = field(default_factory=list)

    # ── Linked issues (structured, but sourced from issue-log sheets) ─────
    mrm_issues: list[Metric] = field(default_factory=list)
    dq_issues: list[Metric] = field(default_factory=list)
    tuning_recommendations: list[Metric] = field(default_factory=list)

    # ── Estate context attached to this model ─────────────────────────────
    sampling_methodology: str = "<not provided>"
    relevant_coverage_gaps: list[dict] = field(default_factory=list)

    def all_metric_domains(self) -> dict[str, list[Metric]]:
        """Return all structured metric lists keyed by domain name."""
        return {
            "performance":            self.performance_kpis,
            "alerts":                 self.alert_kpis,
            "backtesting":            self.backtesting_kpis,
            "data_quality":           self.data_quality_kpis,
            "coverage":               self.coverage_kpis,
            "governance":             self.governance_kpis,
            "mrm_issues":             self.mrm_issues,
            "dq_issues":              self.dq_issues,
            "tuning_recommendations": self.tuning_recommendations,
        }


@dataclass
class EstateDossier:
    """Estate-wide / generic data not bound to a single model.

    This is context that applies across the entire model estate —
    coverage gaps, family-level sampling methodology, and generic
    reference documents.
    """
    coverage_gaps: list[dict] = field(default_factory=list)
    sampling_methodology: list[dict] = field(default_factory=list)
    generic_references: list[dict] = field(default_factory=list)
    unrouted_dq_issues: list[dict] = field(default_factory=list)
    unrouted_mrm_issues: list[dict] = field(default_factory=list)

    def to_dict(self) -> dict:
        return {
            "coverage_gaps": self.coverage_gaps,
            "sampling_methodology": self.sampling_methodology,
            "generic_references": self.generic_references,
            "unrouted_dq_issues": self.unrouted_dq_issues,
            "unrouted_mrm_issues": self.unrouted_mrm_issues,
        }
