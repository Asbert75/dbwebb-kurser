#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Konvertarar olika värden till andra genom funktioner i en CGI-skript. Skickar också en korrekt HTTP-header.
"""


# To write pagecontent to sys.stdout as bytes instead of string
import sys
import codecs


# Enable debugging of cgi-.scripts
import cgitb
cgitb.enable()


# Send the HTTP header
#print("Content-Type: text/plain;charset=utf-8")
print("Content-Type: text/html;charset=utf-8")
print("")

content = """
<!doctype html>
<meta charset="utf-8">
<pre>
<!--
# Definerar meterToFeet funktionen.
def meterToFeet(meter):
    feet = meter*3.28084
    return feet

# Definerar km/h till mph funktionen.
def kmhToMph(kmh):
    mph = kmh*0.62137
    return mph

# Definerar Celsius till Farenheit funktionen.
def celsiusToFarenheit(celsius):
    farenheit = celsius*9/5+32
    return farenheit
-->
1100 meter över havet konverterat till feet över havet ger 3608.924 feet.
1000 km/h konverterat till mp/h ger 621.37 mp/h.
-50 celsius konverterat till farenheit ger -58 grader farenheit.
</pre>
"""


# Write page content
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
sys.stdout.write(content)
