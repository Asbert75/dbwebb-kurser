window.Test = (function(){
    'use strict';

    var test = {
        "iq": 0,
        "score": 0,
        "test1Score": 0,
        "test2Score": 0,
        "test3Score": 0,
        "loadedTest": window.Test1,

        "startTest": document.getElementById("startButton"),
        "endTest1": document.getElementById("endTest1"),
        "endTest2": document.getElementById("endTest2"),
        "endTest3": document.getElementById("endTest3"),


        /**
        * Initializing the tests. Calling function sets onClick events for test buttons.
        */
        "init": function() {
            var that = this;

            this.startTest.addEventListener("click", function() {
                that.loadedTest.displayInfo();
            });

            this.endTest1.addEventListener("click", function() {
                that.test1Score = that.loadedTest.getScore();
                that.loadedTest = window.Test2;
                that.loadedTest.displayInfo();

                document.getElementById("questions").classList.add("hidden");
            });

            this.endTest2.addEventListener("click", function() {
                that.test2Score = that.loadedTest.getScore();
                that.loadedTest = window.Test3;
                that.loadedTest.displayInfo();
            });

            this.endTest3.addEventListener("click", function() {
                that.test3Score = that.loadedTest.getScore();
                that.score = that.test1Score + that.test2Score + that.test3Score;
                that.iq = Math.floor((that.score*5.9)-0.3);

                document.getElementById("perception").classList.add("hidden");
                document.getElementById("finalResult").classList.remove("hidden");

                document.getElementById("finalScore").innerHTML = that.iq;
            });

        },

        /**
        * Resets currently loaded test
        */
        "reset": function() {
            this.loadedTest.reset();
        }
    };

    test.init();

    return test;

})();
