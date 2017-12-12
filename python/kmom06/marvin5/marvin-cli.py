#!/usr/bin/env python3
"""
Börjar med att initialisera lite variabler och importera lite moduler
som kommer att användas senare.
"""

import requests
import getopt
import sys
import os
import sqlite3
import json
import random
from bs4 import BeautifulSoup

VERBOSE = True
VERSION = "1.0.2"
PROGRAM = os.path.basename(sys.argv[0])

OUTPUT_FILE = None
SAVE_TO_FILE = False

INPUT_FILE = None
READ_FROM_FILE = False

EXIT_SUCCESS = 0
EXIT_ARG_ERROR = 1
EXIT_EXECUTE_ERROR = 2

JSONREPORT = False


def usage():
    """
    Prints help for the application.
    """
    print("""##### Marvin Help Menu #####
    Options:
    -h or --help                Prints the help menu.
    -v or --version             Prints the program version.
    --verbose                   Enables verbose output.
    -s or --silent              Disables verbose output.

    title [url]                 Prints the title from [url]
    --input=<file> title        Prints the title from <file>

    quote                       Prints the quote of the day.
    --input=<file> quote        Prints a random quote from <file>.

    get <url>                   Prints the content of <url>
    --output=<file> get <url>   Prints the content of <url> into <file>

    ping <url>                  Pings <url> and returns the status code.
    ping-history                Displays all pinged websites and their statuses.

    seo <url>                   Prints SEO information on the requested URL.
    --input=<file> seo          Prints SEO information from <file>.
    --json --input=<file> seo   Prints SEO information in JSON format.
    """)


def showVersion():
    """
    Prints the current program version.
    """
    print("{program} - Running version: {version}".format(program=PROGRAM,\
version=VERSION))


def ping(url):
    """
    Pings the desired URL.
    """
    try:
        req = requests.head(url)

        if VERBOSE:
            print("rePinging server at", url)

        print("Received status code:", req.status_code)

        connection = sqlite3.connect("ping-history.sqlite")
        dbc = connection.cursor()

        dbc.execute("CREATE TABLE IF NOT EXISTS Pinged (url TEXT, status\
 INTEGER);")
        dbc.execute("INSERT INTO Pinged (url, status) VALUES (?, ?);", (url,\
 req.status_code))
        connection.commit()
        dbc.close()

    except requests.ConnectionError:
        print("Failed to connect to server at", url)
        sys.exit(EXIT_EXECUTE_ERROR)


def ping_history():
    """
    Displays ping history.
    """
    connection = sqlite3.connect("ping-history.sqlite")
    dbc = connection.cursor()

    dbc.execute("SELECT * FROM Pinged")

    print("Ping History:")
    for item in dbc:
        print("Status:", item[1], "URL:", item[0])


def loadWebpage(url):
    """
    Loads a webpage
    """

    try:
        if VERBOSE:
            print("Gathering content from:", url)

        content = requests.get(url).text

        if SAVE_TO_FILE:
            fhand = open(OUTPUT_FILE, "w+")
            fhand.write(content)
            fhand.close()

            if VERBOSE:
                print("Output file selected. Content saved to file:", \
OUTPUT_FILE)
        else:
            if VERBOSE:
                print("Printing webpage content.")

            print(content)

            if VERBOSE:
                print("Completed webpage printing.")

    except requests.ConnectionError:
        print("Failed to connect to server at", url)
        sys.exit(EXIT_EXECUTE_ERROR)


def getTitle(url="http://dbwebb.se"):
    """
    Gets the title of the selected URL.
    """
    try:
        if READ_FROM_FILE:
            url = INPUT_FILE

            if VERBOSE:
                print("Collecting title from", url)
            req = open(url, "r")
            soup = BeautifulSoup(req, "html.parser")
            title = soup.title.string
            print("Website Title:", title)
        else:
            if VERBOSE:
                print("Collecting title from", url)
            req = requests.get(url)
            soup = BeautifulSoup(req.text, "html.parser")
            title = soup.title.string
            print("Website Title:", title)

    except Exception:
        usage()
        sys.exit(EXIT_EXECUTE_ERROR)


def getQuote():
    """
    Loads a quote.
    """
    url = "http://dbwebb.se/javascript/lekplats/get-marvin-quotes-\
using-ajax/quote.php"

    try:
        if READ_FROM_FILE:
            url = INPUT_FILE

            jsonFile = open(url, "r")

            jsonObject = json.load(jsonFile)

            randomized = random.randint(0, (len(jsonObject["quotes"])-1))

            if VERBOSE:
                print("Loading quote from", url)

            print("Quote:", jsonObject["quotes"][randomized])

        else:
            req = requests.get(url)

            if VERBOSE:
                print("Loading quote from", url)

            jsonFile = req.json()
            print("Quote: \"{quote}\"".format(quote=jsonFile["quote"]))

    except Exception:
        usage()
        sys.exit(EXIT_EXECUTE_ERROR)


def searchEngineOptimization(url="http://dbwebb.se"):
    """
    SEO Searches a website/file.
    """
    try:
        if READ_FROM_FILE:
            url = INPUT_FILE

            if VERBOSE:
                print("Collecting data from", url, "\n")

            req = open(url, "r")
            soup = BeautifulSoup(req, "html.parser")

            if VERBOSE:
                print("Retrieving website title.")

            title = soup.title.string

            if VERBOSE:
                print("Website title:", title)

            print("Website title length:", len(title), "\n")

            if VERBOSE:
                print("Calculating header element counts <h1> & <h2>:")

            h1List = soup.find_all("h1")
            h2List = soup.find_all("h2")
            print("Found", len(h1List), "h1-tags.")
            print("Found", len(h2List), "h2-tags.\n")

            if VERBOSE:
                print("Calculating anchor element count:")

            hrefList = soup.find_all("a")
            print("Found", len(hrefList), "a-tags.")


            if JSONREPORT:
                print("JSON Enabled\n")
                if VERBOSE:
                    print("Collecting data in JSON.\n")

                data = {"website": {"title": title, "length": len(title)},\
"h1Count": len(h1List), "h2Count": len(h2List), "aCount": len(hrefList)}

                json_data = json.dumps(data, indent=4)
                print(json_data)

        else:
            if VERBOSE:
                print("Collecting data from", url, "\n")

            req = requests.get(url)
            soup = BeautifulSoup(req.text, "html.parser")

            if VERBOSE:
                print("Retrieving website title.")

            title = soup.title.string

            if VERBOSE:
                print("Website title:", title)

            print("Website title length:", len(title), "\n")

            if VERBOSE:
                print("Calculating header 1 & 2 element counts:")

            h1List = soup.find_all("h1")
            h2List = soup.find_all("h2")
            print("Found", len(h1List), "h1-tags.")
            print("Found", len(h2List), "h2-tags.\n")

            if VERBOSE:
                print("Calculating anchor element count:\n")

            hrefList = soup.find_all("a")
            print("Found", len(hrefList), "a-tags.\n")


            if JSONREPORT:
                print("JSON Enabled\n")
                if VERBOSE:
                    print("Collecting data in JSON.\n")

                data = {"website": {"title": title, "length": len(title)},\
"h1Count": len(h1List), "h2Count": len(h2List), "aCount": len(hrefList)}

                json_data = json.dumps(data, indent=4)
                print(json_data)


    except Exception:
        usage()
        sys.exit(EXIT_EXECUTE_ERROR)


def main():
    """
    The main function, where everything is called upon.
    """
    try:
        global VERBOSE
        global OUTPUT_FILE, INPUT_FILE, SAVE_TO_FILE, READ_FROM_FILE
        global JSONREPORT

        opts, args = getopt.getopt(sys.argv[1:], "hvs", ["help", "verbose", \
"silent", "output=", "input=", "json", "version"])

        for opt, arg in opts:
            if opt in ("-h", "--help"):
                usage()
                sys.exit(EXIT_SUCCESS)

            elif opt in ("-v", "--version"):
                showVersion()
                sys.exit(EXIT_SUCCESS)

            elif opt in ("-s", "--silent"):
                VERBOSE = False

            elif opt in ("--verbose"):
                VERBOSE = True
                print("Verbose output enabled.")

            elif opt in ("--output"):
                OUTPUT_FILE = arg
                SAVE_TO_FILE = True

            elif opt in ("--input"):
                INPUT_FILE = arg
                READ_FROM_FILE = True

            elif opt in ("--json"):
                JSONREPORT = True

        if len(args) > 0:
            if args[0] == "ping":
                if len(args) > 1:
                    ping(args[1])
                else:
                    usage()
                    sys.exit(EXIT_ARG_ERROR)

            elif args[0] == "ping-history":
                ping_history()

            elif args[0] == "get":
                if len(args) > 1:
                    loadWebpage(args[1])
                else:
                    usage()
                    sys.exit(EXIT_ARG_ERROR)

            elif args[0] == "quote":
                getQuote()

            elif args[0] == "title":
                if len(args) > 1:
                    getTitle(args[1])
                else:
                    getTitle()

            elif args[0] == "seo":
                if len(args) > 1:
                    searchEngineOptimization(args[1])
                else:
                    searchEngineOptimization()

    except Exception as err:
        print(err)
        if VERBOSE:
            print("Use -h or --help to get usage help.")
        sys.exit(EXIT_ARG_ERROR)


if __name__ == "__main__":
    main()
