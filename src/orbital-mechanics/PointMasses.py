"""Point Masses
This library implements basic functions for point masses.
"""

import math

def vector_magnitude(ax: float = 0.0, ay: float = 0.0, az: float = 0.0) -> float:
    """
    Compute the magnitude of a 3D vector.

    Parameters
    ----------
    ax : float
        X component of the vector.
    ay : float
        Y component of the vector.
    az : float
        Z component of the vector.

    Returns
    -------
    float
        The Euclidean magnitude of the vector.
    """
    return math.sqrt(ax**2 + ay**2 + az**2)