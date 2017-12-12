#!/usr/bin/env python3
"""
This is the game "engine". This file contains most of the actual game.
"""

import data

def loadFiles():
    """
    Check for wether or not the game is saved previously.
    """
    #if not data.saved:
    #    data.initialize()
    #else:
    #    print("Loading Saved Files")
    data.initialize()


def intro():
    """
    Displays the intro of the game.
    """
    print(r"""
                                   l~~~~~~~l
                          /\   l^^^^^^^^^^^^^^^l  /\
                         /__\ _l O  O  O  O  O l_/__\
                         l   l l               l     l
                         l   l l               l     l
          [^^^]          l  [^^^]             [^^^]  l          [^^^]
          [ o ]-------------[ o ]-------------[ o ]-------------[ o ]
          [   ]             [   ]     ___     [   ]             [   ]
          [   ]             [   ]    /###\    [   ]             [   ]
          [   ]             [   ]   |#####|   [   ]             [   ]
          [   ]             [   ]   |#####|   [   ]             [   ]
__________[___]_____________[___]___|#####|___[___]_____________[___]___________
        """)
    print("Greetings wizard, I am Archmage Waleria. ")
    print("""For thousands of years, the Staff of Netherwind has been but a mere
legend, a tale of the past that has been passed down from generation to genera
tion. But no longer. Thanks to the joint powers of the Kingdom of Sylvanor and
the wizards of Tirasmere, the staff has been located. It it said to be hidden
somewhere within the Castle of Nerzia. Your mission is to find the staff!""")

    print("\nType 'forward' to move into the next room, or 'backwards' to go \
back into the previous room. I will be with you by telepathy through the \
whole thing.")
    print("\nShall you ever need anything, simply type 'help' to ask me for \
help, and I will give you a list of available commands.")

    input("\nHit Enter when you are ready to proceed...")

    data.roomImage(data.playerLocation)
    print(data.roomInformation())


def run():
    """
    Main game function, runs the command-check.
    """
    while data.gameFinished == False:
        print("\nWaleria says: What would you like to do?")
        userChoice = input("--> ")
        command = userChoice.lower()

        args = userChoice.split()

        if command in ("q", "quit"):
            return

        elif command in ("i", "info"):
            print(data.roomInformation())

        elif command in ("fwd", "forward"):
            data.moveForward()

        elif command in ("ba", "back", "backwards"):
            data.moveBackwards()

        elif command in ("v", "view"):
            data.viewRoom()

        elif command in ("h", "help"):
            data.gameHelp()

        elif command in ("c", "clue"):
            data.clue()

        elif len(args) > 1:
            if args[0].lower() in ("k", "kick"):
                data.kickObject(args[1])
            elif args[0].lower()  in ("o", "open"):
                data.openObject(args[1])
            elif args[0].lower()  in ("m", "move"):
                data.moveObject(args[1])
            elif args[0].lower()  in ("s", "see"):
                data.seeObject(args[1])
            elif args[0].lower() in ("d", "debug"):
                data.debugObject(args[1])

        elif command in ("o", "open"):
            print("Incomplete command. Command takes 1 argument. Open [object]")
        elif command in ("k", "kick"):
            print("Incomplete command. Command takes 1 argument. Kick [object]")
        elif command in ("s", "see"):
            print("Incomplete command. Command takes 1 argument. See [object]")
        elif command in ("m", "move"):
            print("Incomplete command. Command takes 1 argument. Move [object]")

        else:
            print("Command:", command, "not recognized. Type 'help' for help.")
