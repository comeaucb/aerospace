# filename: DiscretePayments.py

import math

def simple_interest_final( principal: float = 0.0,
                           periods: float = 0.0,
                           interest_rate: float = 0.0 ):
    """
    Calculate the final value after simple interest is applied.
    Equation 3.2 page 65

    Parameters
    ----------
    principal : float
        Initial account value.
    periods : float
        Number of periods.
    interest_rate : float
        Interest rate in decimal form (e.g., 0.05 for 5%).

    Returns
    -------
    float
        Final value after compound interest.
    """

    return principal * ( 1 + interest_rate * periods )

def compound_interest_final(
    principal: float = 0.0,
    periods: float = 0.0,
    interest_rate: float = 0.0
) -> float:
    """
    Calculate the final value after compound interest is applied.
    Equation 3.3 page 65

    Parameters
    ----------
    principal : float
        Initial account value.
    periods : float
        Number of compounding periods.
    interest_rate : float
        Interest rate in decimal form (e.g., 0.05 for 5%).

    Returns
    -------
    float
        Final value after compound interest.
    """
    return principal * (1 + interest_rate) ** periods