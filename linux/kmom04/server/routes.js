"use strict";


var routes = {};

var fs = require("fs");
var indexData;

routes.home = (res) => {
    res.writeHead(200, { "Content-Type": "text/plain"});
    res.end("Hello World!\n");
};


fs.readFile("./index.html", (err, data) => {
    if (err) {
        console.log(err);
    }
    indexData = data;
});

routes.indexhtml = (res) => {
    res.writeHead(200, { "Content-Type": "text/html"});
    res.end(indexData);
};

routes.status = (res) => {
    var child = require("child_process");

    child.exec("uname -a | tr -d '\\n'", (error, stdout, stderr) => {
        if (error || stderr) {
            console.log("Something went wrong...", error, stderr);
        }

        res.writeHead(200, { "Content-Type": "application/json" });
        res.end(JSON.stringify({"uname": stdout}));
    });
};

routes.sum = (res, qs) => {
    var total = 0;
    var value;

    Object.keys(qs).forEach( key => {
        value = parseInt(key);
        if (typeof value === "number") {
            if (qs[key].length > 0) {
                value *= qs[key].length;
            }
            total += value;
        }
    });

    res.writeHead(200, {"Content-Type": "text/plain"});
    res.end(JSON.stringify({"sum": + total}));
};

routes.filter = (res, qs) => {
    var filteredArray = [];
    var num;

    Object.keys(qs).forEach( key => {
        num = parseInt(key);
        if (typeof num === "number") {
            if (qs[key].length > 0) {
                for (var i = 0; i < qs[key].length; i++) {
                    filteredArray.push(num);
                }
            }
            else {
                filteredArray.push(num);
            }
        }
    });

    function filterTooBig(n) {
        return n <= 42;
    }

    filteredArray = filteredArray.filter(filteredArray => filterTooBig(filteredArray));

    res.writeHead(200, {"Content-Type": "application/json"});
    res.end(JSON.stringify({"filter": filteredArray}));

};

routes.default = (res) => {
    res.writeHead(404, {"Content-Type": "text/plain"});
    res.end("That resource does not exist.");
};


export default routes;
