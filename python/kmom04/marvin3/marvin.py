#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This module contains all of Daleks' functions.
"""

import random
import time

def meImage():
    """
    Store my ascii image in a separat variabel as a raw string
    """
    return r"""
              ___
      D>=G==='   '.
            |======|
            |======|
        )--/]IIIIII]
           |_______|
           C O O O D
          C O  O  O D
         C  O  O  O  D
         C__O__O__O__D
        [_____________]
    """

def menu():
    """
    Display the menu with the options that Dalek can do.
    """
    print(chr(27) + "[2J" + chr(27) + "[;H")
    print(meImage())
    print("Hello, I am a Daaaaaalek. EXTERMINATE! EXTEEEERMINATE! Excuse me, my\
 wirings must be faulty...")
    print("1) Present yourself to Marvin.")
    print("2) Let the Dalek calculate how many seconds you've lived.")
    print("3) Let the Dalek calculate your weight on the moon.")
    print("4) Find out how many hours any amount of minutes is.")
    print("5) Convert Celcius to Fahrenheit.")
    print("6) Print a word a desired amount of times.")
    print("7) Generate 10 random numbers between your desired minimum and\
 maximum number.")
    print("8) Enter any amount of numbers and let the Dalek calculate the sum\
 of your numbers for you.")
    print("9) Calculate your grades.")
    print("10) Play a game of \"Guess The Number\".")
    print("11) Dear Diary.")
    print("12) Shuffle A Word")
    print("q) Quit.")

def invalidNumber():
    """
    Prints when an invalid number has been used.
    """
    print("Dalek says: It seems that the number you entered is invalid.\
 Make sure that you are entering a number and not a letter.")

def myNameIs():
    """
    Read the users name and say hello to Marvin.
    """
    name = input("Doctor, Who? (Enter your name)\n--> ")
    print("[Dalek] says: Greetings Dr.", name + ". How may I be of assistance?")

def ageInSeconds():
    """
    Prints the users age in seconds.
    """
    age = input("Dalek says: How old are you, Doctor? (Enter your age in\
 years)\n--> ")
    try:
        yearsInSeconds = int(age)*31536000
        print("Dalek says: You've lived for", yearsInSeconds, "seconds!")
    except Exception:
        invalidNumber()

def weightOnMoon():
    """
    Calculates and prints the users weight on the moon.
    """
    weight = input("Dalek says: How much do you weight, Doctor? (Enter your\
 weight in kilograms)\n--> ")
    try:
        kg = int(weight)*(1/6)
        print("Dalek says: On the moon, you would weight",\
        format(kg, ".2f"), "kilograms.")
    except Exception:
        invalidNumber()

def minutesToHours():
    """
    Calculates and prints the amount of minutes in hours and minutes.
    """
    minutes = input("Dalek says: How many minutes do you wish to convert\
 into hours? (Enter any amount of minutes)\n--> ")
    try:
        minutesInHours = float(minutes)/60
        minutes = (minutesInHours%1)*60
        hours = int((minutesInHours - minutesInHours%1))
        if hours is 1:
            print("Dalek says: That would be", hours, "hour and",\
format(minutes, ".2f"), "minutes!")
        else:
            print("Dalek says: That would be", hours, "hours and",\
format(minutes, ".2f"), "minutes!")
    except Exception:
        invalidNumber()

def celciusToFahrenheit():
    """
    Converts celcius to fahrenheit
    """
    degrees = input("Dalek says: Enter a temperature in Celcius.\n--> ")
    try:
        celcius = float(degrees)
        fahrenheit = float(format((celcius*9/5+32), ".2f"))

        print("Dalek says: That would convert into", fahrenheit, "fahrenheit.")
    except Exception:
        invalidNumber()

def wordMultiplication():
    """
    Prints a word x amount of times.
    """
    word = input("Dalek says: Enter a word.\n--> ")
    amount = input("Dalek says: Enter a number of times you would like to\
 repeat the word.\n--> ")
    try:
        x = 0

        while x < int(amount):
            print(str(word))
            x = x+1
    except Exception:
        invalidNumber()

def randomNumberGenerator():
    """
    Generates a random number between min and max
    """
    floor = input("Dalek says: Enter a desired minimum number.\n--> ")
    roof = input("Dalek says: Enter a desired maximum number.\n--> ")

    if floor > roof:
        print("The minimum number has to be greater than the maximum number.")
        return

    try:
        floor = int(floor)
        roof = int(roof)

        rng = random.randint(floor, roof)
        x = 0

        while x < 10:
            rng = random.randint(floor, roof)
            print(rng)
            x = x + 1
    except Exception:
        invalidNumber()


def sumOfNumbers():
    """
    Calculates the sum of all numbers entered.
    """

    totalValue = 0.0
    numbers = 0

    while True:
        number = input("Dalek says: Enter any number. Type done once you are\
 finished.\n--> ")

        if number.upper() == "DONE":
            break
        else:
            try:
                totalValue = totalValue + float(number)
                numbers = numbers+1
                print(number)
            except Exception:
                invalidNumber()
                break

    print("The value of the numbers you entered is:", totalValue)
    print("The average of your numbers is\
", float(format((totalValue/numbers), ".2f")))



def gradesCalculator():
    """
    Calculates your grade.
    """
    maxGrade = input("Dalek says: Enter the maximum grade available in your\
 course.\n--> ")
    userGrade = input("Dalek says: Enter the grade you recieved in the course\
.\n--> ")

    """
    >= 0.9 = A
    >= 0.8 = B
    >= 0.7 = C
    >= 0.6 = D
    < 0.6 = F
    """

    try:
        if userGrade > maxGrade:
            print("Dalek says: Unfortunately, your grade can not be higher tha\
n the max grade in your course!")
        else:
            oneTenth = float(maxGrade)/10.0
            gradeA = oneTenth*9.0
            gradeB = oneTenth*8.0
            gradeC = oneTenth*7.0
            gradeD = oneTenth*6.0

            userGrade = float(userGrade)

            if userGrade >= gradeA:
                print("Dalek says: You aced the course. You scored an A!")
            elif userGrade >= gradeB:
                print("Dalek says: Close! You scored a B!")
            elif userGrade >= gradeC:
                print("Dalek says: Could have been worse. You scored a C!")
            elif userGrade >= gradeD:
                print("Dalek says: You scored a D.")
            else:
                print("Dalek says: You failed the course. You scored an F.")

    except Exception:
        invalidNumber()


def guessTheNumber():
    """
    A Game of Guess The Number. The user has 6 tries to get the number right.
    """

    number = random.randint(0, 100)
    guessCount = 0
    maxGuesses = 6
    lower = "Lower, the number is lower!"
    higher = "Higher, the number is higher!"

    print("Dalek says: I think of a random number between 1\
 and 100. If you can guess it right in under 6 tries, you win. What's your\
 first guess?")

    while guessCount < maxGuesses:
        userGuess = input("--> ")

        guessCount = guessCount + 1

        try:
            userGuess = int(userGuess)

            if userGuess > number:
                print(lower)
            elif userGuess < number:
                print(higher)
            else:
                break

        except Exception:
            invalidNumber()

    if userGuess == number:
        print("Correct! You did it, you guessed the number in\
", guessCount, "tries!")

    if userGuess != number:
        print("Sorry, but the number I was thinking of was " + number + "!")

def diary():
    """
    Uses format to print different information.
    """
    openFile = open("content.txt", "r")
    content = openFile.read()

    rainCount = 5
    dalekCount = 10.257

    moods = ["livid", "delighted", "happy", "excited", "sad", "confused"]
    currentMood = random.choice(moods)

    currentTime = time.strftime("%H:%M:%S")

    currentDate = time.strftime("%x")

    print(content.format(currentDate, currentTime, currentMood, rainCount,\
 dalekCount))


def shuffleWords():
    """
    Shuffle the entered word.
    """
    userInput = input("Dalek says: Enter a word you would like me to shuffle.\
    \n--> ")

    userInput = list(userInput)
    random.shuffle(userInput)
    print(''.join(userInput))

def randomQuote():
    """
    Prints a random quote from the Hitchiker's Guide to the Galaxy.
    """
    quotes = open("quotes.txt", "r")
    quote = None

    rng = random.randint(1, 11)

    lineCount = 0
    for line in quotes:
        lineCount = lineCount+1
        if lineCount == rng:
            quote = line

    print("\"" + quote + "\" - Hitchiker's Guide to the Galaxy")
