# file: test_BasicLift.py

import pytest # need for the error raise checks
from aerodynamics.BasicLift import *

def test_freestream_dynamic_pressure():
    density = 1.225 # sea level kg/m^3
    velocity = 50 # m/s
    assert 1531.25 == freestream_dynamic_pressure( density, velocity)

def test_flight_coefficients():
    density = 1.225 # sea level kg/m^3
    velocity = 50 # m/s
    lift_force = 1000 # N
    area = 10 # m^2
    tolerance = 1e-3
    m_arm = 1 # m
    fs_pressure = freestream_dynamic_pressure( density, velocity)
    assert abs(flight_coefficients( lift_force, area, fs_pressure ) - 0.0653) < tolerance # lift
    assert abs(flight_coefficients( lift_force, area, fs_pressure, m_arm ) - 0.0653) < tolerance # moment

