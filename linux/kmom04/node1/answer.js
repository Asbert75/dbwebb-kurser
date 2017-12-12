#!/usr/bin/env node

/**
 * @preserve 7f7519f35f2dcf355f7933334ceec4e3
 *
 * 7f7519f35f2dcf355f7933334ceec4e3
 * linux
 * node1
 * eroa16
 * 2017-02-12 14:30:49
 * v2.2.28* (2017-02-01)
 *
 * Generated 2017-02-12 15:31:30 by dbwebb lab-utility v2.2.28* (2017-02-01).
 * https://github.com/mosbth/lab
 */"use strict";


import dbwebb from "./.dbwebb.js";

var ANSWER = null;
console.log(dbwebb.prompt + "Ready to begin.");



/** ======================================================================
 * node1 - JavaScript med Nodejs
 *
 * JavaScript using nodejs.
 *
 */



/** ----------------------------------------------------------------------
 * Section 1 . nodejs built-ins
 *
 * In this section we try out some of the new nodejs and ES6 features.
 *
 */



/**
 * Exercise 1.1
 *
 * Create a variable called `numbersArray` holding the numbers 6,46,12,19,82.
 *
 * Use find to get the first occurence of a number bigger than or equal to 42.
 *
 * Answer with the number.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */

function findFourtyTwo(element) {
    return element >= 42;
}

var numbersArray = [6, 46, 12, 19, 82];




ANSWER = numbersArray.find(findFourtyTwo);

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("1.1", ANSWER, false);

/**
 * Exercise 1.2
 *
 * Find the smallest number in `numbersArray` by using the spread operator
 * `...` and the function `Math.min()`.
 *
 * Answer with the smallest number.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */

var answer = Math.min(...numbersArray);




ANSWER = answer;

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("1.2", ANSWER, false);

/**
 * Exercise 1.3
 *
 * Create a function called `meaningOfLife()` with one default parameter with
 * the value of 42.
 *
 * The function should return the sentence 'The meaning of life is '
 * concatenated with the parameter.
 *
 * Answer with a call to the `meaningOfLife()` function without any
 * parameters.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */

function meaningOfLife(val=42) {
    return 'The meaning of life is ' + val;
}




ANSWER = meaningOfLife();

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("1.3", ANSWER, false);

/**
 * Exercise 1.4
 *
 * Check if the word Kangaroo contains the letters 'oo'. Return true or false
 * depending on the answer.
 *
 * Tip: Use nodejs function `includes`.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */

var word = "Kangaroo";




ANSWER = word.includes("oo");

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("1.4", ANSWER, false);

/**
 * Exercise 1.5
 *
 * Check if the word Kangaroo starts with the letters 'El'. Return true or
 * false depending on the answer.
 *
 * Tip: Use nodejs function `startsWith`.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */



ANSWER = word.startsWith("El");

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("1.5", ANSWER, false);

/** ----------------------------------------------------------------------
 * Section 2 . Filtering arrays
 *
 * In this section we filter arrays in different ways.
 *
 */



/**
 * Exercise 2.1
 *
 * Use `numbersArray` from above holding the numbers 6,46,12,19,82.
 *
 * Use a for-loop to save all numbers smaller than 42 in a new array.
 *
 * Answer with the resulting array.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */

function smallerThan(element) {
    return element < 42;
}

var newArray = [];

var i;

for (i = 0; i < numbersArray.length; i++) {
    if (smallerThan(numbersArray[i])) {
        newArray.push(numbersArray[i]);
    }
}



ANSWER = newArray;

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("2.1", ANSWER, false);

/**
 * Exercise 2.2
 *
 * Create a variable called `moreNumbersArray` holding the numbers
 * 6,46,12,19,82,71,33.
 *
 * Use the built-in higher-order function `filter` and a callback function to
 * filter out all numbers bigger than or equal to 42.
 *
 * Use arrow-notation to keep the code short and concise.
 *
 * Answer with the resulting array.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */

function filterTooBig(n) {
    return n < 42;
}

var moreNumbersArray = [6, 46, 12, 19, 82, 71, 33];

var newArrayTwo = moreNumbersArray.filter(moreNumbersArray => filterTooBig(moreNumbersArray));




ANSWER = newArrayTwo;

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("2.2", ANSWER, false);

/** ----------------------------------------------------------------------
 * Section 3 . Transforming arrays
 *
 * In this section we change arrays using the higher-order functions map and
 * reduce.
 *
 */



/**
 * Exercise 3.1
 *
 * Create a variable called `stringArray` holding the strings 'Pete
 * Conrad','Richard F. Gordon Jr.','Alan Bean'.
 *
 * Use a for-loop to concatenate the string ' was on the apollo 12' too each
 * name in the array.
 *
 * Store the result in a new array and answer with that array.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */

var stringArray = ['Pete Conrad', 'Richard F. Gordon Jr.', 'Alan Bean'];
var newStringArray = [];

for (i = 0; i < stringArray.length; i++) {
    newStringArray.push(stringArray[i] + " was on the apollo 12");
}




ANSWER = newStringArray;

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("3.1", ANSWER, false);

/**
 * Exercise 3.2
 *
 * Use the `stringArray` from above and the built-in higher-order function
 * `map` to concatenate the string ' was not on the apollo 11' and each name.
 *
 * Use arrow notation to keep the code simple and concise.
 *
 * Answer with the resulting array.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */

var newStrings = stringArray.map(name => name + " was not on the apollo 11");



ANSWER = newStrings;

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("3.2", ANSWER, false);

/**
 * Exercise 3.3
 *
 * Create a variable called `maybePrimeNumber` holding the numbers
 * 113,128,131,136,139,148,151,156,163.
 *
 * In a for-loop sum all prime numbers from `maybePrimeNumber`, you need to
 * find out whether or not the number is a prime number.
 *
 * Answer with the resulting sum.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */

var maybePrimeNumber = [113, 128, 131, 136, 139, 148, 151, 156, 163];

function isPrime(value) {
    for (var i = 2; i < value; i++) {
        if (value % i === 0) {
            return false;
        }
    }
    return value > 1;
}

var primeSum = 0;

for (i = 0; i < maybePrimeNumber.length; i++) {
    if (isPrime(maybePrimeNumber[i])) {
        primeSum += maybePrimeNumber[i];
    }
}




ANSWER = primeSum;

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("3.3", ANSWER, false);

/**
 * Exercise 3.4
 *
 * Create a function `isNotPrime()` that takes one parameter (an integer) and
 * tests if that number is a prime number. If the number is not prime, the
 * number is returned otherwise return 0.
 *
 * Use the built-in higher-order functions `reduce` to sum all numbers that
 * are NOT prime numbers.
 *
 * Answer with the resulting sum.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */

function isNotPrime(value) {
    for (var i = 2; i < value; i++) {
        if (value % i === 0) {
            return value; // Is not a prime
        }
    }
    return 0;
}

var notPrimeSum = maybePrimeNumber.reduce((cur, nxt) => isNotPrime(cur) + isNotPrime(nxt));



ANSWER = notPrimeSum;

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("3.4", ANSWER, true);


process.exit(dbwebb.exitWithSummary());
