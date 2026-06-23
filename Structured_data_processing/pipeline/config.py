"""Pipeline configuration — centralises all project-specific parameters.

These are the "parameters to fix per project" called out in the concept doc.
"""

from pathlib import Path

# ── Paths ─────────────────────────────────────────────────────────────────────
# All paths are relative to the project root (rag_ai_assistant/).
PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATA_DIR = PROJECT_ROOT / "RAG_data"
PARSED_DIR = DATA_DIR / "parsed_outputs" / "docling"
OUTPUT_DIR = PROJECT_ROOT / "Structured_data_processing" / "output"

# Excel workbooks (structured sources)
EXCEL_FILES = {
    "performance": DATA_DIR / "Model_Performance_Metrics.xlsx",
    "backtesting": DATA_DIR / "Backtesting_Results.xlsx",
    "data_quality": DATA_DIR / "Data_Quality.xlsx",
    "coverage":    DATA_DIR / "Detection_Coverage.xlsx",
    "governance":  DATA_DIR / "Model_Risk_Governance.xlsx",
}

# Markdown files (unstructured sources)
FRD_FILE = PARSED_DIR / "FRD_BRD_Model_Information.md"
CR_FILES = sorted(PARSED_DIR.glob("CR-*_Change_Request.md"))

# Generic / estate-wide references (not model-specific)
GENERIC_REFERENCES = [PARSED_DIR / "attention_is_all_you_need.md"]

# ── Excel Layout ──────────────────────────────────────────────────────────────
# All workbooks share a consistent layout:
#   Row 1: Title
#   Row 2: Description
#   Row 3: Blank
#   Row 4: Header
#   Row 5+: Data
EXCEL_HEADER_ROW = 4       # 1-indexed
EXCEL_DATA_START_ROW = 5   # 1-indexed

# Sheets to skip (Overview tabs duplicate data from specific sheets)
SKIP_SHEETS = {"Overview"}

# ── Markdown Parsing ──────────────────────────────────────────────────────────
# FRD heading pattern — each model section starts with this
FRD_HEADING_PATTERN = r"^### 3\.(\d+)\s+Model\s+(\d+)"

# CR metadata field containing affected model IDs
CR_MODEL_FIELD = "Affected Model(s) / Feed"

# ── Conflict Resolution ──────────────────────────────────────────────────────
# Options: "keep_both_with_provenance", "latest_source_wins", "flag_for_review"
CONFLICT_POLICY = "keep_both_with_provenance"

# ── Serialization ─────────────────────────────────────────────────────────────
# Format for the structured block: "xml" (XML-style tags) or "yaml"
SERIALIZATION_FORMAT = "xml"

# Whether to pass large metric sets raw or pre-summarized
METRICS_MODE = "raw"  # or "pre_summarized"

# ── Estate-Wide Sheets ────────────────────────────────────────────────────────
# Sheets that contain estate/family-level data (not per-model rows)
ESTATE_SHEETS = {
    "Coverage_Gaps",
    "Sampling_Methodology",
}

# Sheets that mix model-level and generic rows (need row-level routing)
MIXED_SHEETS = {
    "DQ_Issue_Log",
    "Issue_Tracking",
}
