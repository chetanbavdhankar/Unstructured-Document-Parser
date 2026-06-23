"""FRD/BRD markdown parser — segment, don't parse.

The whole reason an LLM is in the loop is that it ingests prose directly.
This parser locates the boundary that maps a block of text to a model
and passes that block verbatim.

It also extracts the Section 2 summary matrix for ID resolution.
"""

from __future__ import annotations

import re
import logging
from pathlib import Path

from pipeline.config import FRD_HEADING_PATTERN

logger = logging.getLogger(__name__)


def parse_frd_sections(frd_path: Path) -> dict[str, str]:
    """Split the FRD/BRD file on per-model headings.

    Returns:
        dict mapping raw "Model N" → verbatim prose content
    """
    text = frd_path.read_text(encoding="utf-8")
    lines = text.split("\n")

    sections: dict[str, str] = {}
    heading_re = re.compile(FRD_HEADING_PATTERN)

    # Find all heading positions
    headings: list[tuple[int, str]] = []
    for i, line in enumerate(lines):
        m = heading_re.match(line)
        if m:
            model_num = int(m.group(2))
            model_id = f"Model {model_num}"
            headings.append((i, model_id))

    # Extract content between consecutive headings
    for idx, (line_num, model_id) in enumerate(headings):
        if idx + 1 < len(headings):
            end_line = headings[idx + 1][0]
        else:
            end_line = len(lines)

        # Include the heading itself as part of the section content
        section_lines = lines[line_num:end_line]
        content = "\n".join(section_lines).strip()
        sections[model_id] = content

    logger.info("Parsed FRD: %d model sections extracted", len(sections))
    return sections


def parse_frd_summary_matrix(frd_path: Path) -> list[dict]:
    """Parse the Section 2 summary matrix for metadata.

    Returns a list of dicts, one per model, with keys:
    model, code, typology, family, entity, cr
    """
    text = frd_path.read_text(encoding="utf-8")

    table_pattern = re.compile(
        r"\|\s*(Model\s+\d+)\s*\|\s*(\S+)\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*(\S+(?:\s+\S+)?)\s*\|\s*(.+?)\s*\|"
    )

    matrix = []
    for match in table_pattern.finditer(text):
        matrix.append({
            "model": match.group(1).strip(),
            "code": match.group(2).strip(),
            "typology": match.group(3).strip(),
            "family": match.group(4).strip(),
            "entity": match.group(5).strip(),
            "cr": match.group(6).strip() if match.group(6).strip() != "—" else None,
        })

    logger.info("Parsed FRD summary matrix: %d models", len(matrix))
    return matrix
