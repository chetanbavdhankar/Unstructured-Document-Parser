# Per-Model Insight Pipeline — Concept

Merging heterogeneous structured and unstructured sources into one typed record per model, then generating insights per model with an LLM.

## Problem framing

The stated task is "parse structured data and pass it to an LLM." The real task is **entity resolution + merge**. Once each model's information is consolidated into a single clean record, the LLM step is trivial — the model reads markdown and tables natively. Effort belongs in the consolidation, not the prompt.

Inputs are multiple Excel and markdown files describing the *same set of models* along different axes: KPIs, KRIs (structured/numeric), and functional requirements and design (subjective prose). No single file is complete; each contributes a fragment.

## Core abstraction: the dossier

One **dossier** per model, keyed on a canonical `model_id`. The dossier is the merge target into which every source upserts its fragment.

Inviolable rule inside the dossier: **structured stays structured, prose stays prose.** Numeric KPI/KRI data is held as typed fields; functional requirements and design are held as verbatim text. Never flatten prose into fields — that destroys exactly the nuance the insight step is meant to read.

One dossier → one LLM call → one insight set. The per-model boundary is both the merge key and the natural chunking unit.

## Dataflow

```
sources → per-source parser → normalized fragments (keyed by model_id)
       → merge/upsert into ModelDossier → serialize → LLM (one call per model)
```

Parsers are source-specific and dumb; they only produce fragments keyed by id. All intelligence about *how models relate across files* lives in the merge stage.

## Parsing by source type

**Excel — normalize to long form.** Read the sheets, then immediately reshape to `(model_id, metric_name, value, source_file)` regardless of whether the original layout is wide (one row per model) or already long. Long form is the only shape that merges cleanly when files carry disjoint metric sets. Pivot back to wide only at serialization, if a table layout is wanted. Watch for multi-row headers and merged cells in governance spreadsheets — when the header is irregular, read at a lower level than a naive dataframe load so columns don't misalign.

**Markdown — segment, don't parse.** Do not extract prose into fields. Locate the boundary that maps a block of text to a model and pass that block verbatim:
- one file per model → the key comes from the filename or front-matter;
- one file with a heading per model → split on headings, map each section to its `model_id`.

The whole reason an LLM is in the loop is that it ingests prose directly. Preserve the design/requirements text as-is.

## The load-bearing decisions

This is where the pipeline breaks if neglected — not in the parsing.

1. **Canonical ID resolution.** The same model will appear as `Model_A`, `model a`, `MA-001`. Build an alias → canonical map up front. Fail loudly on an unmapped id rather than silently dropping that model's data.
2. **Provenance.** Tag every datum with its source file. Insights must be traceable to inputs (essential in a governance/AML context), and provenance stops the LLM attributing a number to the wrong document.
3. **Explicit absence.** When a model has KPIs but no design section, write an explicit "not provided" marker. Silent omission invites hallucination; an explicit null suppresses it.
4. **Conflict policy.** When two files disagree on the same metric for the same model, the resolution rule — latest-source-wins, flag-for-review, or keep-both-with-provenance — is decided before merge. It is never delegated to the prompt.

## Serialization principle

Serialize each dossier so the LLM can distinguish hard metrics from subjective text. Wrap structured blocks and prose blocks in clearly labelled, separable regions (XML-style tags or YAML for the structured part; raw markdown for prose). The tagging is what lets the insight prompt reason over "the numbers" and "the design intent" as distinct things.

If a model's numeric history is large, aggregate or summarize the metrics before serializing rather than dumping raw rows — keep the dossier within a single-model token footprint.

## The per-model LLM call

One call per dossier. A fixed system prompt defines the insight task and the output schema; the serialized dossier is the user content. Benefits of this boundary:
- token budget bounded by one model's footprint;
- no cross-model bleed in the reasoning — insights for model A never leak context from model B;
- trivially parallelizable and re-runnable per model.

## Illustrative schema (conceptual)

A typed record makes the structured/prose split and the provenance requirement concrete:

```
Metric:        name, value, source
ModelDossier:  model_id
               kpis: [Metric]
               kris: [Metric]
               functional_requirements: str  (default "<not provided>")
               design: str                   (default "<not provided>")
```

Merge is an `upsert(raw_id, **fragment)` that canonicalizes the id, fetches-or-creates the dossier, extends the metric lists, and overwrites prose fields when present — applying the conflict policy as it goes.

## Parameters to fix per project

- Wide vs. long layout of the KPI/KRI sheets.
- Markdown granularity: per-model file vs. per-section headings.
- Conflict resolution rule.
- Serialization format for the structured block (tagged XML vs. YAML).
- Whether large metric sets are passed raw or pre-summarized.
