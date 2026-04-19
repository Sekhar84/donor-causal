"""
Randomisation check — first and most important step.

Tests covariate balance between treatment and control groups.
Standardised Mean Difference (SMD) > 0.1 indicates meaningful
imbalance — evidence that assignment was not random.

Everything else follows from this result. If assignment is
confounded, the entire analytical strategy shifts.
"""
import pandas as pd
import numpy as np
from scipy import stats


def check_covariate_balance(
    df: pd.DataFrame,
    treatment_col: str,
    covariates: list[str],
) -> pd.DataFrame:
    """
    Compute SMD and Mann-Whitney p-value per covariate.

    Returns DataFrame with columns:
        covariate, smd, p_value, imbalanced (bool)

    SMD > 0.1 per covariate → IMBALANCED → assignment not random.
    Result is recorded, not predetermined.
    """
    raise NotImplementedError("Implement in Sprint 2 (Jun 6–14)")


def plot_love_plot(balance_df: pd.DataFrame) -> None:
    """Love plot — visual summary of SMD before/after matching."""
    raise NotImplementedError("Implement in Sprint 2 (Jun 6–14)")
