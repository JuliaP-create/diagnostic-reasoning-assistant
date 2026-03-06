from __future__ import annotations

from typing import List

import numpy as np

from .types import DiagnosisSession


def estimate_p_e_given_d(X_e_train, y_train, n_classes: int, alpha: float = 1.0) -> np.ndarray:
    """Estimate p(e=1 | d) for each disease d and each evidence base e.

    Uses Laplace smoothing (alpha) to avoid zeros.
    Returns:
      p shape (n_classes, n_evidences)
    """
    n_evid = X_e_train.shape[1]
    p = np.zeros((n_classes, n_evid), dtype=float)

    for c in range(n_classes):
        mask = (y_train == c)
        n_c = int(mask.sum())
        if n_c == 0:
            p[c, :] = 0.5  # fallback
            continue

        sums = np.asarray(X_e_train[mask].sum(axis=0)).ravel()
        p[c, :] = (sums + alpha) / (n_c + 2.0 * alpha)

    return p


def entropy(p: np.ndarray, eps: float = 1e-12) -> float:
    p = np.clip(p, eps, 1.0)
    return float(-np.sum(p * np.log(p)))


def choose_next_question_info_gain(
    session: DiagnosisSession,
    disease_proba: np.ndarray,      # model posterior over diseases
    p_e_given_d: np.ndarray,        # shape (n_classes, n_evidences)
    evidence_bases: List[str],      # same order as mlb_base.classes_
    evidences_map: dict,
    top_n: int = 5,
):
    """Rank next evidence bases using expected entropy reduction (information gain).

    Notes:
    - candidates are base evidences (223), not value-level tokens
    - skips anything already in session.asked_bases
    """
    post = disease_proba / (disease_proba.sum() + 1e-12)
    H_before = entropy(post)

    candidates = []
    for j, base in enumerate(evidence_bases):
        if base in session.asked_bases:
            continue

        p_yes = float(np.sum(post * p_e_given_d[:, j]))
        p_no = 1.0 - p_yes

        # Posterior if YES
        post_yes = post * p_e_given_d[:, j]
        if post_yes.sum() > 0:
            post_yes = post_yes / post_yes.sum()
        H_yes = entropy(post_yes)

        # Posterior if NO
        post_no = post * (1.0 - p_e_given_d[:, j])
        if post_no.sum() > 0:
            post_no = post_no / post_no.sum()
        H_no = entropy(post_no)

        H_after = p_yes * H_yes + p_no * H_no
        ig = H_before - H_after

        q_text = evidences_map.get(base, {}).get("question_en") or evidences_map.get(base, {}).get("question-fr") or ""
        candidates.append((base, ig, p_yes, q_text))

    # Sort descending by IG
    candidates.sort(key=lambda x: x[1], reverse=True)
    return candidates[:top_n]


def update_posterior_with_answer(
    posterior: np.ndarray,
    base: str,
    answer: str,  # "yes" | "no" | "unknown"
    *,
    p_e_given_d: np.ndarray,
    evidence_index: dict,
    beta: float = 0.7,
    eps: float = 1e-12,
) -> np.ndarray:
    """Update disease posterior given a YES/NO/UNKNOWN answer for a base evidence.

    beta < 1 makes the update conservative (recommended in early prototype).
    """
    if answer == "unknown":
        return posterior

    j = evidence_index.get(base, None)
    if j is None:
        return posterior

    post = posterior / (posterior.sum() + eps)
    p = np.clip(p_e_given_d[:, j], eps, 1.0 - eps)

    if answer == "yes":
        like = np.power(p, beta)
    elif answer == "no":
        like = np.power(1.0 - p, beta)
    else:
        raise ValueError("answer must be yes/no/unknown")

    post2 = post * like
    s = float(post2.sum())
    return post if s <= 0 else (post2 / s)
