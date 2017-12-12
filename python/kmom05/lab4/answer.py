#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
bab376e61fedf854cbe070e3a7c6d0ac
python
lab4
eroa16
2016-09-29 09:32:15
v2.2.19 (2016-09-27)

Generated 2016-09-29 11:32:15 by dbwebb lab-utility v2.2.19 (2016-09-27).
https://github.com/mosbth/lab
"""


from Dbwebb import Dbwebb

dbwebb = Dbwebb()
print(">>> Ready to begin.")



"""
==========================================================================
Lab 4 - python

Dictionaries and tuples.

"""



"""
--------------------------------------------------------------------------
Section 1. Dictionaries

Some basics with dictionaries.

"""



"""
Exercise 1.1

Create a small phonebook using a dictionary. Use the names as keys and
numbers as values.

Use

> Chandler, Monica, Ross

and corresponding numbers

> 55523645, 55564452, 55545872

Add the phonenumbers as integers. Answer with the resulting dictionary.


Write your code below and put the answer into the variable ANSWER.
"""

phoneBook = {"Chandler": 55523645, "Monica": 55564452, "Ross": 55545872}




ANSWER = phoneBook

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.1", ANSWER, False))

"""
Exercise 1.2

How many items are there in the dictionary?


Write your code below and put the answer into the variable ANSWER.
"""

items = len(phoneBook)




ANSWER = items

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.2", ANSWER, False))

"""
Exercise 1.3

Use the `get()` method on your phonebook and answer with the phonenumber of
'Ross'.


Write your code below and put the answer into the variable ANSWER.
"""

number = phoneBook.get("Ross", 0)




ANSWER = number

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.3", ANSWER, False))

"""
Exercise 1.4

Get all keys from the dictionary and return them in a sorted list.


Write your code below and put the answer into the variable ANSWER.
"""

keys = list()

for k in phoneBook:
    keys.append(k)

keys.sort()


ANSWER = keys

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.4", ANSWER, False))

"""
Exercise 1.5

Get all values from the dictionary and return them in a sorted list.


Write your code below and put the answer into the variable ANSWER.
"""

values = list()
book = phoneBook.items()

for k, v in book:
    values.append(v)

values.sort()





ANSWER = values

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.5", ANSWER, False))

"""
Exercise 1.6

Use the in-operator to test if the name 'Ross' exists in the dictionary.
Answer with the return boolean value.


Write your code below and put the answer into the variable ANSWER.
"""

ross = None

if "Ross" in phoneBook:
    ross = True




ANSWER = ross

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.6", ANSWER, False))

"""
Exercise 1.7

Use the in-operator to test if the phone number 55545872 exists in the
dictionary. Answer with the return boolean value.


Write your code below and put the answer into the variable ANSWER.
"""

number = None

numbers = phoneBook.items()
for k, v in numbers:
    if v == 55545872:
        number = True



ANSWER = number

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.7", ANSWER, False))

"""
Exercise 1.8

Use a for-loop to walk through the dictionary and create a string
representing it. Each name and number should be on its own row, separated
by a space. The names must come in alphabetical order.

Answer with the resulting string.


Write your code below and put the answer into the variable ANSWER.
"""

phoneBookString = ""

phoneList = list()

for k, v in phoneBook.items():
    phoneList.append((k, v))

phoneList.sort()

for k, v in phoneList:
    phoneBookString = phoneBookString + k + " " + str(v) + "\n"



ANSWER = phoneBookString

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.8", ANSWER, False))

"""
Exercise 1.9

Convert the phonenumber to a string and add the prefix '+1-', representing
the language code, to each phone-number.

Answer with the resulting dictionary.


Write your code below and put the answer into the variable ANSWER.
"""

newPhoneBook = dict()

for k, v in phoneBook.items():
    newPhoneBook[k] = "+1-" + str(v)



ANSWER = newPhoneBook

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.9", ANSWER, False))

"""
Exercise 1.10

Get and remove the item 'Ross' from the phonebook (use pop()). Answer with
the resulting dictionary.


Write your code below and put the answer into the variable ANSWER.
"""

tmp = phoneBook
popped = tmp.pop("Ross")




ANSWER = tmp

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.10", ANSWER, False))

"""
Exercise 1.11

Add the item you just popped from the phonebook. Answer with the resulting
dictionary.


Write your code below and put the answer into the variable ANSWER.
"""

tmp["Ross"] = popped




ANSWER = tmp

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.11", ANSWER, False))

"""
--------------------------------------------------------------------------
Section 2. Tuples

Some basics with tuples.

"""



"""
Exercise 2.1

Create a tuple with 'frog, 54, 4.77, fridge, 2'. Answer with the length of
the tuple as an integer.


Write your code below and put the answer into the variable ANSWER.
"""

myTuple = ("frog", 54, 4.77, "fridge", 2)

ANSWER = len(myTuple)

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("2.1", ANSWER, False))

"""
Exercise 2.2

Create a tuple out of:

> (frog, 54, 4.77, fridge, 2).

Assign each value in the tuple to different variables:

> 'a','b','c','d','e'.

Answer with the variable: 'd'. Hint: a,b,c = tuple.


Write your code below and put the answer into the variable ANSWER.
"""

a, b, c, d, e = myTuple

ANSWER = d

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("2.2", ANSWER, False))

"""
Exercise 2.3

Use the list

> [67, 50, 2, 39, 15]

Assign the first two elements to a tuple with a slice on the list.

Answer with the first element in the tuple as an integer.


Write your code below and put the answer into the variable ANSWER.
"""

myList = [67, 50, 2, 39, 15]
myNewTuple = tuple(myList[0:2])

ANSWER = myNewTuple[0]

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("2.3", ANSWER, False))

"""
Exercise 2.4

Create a tuple with

> (frog, 54, 4.77, fridge, 2)

Convert it to a list and replace the second element with:

> "bucket"

Convert it back to a tuple and answer with the first three elements in a
comma-separated string.


Write your code below and put the answer into the variable ANSWER.
"""

myNewTuple = ("frog", 54, 4.77, "fridge", 2)
myNewList = list(myNewTuple)
myNewList[1] = "bucket"
myNewTuple = tuple(myNewList)
res = str(myNewTuple[0]) + "," + str(myNewTuple[1]) + "," + str(myNewTuple[2])




ANSWER = res

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("2.4", ANSWER, False))


dbwebb.exitWithSummary()
