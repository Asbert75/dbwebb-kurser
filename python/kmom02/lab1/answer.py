#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
233a317012e676674fc7496403d9a2d6
python
lab1
eroa16
2016-09-06 13:41:04
v2.2.15 (2016-05-31)

Generated 2016-09-06 15:41:04 by dbwebb lab-utility v2.2.15 (2016-05-31).
https://github.com/mosbth/lab
"""


from Dbwebb import Dbwebb

dbwebb = Dbwebb()
print(">>> Ready to begin.")



"""
==========================================================================
Lab 1 - python

If you need to peek at examples or just want to know more, take a look at
the [Python manual](https://docs.python.org/3/library/index.html).

There you will find everything this lab will go through and much more.

"""

"""
--------------------------------------------------------------------------
Section 1. Integers, strings, floats and basic arithmetics

The foundation of numbers and basic arithmetic.

"""



"""
Exercise 1.1

Create a variable called 'numOne' and give it the value 83. Create another
variable called 'numTwo' and give it the value 40. Create a third variable
called 'result' and assign to it the sum of the first two variables.

Answer with the result.


Write your code below and put the answer into the variable ANSWER.
"""

numOne = 83
numTwo = 40
result = numOne + numTwo


ANSWER = result

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.1", ANSWER, False))

"""
Exercise 1.2

Create a variable called 'numThree' and give it the value 37.

Create another variable called 'numFour' and give it the value 17.

Subtract 'numThree' from 'numFour' and answer with the result.


Write your code below and put the answer into the variable ANSWER.
"""

numThree = 37
numFour = 17
result = numFour - numThree




ANSWER = result

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.2", ANSWER, False))

"""
Exercise 1.3

Find out the product of 'numOne' and 'numThree' and answer with the result.


Write your code below and put the answer into the variable ANSWER.
"""

result = numOne * numThree




ANSWER = result

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.3", ANSWER, False))

"""
Exercise 1.4

Divide 30 with 5 and answer with the result.


Write your code below and put the answer into the variable ANSWER.
"""

result = 30 / 5




ANSWER = result

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.4", ANSWER, False))

"""
Exercise 1.5

Create a variable called 'floatOne' and give it the value 22.88.

Create another variable called 'floatTwo' and give it the value 55.28.

Sum the two values and answer with the result, rounded to 2 decimals.


Write your code below and put the answer into the variable ANSWER.
"""

floatOne = 22.88
floatTwo = 55.28
result = floatOne + floatTwo




ANSWER = result

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.5", ANSWER, False))

"""
Exercise 1.6

Subtract 'floatTwo' from 'floatOne' and answer with the result. Round to 2
decimals.


Write your code below and put the answer into the variable ANSWER.
"""

result = float(format((floatOne - floatTwo), '.2f'))



ANSWER = result

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.6", ANSWER, False))

"""
Exercise 1.7

Answer with the product of 'floatOne' and 'floatTwo', rounded to 4
decimals.


Write your code below and put the answer into the variable ANSWER.
"""

result = float(format((floatOne * floatTwo), ".4f"))




ANSWER = result

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.7", ANSWER, False))

"""
Exercise 1.8

Create three variables: 'n1' = 414, 'n2' = 146 and 'n3' = 23. Sum up 'n1'
and 'n2'. Subtract 'n3' and answer with the result.


Write your code below and put the answer into the variable ANSWER.
"""

n1 = 414
n2 = 146
n3 = 23
result = n1 + n2 - n3




ANSWER = result

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.8", ANSWER, False))

"""
Exercise 1.9

Answer with the result of 148 modulo (%) 40.


Write your code below and put the answer into the variable ANSWER.
"""

result = 148%40




ANSWER = result

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.9", ANSWER, False))

"""
Exercise 1.10

Add the word: 'input' to the word: 'beverage' and answer with the result.


Write your code below and put the answer into the variable ANSWER.
"""


result = "beverage" + "input"



ANSWER = result

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.10", ANSWER, False))

"""
--------------------------------------------------------------------------
Section 2. Conditions, exceptions, booleans, if, else and elif



"""



"""
Exercise 2.1

Answer with the boolean value of: 467 is less than 313.


Write your code below and put the answer into the variable ANSWER.
"""

result = 467 < 313




ANSWER = result

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("2.1", ANSWER, False))

"""
Exercise 2.2

Answer with the boolean value of: 490 is larger than 341.


Write your code below and put the answer into the variable ANSWER.
"""

result = 499 > 341




ANSWER = result

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("2.2", ANSWER, False))

"""
Exercise 2.3

Answer with the boolean value of: 467 == 490.


Write your code below and put the answer into the variable ANSWER.
"""

result = 467 is 490




ANSWER = result

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("2.3", ANSWER, False))

"""
Exercise 2.4

Create three variables representing dice values: 'd1' = 2, 'd2' = 5 and
'd3' = 4. Sum them up and answer with the result.


Write your code below and put the answer into the variable ANSWER.
"""

d1 = 2
d2 = 5
d3 = 4

result = d1+d2+d3




ANSWER = result

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("2.4", ANSWER, False))

"""
Exercise 2.5

Create an if statement to see if the total value of your dices is 11 or
higher. If that is the case, answer with the string: 'big', else answer
with the string: 'nothing'.


Write your code below and put the answer into the variable ANSWER.
"""

if result >= 11:
    result = "big"
else:
    result = "nothing"




ANSWER = result

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("2.5", ANSWER, False))

"""
Exercise 2.6

Create an elif statement that checks your total dice value. The checks and
results should be: three of the same value = 'triple', total of 11 or
higher = 'big', total of 10 or lower = 'small'. If you get a triple you
should not make more checks.


Write your code below and put the answer into the variable ANSWER.
"""

result = d1+d2+d3

if d1 == d2 and d1 == d3 and d2 == d3:
    result = "triple"
elif result >= 11:
    result = "big"
elif result <= 10:
    result = "small"




ANSWER = result

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("2.6", ANSWER, False))

"""
--------------------------------------------------------------------------
Section 3. Built-in functions

Some useful built-in functions.

"""



"""
Exercise 3.1

Use `max()` to find the largest number in the serie:
6,8,95,2,12,152,4,78,621,45.

Answer with the result.


Write your code below and put the answer into the variable ANSWER.
"""

myList = (6, 8, 95, 2, 12, 152, 4, 78, 621, 45)
result = max(myList)




ANSWER = result

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("3.1", ANSWER, False))

"""
Exercise 3.2

Use `min()` to find the smallest number in the serie:
6,8,95,2,12,152,4,78,621,45.

Answer with the result.


Write your code below and put the answer into the variable ANSWER.
"""

myList = (6, 8, 95, 2, 12, 152, 4, 78, 621, 45)
result = min(myList)




ANSWER = result

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("3.2", ANSWER, False))

"""
Exercise 3.3

Use `len()` to find the number of letters in the word: memory.

Answer with the result.


Write your code below and put the answer into the variable ANSWER.
"""

word = "memory"
result = len(word)




ANSWER = result

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("3.3", ANSWER, False))

"""
Exercise 3.4

Convert the number 244 to a string and add it to the word 'memory'. Answer
with the result.


Write your code below and put the answer into the variable ANSWER.
"""

result = "memory" + str(244)




ANSWER = result

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("3.4", ANSWER, False))

"""
Exercise 3.5

Convert the number 140.35 to an integer and then to a string. Add it to the
beginning of the word: 'memory'. Answer with the result.


Write your code below and put the answer into the variable ANSWER.
"""

number = int(140.35)
string = str(number)
result = string + "memory"




ANSWER = result

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("3.5", ANSWER, False))

"""
--------------------------------------------------------------------------
Section 4. Functions

Basic functions.

"""



"""
Exercise 4.1

Create a function called 'prodNr' that takes two arguments, 5 and 19. The
function should return the product of the numbers.

Answer with a call to the function.


Write your code below and put the answer into the variable ANSWER.
"""

def prodNr(a, b):
    """
    Product of 2 numbers
    """
    return a*b


ANSWER = prodNr(5, 19)

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("4.1", ANSWER, False))

"""
Exercise 4.2

Create a function called 'funnyWord' that takes one argument and adds it to
the string ' is a funny word'. If the argument is 'water', the function
should return: 'water is a funny word'.

Use the argument 'restaurant' and answer with a call to the function.


Write your code below and put the answer into the variable ANSWER.
"""

def funnyWord(arg1):
    """
    Adds the word infront of a sentence
    """
    return arg1 + " is a funny word"



ANSWER = funnyWord("restaurant")

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("4.2", ANSWER, False))

"""
Exercise 4.3

Create a function called 'inRange' that takes one argument. The function
should return 'true' if the argument is higher than 50 and lower than 100.
If the number is out of range, the function should return 'false'. The
return type should be boolean.

Use the argument 64 and answer with a call to the function.


Write your code below and put the answer into the variable ANSWER.
"""

def inRange(arg1):
    """
    Decides wether or not the value is in range
    """
    if arg1 > 50 and arg1 < 100:
        return True
    else:
        return False




ANSWER = inRange(64)

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("4.3", ANSWER, False))

"""
--------------------------------------------------------------------------
Section 5. Iteration and loops

For-loops and while-loops.

"""



"""
Exercise 5.1

Create a while-loop that adds 3 to the number 19, 51 times. Answer with the
result.


Write your code below and put the answer into the variable ANSWER.
"""

x = 19
i = 0

while i < 51:
    x = x + 3
    i = i+1





ANSWER = x

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("5.1", ANSWER, False))

"""
Exercise 5.2

Create a while-loop that subtracts 7 from 15, 66 times. Answer with the
result.


Write your code below and put the answer into the variable ANSWER.
"""


x = 15
y = 7
i = 0

while i < 66:
    x = x-y
    i = i+1




ANSWER = x

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("5.2", ANSWER, False))

"""
Exercise 5.3

Create a for-loop that counts the number of elements in the serie:

> 6,8,95,2,12,152,4,78,621,45

Answer with the result.


Write your code below and put the answer into the variable ANSWER.
"""

myList = (6, 8, 95, 2, 12, 152, 4, 78, 621, 45)
numberCount = 0

for number in myList:
    numberCount = numberCount+1





ANSWER = numberCount

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("5.3", ANSWER, False))

"""
Exercise 5.4

Create a for-loop that sums up the numbers in the serie:

> 67,2,12,28,128,15,90,4,579,450

Answer with the result.


Write your code below and put the answer into the variable ANSWER.
"""

myList = (67, 2, 12, 28, 128, 15, 90, 4, 579, 450)
numbersSum = 0

for value in myList:
    numbersSum = numbersSum + value




ANSWER = numbersSum

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("5.4", ANSWER, False))

"""
Exercise 5.5

Create a for-loop that finds the largest number in the serie:

> 6,8,95,2,12,152,4,78,621,45

Answer with the result.


Write your code below and put the answer into the variable ANSWER.
"""

myList = (6, 8, 95, 2, 12, 152, 4, 78, 621, 45)
largestValue = None

for value in myList:
    if largestValue == None or value > largestValue:
        largestValue = value




ANSWER = largestValue

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("5.5", ANSWER, False))

"""
Exercise 5.6

Create a for-loop that goes through the numbers:

> 67,2,12,28,128,15,90,4,579,450

If the current number is even, you should add it to a variable and if the
current number is odd, you should subtract it from the variable.

Answer with the final result.


Write your code below and put the answer into the variable ANSWER.
"""

myList = (67, 2, 12, 28, 128, 15, 90, 4, 579, 450)
total = 0

for value in myList:
    if value%2 is 0:
        total = total + value
    else:
        total = total - value



ANSWER = total

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("5.6", ANSWER, False))


dbwebb.exitWithSummary()
