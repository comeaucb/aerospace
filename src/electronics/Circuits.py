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

def OhmsPowerLaw( power=None, voltage=None, current=None, resistance=None ) -> float:
    """
    Ohm's Power Law. P = V²/R = I²R for the missing value.
    Equation 2.16

    Parameters:
    ----------
    Power: float
        Watts
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

    # find power
    if power is None:
        # If you are wanting power, you must have resistance, 2 options
        if resistance is None and voltage is None:
            raise ValueError("To compute P = V²/R, you must provide voltage and resistance.")
        elif resistance is None and current is None:
            raise ValueError("To compute P = I²/R, you must provide current and resistance.")
        elif voltage is None: # compute via current
            return (current * current ) / resistance
        else: # # compute via voltage
            return ( voltage * voltage ) / resistance

    # find resistance
    elif resistance is None:
        # If you want resistance, you must have power, 2 options.
        if voltage is None and power is None:
            raise ValueError("To compute R = V²/P, you must provide voltage and power.")
        elif current is None and power is None:
            raise ValueError("To compute R = I²/P, you must provide current and power.")
        elif current is None: # computer via voltage
            return (voltage * voltage ) / power
        else: # compute via current
            return (current * current) / power

    # compute voltage
    elif current is None and power is None:
        return math.sqrt( power * resistance )

    # compute current
    elif voltage is None and current is None:
        return math.sqrt( power / resistance )