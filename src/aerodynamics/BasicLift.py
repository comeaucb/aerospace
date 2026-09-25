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

def coefficient_lift( lift_force: float=0.0, surface_area: float=0.0, fs_dynamic_pressure: float=0.0 ) -> float:
    ## @brief Calculates the coefficient of lift for a body.
    # Page 24
    #
    # @param lift_force: total lift upon the body (N)
    # @param surface_area: total surface area lift is acting upon (m²)
    # @return coefficient of lift (no units)
    return lift_force / (fs_dynamic_pressure * surface_area )