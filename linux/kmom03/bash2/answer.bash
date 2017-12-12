#!/usr/bin/env bash

#
# 7531ef58c3f8315305516b15a7c5c4c5
# linux
# bash2
# eroa16
# 2017-02-03 17:17:35
# v2.2.28* (2017-02-01)
#
# Generated 2017-02-03 18:17:37 by dbwebb lab-utility v2.2.28* (2017-02-01).
# https://github.com/mosbth/lab
#

export ANSWER
. .dbwebb.bash
echo "${PROMPT}Ready to begin."



# ==========================================================================
# Lab 2 - linux
#
# A lab where you use Unix tools available from the command line interface
# together with a little Bash, to find and handle information in a [IRC
# loggfil](ircLog.txt).
#

# --------------------------------------------------------------------------
# Section 1. Bash
#
# Train Linux commands and use them together with Bash.
#
# I this exercise you will mainly use comands like `grep`, `wc`, `head` and
# `tail` to search for information in a log file from the irc-chat.
#
# Write HTML in text, wrap in backtick `<a href="moped">mask</a>`
#
# Pure link as HTML <a href="moped">mask</a>
#
# ```
# <html>
# ```
#
# ```
# a > 2
# ```
#
# Then you combine the output of the commands to variables in Bash. Use the
# man-pages when needed to find information on haow to solve the exercises.
#

#"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.1 (1 points)
#
# Create a variable named `FILE` and give it the value `ircLog.txt`.
#
# Answer with the value of `$FILE`.
#
# Write your code below and put the answer into the variable ANSWER.
#

FILE='ircLog.txt'




ANSWER=$FILE

# I will now test your answer - change false to true to get a hint.
assertEqual "1.1" true

#"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.2 (1 points)
#
# Use the `wc` command to count the number of lines in the irc log. Show only
# the number of lines and the name of the file, seperated by a space.
#
# Save the answer in a variable and answer with that variable.
#
# Write your code below and put the answer into the variable ANSWER.
#






ANSWER=$(wc -l ircLog.txt)

# I will now test your answer - change false to true to get a hint.
assertEqual "1.2" false

#"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.3 (1 points)
#
# Use `wc` together with `cut` to count the number of words in the irc log.
#
# Save only the number of words in a variable and answer with the variable.
#
# Tip: Use the pipe (`|`) command.
#
# Write your code below and put the answer into the variable ANSWER.
#

WCOUNT=$(wc -w ircLog.txt | cut -c-5)




ANSWER=$WCOUNT

# I will now test your answer - change false to true to get a hint.
assertEqual "1.3" true

#"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.4 (1 points)
#
# Find the row with 'pansars' opinion of 'notepad'.
#
# Save the answer in a variable and answer with that variable.
#
# Write your code below and put the answer into the variable ANSWER.
#

OPINION=$(grep "pansar" ircLog.txt | grep "notepad")




ANSWER=$OPINION

# I will now test your answer - change false to true to get a hint.
assertEqual "1.4" false

#"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.5 (1 points)
#
# Find the last four rows in the logfile.
#
# Write your code below and put the answer into the variable ANSWER.
#






ANSWER=$(tail -4 ircLog.txt)

# I will now test your answer - change false to true to get a hint.
assertEqual "1.5" false

#"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.6 (1 points)
#
# When was the log opened for the first time? Hint: 'Log opened'.
#
# Answer with the row that says when the log was opened for the first time.
#
# Write your code below and put the answer into the variable ANSWER.
#






ANSWER=$(head -1 ircLog.txt)

# I will now test your answer - change false to true to get a hint.
assertEqual "1.6" false

#"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.7 (1 points)
#
# What does the third line where 'wasa' says something say?
#
# Write your code below and put the answer into the variable ANSWER.
#






ANSWER=$(grep "wasa" ircLog.txt | head -3 | tail -1)

# I will now test your answer - change false to true to get a hint.
assertEqual "1.7" false

#"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.8 (1 points)
#
# How many lines is logged at the time 11:15?
#
# Write your code below and put the answer into the variable ANSWER.
#






ANSWER=$(grep -c "11:15" ircLog.txt)

# I will now test your answer - change false to true to get a hint.
assertEqual "1.8" false

#"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.9 (3 points)
#
# Find the first 10 lines from 'Wed Jun 17 2015'.
#
# Write your code below and put the answer into the variable ANSWER.
#






ANSWER=$(grep -A 10 "Wed Jun 17 2015" ircLog.txt | tail -10)

# I will now test your answer - change false to true to get a hint.
assertEqual "1.9" true

#"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.10 (3 points)
#
# Find the lines that are from the 'forum' and contains details about
# 'projektet' and 'htmlphp'.
#
# Write your code below and put the answer into the variable ANSWER.
#






ANSWER=$(grep "Forumet" ircLog.txt | grep -E "htmlphp" | grep -E "projektet")

# I will now test your answer - change false to true to get a hint.
assertEqual "1.10" true

#"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.11 (3 points)
#
# What did 'Bobbzorzen' say on the line, two lines before he said 'cewl'?
#
# Write your code below and put the answer into the variable ANSWER.
#






ANSWER=$(grep "Bobbzorzen" ircLog.txt | grep -B 2 "cewl" | head -1)

# I will now test your answer - change false to true to get a hint.
assertEqual "1.11" false

#"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.12 (3 points)
#
# How many words are there in the fourth to ninth row, under the day 'Mon Jun
# 08 2015'?
#
# Write your code below and put the answer into the variable ANSWER.
#






ANSWER=$(grep -A 9 "Mon Jun 08 2015" ircLog.txt | tail -6 | wc -w)

# I will now test your answer - change false to true to get a hint.
assertEqual "1.12" true

#"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.13 (3 points)
#
# Find the first row where 'pansar' says something when the time is 07:48.
#
# Write your code below and put the answer into the variable ANSWER.
#






ANSWER=$(grep "07:48" ircLog.txt | grep "pansar" | head -1)

# I will now test your answer - change false to true to get a hint.
assertEqual "1.13" true


exitWithSummary
