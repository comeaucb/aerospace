# file: test_Circuits.py

import pytest # need for the error raise checks
from electronics.Circuits import *

def test_PIV():
    # Tests to show the equations are working.
    assert 3.0 == PIV(current=3.0, voltage=1.0) # power
    assert 2.0 == PIV(power=6.0, current=3.0) # voltage
    assert 4.0 == PIV(power=24.0, voltage=6.0) # current

    # Tests to show the ValueRaise Errors are working.
    # Missing too many arguments
    with pytest.raises(ValueError):
        PIV()  # all three missing

    # Missing one required argument for a branch
    with pytest.raises(ValueError):
        PIV(power=None, current=None, voltage=5.0)

    with pytest.raises(ValueError):
        PIV(power=None, current=3.0, voltage=None)

    # Calling with all three provided
    with pytest.raises(ValueError):
        PIV(power=10.0, current=2.0, voltage=5.0)