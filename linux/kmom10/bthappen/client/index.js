#!/usr/bin/env babel-node

"use strict";

const VERSION = "1.0.0";

var path = require('path');
var scriptName = path.basename(process.argv[1]);
var args = process.argv.slice(2);
var arg;

var http = require("http");

var prompt = "Rooms$ ";
var address = "http://localhost";
var port = 1337;
var server;

var dev = false;


var readline = require("readline");

var rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});


function usage() {
    console.log(`Usage: ${scriptName} [options]

Options:
 -h                     Display help text.
 -v                     Display the version.
 --server <server>      Connect to server on <server>.
 --port <number>        Connect to server on <port>.
 --developer            Enables developer output.`);
}

function version() {
    console.log(VERSION);
}

function menu() {
    console.log(`Commands available:
 exit            Leave this program.
 menu            Print this menu.
 url             Get url to view the server in browser.
 list            List all rooms.
 view <id>       View the room with the selected id.
 house <house>   View the names of all rooms in this building (house).
 search <string> View the details of all matching rooms (one per row).`);
}

function httpGet(route) {
    return new Promise((resolve, reject) => {
        http.get(server + route, (res) => {
            var data = "";

            res.on('data', (chunk) => {
                data += chunk;
            }).on('end', () => {
                if (res.statusCode === 200) {
                    resolve(data);
                } else {
                    reject(data);
                }
            }).on('error', (e) => {
                reject("Error received: " + e.message);
            });
        });
    });
}

function listRooms() {
    return httpGet("/room/list");
}

function viewByRoom(roomId) {
    return httpGet("/room/view/id/" + roomId);
}

function viewByHouse(house) {
    return httpGet("/room/view/house/" + house);
}

function searchRoom(query) {
    return httpGet("/room/search/" + query + "?inList=true");
}


// Walkthrough all arguments checking for options.
while ((arg = args.shift()) !== undefined) {
    switch (arg) {
        case "-h":
            usage();
            process.exit(0);
            break;

        case "-v":
            version();
            process.exit(0);
            break;

        case "--server":
            address = args.shift();
            if (address === undefined) {
                console.log("--server must be followed by a url.");
                process.exit(1);
            }

            if (address.indexOf("http://") == -1) {
                address = "http://" + address;
            }
            break;

        case "--port":
            port = args.shift();
            if (port === undefined) {
                console.log("--port must be followed by a number.");
                process.exit(1);
            }
            break;

        case "--developer":
            dev = true;
            console.log("Dev mode enabled.");
            break;

        default:
            console.log("Unknown argument.");
            process.exit(1);
            break;
    }
}


rl.on("line", function(line) {
    // Split incoming line with arguments into an array
    var args = line.trim().split(" ");
    args = args.filter(value => {
        return value !== "";
    });

    switch (args[0]) {
        case "exit":
            console.log("Bye!");
            process.exit(0);
            break;

        case "menu":
            menu();
            rl.prompt();
            break;

        case "url":
            console.log("Use this address to view the rooms in a browser: " + address + ":" + port + "/");
            rl.prompt();
            break;

        case "list":
            listRooms()
            .then(value => {
                console.log(value);
                if (dev) {
                    console.log("Using server " + server + "/room/list");
                }
                rl.prompt();
            })
            .catch(err => {
                console.log("ERROR: Could not list rooms.\nError details: " + err);
                rl.prompt();
            });
            break;

        case "view":
            var id = args[1];

            viewByRoom(id)
            .then(value => {
                console.log(value);
                if (dev) {
                    console.log("Using server " + server + "/room/view/" + id);
                }
                rl.prompt();
            })
            .catch(err => {
                console.log("ERROR: Could not view room.\nError details: " + err);
                rl.prompt();
            });
            break;

        case "house":
            var house = args[1];

            viewByHouse(house)
            .then(value => {
                console.log(value);
                if (dev) {
                    console.log("Using server " + server + "/room/house/" + house);
                }
                rl.prompt();
            })
            .catch(err => {
                console.log("ERROR: Could not view rooms.\nError details: " + err);
                rl.prompt();
            });
            break;

        case "search":
            var query = args[1];

            searchRoom(query)
            .then(value => {
                console.log(value);
                if (dev) {
                    console.log("Using server " + server + "/room/search" + query);
                }
                rl.prompt();
            })
            .catch(err => {
                console.log("ERROR: Could not search for rooms.\nError details: " + err);
                rl.prompt();
            });
            break;

        default:
            console.log("Type \"menu\" to get an overview of available commands.");
            rl.prompt();
    }
});



rl.on("close", function() {
    rl.write("Bye!");
    process.exit(0);
});


function setServer(address, port) {
    server = address + ":" + port;
}

setServer(address, port);


rl.setPrompt(prompt);
rl.prompt();
