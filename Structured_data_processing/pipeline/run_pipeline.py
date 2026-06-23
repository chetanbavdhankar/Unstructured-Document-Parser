"""Pipeline orchestrator — CLI entry point.

Ties together all pipeline stages:
1. Build canonical ID map from FRD summary matrix
2. Parse all Excel workbooks → structured metric fragments
3. Parse FRD/BRD → prose fragments per model
4. Parse Change Requests → prose fragments per model
5. Collect generic / estate-wide data
6. Merge all fragments into per-model dossiers
7. Finalize: validate & set explicit absence markers
8. Serialize to output directory
9. Print summary

Usage:
    python -m pipeline.run_pipeline
    python -m pipeline.run_pipeline --output-dir custom/path --single-file
"""

from __future__ import annotations

import argparse
import logging
import sys
import time
from pathlib import Path

from pipeline.config import (
    DATA_DIR,
    PARSED_DIR,
    OUTPUT_DIR,
    EXCEL_FILES,
    FRD_FILE,
    CR_FILES,
    GENERIC_REFERENCES,
)
from pipeline.id_resolver import IDResolver
from pipeline.parsers.excel_parser import parse_all_excel
from pipeline.parsers.frd_parser import parse_frd_sections
from pipeline.parsers.cr_parser import parse_all_crs
from pipeline.generic_data import collect_all_generic_data, collect_sampling_methodology
from pipeline.merge import MergeEngine
from pipeline.serializer import write_dossiers

logger = logging.getLogger(__name__)


def setup_logging(verbose: bool = False) -> None:
    """Configure logging for the pipeline."""
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%H:%M:%S",
    )


def run_pipeline(
    data_dir: Path | None = None,
    parsed_dir: Path | None = None,
    output_dir: Path | None = None,
    per_file: bool = True,
) -> None:
    """Execute the full per-model insight pipeline."""
    data_dir = data_dir or DATA_DIR
    parsed_dir = parsed_dir or PARSED_DIR
    output_dir = output_dir or OUTPUT_DIR

    start = time.time()

    # ── Step 1: Build canonical ID map ────────────────────────────────────
    logger.info("=" * 60)
    logger.info("STEP 1: Building canonical ID map from FRD")
    logger.info("=" * 60)

    frd_path = FRD_FILE if FRD_FILE.exists() else parsed_dir / "FRD_BRD_Model_Information.md"
    resolver = IDResolver()
    resolver.build_from_frd(frd_path)

    model_count = len(resolver.all_model_ids())
    logger.info("Canonical map built: %d models registered", model_count)

    # ── Step 2: Parse all Excel workbooks ─────────────────────────────────
    logger.info("=" * 60)
    logger.info("STEP 2: Parsing Excel workbooks")
    logger.info("=" * 60)

    # Resolve Excel paths relative to data_dir if config defaults don't exist
    excel_files = {}
    for domain, path in EXCEL_FILES.items():
        if path.exists():
            excel_files[domain] = path
        else:
            alt = data_dir / path.name
            if alt.exists():
                excel_files[domain] = alt
            else:
                logger.warning("Excel file not found: %s", path)

    all_excel_fragments = parse_all_excel(excel_files)

    total_metrics = sum(
        sum(len(metrics) for metrics in domain_frags.values())
        for domain_frags in all_excel_fragments.values()
    )
    logger.info("Total metrics parsed from Excel: %d across %d domains",
                total_metrics, len(all_excel_fragments))

    # ── Step 3: Parse FRD/BRD ─────────────────────────────────────────────
    logger.info("=" * 60)
    logger.info("STEP 3: Parsing FRD/BRD markdown")
    logger.info("=" * 60)

    frd_sections = parse_frd_sections(frd_path)
    logger.info("FRD sections extracted: %d", len(frd_sections))

    # ── Step 4: Parse Change Requests ─────────────────────────────────────
    logger.info("=" * 60)
    logger.info("STEP 4: Parsing Change Requests")
    logger.info("=" * 60)

    cr_paths = list(CR_FILES) if CR_FILES else list(parsed_dir.glob("CR-*_Change_Request.md"))
    model_crs = parse_all_crs(cr_paths)

    # ── Step 5: Collect generic / estate-wide data ────────────────────────
    logger.info("=" * 60)
    logger.info("STEP 5: Collecting generic / estate-wide data")
    logger.info("=" * 60)

    ref_paths = [p for p in GENERIC_REFERENCES if p.exists()]
    if not ref_paths:
        ref_paths = [p for p in parsed_dir.glob("*.md")
                     if not p.name.startswith("CR-")
                     and "FRD" not in p.name]

    estate_dossier, routable_issues = collect_all_generic_data(excel_files, ref_paths)

    # Get sampling methodology as a family→string dict for attaching to models
    sampling_by_family = {}
    if "backtesting" in excel_files:
        sampling_by_family = collect_sampling_methodology(excel_files["backtesting"])

    # ── Step 6: Merge all fragments ───────────────────────────────────────
    logger.info("=" * 60)
    logger.info("STEP 6: Merging all fragments into dossiers")
    logger.info("=" * 60)

    engine = MergeEngine(resolver)

    # 6a. Structured metrics from Excel
    for domain, fragments in all_excel_fragments.items():
        engine.upsert_metrics(domain, fragments)

    # 6b. FRD prose
    engine.upsert_frd_sections(frd_sections)

    # 6c. Change Requests
    engine.upsert_change_requests(model_crs)

    # 6d. Model-level issues from mixed sheets
    for sheet_name, issues in routable_issues.items():
        engine.upsert_issues(sheet_name, issues)

    # 6e. Estate context per model
    engine.attach_sampling_methodology(sampling_by_family)
    engine.attach_coverage_gaps(estate_dossier.coverage_gaps)

    # ── Step 7: Finalize ──────────────────────────────────────────────────
    logger.info("=" * 60)
    logger.info("STEP 7: Finalizing dossiers")
    logger.info("=" * 60)

    engine.finalize()
    dossiers = engine.get_all_dossiers()

    # ── Step 8: Serialize ─────────────────────────────────────────────────
    logger.info("=" * 60)
    logger.info("STEP 8: Serializing to output")
    logger.info("=" * 60)

    write_dossiers(dossiers, estate_dossier, output_dir, per_file=per_file)

    # ── Step 9: Summary ───────────────────────────────────────────────────
    elapsed = time.time() - start

    logger.info("=" * 60)
    logger.info("PIPELINE COMPLETE")
    logger.info("=" * 60)
    logger.info("Models processed:        %d", len(dossiers))
    logger.info("Excel domains merged:    %d", len(all_excel_fragments))
    logger.info("FRD sections merged:     %d", len(frd_sections))
    logger.info("Change Requests merged:  %d CRs across %d models",
                len(cr_paths), len(model_crs))
    logger.info("Estate coverage gaps:    %d", len(estate_dossier.coverage_gaps))
    logger.info("Generic references:      %d", len(estate_dossier.generic_references))
    logger.info("Output directory:        %s", output_dir)
    logger.info("Time elapsed:            %.2fs", elapsed)

    # Validation warnings
    models_without_frd = [
        mid for mid, d in dossiers.items()
        if d.functional_requirements == "<not provided>"
    ]
    if models_without_frd:
        logger.warning("Models without FRD data: %s", models_without_frd)

    models_without_metrics = [
        mid for mid, d in dossiers.items()
        if all(len(m) == 0 for m in d.all_metric_domains().values())
    ]
    if models_without_metrics:
        logger.warning("Models without any metrics: %s", models_without_metrics)


def main() -> None:
    """CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Per-Model Insight Pipeline — consolidate AML model data into dossiers",
    )
    parser.add_argument(
        "--data-dir",
        type=Path,
        default=None,
        help=f"Path to raw data directory (default: {DATA_DIR})",
    )
    parser.add_argument(
        "--parsed-dir",
        type=Path,
        default=None,
        help=f"Path to parsed markdown outputs (default: {PARSED_DIR})",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=None,
        help=f"Path to output directory (default: {OUTPUT_DIR})",
    )
    parser.add_argument(
        "--single-file",
        action="store_true",
        help="Write all dossiers to a single combined file instead of per-model files",
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Enable verbose (DEBUG) logging",
    )

    args = parser.parse_args()
    setup_logging(args.verbose)

    run_pipeline(
        data_dir=args.data_dir,
        parsed_dir=args.parsed_dir,
        output_dir=args.output_dir,
        per_file=not args.single_file,
    )


if __name__ == "__main__":
    main()
