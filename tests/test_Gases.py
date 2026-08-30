# file: test_Gases.py

import pytest
from thermodynamics.gases import *

def test_ideal_gas_solve_for_moles():
    pressure = 101_320
    temperature = 273.15
    volume = 1.0
    expected_moles = 44.606
    tolerance = 1e-2
    assert abs(ideal_gas(T=temperature, V=volume, P=pressure) - expected_moles) <= tolerance


def test_ideal_gas_solve_for_pressure():
    N = 44.606
    T = 273.15
    V = 1.0
    expected_pressure = 101_298.84
    tolerance = 1e-2
    assert abs(ideal_gas(N=N, T=T, V=V) - expected_pressure) <= tolerance


def test_ideal_gas_solve_for_volume():
    N = 44.606
    T = 273.15
    P = 101_320
    expected_volume = 1.0
    tolerance = 1e-2
    assert abs(ideal_gas(N=N, T=T, P=P) - expected_volume) <= tolerance


def test_ideal_gas_solve_for_temperature():
    N = 44.606
    V = 1.0
    P = 101_320
    expected_temperature = 273.20
    tolerance = 1e-2
    assert abs(ideal_gas(N=N, V=V, P=P) - expected_temperature) <= tolerance

def test_ideal_gas_invalid_missing_count():
    with pytest.raises(ValueError):
        ideal_gas(N=None, T=None, V=1.0, P=101_320)
