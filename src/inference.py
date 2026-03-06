from __future__ import annotations

import numpy as np

from .encoding import encode_single_case
from .types import DiagnosisSession, FeatureSpec


def predict_topk_from_session(
    session: DiagnosisSession,
    model,
    *,
    mlb,
    ohe,
    scaler,
    label_encoder,
    feature_spec: FeatureSpec,
    k: int = 5,
):
    """Base-encoding inference: session -> features -> top-k diseases + full posterior."""
    bases = session.evidence_bases_for_ml()
    num_bases, num_items, extra = session.evidence_counts()

    X = encode_single_case(
        evidence_bases=bases,
        sex=session.sex,
        age=session.age,
        num_bases_effective=num_bases,
        num_items_effective=num_items,
        extra_multi_values=extra,
        mlb=mlb,
        ohe=ohe,
        scaler=scaler,
        feature_spec=feature_spec,
    )

    proba = model.predict_proba(X)[0]  # shape (n_classes,)
    top_idx = np.argsort(proba)[::-1][:k]
    top = [(label_encoder.inverse_transform([i])[0], float(proba[i])) for i in top_idx]
    return top, proba


def predict_topk_from_session_token(
    session: DiagnosisSession,
    model,  # calibrated token model (preferred) or raw logreg_token model
    *,
    mlb_token,
    ohe,
    scaler,
    label_encoder,
    feature_spec: FeatureSpec,
    k: int = 5,
):
    """Token-encoding inference: session -> token features -> top-k diseases + full posterior."""
    tokens = session.evidence_tokens_for_ml()
    num_bases, num_items, extra = session.evidence_counts()

    X = encode_single_case(
        evidence_bases=tokens,  # yes: param name says "bases" but we pass tokens when using mlb_token
        sex=session.sex,
        age=session.age,
        num_bases_effective=num_bases,
        num_items_effective=num_items,
        extra_multi_values=extra,
        mlb=mlb_token,
        ohe=ohe,
        scaler=scaler,
        feature_spec=feature_spec,
    )

    proba = model.predict_proba(X)[0]
    top_idx = np.argsort(proba)[::-1][:k]
    top = [(label_encoder.inverse_transform([i])[0], float(proba[i])) for i in top_idx]
    return top, proba
