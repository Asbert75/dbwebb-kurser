#!/usr/bin/env python3
"""
Module that holds all the help options available.
"""

GAME_VERSION = "1.0.0"
GAME_NAME = "The Castle of Nerzia"

import getopt
import sys

def parseOptions():
    """
    A check for commands entered into the game.
    """
    try:
        opts, _ = getopt.getopt(sys.argv[1:], "achiv", ["about", "cheat", \
        "help", "info", "version"])

        for opt, _ in opts:
            if opt in ("-a", "--about"):
                about()
                sys.exit(0)
            elif opt in ("-c", "--cheat"):
                cheat()
                sys.exit(0)
            elif opt in ("-h", "--help"):
                usage()
                sys.exit(0)
            elif opt in ("-i", "--info"):
                info()
                sys.exit(0)
            elif opt in ("-v", "--version"):
                version()
                sys.exit(0)

    except Exception as err:
        print(err)
        sys.exit(1)

def about():
    """
    Prints a description about the author/creator of the game.
    """
    print("""Erik is an 18 year old amateur programmer whose passion is
designing. Since he was 9 years old he has been passionately designing all
kinds of things using either Gimp, Photoshop or similar programs. It was not
until recently that he also started developing websites.""")

def cheat():
    """
    Prints the secret ways of how to cheat your way through the game.
    """
    print("To get past the first room, simply open the Toolbox, then kick the\
Chest and move forward. After you have entered the second room, you can \
move the painting that you read about in the room description by typing \
'move painting', doing this will unlock all of the rooms and you will be moved\
 to the 7th and final room. To grab the staff and win the game you simply type \
 'open tomb'.")

def usage():
    """
    Prints a help menu.
    """
    print("""\nAvailable commands are:
    -h, --help          -   Prints the help menu.
    -i, --info          -   Prints information about the game.
    -v, --version       -   Prints the game version.
    -a, --about         -   Prints information about the game creator.
    -c, --cheat         -   Prints the fastest way to complete the game, and how
                            you can cheat your way through.
    """)

def info():
    """
    Prints a description about the game.
    """
    print(GAME_NAME, """is a command prompt based Python game where you play as
a powerful mage looking to retrieve the Staff of Netherwind from the dark and
dangerous castle of Nerzia. Throughout your journey you will stumble across a
plethora of puzzles, objectes and creatures that you can interact with in
different ways.""")

def version():
    """
    Prints the current version of the game running.
    """
    print("You are running", GAME_NAME, "version", GAME_VERSION + "!")
