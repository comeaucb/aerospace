# filename: BasicLift.py
# Implements equations from Chapter 01 Aerodynamics: Some Introductory Thoughts, 
# from "Fundamentals of Aerodynamics: 5th Ed" by 
# John D. Anderson, Jr, Copyright 2011 McGraw Hill

import numpy as np
from scipy.optimize import root_scalar

def freestream_dynamic_pressure( fs_density: float=0.0, fs_velocity: float=0.0 ) -> float:
    # Page 24
    # Implements the free stream dynamics pressure; the pressure far ahead of 
    # the airfoil (far enough that the airfoil being there has no effect)

    # fs_density
    # density of free stream fluid (kg/m³)
    # fs_velocity
    # velocity of fluid (m/s)
    # return is free stream pressure (Pa)
    return 0.5 * fs_density * pow(fs_velocity, 2)

def coefficient_lift( lift_force: float=0.0, surface_area: float=0.0, fs_dynamic_pressure: float=0.0 ) -> float:
    # Page 24
    # Calculates the Coefficient of Lift
    # lift_force
    # total lift upon the body (N)
    # surface_area
    # Total surface area lift is acting upon (m²)
    # returns coefficient of lift (no units)
    return lift_force / (fs_dynamic_pressure * surface_area )