"""
Power analysis for proposed 2x3 factorial RCT.

Factor 1 — Pack type (2 levels): Standard vs Gadget
Factor 2 — Donor segment (3 levels): Active, Warm, AtRisk

If causal analysis concludes observational data is insufficient,
this design is ready to propose without delay.

Bonferroni correction: 9 tests → alpha_adjusted = 0.05/9 = 0.0056
"""
import numpy as np
from scipy import stats


def power_for_proportion_test(
    p_control: float,
    mde: float,
    alpha: float = 0.05,
    power_target: float = 0.80,
) -> int:
    """
    Sample size per arm for a two-proportion z-test.

    Args:
        p_control: baseline response rate in control arm
        mde: minimum detectable effect (e.g. 0.03 = 3pp lift)
        alpha: significance level (use Bonferroni-adjusted for multiple tests)
        power_target: desired statistical power

    Returns:
        n: required sample size per arm
    """
    raise NotImplementedError("Implement in Sprint 2 (Jun 6–14)")
