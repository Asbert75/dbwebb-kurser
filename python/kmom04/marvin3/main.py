#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This is Dalek. A Bot.
"""


import marvin
import inventory

def main():
    """
    This is the main method, I call it main by convention.
    Its an eternal loop, until q is pressed.
    It should check the choice done by the user and call a appropriate
    function.
    """

    while True:
        marvin.menu()
        choice = input("--> ")
        userChoice = choice.lower()
        userChoice = userChoice.split()

        if len(userChoice) == 1 and userChoice[0] == "inv":
            inventory.display()

        elif userChoice[0] == "inv" and userChoice[1] == "pick":
            if len(userChoice) < 3:
                print("Dalek says: What do you want me to pick up? Repeat the\
c ommand like this: \"inv pick item\"")
            else:
                inventory.pickItem(userChoice[2])

        elif userChoice[0] == "inv" and userChoice[1] == "drop":
            if len(userChoice) == 2:
                inventory.drop()
            elif len(userChoice) < 3:
                print("Dalek says: What do you want me to drop up? Repeat the\
 command like this: \"inv drop item\"")
            else:
                inventory.dropItem(userChoice[2])


        elif "citat" in userChoice:
            marvin.randomQuote()

        elif choice == "q":
            print("Dalek says: Farewell, Doctor.")
            return

        elif choice == "1":
            marvin.myNameIs()

        elif choice == "2":
            marvin.ageInSeconds()

        elif choice == "3":
            marvin.weightOnMoon()

        elif choice == "4":
            marvin.minutesToHours()

        elif choice == "5":
            marvin.celciusToFahrenheit()

        elif choice == "6":
            marvin.wordMultiplication()

        elif choice == "7":
            marvin.randomNumberGenerator()

        elif choice == "8":
            marvin.sumOfNumbers()

        elif choice == "9":
            marvin.gradesCalculator()

        elif choice == "10":
            marvin.guessTheNumber()

        elif choice == "11":
            marvin.diary()

        elif choice == "12":
            marvin.shuffleWords()

        else:
            print("Dalek says: I'm afraid I do not recognize that command,\
 Doctor. You must choose a valid option from the menu.")

        input("\nPress enter to continue...\n")



if __name__ == "__main__":
    main()
