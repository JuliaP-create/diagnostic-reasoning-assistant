from __future__ import annotations

import pandas as pd
from scipy.sparse import csr_matrix, hstack

from .types import FeatureSpec


def encode_single_case(
    evidence_bases,  # list[str] like ["E_66", "E_201", ...] OR tokens if mlb_token is used
    sex,
    age,
    num_bases_effective: int,
    num_items_effective: int,
    extra_multi_values: int,
    *,
    mlb,
    ohe,
    scaler,
    feature_spec: FeatureSpec,
):
    """Encode one 'patient state' into a single-row sparse feature matrix.

    IMPORTANT: This MUST match the training feature construction in Notebook 02.
    """

    # 1) Evidence (multi-hot)
    X_e = mlb.transform([list(evidence_bases)])

    # 2) Categorical
    cat_data = {"SEX": sex}
    if "age_group" in feature_spec.cat_cols:
        if feature_spec.age_group_func is None:
            raise ValueError("age_group is in CAT_COLS but feature_spec.age_group_func is None.")
        cat_data["age_group"] = (
            feature_spec.age_group_func(pd.DataFrame({"AGE": [age]}))["age_group"].iloc[0]
        )
    X_c = ohe.transform(pd.DataFrame([cat_data])[feature_spec.cat_cols])

    # 3) Numeric (scaled) — use DataFrame to keep feature names
    num_df = (
        pd.DataFrame(
            [
                {
                    "AGE": float(age),
                    "num_bases_effective": float(num_bases_effective),
                    "num_items_effective": float(num_items_effective),
                    "extra_multi_values": float(extra_multi_values),
                }
            ]
        )[feature_spec.num_cols]
        .astype(float)
    )

    num_scaled = scaler.transform(num_df)
    X_n = csr_matrix(num_scaled)

    # 4) Combine
    return hstack([X_e, X_c, X_n], format="csr")
