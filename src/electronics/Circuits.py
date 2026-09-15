"""file: Circuits.py
This library implements basic functions for electric circuits.
"""

def PIV( power=None, current=None, voltage=None) -> float:
    """
    Perform the Power = Current * Voltage calculation for the missing value.
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