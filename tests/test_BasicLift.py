# file: test_BasicLift.py

import pytest # need for the error raise checks
from aerodynamics.BasicLift import *

def test_freestream_dynamic_pressure():
    assert 0.5 == freestream_dynamic_pressure( 1, 1 )

def test_coefficient_lift():
    fs_pressure = freestream_dynamic_pressure( 1, 1 )
    assert 2 == coefficient_lift( 1, 1, fs_pressure )