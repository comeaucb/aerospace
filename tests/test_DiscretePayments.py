# file: tests-PointMasses.py

from engineering_economics.DiscretePayments import *

def test_simple_interest_final():
    assert simple_interest_final(0,0,0) == 0
    assert simple_interest_final(10,10,0) == 10
    assert simple_interest_final(10,10,0.1) == 20

def test_compound_interest_final():
    assert compound_interest_final(10,10,0) == 10
    assert compound_interest_final(0,10,10) == 0
    assert abs(compound_interest_final(10,10,0.1) - 25.9) < 0.1