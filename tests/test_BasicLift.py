# file: test_BasicLift.py

import pytest # need for the error raise checks
from aerodynamics.BasicLift import *

def test_freestream_dynamic_pressure():
    assert 0.5 == freestream_dynamic_pressure( 1, 1 )