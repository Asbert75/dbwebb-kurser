#!/usr/bin/env node

/**
 * @preserve type
 *
 * type
 * linux
 * node2
 * eroa16
 * 2017-02-16 11:17:38
 * v2.2.30 (2017-02-14)
 *
 * Generated 2017-02-16 12:17:38 by dbwebb lab-utility v2.2.30 (2017-02-14).
 * https://github.com/mosbth/lab
 */"use strict";


//import dbwebb from "./.dbwebb.js";
const dbwebb = require("./.dbwebb.js");

var ANSWER = null;
console.log(dbwebb.prompt + "Ready to begin.");



/** ======================================================================
 * Lab 4 - JavaScript with Nodejs
 *
 * JavaScript using nodejs. During these exercises we train on the built-in
 * nodejs modules filesystem, querystring and crypto.
 * Documentation can be found at [nodejs api](https://nodejs.org/api/).
 *
 */



/** ----------------------------------------------------------------------
 * Section 1 . Filesystem
 *
 * This section is about the built-in module filesystem and how to read and
 * write files synchronously.
 *
 */



/**
 * Exercise 1.1
 *
 * Start by importing the filesystem module `fs`.
 *
 * Use the `fs` module and the function `readFileSync` to read the entire
 * `ircLog.txt` in UTF-8 encoding into a variable. Answer with the number of
 * characters in the file.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */

import fs from 'fs';

let fileData = fs.readFileSync("ircLog.txt", "utf-8");



ANSWER = fileData.length;

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("1.1", ANSWER, false);

/**
 * Exercise 1.2
 *
 * Use your variable from the exercise above and answer with the contents on
 * line 4.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */

let data = fileData.split("\n");


ANSWER = data[3];

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("1.2", ANSWER, false);

/**
 * Exercise 1.3
 *
 * Write line number 4 of `ircLog.txt` to a new file that you create called
 * `highlights.txt`. Replace `highlights.txt` if it already exists.
 * Answer with characters 7 through 10 from `highlights.txt`.
 *
 * Tip: Use the function `writeFileSync()` when writing to files.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */

fs.writeFileSync("highlights.txt", data[3], { flag: "w"}, function(err) {
    if (err) {
        console.log(err);
    }
});

let highlightsData = fs.readFileSync("highlights.txt", "utf-8");




ANSWER = highlightsData.slice(6, 9);

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("1.3", ANSWER, false);

/** ----------------------------------------------------------------------
 * Section 2 . querystring
 *
 * This section is about the built-in module querystring and how to parse and
 * encode query strings.
 *
 */



/**
 * Exercise 2.1
 *
 * Start by importing the querystring module `querystring`.
 *
 * Use the `querystring` module to parse a query string
 * 'first_name=Pete&last_name=Conrad&mission=Apollo12'. Answer with the value
 * of mission.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */

import querystring from 'querystring';

let theString = "first_name=Pete&last_name=Conrad&mission=Apollo12";
let qs = querystring.parse(theString);




ANSWER = qs.mission;

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("2.1", ANSWER, false);

/**
 * Exercise 2.2
 *
 * Use the parsed query string from above to concatenate the astronaut's full
 * name with the string ' was on the ' and the mission that the astronaut was
 * on.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */





ANSWER = qs.first_name + " " + qs.last_name + " was on the " + qs.mission;

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("2.2", ANSWER, false);

/**
 * Exercise 2.3
 *
 * Create a javascript object with the following attributes and values:
 *
 * ```json
 * url = https://dbwebb.se/
 * id = 414
 * payload = aHR0cHM6Ly9kYndlYmIuc2Uv
 * type = json
 *
 * ```
 *
 * Encode the javascript object as a querystring and answer with the encoded
 * query string.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */

let jsObject = {url: "https://dbwebb.se/",
                id: 414,
                payload: "aHR0cHM6Ly9kYndlYmIuc2Uv",
                type: "json"};

let result = querystring.stringify(jsObject);


ANSWER = result;

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("2.3", ANSWER, false);

/** ----------------------------------------------------------------------
 * Section 3 . crypto
 *
 * This section is about the built-in module crypto and how to encrypt data
 * with nodejs.
 *
 */



/**
 * Exercise 3.1
 *
 * Start by importing the `crypto` module.
 *
 * Use the `crypto` module to create a hash of 'Couldnt be much more from the
 * heart' using the `sha256` algorithm.
 *
 * Answer with a digest of the hash in `hex` format.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */

import crypto from 'crypto';

var keyString = "Couldnt be much more from the heart";

var encrypted = crypto.createHash("sha256").update(keyString).digest("hex");




ANSWER = encrypted;

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("3.1", ANSWER, false);

/**
 * Exercise 3.2
 *
 * Create an array called `cryptoStrings` holding the strings 'Couldnt be much
 * more from the heart', 'Forever trusting who we are', 'And nothing else
 * matters', 'Never opened myself this way'.
 *
 * Use filter to create an array only containing elements that has the string
 * 'nothing else matters' in them.
 *
 * Answer with the array.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */

function containsString(arrayItem) {
    return arrayItem.indexOf("nothing else matters") >= 0;
}

var cryptoStrings = ["Couldnt be much more from the heart", "Forever trusting who we are", "And nothing else matters", "Never opened myself this way"];

var filteredStrings = cryptoStrings.filter((arrayItem) => containsString(arrayItem));

ANSWER = filteredStrings;

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("3.2", ANSWER, false);

/**
 * Exercise 3.3
 *
 * Use the array from above only containing elements with 'nothing else
 * matters'.
 *
 * For the elements in the array create a hex digest of a hash created with
 * with the `sha256` algorithm of each element.
 *
 * Answer with the array of hashes.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */

let encryptedArray = [];

for (var i = 0; i < filteredStrings.length; i++) {
    encryptedArray.push(crypto.createHash("sha256").update(filteredStrings[i]).digest("hex"));
}




ANSWER = encryptedArray;

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("3.3", ANSWER, false);

/**
 * Exercise 3.4
 *
 * Use `filter` to keep all elements in `cryptoStrings` that contains both an
 * 'i', an 'e', and a 'm', check both capital and non-capital letters.
 *
 * For the remaining elements create a hex digest of a hash created with with
 * the `sha256` algorithm of each remaining element.
 *
 * Answer with the array of hashes.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */

function containsCharacters(element) {
    var charCount = 0;
    if ((element.indexOf("i") >= 0) || (element.indexOf("I") >= 0)) {
        charCount++;
    }
    if ((element.indexOf("e") >= 0) || (element.indexOf("E") >= 0)) {
        charCount++;
    }
    if ((element.indexOf("m") >= 0) || (element.indexOf("M") >= 0)) {
        charCount++;
    }

    if (charCount == 3) {
        return element;
    }
}

cryptoStrings = cryptoStrings.filter((element) => containsCharacters(element));
let stringsEncrypted = [];

for (var c = 0; c < cryptoStrings.length; c++) {
    stringsEncrypted.push(crypto.createHash("sha256").update(cryptoStrings[c]).digest("hex"));
}



ANSWER = stringsEncrypted;

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("3.4", ANSWER, false);

/**
 * Exercise 3.5
 *
 * Using the same `cryptoStrings` array from above, create a hash of the
 * elements containing 'matters', check both capital and non-capital letters.
 *
 * For the remaining elements create a HMAC using the `sha256` algorithm and
 * the secret 'metallica' for each element. Create a `base64` digest of the
 * HMAC for each element.
 *
 * Answer with the array of HMACs.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */

function ifItMatters(element) {
    if (element.toUpperCase().indexOf("MATTERS") >= 0) {
        return element;
    }
}

let mattersArray = cryptoStrings.filter((element) => ifItMatters(element));

let HMACArray = [];

for (var k = 0; k < mattersArray.length; k++) {
    HMACArray.push(crypto.createHmac("sha256", "metallica").update(mattersArray[k]).digest("base64"));
}


ANSWER = HMACArray;

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("3.5", ANSWER, true);


process.exit(dbwebb.exitWithSummary());
