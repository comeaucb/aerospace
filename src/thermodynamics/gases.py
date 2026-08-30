# filename: gases.py


def ideal_gas(N: float = None,
              T: float = None,
              V: float = None,
              P: float = None,
              R: float = 8.314) -> float:
    """
    @brief Compute one variable of the ideal gas law PV = nRT.

    @details
        This function determines which variable is missing (None) and computes it
        using the ideal gas equation:

        @code
            PV = nRT
        @endcode

        Exactly one of the variables (N, T, V, P) must be omitted (set to None).
        The function will solve for that variable.

    @param N
        Number of moles (mol). Set to None to solve for N.

    @param T
        Temperature (Kelvin). Set to None to solve for T.

    @param V
        Volume (m^3). Set to None to solve for V.

    @param P
        Pressure (Pascals). Set to None to solve for P.

    @param R
        Ideal gas constant. Default is 8.314 (J/mol*K).

    @return
        The computed value of the missing variable.

    @throws ValueError
        If zero or more than one variable is missing.
    """

    # Count missing variables
    missing = [var is None for var in (N, T, V, P)].count(True)
    if missing != 1:
        raise ValueError("Exactly one of N, T, V, or P must be None.")

    # Solve for the missing variable
    if P is None:
        return (N * R * T) / V
    if V is None:
        return (N * R * T) / P
    if N is None:
        return (P * V) / (R * T)
    if T is None:
        return (P * V) / (N * R)
