"use strict";

import routes from "./routes.js";

var http = require("http");
var url = require("url");

var server = http.createServer((req, res) => {
    var urlParts = url.parse(req.url, true);
    var route = urlParts.pathname;
    var query = urlParts.query;


    var ipAddress;

    ipAddress = req.connection.remoteAddress;
    console.log("Incoming request from ip " + ipAddress);

    switch (route) {
        case "/":
            routes.home(res);
        break;

        case "/index.html":
            routes.indexhtml(res);
        break;

        case "/status":
            routes.status(res);
        break;

        case "/sum":
            routes.sum(res, query);
        break;

        case "/filter":
            routes.filter(res, query);
        break;

        default:
            routes.default(res);
        break;
    }

});

export default server;
