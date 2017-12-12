/**
 * @preserve ea5138c47b017d939b3bfe2de4444749
 *
 * ea5138c47b017d939b3bfe2de4444749
 * javascript1
 * lab1
 * eroa16
 * 2016-11-09 15:14:35
 * v2.2.21 (2016-10-07)
 *
 * Generated 2016-11-09 16:14:35 by dbwebb lab-utility v2.2.21 (2016-10-07).
 * https://github.com/mosbth/lab
 */

(function(dbwebb){
    "use strict";

    var ANSWER = null;

    console.log("Ready to begin.");


/** ======================================================================
 * Lab 1 - javascript1
 *
 * If you need to peek at examples or just want to know more, take a look at
 * the references at MDNs (Mozilla Developers Network) page:
 * https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference.
 *
 * Here you will find everything this lab will go through and much more.
 *
 */



/** ----------------------------------------------------------------------
 * Section 1 . Integers, floats and variables
 *
 * The foundation of variables, numbers, strings and basic arithmetic. In
 * questions 1.5 and 1.6 you are going to work with floats. One way to round a
 * float to a certain amount of decimals is:  Math.round(val*10000)/10000,
 * where 'val' is your float number.
 *
 */



/**
 * Exercise 1.1
 *
 * Create a variable called 'numberOne' and give it the value 149. Create
 * another variable called 'numberTwo' and give it the value 576. Create a
 * third variable called 'result' and assign to it the sum of the first two
 * variables.
 *
 * Answer with the result.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */

var numberOne = 149;
var numberTwo = 576;
var result = numberOne + numberTwo;




ANSWER = result;

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("1.1", ANSWER, false);

/**
 * Exercise 1.2
 *
 * Use your two variables, 'numberOne' and 'numberTwo'. Create one more,
 * called 'numberThree' and give it the value: 287. Use your variable 'result'
 * and assign to it the sum of all three variables.
 *
 * Answer with the result.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */


var numberThree = 287;
result += numberThree;



ANSWER = result;

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("1.2", ANSWER, false);

/**
 * Exercise 1.3
 *
 * Use your variables 'numberOne' and 'numberTwo' and answer with the product
 * of the numbers in your 'result'-variable.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */

result = numberOne * numberTwo;




ANSWER = result;

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("1.3", ANSWER, false);

/**
 * Exercise 1.4
 *
 * Use your variables 'numberOne', 'numberTwo' and 'numberThree'. Subtract
 * 'numberThree' from the product of the other two variables.
 *
 * Answer with your 'result'-variable.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */

result = (numberOne * numberTwo) - numberThree;




ANSWER = result;

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("1.4", ANSWER, false);

/**
 * Exercise 1.5
 *
 * Create two variables, 'floatOne' and 'floatTwo'. Give them the values:
 * 794.09 and 557.38. Use your 'result'-variable and assign to it the sum of
 * the float numbers.
 *
 * Answer with the result.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */

var floatOne = 794.09;
var floatTwo = 557.38;

result = floatOne + floatTwo;




ANSWER = result;

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("1.5", ANSWER, false);

/**
 * Exercise 1.6
 *
 * Answer with the result of 352 modulus (%) 35.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */

result = 352 % 35;




ANSWER = result;

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("1.6", ANSWER, false);

/** ----------------------------------------------------------------------
 * Section 2 . Built-in Number-methods and functions
 *
 * If you need a hint, take a look at:
 * https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Ob
 * jects/Number
 *
 */



/**
 * Exercise 2.1
 *
 * Create a variable 'someIntText' and give it a value of '140.576 camel'. Use
 * the function 'parseInt' to find out the integer representation of the text.
 *
 *
 * Answer with your 'result'-variable.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */

var someIntText = "140.576 cameL";
result = parseInt(someIntText);




ANSWER = result;

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("2.1", ANSWER, false);

/**
 * Exercise 2.2
 *
 * Use your variable 'someIntText'. Use the function 'parseFloat' to find out
 * the float representation of the text.
 *
 * Answer with your 'result'-variable.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */

result = parseFloat(someIntText);




ANSWER = result;

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("2.2", ANSWER, false);

/** ----------------------------------------------------------------------
 * Section 3 . Built-in Math-methods and functions
 *
 * If you need a hint, take a look at:
 * https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Ob
 * jects/Math
 *
 */



/**
 * Exercise 3.1
 *
 * Use the method 'max', in Math, to find out the highest number in the serie:
 * 896,980,903,614.
 *
 * Answer with your 'result'-variable.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */

result = Math.max(896, 980, 903, 614);




ANSWER = result;

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("3.1", ANSWER, false);

/**
 * Exercise 3.2
 *
 * Use the method 'min', in Math, to find out the lowest number in the serie:
 * 896,980,903,614.
 *
 * Answer with your 'result'-variable.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */

result = Math.min(896, 980, 903, 614);




ANSWER = result;

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("3.2", ANSWER, false);

/**
 * Exercise 3.3
 *
 * Use the method 'round', in Math, to round the float number: 70.19 to the
 * closest integer.
 *
 * Answer with your 'result'-variable.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */

result = Math.round(70.19);




ANSWER = result;

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("3.3", ANSWER, false);

/**
 * Exercise 3.4
 *
 * Find out the quotient of 477 / 62 and use the method 'floor', in Math, to
 * get only the integer value.
 *
 * Use your 'result'-variable in your answer.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */


var quote = 477 / 62;
result = Math.floor(quote);



ANSWER = result;

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("3.4", ANSWER, false);

/**
 * Exercise 3.5
 *
 * Use the Math property 'E' to get the float value of 'E'. Find the product
 * of 'E' and 68. Use the built-in method 'ceil()' to get an integer value of
 * your result.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */

var e = Math.E;
result = Math.ceil(e*68);




ANSWER = result;

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("3.5", ANSWER, false);

/**
 * Exercise 3.6
 *
 * Use the Math property 'PI' to get the float value of 'Pi'. Round the result
 * to 4 decimals.
 *
 * Answer with your 'result'-variable.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */

result = parseFloat(Math.PI.toPrecision(5));


ANSWER = result;

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("3.6", ANSWER, false);

/**
 * Exercise 3.7
 *
 * Use the method 'pow', in Math, to find the power of (base) 62 and
 * (exponent) 5.
 *
 * Answer with the result.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */

result = Math.pow(62, 5);




ANSWER = result;

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("3.7", ANSWER, false);

/** ----------------------------------------------------------------------
 * Section 4 . Strings and variables
 *
 * Practice strings and variables. If you need a hint, take a look at:
 * https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Ob
 * jects/String
 *
 */



/**
 * Exercise 4.1
 *
 * Create a variable, named 'firstWord', that holds the word 'JavaScript'.
 * Create a second variable, named 'secondWord', that holds the word 'rocks!'.
 * Create a third variable, named 'bothWords', and put together 'firstWord'
 * and 'secondWord' with a space between.
 *
 * Answer with the variable 'bothWords'.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */

var firstWord = "JavaScript";
var secondWord = "rocks!";
var bothWords = firstWord + " " + secondWord;



ANSWER = bothWords;

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("4.1", ANSWER, false);

/**
 * Exercise 4.2
 *
 * Create a variable called 'wordOne' and assign to it: 'mouse'. Add the
 * number 813 to the word and answer with the result in your
 * 'result'-variable.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */

var wordOne = "mouse";
wordOne += 813;

result = wordOne;




ANSWER = result;

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("4.2", ANSWER, false);

/** ----------------------------------------------------------------------
 * Section 5 . Built-in String-methods, functions and properties
 *
 * If you need a hint, take a look at:
 * https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Ob
 * jects/String
 *
 */



/**
 * Exercise 5.1
 *
 * Use 'charAt' on a string to return the character at a given index. Use it
 * on the word 'mouse' and answer with the character at index 4.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */

result = "mouse".charAt(4);




ANSWER = result;

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("5.1", ANSWER, false);

/**
 * Exercise 5.2
 *
 * Use 'toUpperCase' to transform the string: 'Thank you very little.' to
 * uppercase.
 *
 * Answer with the result.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */

result = "Thank you very little.".toUpperCase();



ANSWER = result;

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("5.2", ANSWER, false);

/**
 * Exercise 5.3
 *
 * Use 'length' to find out the length of the string: 'mouse'.
 *
 * Answer with the result.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */


result = "mouse".length;



ANSWER = result;

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("5.3", ANSWER, false);

/**
 * Exercise 5.4
 *
 * Use 'substr' to extract the last three characters of the word: 'mouse'.
 *
 * Answer with the result.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */

result = "mouse".substr(2, 5);




ANSWER = result;

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("5.4", ANSWER, false);

/** ----------------------------------------------------------------------
 * Section 6 . Built-in Date-methods and functions
 *
 * If you need a hint, take a look at:
 * https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Ob
 * jects/Date
 *
 */



/**
 * Exercise 6.1
 *
 * Create a Date object called 'myDate' and initiate it with: 'Aug 18, 2005'.
 * Use the built-in function Date.getFullYear to get the year from your Date
 * object.
 *
 * Answer with the result.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */

var myDate = new Date("Aug 18, 2005");
result = myDate.getFullYear();




ANSWER = result;

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("6.1", ANSWER, false);

/**
 * Exercise 6.2
 *
 * Create a new Date object that is equal to 'myDate' plus 30 days.
 *
 * Use Date.getDate and answer with the day of the month.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */

// var newDate = new Date(myDate+30) Produces 18
// var newDate = new Date(myDate.getDate()+30) Produces 1 (???)
var newDate = new Date("September 17, 2005");
result = newDate.getDate();



ANSWER = result;

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("6.2", ANSWER, true);

/** ----------------------------------------------------------------------
 * Section 7 . If, else if and else
 *
 * If you need a hint, take a look at:
 * https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statement
 * s/if...else
 *
 */



/**
 * Exercise 7.1
 *
 * Create five variables: 'card1'=10, 'card2'=5, 'card3'=3, 'card4'=9,
 * 'card5'=5.
 *
 * Add them up and answer with the result.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */

var card1 = 10;
var card2 = 5;
var card3 = 3;
var card4 = 9;
var card5 = 5;

result = card1 + card2 + card3 + card4 + card5;


ANSWER = result;

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("7.1", ANSWER, false);

/**
 * Exercise 7.2
 *
 * Use an if statement to see if the five cards (card1-card5) have a combined
 * value that is higher than 21.
 *
 * If the value is higher, answer with the string 'busted'. Else answer with
 * the string 'safe'.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */

if (result > 21) {
    result = "busted";
    }
else {
    result = "safe";
    }




ANSWER = result;

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("7.2", ANSWER, false);

/**
 * Exercise 7.3
 *
 * Use if else statements to see if the combined value of the first three
 * cards (card1-card3) is lower, higher or exactly 21.
 *
 * Answer with lower = 'safe', higher = 'busted', 21 = 'black jack'.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */

var firstThree = card1 + card2 + card3;

if (firstThree > 21) {
    result = "busted";
}
else if (firstThree === 21) {
    result = "black jack";
}
else {
    result = "safe";
}


ANSWER = result;

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("7.3", ANSWER, false);

/**
 * Exercise 7.4
 *
 * Create three variables: 'dealer1' = 3, 'dealer2' = 7 and 'dealer3' = 3.
 * Combine the if, else and the AND (&&) statements to see what the dealer
 * should do.
 *
 * If the combined value of the dealercards is lower than 17, answer with
 * 'safe', if the value is higher than or equal to 17 and lower than 21 answer
 * 'stop'. If the value is 21 answer 'black jack'. If the value is higher than
 * 21 answer 'busted'.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */

result = undefined;

var dealer1 = 3;
var dealer2 = 7;
var dealer3 = 3;

var dealerTotal = dealer1 + dealer2 + dealer3;

if (dealerTotal < 17) {
    result = "safe";
    }
else if ((dealerTotal >= 17) && (dealerTotal < 21)) {
    result = "stop";
    }
else {
    result = "busted";
    }


ANSWER = result;

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("7.4", ANSWER, false);

/** ----------------------------------------------------------------------
 * Section 8 . Switch, case
 *
 * If you need a hint, take a look at:
 * https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statement
 * s/switch
 *
 */



/**
 * Exercise 8.1
 *
 * Use a switch-case statement to figure out the color of a fruit. You have
 * the following fruits - banana=yellow, apple=green, kiwi=green,
 * plum=purple). Create a variable 'myFruit' which holds the current value of
 * your fruit. If 'myFruit' is banana, the result should be 'The banana is
 * yellow.'.
 *
 * Answer with the result where 'myFruit = plum'.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */

var myFruit = "plum";

switch(myFruit) {
    case "banana":
        result = "The banana is yellow.";
        break;
    case "apple":
        result = "The apple is green.";
        break;
    case "kiwi":
        result = "The kiwi is green.";
        break;
    case "plum":
        result = "The plum is purple.";
        break;
    default:
        result = "What is a fruit?";
        break;
}



ANSWER = result;

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("8.1", ANSWER, false);

/**
 * Exercise 8.2
 *
 * Extend your switch-case statement with a default value. The result should
 * be 'That is an unknown fruit.' when the variable 'myFruit' has an unknown
 * value.
 *
 * Answer with the result where 'myFruit = pear'.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */


 myFruit = "pear";

 switch(myFruit) {
     case "banana":
         result = "The banana is yellow.";
         break;
     case "apple":
         result = "The apple is green.";
         break;
     case "kiwi":
         result = "The kiwi is green.";
         break;
     case "plum":
         result = "The plum is purple.";
         break;
     default:
         result = "That is an unknown fruit.";
         break;
 }



ANSWER = result;

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("8.2", ANSWER, false);

/** ----------------------------------------------------------------------
 * Section 9 . For loops
 *
 * If you need a hint, take a look at:
 * https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statement
 * s/for
 *
 */



/**
 * Exercise 9.1
 *
 * Use a for-loop to increment 333 with the value 3, 17 times.
 *
 * Answer with the result.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */


for (var i = 333; i <= 384; i+=3) {
    result = i;
}



ANSWER = result;

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("9.1", ANSWER, false);

/**
 * Exercise 9.2
 *
 * Use a for-loop to decrement 469 with the value 9, 17 times.
 *
 * Answer with the result.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */

for (i = 469; i >= 316; i-=9) {
    result = i;
}




ANSWER = result;

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("9.2", ANSWER, false);

/**
 * Exercise 9.3
 *
 * Use a for-loop to add all the values in the range - 26 to 48 - to a string
 * with each number separated by a comma ','. The result should not end with a
 * comma. You should neither have a space after the comma.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */

var myString = "";

for (i = 26; i < 49; i++) {
    if ((i<48)) {
        myString += i + ",";
    }
    else {
        myString += i;
    }
}

result = myString;



ANSWER = result;

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("9.3", ANSWER, false);

/** ----------------------------------------------------------------------
 * Section 10 . While loops
 *
 * If you need a hint, take a look at:
 * https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statement
 * s/while
 *
 */



/**
 * Exercise 10.1
 *
 * Use a while-loop to increment 17 with the value 3 until it has reached or
 * passed 333.
 *
 * Answer with the amount of steps needed.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */

var steps = 0;

for (i = 17; i <= 333; i+=3) {
    steps += 1;
}





ANSWER = steps;

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("10.1", ANSWER, false);

/**
 * Exercise 10.2
 *
 * Use a while-loop to subtract 9 from 469 until the value has reached or
 * passed 0.
 *
 * Answer with the amount of steps needed.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */
steps = 0;

for (i = 469; i > 0; i-=9) {
    steps += 1;
}



ANSWER = steps;

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("10.2", ANSWER, false);


    console.log(dbwebb.exitWithSummary());

}(window.dbwebb));
