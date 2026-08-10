"""file: PointMasses.py
This library implements basic functions for point masses.
"""

import math

def vector_magnitude(ax: float = 0.0, ay: float = 0.0, az: float = 0.0) -> float:
    """
    Compute the magnitude of a 3D vector.
    Equation 1.4, page 4

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

def vector_direction_angle(direction_magnitude: float = 0.0, vector_magnitude: float = 0.0, 
                           return_degrees: bool = True ) -> float:
    """
    Computes the direction angle of a vector component.
    Equation 1.6, page 4

    Parameters
    ----------
    direction_magnitude : float
        Component magnitude of vector.
    vector_magnitude : float
        Overall magnitude of vector.
    return_degrees : bool
        If set to true (default), then value returned is in degrees.

    Returns
    -------
    float
        Either the degrees or radians of the direction of the vector component

    """
    if vector_magnitude == 0.0:
        # Divide by zero check
        return 0.0

    angle = math.acos( direction_magnitude / vector_magnitude )

    if return_degrees == True:
        return math.degrees( angle )
    else:
        return angle