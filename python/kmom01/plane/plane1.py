#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Konvertarar olika värden till andra genom funktioner.
"""

# Definerar meterToFeet funktionen.
def meterToFeet(meter):
    """
    Konverterar meter till feet.
    """
    feet = meter*3.28084
    return feet

# Definerar km/h till mph funktionen.
def kmhToMph(kmh):
    """
    Konverterar km/h till mph.
    """
    mph = kmh*0.62137
    return mph

# Definerar Celsius till Farenheit funktionen.
def celsiusToFarenheit(celsius):
    """
    Konverterar celsius till farenheit.
    """
    farenheit = celsius*9/5+32
    return farenheit

print("1100 meter över havet konverterat till feet över havet ger", meterToFeet(1100), "feet.")
print("1000 km/h konverterat till mp/h ger", kmhToMph(1000), "mp/h")
print("-50 celsius konverterat till farenheit ger", celsiusToFarenheit(-50), "farenheit.")
