window.Test3 = (function() {
    "use strict";

    var test3 = {
        "interv": "",
        "hideInterv": "",
        "num": 0,
        "score": 0,
        "correct": {
            "shape": "square",
            "color": "red",
        },
        "clicked": false,
        "object": document.getElementById("object"),
        "objects": {
            0: {
                "shape": "circle",
                "color": "red",
            },
            1: {
                "shape": "square",
                "color": "red",
            },
            2: {
                "shape": "square",
                "color": "blue",
            },
            3: {
                "shape": "circle",
                "color": "blue",
            },
            4: {
                "shape": "circle",
                "color": "green",
            },
            5: {
                "shape": "square",
                "color": "red",
            },
            6: {
                "shape": "square",
                "color": "blue",
            },
            7: {
                "shape": "circle",
                "color": "red",
            },
            8: {
                "shape": "square",
                "color": "yellow",
            },
            9: {
                "shape": "square",
                "color": "red",
            },
        },

        "displayInfo": function() {
            var that = this;
            document.getElementById("fizzBuzz").classList.add("hidden");
            document.getElementById("perception").classList.remove("hidden");

            document.getElementById("perceptionStartButton").addEventListener("click", function() {
                that.startTest();
            });
        },

        "changeObject": function() {
            this.object.classList.remove(this.objects[this.num-1].color);
            this.object.classList.remove(this.objects[this.num-1].shape);

            this.object.classList.add(this.objects[this.num].color);
            this.object.classList.add(this.objects[this.num].shape);
        },

        "startTest": function() {
            var that = this;

            document.getElementById("perceptionInfo").classList.add("hidden");
            document.getElementById("perceptionTest").classList.remove("hidden");

            this.object.classList.add(this.objects[0].color);
            this.object.classList.add(this.objects[0].shape);

            this.object.addEventListener("click", function() {
                if((!that.object.classList.contains("hidden")) && (that.clicked === false)) {
                    var shape = that.objects[that.num].shape;
                    var color = that.objects[that.num].color;
                    that.checkObject(shape, color);

                    that.clicked = true;
                }
            });

            this.hideInterv = window.setInterval(function() {
                that.object.classList.toggle("hidden");
            }, 1000);

            this.interv = window.setInterval(function() {
                that.num += 1;
                that.changeObject();
                that.clicked = false;

                document.getElementById("objectCount").innerHTML = that.num + 1;

                if(that.num == 9) {
                    window.clearInterval(that.interv);
                    window.setTimeout(function() {
                        that.object.classList.add("hidden");
                        window.clearInterval(that.hideInterv);
                        that.testFinished();

                        document.getElementById("perceptionTestScore").innerHTML = that.score;
                        document.getElementById("objectCount").classList.add("hidden");
                    }, 1000);
                }
            }, 2000);

        },

        "checkObject": function(shape, color) {
            if((shape === this.correct.shape) && (color === this.correct.color)) {
                this.score += 1;
            }
            else if((shape !== this.correct.shape) && (color !== this.correct.color)) {
                this.score += 1;
            }
            else {
                if(this.score > 0) {
                    this.score -= 1;
                }
            }
        },

        "reset": function() {
            this.score = 0;
            this.clicked = false;
            this.num = 0;

            document.getElementById("perceptionInfo").classList.remove("hidden");
            document.getElementById("perceptionTest").classList.add("hidden");
            this.displayInfo();

            window.clearInterval(this.interv);
            window.clearInterval(this.hideInterv);
        },

        /**
        * Returns testscore
        */
        "getScore": function() {
            return this.score;
        },

        "testFinished": function() {
            // Display results
            document.getElementById("perceptionTest").classList.add("hidden");
            document.getElementById("perceptionResultsPage").classList.remove("hidden");

            document.getElementById("perceptionTestScore").innerHTML = this.score;
        }

    };

    return test3;
})();
