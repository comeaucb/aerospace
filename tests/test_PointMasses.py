# file: test-PointMasses.py

from orbital_mechanics.PointMasses import *

def test_vector_magnitude():
    assert vector_magnitude(0, 0, 0) == 0.0
    assert vector_magnitude(3, 4, 0) == 5.0

def test_vector_direction_angle():
    tolerance = 1e-2
    assert abs(vector_direction_angle( 1, 9, True ) - 83.62) <= tolerance
    assert abs(vector_direction_angle( 1, 9 ) - 83.62) <= tolerance
    assert abs(vector_direction_angle( 1, 9, False ) - 1.4594) <= tolerance
