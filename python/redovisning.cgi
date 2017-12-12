#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Me-page redovisning som cgi-skript, här kommer jag uppdatera mina redovisningar
under kursensgång.

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


# Here comes the content of the webpage
content = """<!doctype html>
<meta charset="utf-8">
<title>Min redovisnings-sida</title>
<pre>
Min Redovisnings-sida
==============================================================================

<h1>Kmom01:</h1>
------------------------------------------------------------------------------

<h2>Vilken utvecklingsmiljö använder du?</h2>
Jag har valt att använda mig av Windows 7 (skulle haft Windows 10 men det vägrar
att fungera på min dator sedan jag skaffade nya delar) då jag känner mig bekväm
med att arbeta med just Windows. Jag har laddat ner Atom och lärt känna hur det
fungerar genom att helt gå över från Notepad++ och Brackets till att bara
använda Atom för mina andra sido-projekt (hemsida till min guild på World of
Warcraft t.ex.). Jag har också laddat ner Cygwin och Python3 och försöker att
lära mig litte  bättre hur den unix-baserade kommandtolken används/fungerar.
Vi läste lite om Linux/Ubunut osv. i skolan men jag har inget vidare minne av
just alla kommandon som finns. Cd, ls, mkdir och så vidare är jag dock väldigt
bekant med men de mer invecklade kommandona har jag ingen vidare koll på (inte
för att det är något vi behöver kunna just för detta kursmoment, tyckte bara
det kunde vara kul att lära sig).



<h2>Är du bekant med Python sedan tidigare?</h2>
Nej faktiskt inte, Python är ett utav de programmeringsspråket som jag länge
har planerat att lära mig men det har aldrig blivit av då jag inte haft så
mycket tid förut. När jag blev antagen till denna kurs tänkte jag att jag
skulle göra klart Python-kursen på http://www.codecademy.com, men eftersom
jag jobbat så mycket denna sommaren har jag inte hunnit med det denna gång
heller tyvärr, så det ska bli intressant att läsa det nu!



<h2>Är du bekant med programmering och problemlösning sedan tidigare?</h2>
Ja det är jag, har hållt på och programmerat i både C++, C#, Lua och lite
JavaScript sedan några år tillbaka (fast inte så hemskt mycket sedan jag
började gymnasiet, mer än JavaScript som jag läst på gymnasiet då). Så jag har
väl ganska bra erfarenhet av programmering och problemlösning.

Har skrivit allt från egna miniräknare och enkla \"alternativ-spel\" till lite
större och mer invecklade grejer så som Creature-scripts för spelservrar och
liknande



<h2>Är du bekant med terminalen och Unix-kommandon sedan tidigare?</h2>
Jag är lite bekant med det ja, men inte så hemskt mycket. Som jag skrev lite
längre upp så har vi under gymnasiet gått igenom kommandon för den
unix-baserade terminalen, men det var inte så hemskt mycket och vi använde det
aldrig till något så jag har inte så hemskt bra minne av alla kommandon utan
kan endast några få.



<h2>Gick det bra att komma igång med kursmomentet, var det lagom, för litet, för
stort?</h2>
Jag tycker att det har gått väldigt bra med detta kursmoment, det var en bra
\"storlek\" på arbetet och man fick lära sig grunderna för det som komma skall
(eller vad jag förväntar mig iallafall).



<h2>Vilken del av kursmaterialet (böcker, artiklar, videor, etc) uppskattade du
mest?</h2>
Jag är en person som inte gillar att läsa böcker, men när det gäller något man
faktiskt är djupt intresserad av, istället för någon löjligt roman eller
drama bok, då kan jag faktiskt tycka att det är väldigt roligt att läsa, och
just så har det varit nu. Jag tycker böckerna var den bästa delen i detta
moment.


<h1>Kmom02:</h1>
------------------------------------------------------------------------------

<h2>Reflektion</h2>
Jag tyckte detta moment var ett både mycket lärorikt och mycket roligt moment.
Vi fick arbeta mycket med ett antal olika syntax och funktioner i Python och
man hade mycket yta att hitta på lite vad man ville om man kände sig kreativ.

Eftersom jag har programmerat ganska mycket i andra språk så som JS, C++ och C#
där man använder sig av semicolon för att avsluta rader så har jag haft väldigt
mycket \"tvångstankar\" om att vilja sätta semicolon varje gång jag börjar på
en ny rad, men då har jag fått fy skam av valideringsverktyget vilket har
underlättat det hela väldigt mycket till att jag nu har börjat få in känslan
för att det faktiskt GÅR att programmera utan att alltid avsluta med semicolon.

Det är lite annat som också har varit lite svårt för mig att sätta mig in i när
jag gått från andra språk till Python och det är att man inte använder sig av
paranteser för t.ex. if-satser när man skriver själva if-delen, och att man
inte använder sig av brackets för funktioner, \"stycken\", if-satser och
liknande. Det har varit lite jobbigt att vänja sig, men jag tror jag börjar
få in känslan i mina fingrar och tanken i huvudet nu. Jag kan definitivt känna
att jag lärt mig en hel del från detta moment. Jag hade lite problem i början
eftersom jag så jätte gärna ville sätta ut en massa fina semicolon, parantseser
och brackets, men jag lärde mig ändå relativt snabbt att det inte riktigt
funkade så som i de andra språk jag använt mig av.

I slutändan är jag ändå nöjd med mitt resultat och jag tycker att jag har fått
till en väldigt trevlig bot med en relativt enkelläst kod och bra struktur. Jag
har fått en känsla lite för hur man kan sätta ihop funktioner på så sätt att
man inte behöver repetera en stor del kod i flera andra funktioner utan man kan
istället bara kalla på en funktion i alla dessa fall istället. Jag har också
hittat hur Python hanterar \"här slutar funktionen\" när språket inte använder
sig av semicolon och brackets som sagt tidigare. Kanske egentligen är
självklart att den använder sig av indentation och man kände sig lite dum när
man läste det, men jag kunde faktiskt inte lista ut det, om jag ska vara helt
ärlig.


<h2>Hur känns syntaxen i Python? Är det enkelt att se programmets struktur och
vad det gör?</h2>
Jag tycker helt klart att det känns väldigt bra, Python känns nästan lite som
ren engelska om man jämför med t.ex. C++. t.ex. \"if x is y\" istället för
\"if (x == y)\". Även om båda är enkla att förstå och enkla att läsa så kan
man tycka att det blir lite enklare när man tar bort paranteserna, just i detta
fall kanske man hellre har x == y än x is y då if och is är ganska lika och man
då kanske läser lite fel, men det är väl upp till var och en hur dem läser.
Annars tycker jag att språket är enkelt att förstå och strukturen förstår man
sig på. Den har en logik som är lätt att förstå.

<h2>Hur går det med valideringen av uppgifterna?</h2>
Det går bra, jag har stött på några valideringsfel ett antal gånger men det
har varit lätt att förstå vad som är fel mestadels av tiden, när det inte har
varit det så har google varit till stor hjälp och snabbt hjälpt mig hitta
lösningen. (T.ex. som i början när den gav mig något fel om line-breaks och
jag inte förstöd vad den menade, visade sig att jag bara kunde klicka på CRLF
så att det istället byte till LF radbrytningar.)

<h2>Är du överens med pylint om eventuella felmeddelanden vid valideringen?</h2>
Ja hittils har jag väl varit överens med pylint. Jag är ju inget proffs på
python och jag kanske förstår frågan fel men den har ju inte haft fel i sina
felmeddelanden iallafall.

<h2>Hur gick det att utföra uppgifterna, var de enkla eller svåra?</h2>
Jag tycker att precis som i förra momentet så var uppgifterna på en bra nivå
och extrauppgifterna gav en extra chans att göra något lite mer invecklat
om man kände för det, tyvärr har jag haft lite fullt upp denna veckan och har
därför valt att inte göra dem. Har dock tänkt göra dem framöver när jag får tid
för att lära mig extra.


<h1>Kmom03:</h1>
------------------------------------------------------------------------------

<h2>Reflektion</h2>
Detta moment var ett väldigt intressant moment med mycket nya och riktigt
roliga grejer att lära sig. Moduler och att använda sig av / skapa filer är
något som jag inte har lärt mig så mycket av i de andra språk jag programmerat.
Eller jo, moduler har jag använt mig av en del, men att skapa/öppna filer och
läsa av innehållet i dem är något jag inte gjort mycket alls förut och det är
också något jag tycker är väldigt spännande. Under labben hade jag lite problem
med att få filerna som jag öppnat att fungera som jag ville, av någon anledning
kunde jag inte använda samma fil jag öppnat redan flera gånger under samma
variabel utan var tvungen att öppna den igen i nya variablar för att jag skulle
få rätt på uppgiften. Har inte riktigt fattat varför ännu, men det tog mig ett
tag att lista ut hur jag skulle lösa problemet. Jag använde mig utav print
felsökning och kom tillslut fram till att det inte var något fel i koden men
att det inte funkade ändå och testade därför att helt enkelt öppna filen i
en ny variabel och helt plötsligt så funkade det.

Det som var svårast under detta arbete var nog att vända på ord. Tog ett tag
innan jag fattade hur man skulle göra genom att använda sig av slice. Att helt
enkelt börja från 0 och gå till slutet av ordet, sen bara använda sig av step
för att gå baklänges 1 steg varje gång. Alltså word[::-1]. Har inte använt
mycket wordslicing förut och visste därför inte riktigt hur det fungerade, har
ju självklart använt mig av [0] o.s.v för arrays och liknande, men som sagt
aldrig av slicing. Men jag kan tänka mig att man kan ha stor nytta av att kunna
använda sig av det i många olika områden.

Jag tror att jag ibland gör det mer invecklat för mig än det behöver vara, t.ex.
när när jag skulle göra momentet där man skulle få input på ett ord, och sedan
scrambla ordet så att det blev något helt annat men med samma bokstäver. Först
satt jag en stund och tänkte på om man kanske kunde använda sig av splice på
något sätt för att göra det. Typ lägga in allt i en for-loop och har ett
incremerande nummer inuti splicen t.ex. word[a] och ha att a blir ett nytt tal
efter varje loop beroende på längden av ordet, och sedan ta bort word[a] från
strängen efter varje loop så att bara bokstäverna som inte redan använts fanns
kvar i ordet. Men efter att ha tänkt på det en stund så kom jag fram till att
det fanns ett mycket enklare sätt (genom leta runt lite på internet) som helt
enkelt använde sig av random-modulen och några förbyggda metoder. Det förenklade
mitt arbete en hel del på den delen.

<h2>Har du programmerat med filhantering tidigare, känns det lätt eller
svårt?</h2>
Jag har arbetat lite med filhantering förut men inget extensivt så jag vet lite
hur det fungerar med metoder och dot-notation för metoder osv. Jag tycker dock
inte det vi har gjort hittils har varit så svårt, men jag vet att när jag
försökte mig på det för några årsedan i ett annat språk så hade jag lite svårt
för att få in det i huvudet, men jag känner att jag mognat lite nu och kan
ta in saker bättre och tror att det kommer bli väldigt intressant nu.

Svårighetsgraden beror väl helt klart på hur invecklat man använder det, hur
många \"lager\" man använder sig av och så vidare. Men just det vi har använt
oss av nu är ju inte så värst svårt, men jag känner på mig att det kanske kan
bli lite svårare i framtiden.

<h2>Vad tycker du om video som läromedel, tycker du att de tillför något som
läromedel?</h2>
Jag är inte så mycket för att titta på en video när jag ska lära mig, jag anser
att det ofta är för sakta. Om man läser något kan man ju själv bestämma i vilken
takt man ta sig igenom materialat och jag tycker man får en bättre uppfattning
om allting när man har det i svart och vit framför sig istället för att någon
ska sitta och berätta för dig. Min åsikt är att det inte tillför något extra.

<h2>Du har gjort din första modul i Python, känns strukturen bra?</h2>
Den känns väl okej, jag skulle säkert kunna bryta upp några utav mina funktioner
inuti modulen för att skapa ännu bättre struktur men jag tycker ändå att det
som helhet ser bra ut och det fungerar, så det är ju bra.

<h2>Vad tyckte du om de olika uppgifterna? Hur tänkte du när du utförde dem?
Var de utmanande eller lätta?</h2>
Jag tyckte uppgifterna var mycket bra och på en nivå som utmanade lite men ändå
tillät en att göra allt för hand utan att behöva ta hjälp från andra eller från
internet (mer än kurslitteraturen, såklart). Det var några uppgifter som var
ännu lite mer utmanande och dessa fick jag faktiskt medge att jag var tvungen
att googla runt lite för att lösa men det kanske bara är jag som förstod något
dåligt.


<h1>Kmom04:</h1>
------------------------------------------------------------------------------

<h2>Reflektion</h2>
Denna veckan har varit en väldigt spännande och extremt lärorik vecka. Inte
bara när det gäller kod, utan även allmänt, jag har har lärt mig mycket om
listor, slices, split, och så vidare. Jag har också lärt mig mer om hur man kan
lägga upp funktioner och använda sig av listor för att skriva in föremål i en
textfil. Men jag har också lärt mig annat som inte har med just Python att göra
så som att det inte skadar att läsa uppgifterna fler gånger än en, så kanske
man slipper göra om hela arbetet (oops), men samtidigt har jag ju bara lärt
mig ännu mer på att göra om uppgiften. Det var nämligen så att jag gjorde en
inventory för min bot som jag var väldigt stolt över, och sedan läste jag en
tråd på forumet och kom på att jag typ hade gjort hela grejen fel, jag tänkte
att när det stog att man skulle ha ett kommand som funkade när man skrev
t.ex. inv pick flower att BARA inv pick flower skulle funka, alltså använde
jag mig av itemet flower i all min kod, istället för att ha ett kommando
inv pick item där item kunde bytas ut till vad än användaren ville. Och för att
kunna ändra till det var jag tvungen att skriva om i stort sett alla kod från
att varken använda lists eller splice till att använda allt och lite till, så
som .split, .append och så vidare.

Jag tycker uppgifterna gick väldigt mycket frihet i framförandet av programmet.
Man får helt själv bestämma hur man vill lägga upp koden och vilka metoder man
vill använda sig av. För att göra det enkelt så bestämmde jag mig för att göra
en helt ny modul för inventoryt (inventory.py) och sen importera den i main.py
precis som vi importerat marvin.py. På detta sätt fick jag en bra struktur
i programmet och kan enkelt urskilja vart koden för inventoryt ligger och vart
koden för marvin själv ligger.

Jag hade lite problem med att välja hur jag skulle designa programmet först,
vill jag ha typ tre stora funktioner, eller vill jag bryta ner det i leta fler
små funktioner, vilket jag nu gjorde. Jag har t.ex. en funktion som öppnar
filen i read-mode och returnar datan och en funktion som öppnar den i
write-mode. Sen har jag en funktion som läser av alla raderna i filen och sen
lägger in varje item i en lista. Men jag är relativt nöjd med det jag har
åstadkommit ändå.

<h2>Var det svårt att bekanta sig med datastrukturen för listor eller flöt det
på bra?</h2>
Nej jag tycker inte det var några större problem, har ju stött på listor i andra
programmeringspråk också, även om det inte ser likadant ut i någon utav språken
så är det ändå lite same-same och man lär sig ganska enkelt det generella
"reglerna" och utseéndena för listor tycker jag. Även om man initialiserar dem
väldigt olika i olika språk.

<h2>Har du jobbat med listor, eller arrayer, i andra programmeringsspråk – kan
du isåfall jämföra Python listor mot andra programmeringsspråk?</h2>
Ja jag har jobbat med listor i både C++ och Javascript, den största skillnaden
jag tänkt på är väl att man inte kan initialisera en tom lista i C++ då man
måste bestämma hur många element den ska ha i förtid (har jag för mig) samt att
listor i C++ använder sig av curly brackets {} istället för []. Jag har inte
arbetat så mycket med det utan det är mest att jag har använt mig av C++ lite då
och då när jag kännt för att lära mig lite programmering. Senast jag använde
mig av det var för att göra egna grejer till en spelemulator för något år sedan.


<h2>Hur gick det att utföra uppgifterna, vilken tog mest tid och vilken var
mest lärorik när det gäller listor?</h2>
Det gick väl relativt bra, den som både tog längst och var mest lärorik var helt
klart inventoryt. Kanske för att jag fick göra uppgiften två gånger då jag tror
jag missuppfattade uppgiften först, men det klagar jag inte på. Jag lärde
mig som sagt extra mycket.

<h1>Kmom05:</h1>
------------------------------------------------------------------------------

<h2>Reflektion</h2>
Denna veckans uppgifter var något mer utmanande än vad det har varit hittils
(om man räknar bort extra uppgifterna, antar jag), jag tycker verkligen att
man har blivit utmanad av uppgifterna på en helt ny nivå, förut kunde man i
stort sett använda sig av exakt samma kod som det man kollade på videor/läste
om, men jag tror att detta kapitel krävde lite mer egentänkande än vad som
krävts förut.
Jag känner att jag fick lärt mig en hel del och man fick tänka igenom hur man
ville utföra uppgiften ett antal gånger. Jag satt ganska länge med denna
uppgiften, troligen längre än dem 12-16 timmarna som var tänkta att läggas, men
det var bara för jag hade beslutsångest och inte kunde bestämma
mig om hur jag skulle lösa några olika grejer. T.ex. delen där den skall
rätta stavningen på ord och sen räkna de mest frekvent använda rättstavade
orden, jag försökte i en lång stund att inte ta bort punctuation och inte
heller använda mig av .lower() men det var inte jättelätt att få det att fungera
eftersom man då har kvar ord som blir typ "hej!" vilket då inte räknas som samma
ord som "hej" eller "Hej".

Jag tycker att upplägget på kursen hittils har varit väldigt spännande, att
göra en egen bot som utvecklas i samma takt som ens egna erfarenheter och ens
egna färdigheter i programmeringspråket tycker jag är väldigt roligt. Man ser
direkt hur man utvecklas, eller kanske snarare hur det man lär sig utvecklas
i svårighetsgrad.

Jag märker nu att svårighetsgraden på det vi lär oss snabbt ökar, vilket jag
gillar då jag inte tyckte att det var så hemskt utmananande de första veckorna
(eller inte så mycket nytt iallafall), även om jag kanske gjorde lite fel här
och där, men det är ändå inte så hemskt stora fel som jag gjorde för att det
var svårt, utan mindre fel som händer för man antingen skriver för snabbt eller
för att man inte är van vid användningen av vissa grejer (t.ex. input, att man
måste convertera inputtet till int om man vill jämföra den med ett annat
nummer).


<h2>Hur kändes det med datastrukturerna dictionaries och tupler? Har du sett
något liknande förut?</h2>
Det kändes bra, jag har använt mig av liknande datastrukturer i både JavaScript
och C++ men som jag har sagt i andra redovisningar så var det ett tag sedan
jag använde mig av något av de språken, men jag har ju ändå kvar mycket utav
det i huvudet så jag har ju lite koll på hur det ser ut i andra språk också.


<h2>Känns det som du fick ordning på listor, dictionaries och tupler? När man
skall använda respektive och hur de kan användas?</h2>
Jag tror det, det kändes ganska enkelt att välja vad man skulle använda vart
och vid vilka tillfällen, kanske för att mycket utav det man gjorde liknade de
exempel som fanns med i textboken och på videoklippen. Så nu har man lärt sig
vart man kan använda sig av allt efter att man gjorde alla de olika uppgifterna,
helt enkelt.

<h2>Använde du något av listor, dictionaries eller tupler när du gjorde
uppgifterna, på vilket sätt?</h2>
Ja, jag använde mig av alla de olika grejerna. Listor använde jag för att lägga
in alla ord från words.txt och common-words.txt där jag kollade om orden fanns
och om dem fanns där och även fanns i min dictionary så las dem in i dicten där
jag sparade in frekvensen av rättstavade ord. Sen använde jag mig av listor av
tuplar för att loopa igenom dictarna.

<h2>Hur gick det att utföra uppgifterna, vilken tog mest tid och vilken var
mest lärorik?</h2>
Det gick väl sådär, fastnade lite på några olika grejer, men tillslut löste det
sig iallafall. Det som tog mest tid var nog den delen av Marvin-uppgiften
när man skulle ha en dict med frekvensen på rättstavade ord, jag försökte först
med att inte använda mig av translate och string.punctuation men det var svårt
att få det att fungera så jag spenderade en ganska lång tid på det. Efter att
jag lagt en helt klart för lång tid på det så valde jag att helt enkelt försöka
utan och då var det mycket enklare (självklart, antar jag). Får försöka att
lösa det när jag får mer tid till det kanske.



<h1>Kmom06:</h1>
------------------------------------------------------------------------------

<h2>Reflektion</h2>

En uppgift med mycket utrymme för egentänkande och improvisering. En uppgift
med många olika uppfattningar om hur man skall strukturera allt. Denna veckan
fick vi testa på något helt nytt men något ändå bekant. Att få göra en kommando-
rads anpassad Marvin har varit ett både roligt, jobbigt och tidskrävande arbete.
Jag har lärt mig massa nytt om allting från globala variabler till json-object
och även fått breda mina kunskaper inom att öppna och hämta information från
hemsidor.

Ibland kan man lura sig själv till att felsöka sånt som inte egentligen behöver
felsökas. Kanske så var det lite mitt eget fel på det sättet jag valde att
strukturera programmet dock. Jag la nämligen en if-else sats för options först,
och sen la jag en if-else sats för args, dessa hade jag i ett Try:Except block
och när jag testade om --silent funkade så fick jag ett error "list index out
of range". Jag förstod inte hur jag kunde få detta error när den enda koden
jag hade i --silent funktionen var "VERBOSE = False". Så jag testade att lägga
in en print(opt, arg, VERBOSE) i funktionen och den printade utan problem, men
jag fick fortfarande list index out of range. Det visade sig att det var ett
problem längre ner i if-else satsen för argumenten som krånglade och tydligen
callades hela tiden och det var den som kastade exceptionen. Alltså var det
inget fel på --silent funktionen som jag satt och försökte lösa i säkert någon
timme genom att testa olika grejer så som att lägga in "global VERBOSE" direkt i
if: blocket istället för precis utanför. Om jag bara hade tagit bort delen
"VERBOSE = False" och lagt in en print istället hade jag direkt fattat att det
inte var silent funktionen det var fel på, utan något annat. Egentligen hittade
jag aldrig direkt anledningen till felet, utan jag bestämmde mig för att
fortsätt på koden på andra ställen, och till slut så hittade jag felet. I koden
som ser ut typ såhär:

[code]for opt, arg in opts:
if arg[0] == stuff:
    dostuff
elif arg[0] == stuff2:
    dosomethingelse
[/code]

Så hade jag tydligen påbörjat ett styckte kod utan att bli klar med det, så då
använde den sig av typ arg[3] som såklart var "out of range" i list-indexen och
på så sätt kastade ett exception. Vad jag lärde mig av detta var att det är bra
att göra klart ett stycke kod man påbörjat innan man flyttar sig och börjar
koda på ett styckte någon annanstans.


Jag hade lite svårt att bestämma mig hur jag skulle kolla argumenten. I början
valde jag att som sagt använda mig av två olika if-else satser, en för options
och en för argumenten. Men jag funderade starkt på att kanske använda en if-else
sats med argumenten och sen nesta if-else satser inuti dem där jag kollade efter
options som funkade med det argumentet. Men jag valde till slut att använda
det sättet jag började med, alltså två olika if-satser.


Något annat som var lite svårt att bestämma sig för var vad för något man skulle
printa när verbose var på och vad som skulle printas när det inte var på. Det
är ju inte direkte något jätteviktigt men jag brukar ha svårt för lite mindre
detaljer ibland.


<h2>Har du jobbat med liknande tekniker innan (JSON, HTTP, webbtjänster,
SQLite, scrapa från HTML-formatet, kommandorads options), eller var detta
helt nytt för dig?</h2>
Det mesta var helt nytt för mig, jag har arbetat ganska mycket i MySQL förut, så
SQL är ett språk som inte alls är okänt för mig och jag är faktiskt ganska van
vid det. JSON har jag kollat runt lite på förut i gymnasiet då vi arbetade lite
med det, men inte mycket. Allt annat har jag bara läst om, men jag har aldrig
faktiskt använt mig av det förut, så det var helt nytt för mig.


<h2>Känns det bra att jobba på kommandoraden, ser du ett användningsområde för
den typen av Python-program?</h2>
Det känns ganska bra, man skulle ju kunna skapa en hel rad användbara kommandon
i Python för användning i kommandoraden. Samtidigt är det ju väldigt nytt så
det är lite ovant att arbeta med det och jag vet inte riktigt hur man ska
optimera det.


<h2>Hur gick det att utföra uppgifterna, vilken tog mest tid och vilken var
mest lärorik?</h2>
Det gick relativt bra, i början kände jag mig lite lost, visste inte riktigt
hur jag skulle gå tillväga, men efter ett tag så kom man liksom in i någon
sorts "flow" och det bara rullade på. Men jag känner ändå att jag börjar få in
känslan för hur allt fungerar nu och att jag lär mig snabbt. Det var helt
klart Marvin uppgiften som tog längst tid, men det är väl inte så konstigt då
de andra uppgifterna inte var så hemskt mycket mer än att läsa och skriva av
lite grann. Man lärde sig dock väldigt mycket av dem och det var dem jag gick
tillbaks och kollade på när det var något jag behövde hjälp med för jag glömt
hur man gör något.

<h2>Var uppgiften i tuffaste laget, vilken del hade du valt bort om du hade
haft det valet?</h2>
Nej jag tycker den var lagom tuff. Den var svår, men inte helt omöjlig, man
kunde lösa den även om man aldrig programmerat något före denna kurs (tror jag).


<h1>Kmom07/10 - Projectarbete:</h1>
------------------------------------------------------------------------------

Idén för mitt spel är typ självklar för mig, när jag tänker på ett spel då
tänker jag direkt på något mer 'rpg' eller actionspel. Därför valde jag att mitt
spel skulle handla om en trollkarl som ger sig ut för att återhämta en stav som
länge har varit en mystisk legend. Spelet går alltså ut på att trollkarlen ska
ta sig igenom ett antal rum i ett slot, och i sista rummet hittar han staven.

För att ta sig vidare måste han göra ett antal olika grejer, så som att svara på
några gåtor, lösa några ekvationer, hitta olika objekt och använda dem för att
förstöra andra objekt, slåss mot monster och så vidare.

I början hade jag väldigt svårt för att komma på mer exakt vad jag ville göra,
så då bestämmde jag fick för att börja programmera spelet utan en idé för själva
handlingen, utan jag programmerade snarare en 'mall' som jag sedan redigerade
när jag väl kommit fram till vad jag ville att spelet skulle vara.

På den grafiska illustrationen av mina rum har jag valt att använda mig av en
enklare sorts ASCII-bild där varje rum är en liten fyrkant och spelaren visuali-
seras genom ett 'o' i rummet. Ex:
▬▬▬▬▬▬▬▬▬▬▬___▬▬▬▬▬▬▬▬▬▬▬
▌    │   ●●●●●●●  ______▐
▌    │            │    ║▐
▌    │            │_/ __▐
▌                 │     ▐
▌    │                  ▐
▌║   │            │_  /_▐
▌    │      o     │     ▐
▌    │            │     ▐
▬▬▬▬▬▬▬▬▬▬▬   ▬▬▬▬▬▬▬▬▬▬▬

Något som förlorade mig mycket av projekttiden var att bestämma mig för hur jag
ville hantera data och hur jag ville lägga upp alla funktioner. Jag spenderade
hela första veckan på att bygga upp en massa olika classer, 1 super-class för
alla object, sen sub-classer för dem, 1 super-class för alla rum, och också här
en sub-class för varje rum. Efter att jag kommit en lång bit in i arbetet så
bestämmde jag mig för att det var alldeles för krångligt, och om jag skulle
vilja implentera save-funktionen i mitt spel så skulle det vara enklare med en
annan metod. Jag bestämmde mig då för att göra om allt och gå över till SQLite3,
dels för att det verkade bättre, men dels också för att jag har använt mig av
SQL förut (MySQL) både i skolan och på min fritid. Inte nog med den men jag
läste också ett utav datumen fel och trodde därför att jag hade en vecka till
på mig, vilket jag inte hade.

Tyvärr så resulterade denna slösade tid i att jag istället inte hann göra klart
de sista 3 kraven, speciellt då programmering inte är min starkaste sida och jag
krånglade därför på ganska många olika grejer genom projektets gång. Jag är dock
relativt nöjd med mitt spel i slutändan ändå.

<h2>Krav 1: Kommand och Argument</h2>
Att implentera kommandon och argument var det första jag gjorde när jag startade
med denna uppgift, eftersom det var väldigt färskt i minnet gick det också
snabbt att starta upp och jag visste direkt hur jag skulle göra. Jag började med
att tänka igenom hur jag ville lägga upp det, ville jag ha hela spelet i en fil
eller ville jag ha ett antal olika moduler, självklart valde jag att ha flera
moduler. I början hade jag lite svårt att bestämma mig för vilka sorters moduler
jag ville ha, det började med att jag hade 1 för varje rum, 1 för 'player', 1
för 'objects' och så vidare, men det slutade med att jag hade 4 olika filer,
adventure.py, som är en väldigt liten fil men som ändå är det som gör så att
hela grejen fungerar, det är adventure.py som har main-loopen som 'callar' alla
funktioner från de andra filerna. Utöver adventure.py har jag också game.py,
data.py och options.py. Game.py innehåller while-loopen som lyssnar efter
kommandon när spelet är aktivt, och den innehåller även en intro funktion som
är en sorts 'välkommen till mitt spel' funktion som printar ut lite bakgrundsin-
formation om spelet och lite ASCII.

Data.py är filen där allting händer, det är här de flesta funktionerna finns och
det är också här alla variabler (som inte finns i databasen) finns. I data.py
finnar man alla funktioner som hämtar, ändrar, och uppdaterar data i/från
databasen 'game.sqlite'. Jag tänkte egentligen från början ha det mesta i
game.py och sen låta funktionerna finnas i data.py, alltså t.ex. hade jag från
början en alternativ funktion till SQLites cursor.execute där funktionen tog
emot ett varierande antal argument (def function(*arg)) vilken betyde att jag
kunde enkelt exekvera flera kommandon i min databas med en enda funktion, jag
fick dock lite problem med denna funktion och valde att scrapa idén. Hade jag
haft mer tid hade jag nog försökt att fixa den funktionen igen då den hade
gjort min kod väldigt mycket kortare och enklare att läsa/ändra.

<h2>Krav 2: Spelkommandon</h2>
Kommandona för själva spelaren och ens karaktär var relativt enkla att fixa, och
dem växte lite för varje nytt objektkommando som jag implementerade och nästa
varje gång jag implementerade något nytt i ett rum.

Att få 'framåt' och 'backåt' att fungera var enkelt. Jag började med att skapa
en variable 'playerLocation' som alltså är en integer mellan 1 och 7, berorende
på vilket rum spelaren är i. I 'framåt' hade jag en check som kollade om
spelaren var i sista rummet (7) om man var det så printa den helt enkelt att
det inte går att gå frammåt. Var man i första rummet (1) så printade 'backåt'
funktionen också att man inte kan gå det hållet. För resten av rummen använde
jag mig av ett SELECT FROM statement på mitt 'Rooms' table där jag hade en
'unlocked' column som antingen var True eller False. Var den False så hände
inget mer än att funktionen printade att dörren var låst. Var den True gick man
framåt och playerLocation ställdes till playerLocation + 1.
playerLocation använde jag också i andra funktioner så som 'info' för att
SELECT(a) information från det rummet spelaren var i. Samma sak gjorde jag också
för 'ledtråd' och 'se'. All information om rummen fanns alltså i ett table
'Rooms' i min databas, och de olika funktionerna anvnände sig av information
från detta table för att fungera.

Jag har i mitt arbete valt att skapa spelet på engelska, och har därför också
översatt alla kommandon till engelska, jag har därför inte t.ex. 'ledtråd' och
så vidare utan har istället 'clue', 'forward', 'backwards', 'help' och så
vidare. Detta för att jag helt enkelt föredrar engelska när det gäller spel.

<h2>Krav 3: Objektkommandon</h2>
Dessa kommandon var väldigt intressanta att implementera och gav en väldigt bra
utmaning. Hur ska jag implementera alla 'funktioner' för objecten, ska jag göra
en flytta-funktion som inuti sig har en egen funktion för varje objekt, eller
ska jag bara skriva koden direkt i flytta-funktionen, så att t.ex.
'if objekt == "Chair": do stuff"' eller ska man helt enkelt ha en funktion som
ser ut snarare såhär:
def flyttaObjekt():
    flyttaStol()
    flyttaGarderob()
    flyttaAnnat()

och så vidare. Jag valde att denna gång arbeta med att för varje objekt som det
skulle gå att göra något speciellt med så skrev jag koden direkt in i "huvud"
funktionen, som också innehåll den generella-koden som callades för i stort sett
alla objekt. Jag valde att lägga alla kommandon i samma fil som det mesta annat
(data.py) men såhär i efterhand tänker jag att jag kanske hade kunnat göra en
helt egen fil t.ex. commands.py för dem för att göra det hela lite mer lättläst.

Några kommandon var mycket enklare än andra att implementera, t.ex. så var
titta [objekt] (som jag valde att döpa till see [object]) väldigt enkel att fixa
då alla objekt reagerar samma till det, alltså behövde jag bara göra en funktion
som använde sig av SELECT FROM och valde "description" från databasen på det
valda objektet. Tvärtemot detta så var 'move' det svåraste, då alla objekt som
gick att flytta på gjorde något helt annorlunda, vilket slutade i att jag helt
enkelt fick skriva fristående kod för varje objekt som skulle göra något när
man flyttade det.

<h2>Tankar och reflektion</h2>
Såhär i efterhand känner jag att planering kan vara en bra start på ett projekt
i denna storleken, jag hade inte jättebra planering på hur jag ville lägga upp
allt, men det kanske låg delvis i att jag inte hade arbetat med något liknande
förut och inte visste hur jag skulle börja. Som jag skrivit tidigare så hade
jag i början problem med att bestämma mig för hur jag skulle hantera alla data.
Skulle jag använda JSON direkt? SQLite3? Något annat?
Efter detta var det också problemet med hur man skulle lägga upp filerna och
vart man skulle ha alla funktioner och liknande. Jag tycker det är riktigt
roligt och spännande (helt ärligt) att bara pyssla med att skapa de olika
modulerna.

Jag tycker att uppgiften vi hade var en väldigt bra uppgift där man var tvungen
att tänka en hel del på hur man skulle lägga upp det, vilka sorters metoder
man ville använda sig av och så vidare.

Det som var svårast med projektet var nog att komma på vad för sorts spel man
ville göra, det finns så mycket olika grejer man kan göra att man lixom får
svårt att bestämma sig.

<h2>Kursreflektion</h2>
Jag tycker att denna kursen har varit både väldigt lärorik och väldigt rolig.
Jag har fått lära mig en massa nytt och har nu äntligen fått börja programmera
i Python (har länge tänkt starta kursen på codecademy men det har inte blivit
av). I början tyckte jag det var mycket att ta in, dels för att det finns så
många länkar och liknande på dbwebb med olika resursers osv, och dels för att
allting är helt nytt, jag har inte jobbat med denna sortens sida förut utan
vi använde oss ju utav Fronter i gymnasiet (och högstadiet).
Jag lärde mig dock ganska snabbt hur jag skulle hitta t.ex. allt kursmaterial
och hur man skulle gå till vida, och efter det tycker jag allting har varit
väldigt bra. Upplägget är snyggt och organiserat, man kan enkelt läsa sig fram
till i vilken ordning man ska göra allt och vad man ska göra. Jag tycker det
är väldigt lärorikt att alla lägger upp sina redovisningar på forumet eftersom
man då kan läsa och lära från andra också.

Svårt att säga mycket om handledarna när det ser ut som det gör, de har skött
sitt jobb och rättat arbetena. När jag har lämnat in något som inte fungerat
eller som inte stämmer så har de väl helt enkelt berättat vad som är fel och
fått mig att fixa det, så det är väl bra.

Jag är väldigt nöjd med kursen i sin helhet och hoppas att de andra kurserna är
lika givande, intressanta och välupplagda. Jag hade helt klart rekommenderat
kursen till mina kompisar (har redan gjort det). Jag ger kursen 8/10.

http://www.student.bth.se/~eroa16/dbwebb-kurser/python/me/
http://www.student.bth.se/~eroa16/dbwebb-kurser/python/me/redovisning.cgi
http://www.student.bth.se/~eroa16/dbwebb-kurser/python/me/kmom10/adventure/

</pre>
"""


# Write page content
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
sys.stdout.write(content)
