"""Change Request markdown parser.

Each CR file is a single document. We extract:
1. The CR ID from the metadata table
2. The affected model IDs from the "Affected Model(s) / Feed" row
3. The entire CR content as verbatim prose — attached to each affected model
"""

from __future__ import annotations

import re
import logging
from pathlib import Path

from pipeline.models import ChangeRequest

logger = logging.getLogger(__name__)


def parse_cr_file(cr_path: Path) -> tuple[str, list[str], str]:
    """Parse a single Change Request markdown file.

    Returns:
        (cr_id, affected_model_ids_raw, full_prose)
    """
    text = cr_path.read_text(encoding="utf-8")
    filename = cr_path.name

    # Extract CR ID from the metadata table
    cr_id_match = re.search(r"\|\s*\*\*CR ID\*\*\s*\|\s*(CR-\d+)\s*\|", text)
    cr_id = cr_id_match.group(1).strip() if cr_id_match else filename.split("_")[0]

    # Extract affected models from "Affected Model(s) / Feed" row
    affected_match = re.search(
        r"\|\s*\*\*Affected Model\(s\).*?\*\*\s*\|\s*(.+?)\s*\|",
        text,
        re.IGNORECASE,
    )

    raw_model_ids: list[str] = []
    if affected_match:
        affected_text = affected_match.group(1).strip()

        # Handle "Models N, N, N..." pattern (e.g. "Models 1, 9, 17, 25")
        # This appears when a CR affects a whole family with listed model numbers
        models_list_match = re.search(
            r"Models?\s+([\d,\s]+)", affected_text, re.IGNORECASE
        )
        if models_list_match:
            nums_str = models_list_match.group(1)
            for num in re.findall(r"\d+", nums_str):
                model_id = f"Model {int(num)}"
                if model_id not in raw_model_ids:
                    raw_model_ids.append(model_id)

        # Also extract "Model N (TM-XXX-NNN)" patterns for individual model refs
        for m in re.finditer(r"Model\s+(\d+)\s*\(", affected_text, re.IGNORECASE):
            model_id = f"Model {int(m.group(1))}"
            if model_id not in raw_model_ids:
                raw_model_ids.append(model_id)

    # The full prose is the entire file content — verbatim
    full_prose = text.strip()

    logger.info("Parsed CR %s: affects %d models (%s)",
                cr_id, len(raw_model_ids),
                ", ".join(raw_model_ids) if len(raw_model_ids) <= 5
                else f"{', '.join(raw_model_ids[:3])}... +{len(raw_model_ids) - 3} more")

    return cr_id, raw_model_ids, full_prose


def parse_all_crs(cr_paths: list[Path]) -> dict[str, list[ChangeRequest]]:
    """Parse all Change Request files.

    Returns:
        dict mapping raw "Model N" → [ChangeRequest]
    """
    model_crs: dict[str, list[ChangeRequest]] = {}

    for cr_path in cr_paths:
        if not cr_path.exists():
            logger.warning("CR file not found: %s", cr_path)
            continue

        cr_id, raw_model_ids, full_prose = parse_cr_file(cr_path)
        cr = ChangeRequest(cr_id=cr_id, prose=full_prose, source=cr_path.name)

        for model_id in raw_model_ids:
            if model_id not in model_crs:
                model_crs[model_id] = []
            model_crs[model_id].append(cr)

    total_mappings = sum(len(v) for v in model_crs.values())
    logger.info("Parsed %d CR files → %d model-CR mappings across %d models",
                len(cr_paths), total_mappings, len(model_crs))

    return model_crs
