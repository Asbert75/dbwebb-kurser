#!/usr/bin/env babel-node

"use strict";

import GomokuBoard from "./GomokuBoard.js";

const VERSION = "1.0.0";

var path = require('path');
var scriptName = path.basename(process.argv[1]);
var args = process.argv.slice(2);


var size = 20,
    prompt = "Gomoku$ ",
    gameBoard;

gameBoard = new GomokuBoard();



var readline = require("readline");

var rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});


function usage() {
    console.log(`Usage: ${scriptName} [options] <min> <max>

Options:
 -h        Display help text.
 -v        Display the version.`);
}

function version() {
    console.log(VERSION);
}


// Checks for arguments in shell
args.forEach((arg) => {
    switch (arg) {
        case '-h':
            usage();
            process.exit(0);
            break;

        case '-v':
            version();
            process.exit(0);
            break;

        case '15':
            size = 15;
    }
});


/**
 * Place a marker on the board.
 */
function placeMarker(posX, posY) {
    var player = gameBoard.playerInTurn();

    if (!gameBoard.isPositionTaken(posX, posY)) {
        gameBoard.place(posX, posY);
        console.log(">>> " + player + " places " + posX + " " + posY + "\n");
        console.log(gameBoard.asAscii());
    }
    else {
        console.log("Position X: " + posX + " Y: " + posY + " is taken.");
    }
}



rl.on("line", function(line) {
    switch (line.trim()) {
        case "exit":
            console.log("Bye!");
            process.exit(0);
            break;
        default:
            let nums = line.split(" ");

            let x = parseInt(nums[0]);
            let y = parseInt(nums[1]);

            placeMarker(x, y);
    }
    rl.prompt();
});



rl.on("close", function() {
    rl.write("Bye!");
    process.exit(0);
});



console.log(">>> Start the game with board size of " + size);
gameBoard.start(size);

rl.setPrompt(prompt);
rl.prompt();
