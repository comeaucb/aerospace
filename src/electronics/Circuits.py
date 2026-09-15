"""file: Circuits.py
This library implements basic functions for electric circuits.
"""

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