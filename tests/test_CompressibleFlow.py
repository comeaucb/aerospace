# file: test_CompressibleFlow.py

from aerodynamics.CompressibleFlow import *

def test_a_over_astar():
    gamma = 1.4
    area_ratio = 2.0

    Msup, Msub = a_over_astar(gamma, area_ratio)

    # Expected values from isentropic flow tables
    expected_sub = 0.3059038
    expected_sup = 2.2

    # Numerical solvers require tolerances
    assert abs(Msub - expected_sub) <= 1e-4
    assert abs(Msup - expected_sup) <= 1e-2
