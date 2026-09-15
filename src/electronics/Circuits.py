"""file: Circuits.py
This library implements basic functions for electric circuits.
"""

import math

def PIV( power=None, current=None, voltage=None) -> float:
    """
    P = IV for the missing value.
    Equation 2.3

    Parameters:
    ----------
    power: float
        Watts
    current: float
        amperes
    voltage: float
        volts

    Returns:
    -------
    float
    """
    # If power is missing, compute it
    if power is None:
        if current is None or voltage is None:
            raise ValueError("To compute power, provide current and voltage.")
        return current * voltage

    # If current is missing, compute it
    elif current is None:
        if power is None or voltage is None:
            raise ValueError("To compute current, provide power and voltage.")
        return power / voltage

    # If voltage is missing, compute it
    elif voltage is None:
        if power is None or current is None:
            raise ValueError("To compute voltage, provide power and current.")
        return power / current

    # If all 3 were provided.
    else:
        raise ValueError("Why did you call this function if you already know all 3?")


def OhmsLaw( voltage=None, current=None, resistance=None ) -> float:
    """
    Ohm's Law. V = IR for the missing value.
    Equation 2.15

    Parameters:
    ----------
    Voltage: float
        Volts
    Current: float
        Amperes
    Resistance: float
        Ohms

    Returns:
    -------
    float
    """

    # find voltage
    if voltage is None:
        if current is None or resistance is None:
            raise ValueError("To compute voltage, provide current and resistance.")
        return current * resistance

    # find current
    if current is None:
        if voltage is None or resistance is None:
            raise ValueError("To compute current, provide voltage and resistance.")
        return voltage / resistance

    # find resistance
    if resistance is None:
        if current is None or voltage is None:
            raise ValueError("To compute resistance, provide current and voltage.")
        return voltage / current

    # If all 3 were provided.
    else:
        raise ValueError("Why did you call this function if you already know all 3?")

def OhmsPowerLaw(power=None, voltage=None, current=None, resistance=None) -> float:
    """
    Ohm's Power Law. Computes the missing value using:
        P = V^2 / R
        P = I^2 * R
        V = sqrt(P * R)
        I = sqrt(P / R)
        R = V^2 / P
        R = P / I^2
    """

    # --- Compute POWER ---
    if power is None:
        # Need resistance + (voltage or current)
        if resistance is None:
            raise ValueError("To compute power, provide resistance and either voltage or current.")

        if voltage is not None:
            return (voltage * voltage) / resistance

        if current is not None:
            return (current * current) * resistance

        raise ValueError("To compute power, provide voltage or current.")

    # --- Compute RESISTANCE ---
    if resistance is None:
        # Need power + (voltage or current)
        if power is None:
            raise ValueError("To compute resistance, provide power and either voltage or current.")

        if voltage is not None:
            return (voltage * voltage) / power

        if current is not None:
            return power / (current * current)

        raise ValueError("To compute resistance, provide voltage or current.")

    # --- Compute VOLTAGE ---
    if voltage is None:
        # Need power + resistance
        if power is None or resistance is None:
            raise ValueError("To compute voltage, provide power and resistance.")
        return math.sqrt(power * resistance)

    # --- Compute CURRENT ---
    if current is None:
        # Need power + resistance
        if power is None or resistance is None:
            raise ValueError("To compute current, provide power and resistance.")
        return math.sqrt(power / resistance)

    # --- If all four provided ---
    raise ValueError("All four values provided; nothing to compute.")