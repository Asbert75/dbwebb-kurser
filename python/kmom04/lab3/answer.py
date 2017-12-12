#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
11b0a51372f3a4069901684ccadf5d7c
python
lab3
eroa16
2016-09-20 18:37:40
v2.2.15 (2016-05-31)

Generated 2016-09-20 20:37:41 by dbwebb lab-utility v2.2.15 (2016-05-31).
https://github.com/mosbth/lab
"""


from Dbwebb import Dbwebb

dbwebb = Dbwebb()
print(">>> Ready to begin.")



"""
==========================================================================
Lab 3 - python



"""



"""
--------------------------------------------------------------------------
Section 1. List basics



"""



"""
Exercise 1.1

Concatenate the two lists [drums, bumblebee] and [piano, wall].

Answer with your list.


Write your code below and put the answer into the variable ANSWER.
"""

result = ["drums", "bumblebee"] + ["piano", "wall"]




ANSWER = result

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.1", ANSWER, False))

"""
Exercise 1.2

Use the list [wasp, fly, butterfly, bumblebee, mosquito].

Add the words 'icecream' and 'donkey' as the second and third element.

Answer with the modified list.


Write your code below and put the answer into the variable ANSWER.
"""

myList = ["wasp", "fly", "butterfly", "bumblebee", "mosquito"]
myList.insert(1, "icecream")
myList.insert(2, "donkey")




ANSWER = myList

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.2", ANSWER, False))

"""
Exercise 1.3

Use the list [wasp, fly, butterfly, bumblebee, mosquito].

Replace the third word with: 'tablet'.

Answer with the modified list.


Write your code below and put the answer into the variable ANSWER.
"""

myList = ["wasp", "fly", "butterfly", "bumblebee", "mosquito"]
myList[2] = "tablet"




ANSWER = myList

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.3", ANSWER, False))

"""
Exercise 1.4

Sort the list

> [Dafoe, Sheen, Berenger, Depp, Whitaker]

in ascending alphabetical order. Answer with the sorted list.


Write your code below and put the answer into the variable ANSWER.
"""

myList = ["Dafoe", "Sheen", "Berenger", "Depp", "Whitaker"]
myList.sort()




ANSWER = myList

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.4", ANSWER, False))

"""
Exercise 1.5

Use the list from the last excercise

> [Dafoe, Sheen, Berenger, Depp, Whitaker]

and sort it in decending alphabetical order. Answer with the sorted list.


Write your code below and put the answer into the variable ANSWER.
"""

myList = ["Dafoe", "Sheen", "Berenger", "Depp", "Whitaker"]
myList.sort()
myList.reverse()




ANSWER = myList

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.5", ANSWER, False))

"""
Exercise 1.6

Use `pop()` to get the second and the last element in the list:

> [wasp, fly, butterfly, bumblebee, mosquito]

Answer with the popped elements in a new list.


Write your code below and put the answer into the variable ANSWER.
"""

myList = ["wasp", "fly", "butterfly", "bumblebee", "mosquito"]

removeOne = myList.pop(1)
removeTwo = myList.pop(-1)

poppedList = [removeOne, removeTwo]




ANSWER = poppedList

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.6", ANSWER, False))

"""
Exercise 1.7

Use `remove()` to delete the word:

> 'bobcat'

from the list:

> [lion, tiger, ozelot, bobcat, cougar]

Answer with the modified list.


Write your code below and put the answer into the variable ANSWER.
"""

myList = ["lion", "tiger", "ozelot", "bobcat", "cougar"]

myList.remove("bobcat")




ANSWER = myList

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.7", ANSWER, False))

"""
--------------------------------------------------------------------------
Section 2. Built-in list functions

Some basic built-in functions.

"""



"""
Exercise 2.1

Use a built-in function to sum all numbers in the list:

> [123, 4, 125, 69, 155]

Answer with the result as an integer.


Write your code below and put the answer into the variable ANSWER.
"""

myList = [123, 4, 125, 69, 155]
result = sum(myList)




ANSWER = result

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("2.1", ANSWER, False))

"""
Exercise 2.2

Use built-in functions, such as `sum` and `len` to get the average value of
the list:

> [123, 4, 125, 69, 155]

Answer with the result as a float with at most one decimal.


Write your code below and put the answer into the variable ANSWER.
"""

result = sum(myList)/len(myList)




ANSWER = result

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("2.2", ANSWER, False))

"""
Exercise 2.3

Use a built-in function to get the lowest number in the list:

> [67, 50, 2, 39, 15]

Answer with the result as a integer.


Write your code below and put the answer into the variable ANSWER.
"""

myList = [67, 50, 2, 39, 15]
result = min(myList)




ANSWER = result

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("2.3", ANSWER, False))

"""
Exercise 2.4

Use the built-in functions `split()` and `join()` to fix this string:

> "The?grass?is?growing"

into a real sentence, (without '?').

Answer with the fixed string.


Write your code below and put the answer into the variable ANSWER.
"""

mess = "The?grass?is?growing"
splitMess = mess.split("?")
fix = " ".join(splitMess)





ANSWER = fix

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("2.4", ANSWER, False))

"""
Exercise 2.5

Use the string:

> "For every minute you are angry you lose sixty seconds of happiness."

and split it with the delimiter " " (space).

Answer with the element at index 2.


Write your code below and put the answer into the variable ANSWER.
"""

word = "For every minute you are angry you lose sixty seconds of happiness"
myList = word.split(" ")
result = myList[2]


ANSWER = result

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("2.5", ANSWER, False))

"""
Exercise 2.6

Use slice on the list

> [a, b, c, d, e]

and replace the second and third element with

> "green, purple"

Answer with the modified list.


Write your code below and put the answer into the variable ANSWER.
"""

myList = ["a", "b", "c", "d", "e"]

myList[1:3] = "green", "purple"




ANSWER = myList

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("2.6", ANSWER, False))

"""
Exercise 2.7

Use slice on the list

> [a, b, c, d, e]

and replace the last two elements with

> "green, purple"

Answer with the modified list.


Write your code below and put the answer into the variable ANSWER.
"""

myList = ["a", "b", "c", "d", "e"]
myList[-2:] = "green", "purple"




ANSWER = myList

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("2.7", ANSWER, False))

"""
Exercise 2.8

Use slice on the list

> [a, b, c, d, e]

and insert the words

> "green, purple"

after the third element.

Answer with the modified list.


Write your code below and put the answer into the variable ANSWER.
"""

myList = ["a", "b", "c", "d", "e"]
myList[3:3] = ["green"]
myList[4:4] = ["purple"]


ANSWER = myList

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("2.8", ANSWER, True))

"""
Exercise 2.9

Use `del` on the list

> [dvd, mp3, blu-ray, vhs, cd]

and delete the first element.

Answer with the modified list.


Write your code below and put the answer into the variable ANSWER.
"""

myList = ["dvd", "mp3", "blu-ray", "vhs", "cd"]
del myList[0]




ANSWER = myList

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("2.9", ANSWER, False))

"""
Exercise 2.10

Use `del` on the list

> [dvd, mp3, blu-ray, vhs, cd]

and delete the second and third element.

Answer with the modified list.


Write your code below and put the answer into the variable ANSWER.
"""
myList = ["dvd", "mp3", "blu-ray", "vhs", "cd"]
del myList[1:3]





ANSWER = myList

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("2.10", ANSWER, False))

"""
Exercise 2.11

Assign the list

> [d, c, b, a, e]

to a variable called 'list1'.

Assign the list again, but to another variable called 'list2'.

Answer with the result of 'list1 is list2'.


Write your code below and put the answer into the variable ANSWER.
"""

list1 = ["d", "c", "b", "a", "e"]
list2 = ["d", "c", "b", "a", "e"]

result = list1 is list2




ANSWER = result

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("2.11", ANSWER, False))

"""
Exercise 2.12

Use your lists from the last exercise. Assign 'list1' to another variable
called 'list3' like this:

> list3 = list1

Answer with the result of 'list1 is list3'.


Write your code below and put the answer into the variable ANSWER.
"""

list3 = list1
result = list1 is list3




ANSWER = result

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("2.12", ANSWER, False))

"""
Exercise 2.13

Use your lists from the last exercise. Change the first element in 'list1'
to

> "x"

Answer with 'list3'.


Write your code below and put the answer into the variable ANSWER.
"""

list1[0] = "x"

ANSWER = list3

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("2.13", ANSWER, False))

"""
--------------------------------------------------------------------------
Section 3. Lists as arguments

Some excercises with passing lists as arguments to a function.

"""


"""
Exercise 3.1

Create a function that returns the list passed as argument sorted in
numerical and ascending order. Also multiply all values with 10.

Use the list:

> [67, 50, 2, 39, 15]

and the built-in method `sort()`.

Answer with the sorted list.


Write your code below and put the answer into the variable ANSWER.
"""

def returnList(listToReturn):
    """
    Returns list multiplied by 10 and sorted.
    """
    newList = []
    for i in range(len(listToReturn)):
        item = listToReturn[i]*10
        newList.append(item)
    newList.sort()
    return newList

myList = [67, 50, 2, 39, 15]
result = returnList(myList)



ANSWER = result

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("3.1", ANSWER, False))

"""
Exercise 3.2

Create a function that takes the list:

> [123, 4, 125, 69, 155]

as argument.

The function should multiply all even numbers by 3 and add 8 to all odd
numbers.

Answer with the modified list sorted in numerical order, descending.


Write your code below and put the answer into the variable ANSWER.
"""

myList = [123, 4, 125, 69, 155]

def multiplyList(theList):
    """
    Exercise function
    """
    newList = []
    item = None
    for i in range(len(theList)):
        item = theList[i]
        if (item%2) == 0:
            item = (item*3)
        else:
            item = (item+8)
        newList.append(item)

    newList.sort()
    newList.reverse()
    return newList

result = multiplyList(myList)



ANSWER = result

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("3.2", ANSWER, False))


dbwebb.exitWithSummary()
