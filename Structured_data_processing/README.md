# Per-Model Insight Pipeline

Consolidates 100 AML transaction-monitoring models from heterogeneous structured (Excel) and unstructured (Markdown) sources into **one dossier per model**, ready for LLM insight generation.

## What It Does

The pipeline reads **10 source files** (5 Excel workbooks + 5 parsed Markdown files), resolves every fragment to its canonical model ID, merges them into per-model dossiers, and serializes the output in an XML-tagged format that separates structured metrics from verbatim prose.

```
sources → per-source parser → normalized fragments (keyed by model_id)
       → merge/upsert into ModelDossier → serialize → output (one file per model)
```

### Source Files

| File | Type | What It Contains |
|------|------|------------------|
| `Model_Performance_Metrics.xlsx` | Excel (6 sheets) | Confusion matrix, precision/recall/F1, alert volumes, thresholds |
| `Backtesting_Results.xlsx` | Excel (6 sheets) | ATL/BTL testing, quarterly trends, tuning recommendations |
| `Data_Quality.xlsx` | Excel (6 sheets) | Completeness, accuracy, timeliness, data lineage |
| `Detection_Coverage.xlsx` | Excel (5 sheets) | Typology, segment, geography coverage + gaps |
| `Model_Risk_Governance.xlsx` | Excel (6 sheets) | Risk tiering, lifecycle, ownership RACI, validation log |
| `FRD_BRD_Model_Information.md` | Markdown | Business requirements for all 100 models (verbatim prose) |
| `CR-001_Change_Request.md` | Markdown | Threshold re-tuning for Model 7 |
| `CR-002_Change_Request.md` | Markdown | SWIFT MT103 data fix for Models 12 & 13 |
| `CR-003_Change_Request.md` | Markdown | Structuring family recalibration (13 models) |
| `attention_is_all_you_need.md` | Markdown | Generic reference (estate-wide, not model-specific) |

---

## Prerequisites

- **Python 3.10+**
- **openpyxl** (already in the project's virtual environment)

If `openpyxl` is not installed:

```bash
source ../.venv/bin/activate
pip install openpyxl
```

---

## How to Run

### Quick Start (from the project root)

```bash
cd /Users/chetanbavdhankar/coding/rag_ai_assistant
source .venv/bin/activate

cd Structured_data_processing
PYTHONPATH=.. python -m pipeline.run_pipeline
```

### From the `Structured_data_processing/` directory

```bash
source ../.venv/bin/activate
PYTHONPATH=.. python -m pipeline.run_pipeline
```

### With Options

```bash
# Verbose logging (shows DEBUG-level detail)
PYTHONPATH=.. python -m pipeline.run_pipeline --verbose

# Custom output directory
PYTHONPATH=.. python -m pipeline.run_pipeline --output-dir /path/to/custom/output

# Single combined file instead of per-model files
PYTHONPATH=.. python -m pipeline.run_pipeline --single-file

# Custom source paths
PYTHONPATH=.. python -m pipeline.run_pipeline \
  --data-dir ../RAG_data \
  --parsed-dir ../RAG_data/parsed_outputs/docling \
  --output-dir ./output
```

### CLI Reference

| Flag | Default | Description |
|------|---------|-------------|
| `--data-dir` | `RAG_data/` | Directory containing the Excel workbooks |
| `--parsed-dir` | `RAG_data/parsed_outputs/docling/` | Directory containing the parsed Markdown files |
| `--output-dir` | `Structured_data_processing/output/` | Where to write the dossier output |
| `--single-file` | off | Write all dossiers into one combined file |
| `--verbose` / `-v` | off | Enable DEBUG-level logging |

---

## Output Structure

After a successful run, the output directory contains:

```
output/
├── per_model/                    # One dossier per model (100 files)
│   ├── model_1_dossier.md        # ~12-16 KB each
│   ├── model_2_dossier.md
│   ├── ...
│   └── model_100_dossier.md
├── estate_dossier.md             # Estate-wide context (coverage gaps, sampling, generic refs)
└── pipeline_summary.json         # Programmatic summary for downstream tools
```

### Dossier Format

Each per-model dossier uses **XML-style tags** to separate structured metrics from prose:

```xml
<model id="Model 1" code="TM-STR-001">

<structured_metrics>
  <domain name="performance">
    | Metric | Value | Source |
    |--------|-------|--------|
    | Precision | 0.075 | Model_Performance_Metrics.xlsx/Precision_Recall_F1 |
    ...
  </domain>
  <domain name="backtesting">...</domain>
  <domain name="data_quality">...</domain>
  <domain name="coverage">...</domain>
  <domain name="governance">...</domain>
</structured_metrics>

<functional_requirements>
  [verbatim FRD/BRD section — never parsed into fields]
</functional_requirements>

<change_requests>
  <cr id="CR-003" source="CR-003_Change_Request.md">
    [full CR content]
  </cr>
</change_requests>

<estate_context>
  <sampling_methodology>...</sampling_methodology>
  <relevant_coverage_gaps>...</relevant_coverage_gaps>
</estate_context>

</model>
```

### Pipeline Summary JSON

`pipeline_summary.json` provides a quick programmatic overview:

```json
{
  "total_models": 100,
  "models": [
    {
      "model_id": "Model 1",
      "model_code": "TM-STR-001",
      "metrics_count": 119,
      "has_frd": true,
      "change_requests": ["CR-003"],
      "has_sampling_methodology": true,
      "coverage_gaps_count": 0
    },
    ...
  ]
}
```

---

## Pipeline Stages

| Stage | Module | What It Does |
|-------|--------|--------------|
| 1. ID Resolution | `id_resolver.py` | Builds canonical map (`Model N` ↔ `TM-XXX-NNN`) from FRD |
| 2. Excel Parsing | `parsers/excel_parser.py` | Normalizes 25+ sheets to long-form `(model, metric, value, source)` |
| 3. FRD Parsing | `parsers/frd_parser.py` | Splits FRD/BRD on `### 3.N Model N` headings |
| 4. CR Parsing | `parsers/cr_parser.py` | Extracts affected models, keeps full CR prose |
| 5. Generic Data | `generic_data.py` | Collects coverage gaps, sampling methodology, issue logs |
| 6. Merge | `merge.py` | Upserts all fragments into per-model dossiers |
| 7. Finalize | `merge.py` | Sets `<not provided>` markers for missing data |
| 8. Serialize | `serializer.py` | Writes XML-tagged dossier files + estate context + JSON summary |

---

## Module Reference

```
pipeline/
├── __init__.py            # Package init
├── config.py              # All configurable parameters (paths, conflict policy, etc.)
├── models.py              # Dataclasses: Metric, ChangeRequest, ModelDossier, EstateDossier
├── id_resolver.py         # Canonical ID map + alias normalization
├── parsers/
│   ├── __init__.py
│   ├── excel_parser.py    # Excel workbooks → long-form metric fragments
│   ├── frd_parser.py      # FRD/BRD markdown → per-model prose sections
│   └── cr_parser.py       # Change Requests → affected models + verbatim prose
├── merge.py               # Upsert engine with provenance + conflict handling
├── generic_data.py        # Estate-wide data collector
├── serializer.py          # XML-tagged LLM-ready serialization
└── run_pipeline.py        # CLI entry point
```

---

## Configuration

All tunable parameters live in [`pipeline/config.py`](pipeline/config.py):

| Parameter | Default | Description |
|-----------|---------|-------------|
| `CONFLICT_POLICY` | `"keep_both_with_provenance"` | How to handle duplicate metrics from different sources |
| `SERIALIZATION_FORMAT` | `"xml"` | Output format for structured blocks |
| `METRICS_MODE` | `"raw"` | Pass metrics raw or pre-summarized |
| `EXCEL_HEADER_ROW` | `4` | Row containing column headers (1-indexed) |
| `EXCEL_DATA_START_ROW` | `5` | First data row (1-indexed) |
| `SKIP_SHEETS` | `{"Overview"}` | Sheets to skip (duplicates of specific tabs) |

---

## Typical Run Output

```
STEP 1: Building canonical ID map from FRD
  → 100 models registered

STEP 2: Parsing Excel workbooks
  → 11,700 metrics across 5 domains

STEP 3: Parsing FRD/BRD markdown
  → 100 model sections extracted

STEP 4: Parsing Change Requests
  → CR-001: 1 model, CR-002: 2 models, CR-003: 13 models

STEP 5: Collecting generic / estate-wide data
  → 18 coverage gaps, 8 family methodologies, 179 issues/recommendations

STEP 6-7: Merging and finalizing
  → 100 dossiers finalized

STEP 8: Serializing
  → 100 per-model files + estate dossier + JSON summary

PIPELINE COMPLETE — 0.13s
```

---

## Using the Output with an LLM

Each dossier file is designed as the **user content** for a single LLM call:

```
System prompt:  [Your insight task definition + output schema]
User content:   [Contents of model_N_dossier.md]
```

Benefits of the per-model boundary:
- Token budget bounded by one model's footprint (~4-8K tokens per dossier)
- No cross-model bleed in the reasoning
- Trivially parallelizable across all 100 models
