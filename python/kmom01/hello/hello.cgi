#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Using .cgi to publish a website!
"""
import sys
import codecs

import cgitb
cgitb.enable()

print("Content-Type: text/html;charset=utf-8")
print("")

pageContent = """
<!DOCTYPE html>
<html>
<head>
<title>.cgi Test Website</title>
<meta charset="utf-8">
</head>
<body>
<h1>Hello World!</h1>
<p>Saying Hello World through a .cgi script!</p>
</body>
</html>
"""



sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
sys.stdout.write(pageContent)
