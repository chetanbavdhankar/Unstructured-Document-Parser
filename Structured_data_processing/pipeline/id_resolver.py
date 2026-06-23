"""Canonical ID resolution — the load-bearing decision #1.

The same model may appear as "Model_7", "model 7", "Model 07", "TM-CRYPTO-007".
This module maps every variant to a single canonical form: "Model N".

Fails loudly on unmapped IDs rather than silently dropping data.
"""

from __future__ import annotations

import re
import logging
from pathlib import Path

logger = logging.getLogger(__name__)


class IDResolutionError(Exception):
    """Raised when a raw ID cannot be mapped to a canonical model ID."""


class IDResolver:
    """Builds and maintains the alias → canonical model_id map."""

    def __init__(self) -> None:
        # canonical_id → metadata dict
        self._registry: dict[str, dict] = {}
        # lowercase alias → canonical_id
        self._alias_map: dict[str, str] = {}

    # ── Build the map from the FRD summary matrix ─────────────────────────

    def build_from_frd(self, frd_path: Path) -> None:
        """Parse Section 2 (Model Summary Matrix) of the FRD to build
        the canonical map: Model N → {code, typology, family, entity, cr}.
        """
        text = frd_path.read_text(encoding="utf-8")
        # The summary matrix is a markdown table in Section 2.
        # Each row: | Model N | TM-XXX-NNN | Typology | Family | Entity | CR |
        table_pattern = re.compile(
            r"\|\s*(Model\s+\d+)\s*\|\s*(\S+)\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*(\S+(?:\s+\S+)?)\s*\|\s*(.+?)\s*\|"
        )

        for match in table_pattern.finditer(text):
            raw_model = match.group(1).strip()
            code = match.group(2).strip()
            typology = match.group(3).strip()
            family = match.group(4).strip()
            entity = match.group(5).strip()
            cr = match.group(6).strip()

            canonical = self._normalize(raw_model)
            metadata = {
                "model_code": code,
                "typology": typology,
                "family": family,
                "entity": entity,
                "cr": cr if cr != "—" else None,
            }
            self._registry[canonical] = metadata

            # Register aliases
            self._register_alias(raw_model, canonical)
            self._register_alias(code, canonical)

        logger.info("IDResolver: registered %d models from FRD", len(self._registry))

    # ── Resolution ────────────────────────────────────────────────────────

    def resolve(self, raw_id: str) -> str:
        """Resolve a raw ID to its canonical form.

        Raises IDResolutionError if the ID cannot be mapped.
        """
        canonical = self._normalize(raw_id)

        # Direct match
        if canonical in self._registry:
            return canonical

        # Alias lookup
        key = raw_id.strip().lower()
        if key in self._alias_map:
            return self._alias_map[key]

        # Try extracting a number from the raw string
        num_match = re.search(r"(\d+)", raw_id)
        if num_match:
            candidate = f"Model {int(num_match.group(1))}"
            if candidate in self._registry:
                # Cache this alias for future lookups
                self._register_alias(raw_id, candidate)
                return candidate

        raise IDResolutionError(
            f"Cannot resolve '{raw_id}' to a canonical model ID. "
            f"Known models: {len(self._registry)}"
        )

    def get_metadata(self, model_id: str) -> dict:
        """Return the metadata dict for a canonical model_id."""
        canonical = self.resolve(model_id)
        return self._registry[canonical]

    def all_model_ids(self) -> list[str]:
        """Return all canonical model IDs in sorted order."""
        return sorted(self._registry.keys(), key=lambda x: int(re.search(r"\d+", x).group()))

    def get_family(self, model_id: str) -> str:
        """Return the scenario family for a model."""
        return self.get_metadata(model_id).get("family", "")

    # ── Internal helpers ──────────────────────────────────────────────────

    @staticmethod
    def _normalize(raw: str) -> str:
        """Normalize to canonical form 'Model N' (no leading zeros)."""
        raw = raw.strip()
        # Match patterns like "Model 1", "Model_07", "model 007"
        m = re.match(r"(?i)model[\s_-]*0*(\d+)", raw)
        if m:
            return f"Model {int(m.group(1))}"
        return raw

    def _register_alias(self, alias: str, canonical: str) -> None:
        """Register a lowercase alias pointing to the canonical ID."""
        key = alias.strip().lower()
        if key and key not in self._alias_map:
            self._alias_map[key] = canonical

    # ── Extraction helpers for CR files ───────────────────────────────────

    def extract_model_ids_from_text(self, text: str) -> list[str]:
        """Extract all model IDs mentioned in a text string.

        Handles patterns like:
          - "Model 7 (TM-BEHAV-007)"
          - "Model 12 (TM-CRYPTO-012), Model 13 (TM-NETWORK-013)"
          - "Models 1, 9, 17, 25, ..."
        """
        found = []

        # Pattern 1: "Model N" with optional parenthetical code
        for m in re.finditer(r"Model\s+(\d+)", text, re.IGNORECASE):
            try:
                canonical = self.resolve(f"Model {m.group(1)}")
                if canonical not in found:
                    found.append(canonical)
            except IDResolutionError:
                logger.warning("Unresolvable model reference in text: Model %s", m.group(1))

        # Pattern 2: TM-XXX-NNN codes
        for m in re.finditer(r"TM-[A-Z]+-\d+", text):
            try:
                canonical = self.resolve(m.group(0))
                if canonical not in found:
                    found.append(canonical)
            except IDResolutionError:
                logger.warning("Unresolvable code in text: %s", m.group(0))

        return found
