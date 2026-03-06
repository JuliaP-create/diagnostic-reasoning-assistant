from __future__ import annotations

from dataclasses import dataclass, field
from typing import Callable, List, Optional, Set, Tuple


@dataclass(frozen=True)
class FeatureSpec:
    """Defines how we turn a case/session into model features.

    Keeping this in one place prevents inconsistencies between:
    - training feature engineering (Notebook 02)
    - interactive inference (Streamlit / API)
    - question policy + RAG notebooks
    """

    evidence_mode: str  # "base" or "token"
    cat_cols: List[str]
    num_cols: List[str]
    age_group_func: Optional[Callable] = None


def parse_token(token: str) -> Tuple[str, Optional[str]]:
    """Parse a DDXPlus evidence item/token into (base, value).

    Accepts:
      - "E_66"          -> ("E_66", None)
      - "E_58=3"        -> ("E_58", "3")
      - "E_58=V_3"      -> ("E_58", "V_3")
      - "E_58_@_3"      -> ("E_58", "3")
      - "E_58_@_V_3"    -> ("E_58", "V_3")
    """
    if "_@_" in token:
        base, val = token.split("_@_", 1)
        return base, val
    if "=" in token:
        base, val = token.split("=", 1)
        return base, val
    return token, None


@dataclass
class DiagnosisSession:
    """Stores what we know about the current patient interaction.

    - asked_bases: evidence concepts already asked (avoid repeats)
    - pos_items: positive evidence items (can include multiple values for one base)
    - neg_bases: asked and explicitly negative (e.g., no travel)
    - unk_bases: asked but unknown / refused
    """

    age: float
    sex: str
    asked_bases: Set[str] = field(default_factory=set)
    pos_items: Set[str] = field(default_factory=set)  # tokens like "E_66" or "E_58=V_3"
    neg_bases: Set[str] = field(default_factory=set)
    unk_bases: Set[str] = field(default_factory=set)

    def add_positive(self, token: str) -> None:
        """Add a positive finding (binary or value-coded)."""
        base, val = parse_token(token)
        self.asked_bases.add(base)
        if val is None:
            self.pos_items.add(base)
        else:
            # normalize to the token format used by mlb_token classes: "E_58=V_3"
            self.pos_items.add(f"{base}={val}")

    def add_negative(self, base: str) -> None:
        """Mark an evidence concept as explicitly negative."""
        self.asked_bases.add(base)
        self.neg_bases.add(base)

    def add_unknown(self, base: str) -> None:
        """Mark an evidence concept as asked but unknown."""
        self.asked_bases.add(base)
        self.unk_bases.add(base)

    @property
    def pos_bases(self) -> Set[str]:
        """Bases implied by positive items."""
        bases: Set[str] = set()
        for it in self.pos_items:
            b, _ = parse_token(it)
            bases.add(b)
        return bases

    def evidence_bases_for_ml(self) -> List[str]:
        """For base-encoding ML: return sorted positive base codes."""
        return sorted(self.pos_bases)

    def evidence_tokens_for_ml(self) -> List[str]:
        """For token-encoding ML: return sorted positive tokens/items."""
        return sorted(self.pos_items)

    def evidence_counts(self) -> Tuple[int, int, int]:
        """Return (num_bases_effective, num_items_effective, extra_multi_values)."""
        num_items = len(self.pos_items)
        num_bases = len(self.pos_bases)
        return num_bases, num_items, (num_items - num_bases)
