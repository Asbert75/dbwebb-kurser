/**
 * @preserve 7f66622509c90bbe55081f0d501b4110
 *
 * 7f66622509c90bbe55081f0d501b4110
 * javascript1
 * lab2
 * eroa16
 * 2016-11-17 11:35:12
 * v2.2.21 (2016-10-07)
 *
 * Generated 2016-11-17 12:35:13 by dbwebb lab-utility v2.2.21 (2016-10-07).
 * https://github.com/mosbth/lab
 */

(function(dbwebb){
    "use strict";

    var ANSWER = null;

    console.log("Ready to begin.");


/** ======================================================================
 * Lab 2 - javascript1
 *
 * Practice to write functions.
 *
 */



/** ----------------------------------------------------------------------
 * Section 1 . Basic functions
 *
 * Practice on basic functions.
 *
 */



/**
 * Exercise 1.1
 *
 * Create a function called 'sumNumbers()'. The function should take two
 * arguments and return the sum of them. Test the function using the arguments
 * 555 and 197.
 *
 * Answer with the result.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */

function sumNumbers(a, b) {
    return (a + b);
}

var result = sumNumbers(555, 197);



ANSWER = result;

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("1.1", ANSWER, false);

/**
 * Exercise 1.2
 *
 * Create a function called 'productNumbers()'. The function should take three
 * arguments and return the product of them. Try the function using the
 * numbers 555, 197 and 889.
 *
 * Answer with the result.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */

function productNumbers(a, b, c) {
    return a * b * c;
}

result = productNumbers(555, 197, 889);




ANSWER = result;

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("1.2", ANSWER, false);

/**
 * Exercise 1.3
 *
 * Create a function 'sumRangeNumbers()' that returns the sum of all numbers
 * between two chosen numbers. The function should take two arguments, one
 * representing the lowest boundary and one that represents the highest
 * boundary. For example, the arguments 10 and 20 should return the sum of
 * 10+11+12+13...+20.
 *
 * Test it using the values 24 and 88 and answer with the result.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */

function sumRangeNumbers(min, max) {
    var range = 0;

    for (min; min <= max; min++) {
        range += min;
    }

    return range;
}

result = sumRangeNumbers(24, 88);


ANSWER = result;

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("1.3", ANSWER, false);

/**
 * Exercise 1.4
 *
 * Create a function 'stringPhrase()' that returns a phrase. Your word is
 * 'grey'. Pass the word as an argument to the function and the returned
 * phrase should be: 'My favorite color is grey.'.
 *
 * Test your function and answer with the result.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */


function stringPhrase(color) {
    return "My favorite color is " + color + ".";
}

result = stringPhrase("grey");


ANSWER = result;

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("1.4", ANSWER, false);

/**
 * Exercise 1.5
 *
 * Create a function called 'fruitColor()' that takes one argument called
 * 'fruit' and returns the color of the fruit. The function should be aware of
 * the following fruits (banana, apple, kiwi, plum) with respective color
 * (yellow, green, green, red).
 *
 * Try it out using the fruit 'plum' and answer with the result.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */


function fruitColor(fruit) {
    var color = null;

    switch (fruit) {
        case "banana":
            color = "yellow";
            break;
        case "apple":
            color = "green";
            break;
        case "kiwi":
            color = "green";
            break;
        case "plum":
            color = "red";
            break;
        default:
            color = undefined;
            break;
    }

    return color;
}

result = fruitColor("plum");

ANSWER = result;

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("1.5", ANSWER, false);

/**
 * Exercise 1.6
 *
 * Create a function 'printRange()' that takes two arguments 'rangeStart' and
 * 'rangeStop' and returns a string with all numbers comma-separated in the
 * range. Try it using the arguments 29 and 46.
 *
 * Answer with the result.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */


function printRange(rangeStart, rangeStop) {
    var rangeString = "";

    for (var i = rangeStart; i < rangeStop; i++) {
        rangeString += i + ",";
    }

    rangeString += rangeStop;
    return rangeString;
}

result = printRange(29, 46);

ANSWER = result;

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("1.6", ANSWER, false);

/**
 * Exercise 1.7
 *
 * Create a function 'printRangeReversed()' that takes two arguments
 * 'rangeStart' and 'rangeStop' and returns a string with all numbers
 * comma-separated in the range. Try it using the arguments 46 and 29.
 *
 * Answer with the result.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */

function printRangeReversed(rangeStart, rangeStop) {
    var rangeString = "";

    for (var i = rangeStart; i > rangeStop; i--) {
        rangeString += i + ",";
    }

    rangeString += rangeStop;
    return rangeString;
}

result = printRangeReversed(46, 29);


ANSWER = result;

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("1.7", ANSWER, false);

/**
 * Exercise 1.8
 *
 * Create a function 'printAnyRange()' that takes two arguments 'rangeStart'
 * and 'rangeStop' and returns a string with all numbers comma-separated in
 * the range. If 'rangeStart' is smaller than 'rangeStop' then call the
 * function 'printRange()'.  If 'rangeStart' is greater than 'rangeStop' the
 * call the function 'printRangeReversed()'. Try it using the arguments 29 and
 * 46 (both ways).
 *
 * Answer with the result using arguments 29 and 46.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */

function printAnyRange(rangeStart, rangeStop) {
    var rangeString = "";

    if (rangeStart > rangeStop) {
        return printRangeReversed(rangeStart, rangeStop);
    }
    else if (rangeStart < rangeStop) {
        return printRange(rangeStart, rangeStop);
    }
    else {
        rangeString = rangeStart;
        return rangeString;
    }
}

result = printAnyRange(29, 46);

ANSWER = result;

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("1.8", ANSWER, false);

/**
 * Exercise 1.9
 *
 * Create a function called 'stringRepeat()' that returns a string a specific
 * number of times. The function should take two arguments, one string and one
 * number: 'yellow' and 10. The number represents the number of times the
 * string should be added to a string.
 *
 * Test the function and answer with the result.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */

function stringRepeat(string, numTimes) {
    var repeatedString = "";

    for (var i = 0; i < numTimes; i++) {
        repeatedString += string;
    }

    return repeatedString;
}

result = stringRepeat("yellow", 10);



ANSWER = result;

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("1.9", ANSWER, false);

/**
 * Exercise 1.10
 *
 * Create a function called 'calculateInterest()' that returns the money you
 * have after x years of interest, given three arguments: 993, 15 and 3. First
 * argument represents the start money, the second argument represents the
 * number of years your money produces interest. The third argument is the
 * interest rate in percent (%).
 *
 * Test your function and answer with the result with a maximum of 4 decimals.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */

function calculateInterest(capital, years, interestRate) {
    interestRate = 1 + (interestRate / 100);
    var total = null;

    for (var i = 0; i < years; i++) {
        capital *= interestRate;
    }

    total = parseFloat(capital.toFixed(4));
    return total;
}

result = calculateInterest(993, 15, 3);


ANSWER = result;

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("1.10", ANSWER, false);

/**
 * Exercise 1.11
 *
 * Create a function 'inRange()' that takes three arguments, 'rangeStart',
 * 'rangeStop' and 'value'. The function should return boolean 'true' if
 * 'value' is greater than 'rangeStart' and less than 'rangeStop'. Otherwise
 * it should return boolean 'false'. Try it out using the range 162 - 541 and
 * the value 418.
 *
 * Answer with the result.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */

function inRange(rangeStart, rangeStop, value) {
    if ((value > rangeStart) && (value < rangeStop)) {
        return true;
    }
    else {
        return false;
    }
}

result = inRange(162, 541, 418);


ANSWER = result;

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("1.11", ANSWER, false);

/**
 * Exercise 1.12
 *
 * Try out the function 'inRange()' using the range 162 - 541 and the value
 * 673.
 *
 * Answer with the result.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */

result = inRange(162, 541, 673);




ANSWER = result;

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("1.12", ANSWER, false);

/**
 * Exercise 1.13
 *
 * Create a function called 'degreesToRadians()' that should take one
 * argument, a degree value. The function should convert the value to radians
 * and return the result with max 4 decimals.
 *
 * Test your function with the value 335 and answer with the result.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */

function degreesToRadians(degrees) {
    var radians = degrees * (Math.PI/180);
    radians = parseFloat(radians.toFixed(4));
    return radians;
}


result = degreesToRadians(335);

ANSWER = result;

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("1.13", ANSWER, false);

/**
 * Exercise 1.14
 *
 * Create a function called 'fizzBuzz()' that takes two arguments 'start' and
 * 'stop' and returns a comma-separated string. The arguments represents the
 * starting point and stop point of the game 'Fizz Buzz'
 * (http://en.wikipedia.org/wiki/Fizz_buzz). The function should run from
 * start to stop and add 'Fizz', 'Buzz' or both to your 'result'-variable at
 * appropriate numbers. Each entry to your result should be comma-separated.
 * If 'stop' is equal or lower than 'start', the function should return an
 * appropriate error message.
 *
 * Test the function using start=2 and stop=28.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */

function fizzBuzz(start, stop) {
    var fizzString = "";

    /*
    *  Divisible by 3 = Fizz
    *  Divisible by 5 = Buzz
    */

    if (stop <= start) {
        return "Error: Stop-value must be greater than start-value.";
    }

    for (var i = start; i < stop; i++) {
        if (((i % 5) === 0) && ((i % 3) === 0)) {
            fizzString += "Fizz Buzz,";
        }
        else if ((i % 5) === 0) {
            fizzString += "Buzz,";
        }
        else if ((i % 3) === 0) {
            fizzString += "Fizz,";
        }
        else {
            fizzString += i + ",";
        }
    }

    if ((stop % 5) === 0) {
        fizzString += "Buzz";
    }
    else if ((stop % 3) === 0) {
        fizzString += "Fizz";
    }
    else {
        fizzString += stop;
    }

    return fizzString;
}


result = fizzBuzz(2, 28);

ANSWER = result;

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("1.14", ANSWER, false);

/** ----------------------------------------------------------------------
 * Section 2 . Black jack functions
 *
 * In this section, you could re-use your code from lab 1
 *
 */



/**
 * Exercise 2.1
 *
 * Create a function called 'printSum()' that should take two variables, the
 * sum of the players hand and the sum of the dealers hand. Your hand should
 * be three cards with the values: 6, 4 and 4. The dealers hand should be
 * three card with the values: 10, 11, 10. The function should return the sum
 * and the player: 'Player: 14, Dealer: 31'.
 *
 * Test your function with the given values and answer with the result.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */

var playerSum = 6 + 4 + 4;
var dealerSum = 10 + 11 + 10;

function printSum(playerHand, dealerHand) {
    return "Player: " + playerHand + ", Dealer: " + dealerHand;
}

result = printSum(playerSum, dealerSum);


ANSWER = result;

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("2.1", ANSWER, false);

/**
 * Exercise 2.2
 *
 * Create a function called 'printResult()' that should take two variables,
 * the sum of the players hand and the sum of the dealers hand. Players hand
 * should be three cards with the values: 6, 4 and 4. The dealers hand should
 * be three card with the values: 10, 11, 10. This time you should include the
 * check from lab 1 where you find out the boundaries of the player and the
 * dealer. Player hand = 21 ('black jack'), Player hand less than 21 ('safe'),
 * Player hand larger than 21 ('busted'). Dealer hand less than 17 ('safe'),
 * Dealer hand larger or equal to 17 and less than 21 ('stop'), Dealer hand =
 * 21 ('black jack'), Delaer hand larger than 21 ('busted'). Return a string
 * in the format: 'Player: safe, Dealer: busted'.
 *
 * Test your function with the given values and answer with the result.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */


function printResult(playerHand, dealerHand) {
    var string = "";

    if (playerHand == 21) {
        string = "Player: black jack, Dealer: ";
    }
    else if (playerHand > 21) {
        string = "Player: busted, Dealer: ";
    }
    else if (playerHand < 21) {
        string = "Player: safe, Dealer: ";
    }

    if (dealerHand == 21) {
        string += "black jack";
    }
    else if (dealerHand < 17) {
        string += "safe";
    }
    else if (dealerHand > 21) {
        string += "busted";
    }

    return string;
}

result = printResult(playerSum, dealerSum);


ANSWER = result;

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("2.2", ANSWER, false);


    console.log(dbwebb.exitWithSummary());

}(window.dbwebb));
