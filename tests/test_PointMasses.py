# file: tests-PointMasses.py

from orbital_mechanics.PointMasses import vector_magnitude

def test_vector_magnitude():
    assert vector_magnitude(0, 0, 0) == 0.0
    assert vector_magnitude(3, 4, 0) == 5.0
