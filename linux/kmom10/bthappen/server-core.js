/* jshint node: true */

"use strict";


import Router from "./router.js";
var router = new Router();

var http = require("http");
var url = require("url");
var fs = require("fs");

var dev = false;

function enableDev() {
    dev = true;
    console.log("Dev mode enabled.");
}

/*
Load salar.json into var rooms and parse JSON data.
*/
var maxNum = 0;
var rooms,
    matches;


fs.readFile("./salar.json", "utf8", function(err, data) {
    if (err) {
        console.log(err);
    }
    rooms = JSON.parse(data);
    rooms.pop(); // Remove last item in JSON-object (null-value object)
});


function matchAll(key, value) {
    var results = [];

    for (var i=0; i < rooms.length; i++)
    {
        if (rooms[i][key] == value) {
            results.push(rooms[i]);
        }
    }

    if (results.length === 0) {
        return [{"Response": "Zero matches found for " + key + ": '" + value + "'"}];
    }
    else {
        return results;
    }
}


function search(query) {
    var results = [];

    for (var i=0; i < rooms.length; i++)
    {
        for (var key in rooms[i]) {
            if (rooms[i][key] !== null) {
                if (rooms[i][key].toLowerCase().indexOf(query.toLowerCase()) != -1) {
                    results.push(rooms[i]);
                }
            }
        }
    }

    if (results.length === 0) {
        return [{"Response": "Zero matches found for string: '" + query + "'"}];
    }
    else {
        return results;
    }
}


function getKeyMatch(key) {
    var score = 0;

    var keys = {"Salsnr": 0.22, "Salsnamn": 0.13, "Hus": 0.08,
                "Ort": 0.06, "Lat": 0.04, "Long": 0.04, "Storlek": 0.02, "Typ": 0.01};

    for (var k in keys) {
        if (key === k) {
            score = keys[k];
        }
    }

    return score;
}

function prioritySearch(query) {
    /*
    Priority order:
    1. Salsnr 2. Salsnamn 3. Hus 4. Ort 5. Lat & Long 6. Storlek 7. Typ
    Total Prio: 0.6

    Om söksträngen matchar ett helt fält, inte bara en delsträng av fältet, så har det hög prioritet.
    Total Prio: 0.2

    Det är alltså bättre om söksträngen abc matchar abcdef än defabc.
    Total prio: 0.2
    */

    var results = [];

    // Initial search to find matches
    for (var i=0; i < rooms.length; i++)
    {
        var priority = 0;

        for (var key in rooms[i]) {
            if (rooms[i][key] !== null) {
                if (rooms[i][key].toLowerCase().indexOf(query.toLowerCase()) != -1) {
                    priority += getKeyMatch(key);

                    // Find full string matches
                    if (rooms[i][key].toLowerCase() === query.toLowerCase()) {
                        priority += 0.2;
                    } // Else, look for the match location, abc -> abcdef vs defabc
                    else if (rooms[i][key].startsWith(query)) {
                        priority += 0.125;
                    }
                    else {
                        priority += 0.075;
                    }

                    priority = parseFloat(priority).toFixed(3);

                    rooms[i].priority = String(priority);
                    results.push(rooms[i]);
                }
            }
        }
    }


    if (results.length === 0) {
        return [{"Response": "Zero matches found for string: '" + query + "'"}];
    }
    else {
        return results.sort((x, y) =>
        {
            if (x.priority > y.priority) {
                return -1;
            }

            if (x.priority < y.priority) {
                return 1;
            }
            return 0;
        });
    }
}


// Filters the amount of results returned.
function filterResults(object, maxResults) {
    var filtered = [];

    if ((maxResults === 0) || (maxResults > object.length)) {
        return object;
    }
    else {
        for (var i = 0; i < maxResults; i++) {
            filtered.push(object[i]);
        }

        return filtered;
    }
}


function createRows(object) {
    var listed = "";

    for (var i = 0; i < object.length; i++) {
        listed += "Salsnr: " + object[i].Salsnr + ", Salsnamn: " + object[i].Salsnamn + ", Lat: " + object[i].Lat + ", Long: " +
                    object[i].Long + ", Ort: " + object[i].Ort + ", Hus: " + object[i].Hus + ", Våning: " + object[i].Våning +
                    ", Typ: " + object[i].Typ + ", Storlek: " + object[i].Storlek + "\n\n";
    }

    return listed;
}


function sendResponse(res, type, content, code = 200) {
    if (type === "json") {
        res.writeHead(code, "Content-Type: application/json", "utf-8");
        res.write(JSON.stringify(content, null, "    "));

        if (dev) {
            console.log(JSON.stringify(content, null, "   "));
        }

        res.end();
    }
    else if (type === "text") {
        res.writeHead(code, "Content-Type: text/plain", "utf-8");
        res.write(content);

        if (dev) {
            console.log(content);
        }

        res.end();
    }
}

router.get("/", (req, res) => {
    sendResponse(res, "text", "You are currently viewing the BTHAppen API. Below is a list of valid routes.\n\n" +
        " /                         Display the API (current).\n" +
        " /room/list                Display a list of all rooms.\n" +
        " /room/view/id/:number     Display details on selected room by room id.\n" +
        " /room/view/house/:house   Display a list of all rooms by house.\n" +
        " /room/search/:search      Display a list of all rooms matching :search.\n"
    );
});


router.get("/room/list", (req, res) => {
    maxNum = parseInt(req.query.max) || maxNum;

    sendResponse(res, "json", filterResults(rooms, maxNum));
});


router.get("/room/view/id/:number", (req, res) => {
    var roomId = decodeURI(req.params.number);

    // Search for matching roomIDs
    matches = matchAll("Salsnr", roomId);

    sendResponse(res, "json", matches);
});


router.get("/room/view/house/:house", (req, res) => {
    // Parse maxNum and specified house.
    maxNum = parseInt(req.query.max) || maxNum;

    var house = decodeURI(req.params.house);

    // Search for matching houses
    matches = matchAll("Hus", house);

    sendResponse(res, "json", filterResults(matches, maxNum));
});


router.get("/room/search/:search", (req, res) => {
    // Parse inList & maxNum from query. Also parse search parameters and decode it.
    var inList = req.query.inList || false;
    maxNum = parseInt(req.query.max) || maxNum;

    var query = decodeURI(req.params.search);

    matches = search(query);

    // if InList = true -> Send one response per row (for Client Search)
    if (inList) {
        matches = createRows(matches);
        sendResponse(res, "text", matches);
    }
    else {
        sendResponse(res, "json", filterResults(matches, maxNum));
    }
});


router.get("/room/searchp/:searchp", (req, res) => {
    var query = decodeURI(req.params.searchp);

    matches = prioritySearch(query);

    sendResponse(res, "json", filterResults(matches, 0));
});



var server = http.createServer((req, res) => {
    var ipAddress,
        route;

    ipAddress = req.connection.remoteAddress;

    route = url.parse(req.url).pathname;
    console.log("Incoming route " + route + " from ip " + ipAddress);

    fs.appendFile("connections.txt", "From IP: " + ipAddress + " Incoming Route: " + route + "\n", function(err) {
        if (err) {
            console.log(err);
        }
    });

    router.route(req, res);
});


export {server, enableDev};
