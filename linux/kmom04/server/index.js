"use strict";
import server from "./server.js";

const path = require("path");
const fs = require("fs");

var port = 1337;


if ("LINUX_PORT" in process.env) {
    console.log("LINUX_PORT is defined. Listening to port " + process.env.LINUX_PORT);
    port = process.env.LINUX_PORT;
}
else {
    console.log("LINUX_PORT is not defined. Listening to port 1337");
}

server.listen(port);

var pidFile = path.join(__dirname, "pid");
fs.writeFile(pidFile, process.pid, function(err) {
    if (err) {
        return console.log(err);
    }
    console.log("Wrote process id to file");
});
