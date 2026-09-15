# filename: CompressibleFlow.py
# Implements equations from Chapter 10: Compressible Flow through Nozzles, 
# Diffusers, and Wind Tunnels from "Fundamentals of Aerodynamics: 5th Ed" by 
# John D. Anderson, Jr, Copyright 2011 McGraw Hill

import numpy as np
from scipy.optimize import root_scalar

## @file compressible_flow.py
#  @brief Implements isentropic nozzle flow relations from Anderson's
#         *Fundamentals of Aerodynamics*, 5th Edition.
#
#  This module provides numerical solutions to the area–Mach relation
#  (Eq. 10.32), which governs isentropic flow of a calorically perfect gas
#  through nozzles, diffusers, and wind tunnels. For a given area ratio,
#  two Mach numbers satisfy the equation: one subsonic and one supersonic.
#

def a_over_astar(gamma: float = 1.4, area_ratio: float = 1.0):
    ## @brief Solve the area–Mach relation (Eq. 10.32) for a given area ratio.
    #
    #  This function computes both the subsonic and supersonic Mach numbers
    #  that satisfy the isentropic area–Mach relation:
    #
    #      A/A* = (1/M^2) * [ (2/(γ+1)) * (1 + (γ−1)M^2/2 ) ]^((γ+1)/(γ−1))
    #
    #  The equation is nonlinear and has two valid roots for M:
    #    - A subsonic root (M < 1)
    #    - A supersonic root (M > 1)
    #
    #  @param gamma      Ratio of specific heats (default 1.4 for air).
    #  @param area_ratio The ratio A/A* of duct area to sonic throat area.
    #
    #  @return A tuple (Msup, Msub) containing:
    #          - Msup : Supersonic Mach number solution
    #          - Msub : Subsonic Mach number solution
    #
    #  The numerical solver uses SciPy's fsolve with two different initial
    #  guesses to ensure convergence to the correct branch of the solution.
    #

    def relation(M):
        ## @brief Area–Mach relation residual function.
        #  @param M Mach number.
        #  @return Residual of Eq. 10.32 for root solving.
        term1 = 1.0 / M**2
        term2 = (2.0 / (gamma + 1.0)) * (1.0 + (gamma - 1.0) * M**2 / 2.0)
        exponent = (gamma + 1.0) / (gamma - 1.0)
        return term1 * term2**exponent - area_ratio**2

    # Supersonic root: bracket between Mach 1 and Mach 10
    Msup = root_scalar(relation, bracket=[1.0, 10.0]).root

    # Subsonic root: bracket between Mach 0 and Mach 1
    Msub = root_scalar(relation, bracket=[1e-6, 1.0]).root

    return Msup, Msub