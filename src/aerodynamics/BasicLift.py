# filename: BasicLift.py
# Implements equations from Chapter 01 Aerodynamics: Some Introductory Thoughts, 
# from "Fundamentals of Aerodynamics: 5th Ed" by 
# John D. Anderson, Jr, Copyright 2011 McGraw Hill

import numpy as np
from scipy.optimize import root_scalar

def freestream_dynamic_pressure( fs_density: float=0.0, fs_velocity: float=0.0 ) -> float:
    ## @brief: Implements the free stream dynamics pressure; the pressure far 
    # ahead of the airfoil (far enough that the airfoil being there has no effect).
    # Page 24
    # 
    # @param fs_density: density of free stream fluid (kg/m³)
    # @param fs_velocity: velocity of fluid (m/s)
    # @return Free stream pressure (Pa)
    return 0.5 * fs_density * pow(fs_velocity, 2)

def flight_coefficients( force: float=0.0, surface_area: float=0.0, fs_dp: float=0.0, m_arm: float=None ) -> float:
    ## @brief Calculates the coefficient for a body depding  on what force is
    # inputed into the function.
    # Coefficient of Lift = force / (fs_dp * surface_area)
    # Coefficient of Drag, Normal Force, and Axial force computed in same way
    # as CL.
    # Moment Coefficient = force / (fs_dp * surface_area * m_arm )
    # Page 24
    # 
    #
    # @param force: total force upon the body (N)
    # @param surface_area: total surface area lift is acting upon (m²)
    # @param fs_dp: free stream dynamic pressure (Pa)
    # @param m_arm: moment arm (m)
    # @return coefficient of lift (no units)

    if m_arm is None:
        return force / (fs_dp * surface_area )
    else:
        return force / (fs_dp * surface_area * m_arm )