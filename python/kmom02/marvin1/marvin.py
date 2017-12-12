#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Marvin with a simple menu to start up with.
Marvin doesnt do anything, just presents a menu with some choices.
You should add functinoality to Marvin.

"""


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
        import random
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
        maxGrade = int(maxGrade)
        userGrade = int(userGrade)
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



def main():
    """
    This is the main method, I call it main by convention.
    Its an eternal loop, until q is pressed.
    It should check the choice done by the user and call a appropriate
    function.
    """
    while True:
        menu()
        choice = input("--> ")

        if choice == "q":
            print("Dalek says: Farewell, Doctor.")
            return

        elif choice == "1":
            myNameIs()

        elif choice == "2":
            ageInSeconds()

        elif choice == "3":
            weightOnMoon()

        elif choice == "4":
            minutesToHours()

        elif choice == "5":
            celciusToFahrenheit()

        elif choice == "6":
            wordMultiplication()

        elif choice == "7":
            randomNumberGenerator()

        elif choice == "8":
            sumOfNumbers()

        elif choice == "9":
            gradesCalculator()

        else:
            print("Dalek says: I'm afraid I do not recognize that command,\
 Doctor. You must choose a valid option from the menu.")

        input("\nPress enter to continue...")



if __name__ == "__main__":
    main()
