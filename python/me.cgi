#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Här exekverar jag ett cgi-skript och skickar en HTTP header.

"""


# To write pagecontent to sys.stdout as bytes instead of string
import sys
import codecs


#Enable debugging of cgi-.scripts
import cgitb
cgitb.enable()


# Send the HTTP header
#print("Content-Type: text/plain;charset=utf-8")
print("Content-Type: text/html;charset=utf-8")
print("")

# Här lägger jag in ASCII-text för senare användning på sidan.
wickedASCII = r"""
__          _______ _____ _  ________ _____
\ \        / /_   _/ ____| |/ /  ____|  __ \
 \ \  /\  / /  | || |    | ' /| |__  | |  | |
  \ \/  \/ /   | || |    |  < |  __| | |  | |
   \  /\  /   _| || |____| . \| |____| |__| |
    \/  \/   |_____\_____|_|\_\______|_____/
"""



# Here comes the content of the webpage
content = """<!doctype html>
<meta charset="utf-8">
<title>Min me-sida</title>
<pre>
Min Me-sida
_________________________________________________________________________________

<h1>Om mig</h2>
Mitt namn är <i>Erik Olsson</i>, jag går online under smeknamnet Wicked,
jag är en 19-årig kille från Stenungsund som har ett stort intresse för allt
som relaterar till webbutveckling. Jag har precis tagit studenten från
Nösnäsgymnasiet där jag läste linjen Informations -och medieteknik.

{image}

Mina fritidsintressen inkluderar att designa olika grejer i Photoshop, så som
hemsidor, forum-avatarer, logos och logotyper, signaturer och andra grafiska
föremål. Annat som jag brukar göra på min fritid är att spela olika spel
(för det mesta World of Warcraft eller Counter-Strike), hänga med polare, gå
på promenader och att åka longboard. Jag har också ett stort intresse för sport
och gick själv i handboll från att jag var 9 tills för 2 år sedan. Innan det
spelade jag fotboll så långt tillbaks jag kan minnas.

Som gymnasiearbete gjorde jag det enda jag tycker är rätt, nämligen startade en
webbdesignbyråe med några andra ifrån min klass, med syftet att lära oss mer
om både webbutvecklingen i sig, men också hur det är att jobba som
webbutvecklare. Vår sida finns att hitta på http://www.webdesign-sto.se och där kan
man även hitta några utav de hemsidor vi skapade under denna tid.
Under gymnasiearbetets gång så hade vi inte lärt oss så mycket om Drupal, och
jag har inte heller kollat något på det själv hemma, vilket ledde till att vi
valde att inte använda oss av några CMS:er just för dessa hemsidor.


Jag tycker att denna kurs är en bra chans för mig att få lära mig mer om
webbutveckling  och programmering samtidigt som jag kan arbeta ihop lite pengar
eftersom det endast är halvtakt, vilket passar väldigt bra just nu då jag
egentligen tänkt ta ett sabbatsår men tänkte att eftersom det bara är halvtakt
så får jag lärt mig något samtidigt som jag ändå har det lite "ledigt".
</pre>
"""


# Write page content
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
sys.stdout.write(content.format(image=wickedASCII))
