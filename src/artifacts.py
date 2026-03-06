from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, Optional

import joblib


def load_json(path: Path | str) -> dict:
    path = Path(path)
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def load_joblib(path: Path | str) -> Any:
    path = Path(path)
    return joblib.load(path)


def load_preprocessors(path: Path | str) -> Dict[str, Any]:
    """Load preprocessors artifact saved from Notebook 02.

    Expected to contain at least:
    - ohe, scaler, label_encoder
    - mlb_base and mlb_token (preferred) OR a single mlb (legacy)
    """
    art = load_joblib(path)

    # Backward-compatible convenience aliases
    if "mlb_base" not in art and "mlb" in art:
        art["mlb_base"] = art["mlb"]

    return art


def resolve_best_token_model(
    models_dir: Path | str,
    *,
    calibrated_name: str = "logreg_token_calibrated.joblib",
    raw_name: str = "logreg_token_multinomial.joblib",
):
    """Load the calibrated token model if present; otherwise fall back to raw token LR."""
    models_dir = Path(models_dir)
    cal_path = models_dir / calibrated_name
    raw_path = models_dir / raw_name

    if cal_path.exists():
        return load_joblib(cal_path)
    if raw_path.exists():
        return load_joblib(raw_path)

    raise FileNotFoundError(f"Neither {cal_path} nor {raw_path} exists.")


def load_policy_artifacts(path: Path | str) -> Dict[str, Any]:
    """Load policy artifacts (p_e_given_d, evidence_bases, evidence_index, ...)."""
    return load_joblib(path)
