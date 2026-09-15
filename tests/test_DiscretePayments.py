# file: test-DiscretePayments.py

from engineering_economics.DiscretePayments import *

def test_simple_interest_final():
    assert simple_interest_final(0,0,0) == 0
    assert simple_interest_final(10,10,0) == 10
    assert simple_interest_final(10,10,0.1) == 20

def test_compound_interest_final():
    assert compound_interest_final(10,10,0) == 10
    assert compound_interest_final(0,10,10) == 0
    assert abs(compound_interest_final(10,10,0.1) - 25.9) < 0.1

def test_compound_present_worth():
    assert abs(compound_present_worth( 10, 10, 0.05 ) - 6.139) < 0.01

def test_compound_compound_amount():
    assert compound_compound_amount(1,10,0) == 0

def test_compound_sinking_fund():
    assert compound_sinking_fund(0,10,0) == 0