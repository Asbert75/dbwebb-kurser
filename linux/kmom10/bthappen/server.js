#!/usr/bin/env babel-node

"use strict";

import {server, enableDev} from "./server-core.js";

const VERSION = "1.0.0";

var path = require("path");
var scriptName = path.basename(process.argv[1]);
var args = process.argv.slice(2);
var arg;

var port = 1337;


function usage() {
    console.log(`Usage: ${scriptName} [options]

Options:
 -h               Displays the help text.
 -v               Display the script version.
 --port <number>  Run server using specified port number.
 --developer      Enables developer output.`);
}

function version() {
    console.log(VERSION);
}

function badUsage(message) {
    console.log(`${message}
Type -h to display command usage help.`);
}


while ((arg = args.shift()) !== undefined) {
    switch (arg) {
        case "-h":
        case "--help":
            usage();
            process.exit(0);
            break;

        case "-v":
        case "--version":
            version();
            process.exit(0);
            break;

        case "-p":
        case "--port":
            port = Number.parseInt(args.shift());
            if (Number.isNaN(port)) {
                badUsage("--port must be followed by a port number.");
                process.exit(1);
            }
            break;

        case "--developer":
            enableDev();
            break;

        default:
            badUsage("Unknown argument.");
            process.exit(1);
            break;
    }
}

server.listen(port);
console.log("The server is now listening on port: " + port);
