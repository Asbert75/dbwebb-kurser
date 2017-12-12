#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Convertarar olika värden till andra genom funktioner.
"""

# Definerar meterToFeet funktionen.
def meterToFeet(meter):
    """
    Converterar meter till feet.
    """
    feet = meter*3.28084
    return feet

# Definerar km/h till mph funktionen.
def kmhToMph(kmh):
    """
    Converterar km/h till mph.
    """
    mph = kmh*0.62137
    return mph

# Definerar Celsius till Farenheit funktionen.
def celsiusToFarenheit(celsius):
    """
    Converterar celsius till farenheit.
    """
    farenheit = celsius*9/5+32
    return farenheit

try:
    userValue = float(input("Var vänlig ange en höjd över havet i meter (m):\n"))
    print(meterToFeet(userValue))
except Exception:
    print("Du angav inte en giltig höjd")

try:
    userValue = float(input("Var vänlig ange en hastighet i kilometer per timme (km/h):\n"))
    print(kmhToMph(userValue))
except Exception:
    print("Du angav inte en giltig hastighet")
try:
    userValue = float(input("Var vänlig ange en temperatur i celsius (c):\n"))
    print(celsiusToFarenheit(userValue))
except Exception:
    print("Du angav inte en giltig temperatur.")
