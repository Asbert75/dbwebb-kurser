#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
45de5c17724ce7b98b2d3c6c65e7748c
python
lab2
eroa16
2016-09-13 16:02:07
v2.2.15 (2016-05-31)

Generated 2016-09-13 18:02:08 by dbwebb lab-utility v2.2.15 (2016-05-31).
https://github.com/mosbth/lab
"""


from Dbwebb import Dbwebb

dbwebb = Dbwebb()
print(">>> Ready to begin.")



"""
==========================================================================
Lab 2 - python

Strings and files.

"""



"""
--------------------------------------------------------------------------
Section 1. Strings

The basics of strings.

"""



"""
Exercise 1.1

Assign the word: 'banana' to a variable and put your variable as the
answer.


Write your code below and put the answer into the variable ANSWER.
"""

result = "banana"




ANSWER = result

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.1", ANSWER, False))

"""
Exercise 1.2

Assign the word 'banana' to a variable. Create another variable where you
put the first and the last letter in the word.

Answer with the second variable.


Write your code below and put the answer into the variable ANSWER.
"""

word = "banana"
result = word[0] + word[-1]




ANSWER = result

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.2", ANSWER, False))

"""
Exercise 1.3

Assign the word: orange to a variable. Answer with the length of the word
as an integer.


Write your code below and put the answer into the variable ANSWER.
"""

word = "orange"
result = int(len(word))




ANSWER = result

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.3", ANSWER, False))

"""
Exercise 1.4

Use the 'in-operator' to see if the word: 'milk' contains the letter 'a'.
Answer with a boolean result.


Write your code below and put the answer into the variable ANSWER.
"""

result = ""

if "a" in "milk":
    result = True
else:
    result = False




ANSWER = result

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.4", ANSWER, False))

"""
Exercise 1.5

Make all the letters in the word 'orange' capitalized. Answer with the
capitalized word.


Write your code below and put the answer into the variable ANSWER.
"""

word = "orange"
result = word.upper()




ANSWER = result

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.5", ANSWER, False))

"""
Exercise 1.6

Use the built-in function `startswith()` to see if the word 'potato' starts
with the letter 't'. Answer with the boolean value.


Write your code below and put the answer into the variable ANSWER.
"""

word = "potato"

if word.startswith("t"):
    result = True
else:
    result = False




ANSWER = result

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.6", ANSWER, False))

"""
Exercise 1.7

Assign the words: 'milk' and 'car' to two different variables.

Create a function and pass the two words as arguments to it. Your function
should return them as a single word.

Answer with the result.


Write your code below and put the answer into the variable ANSWER.
"""

word1 = "milk"
word2 = "car"

def combineWord(wordOne, wordTwo):
    """
    An exercise function
    """
    return wordOne+wordTwo

result = combineWord(word1, word2)




ANSWER = result

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.7", ANSWER, False))

"""
Exercise 1.8

Create a function and pass the word: 'banana' to it. Your function should
return the sentence:

> "This word was: banana"

Answer with the result.


Write your code below and put the answer into the variable ANSWER.
"""

def returnWord(wordToReturn):
    """
    An exercise function
    """
    return "This word was: " + wordToReturn

result = returnWord("banana")




ANSWER = result

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.8", ANSWER, False))

"""
Exercise 1.9

Create a function and pass the word: 'car' to it.

Your function should return the string 'yes' if the word is longer than 5
characters. Else return 'no'.

Answer with the result.


Write your code below and put the answer into the variable ANSWER.
"""

def returnString(returnedWord):
    """
    An exercise function
    """
    if len(returnedWord) > 5:
        return "yes"
    else:
        return "no"

result = returnString("car")




ANSWER = result

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.9", ANSWER, False))

"""
Exercise 1.10

Create a function and pass the word: 'orange' to it.

Your function should return a string with the word backwards.

Answer with the result.


Write your code below and put the answer into the variable ANSWER.
"""

def backwardString(wordToReverse):
    """
    An exercise function
    """
    return wordToReverse[::-1]

result = backwardString("orange")


ANSWER = result

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.10", ANSWER, False))

"""
Exercise 1.11

Create a function and pass the word: 'milk' to it.

Your function should exclude the first and the last letter of the word and
return it.

Answer with the result.


Write your code below and put the answer into the variable ANSWER.
"""

def removeLetters(oldWord):
    """
    An exercise function
    """
    return oldWord[1:-1]

result = removeLetters("milk")




ANSWER = result

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.11", ANSWER, False))

"""
Exercise 1.12

Use `str.format()` to print out:

> 'My 'string' has 'integer' 'string''.

Use the values: 'brother', '2' and 'dogs'. Answer with the result.


Write your code below and put the answer into the variable ANSWER.
"""


result = "My {0} has {1} {2}".format("brother", 2, "dogs")
print(result)



ANSWER = result

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.12", ANSWER, False))

"""
Exercise 1.13

Use `find` and `slice` on the string:

> "984.45.6.65 : (wasp), boat"

to get the word inside the parenthesis.

Answer with the word as a string.


Write your code below and put the answer into the variable ANSWER.
"""

word = "984.45.6.65 : (wasp), boat"

spos = word.find("(")
epos = word.find(")")
result = word[spos+1:epos]




ANSWER = result

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("1.13", ANSWER, False))

"""
--------------------------------------------------------------------------
Section 2. Files

This section uses the text file: '[httpd-access.txt](httpd-access.txt)'.

"""



"""
Exercise 2.1

Open the file and count the number of times a line starts with '81'. Answer
with the result as an integer.


Write your code below and put the answer into the variable ANSWER.
"""

textFile = open("httpd-access.txt", "r")

count = 0

for line in textFile:
    if line.startswith("81"):
        count = count + 1

textFile.close()

ANSWER = count

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("2.1", ANSWER, False))

"""
Exercise 2.2

Find out the last 4 digits on line 821 in the file. Answer with the result
as an integer.


Write your code below and put the answer into the variable ANSWER.
"""

newFile = open("httpd-access.txt", "r")

lineCount = 0
result = " "

for newLine in newFile:
    lineCount = lineCount+1
    if lineCount == 821:
        result = int(newLine[-5:-1])


ANSWER = result

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("2.2", ANSWER, False))

"""
Exercise 2.3

Find out which of the ip adresses 81.226.253.26 and 95.19.133.73 that has
the highest amount of entries in the file.

Answer with the result as an integer.


Write your code below and put the answer into the variable ANSWER.
"""

ip1Count = 0
ip2Count = 0
result = 0

newFile = open("httpd-access.txt", "r")

for line in newFile:
    if "81.226.253.26" in line:
        ip1Count = ip1Count + 1
    elif "95.19.133.73" in line:
        ip2Count = ip2Count + 1

if ip1Count > ip2Count:
    result = ip1Count
else:
    result = ip2Count




ANSWER = result

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("2.3", ANSWER, False))

"""
Exercise 2.4

Count the number of periods (.) there are in the file.

Use the built-in function `count()` on the file after you have converted it
to a string.

Answer with the result as an integer.


Write your code below and put the answer into the variable ANSWER.
"""

openFile = open("httpd-access.txt")

periodCount = 0

for line in openFile:
    periodCount = periodCount + line.count(".")

result = periodCount





ANSWER = result

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("2.4", ANSWER, False))

"""
Exercise 2.5

Find the characters on line 637 from index 65 to index 75. Make sure that
the character at index 75 also gets included.

Answer with the piece of string you found.


Write your code below and put the answer into the variable ANSWER.
"""

openNewFile = open("httpd-access.txt")

lineCount = 0

for line in openNewFile:
    lineCount = lineCount + 1
    if lineCount == 637:
        result = line[65:76]

openNewFile.close()


ANSWER = result

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("2.5", ANSWER, False))

"""
Exercise 2.6

Find the last element (digit) on each line, if there are any, and sum all
that are even.

Answer with the result as an integer.


Write your code below and put the answer into the variable ANSWER.
"""

openNewFile = open("httpd-access.txt")
numbersSummed = 0

for line in openNewFile:
    line.strip()
    try:
        lastLetter = int(line[-2])
        if lastLetter % 2 == 0:
            numbersSummed = numbersSummed + lastLetter
    except Exception:
        continue

result = numbersSummed

ANSWER = result

# I will now test your answer - change false to true to get a hint.
print(dbwebb.assertEqual("2.6", ANSWER, False))


dbwebb.exitWithSummary()
