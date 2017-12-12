window.Test2 = (function() {
    "use strict";

    var test2 = {
        "answer": null,
        "score": 0,
        "buttonOne": document.getElementById("fizzButtonOne"),
        "buttonTwo": document.getElementById("fizzButtonTwo"),
        "buttonThree": document.getElementById("fizzButtonThree"),
        "buttonFour": document.getElementById("fizzButtonFour"),
        "buttonFive": document.getElementById("fizzButtonFive"),
        "resultsButton": document.getElementById("fizzResultButton"),

        "displayInfo": function() {
            document.getElementById("fizzBuzz").classList.remove("hidden");
            var that = this;

            var startButton = document.getElementById("fizzStartButton");
            startButton.addEventListener("click", function() {
                that.startGame();
            });
        },

        "reset": function() {
            this.answer = null;
            this.score = 0;

            this.resultsButton.classList.add("hidden");
            document.getElementById("fizzResultsPage").classList.add("hidden");
            document.getElementById("fizzTest").classList.remove("hidden");

            this.buttonOne.className = "";
            this.buttonTwo.className = "";
            this.buttonThree.className = "";
            this.buttonFour.className = "";
            this.buttonFive.className = "";

            this.enableButtons();
        },

        "startGame": function() {
            var that = this;
            document.getElementById("fizzInfo").classList.add("hidden");
            document.getElementById("fizzTest").classList.remove("hidden");

            this.buttonOne.addEventListener("click", function() {
                that.answer = "Fizz";
                that.tryAnswer();
            });

            this.buttonTwo.addEventListener("click", function() {
                that.answer = "19";
                that.tryAnswer();
            });

            this.buttonThree.addEventListener("click", function() {
                that.answer = "FizzBuzz";
                that.tryAnswer();
            });

            this.buttonFour.addEventListener("click", function() {
                that.answer = "24";
                that.tryAnswer();
            });

            this.buttonFive.addEventListener("click", function() {
                that.answer = "Buzz";
                that.tryAnswer();
            });
        },

        "tryAnswer": function() {
            var that = this;
            this.disableButtons();

            switch(this.answer) {
                case "Fizz":
                    this.buttonOne.classList.add("incorrect");
                    this.buttonTwo.classList.add("correct");

                    this.resultsButton.classList.remove("hidden");
                    this.resultsButton.addEventListener("click", function() { that.displayResult(); });
                    break;

                case "19":
                    this.buttonTwo.classList.add("correct");
                    this.score = 3;

                    this.resultsButton.classList.remove("hidden");
                    this.resultsButton.addEventListener("click", function() { that.displayResult(); });
                    break;

                case "FizzBuzz":
                    this.buttonThree.classList.add("incorrect");
                    this.buttonTwo.classList.add("correct");

                    this.resultsButton.classList.remove("hidden");
                    this.resultsButton.addEventListener("click", function() { that.displayResult(); });
                    break;

                case "24":
                    this.buttonFour.classList.add("incorrect");
                    this.buttonTwo.classList.add("correct");

                    this.resultsButton.classList.remove("hidden");
                    this.resultsButton.addEventListener("click", function() { that.displayResult(); });
                    break;

                case "Buzz":
                    this.buttonFive.classList.add("incorrect");
                    this.buttonTwo.classList.add("correct");

                    this.resultsButton.classList.remove("hidden");
                    this.resultsButton.addEventListener("click", function() { that.displayResult(); });
                    break;
            }


        },

        "displayResult": function() {
            document.getElementById("fizzTest").classList.add("hidden");
            document.getElementById("fizzResultsPage").classList.remove("hidden");

            document.getElementById("fizzTestScore").innerHTML = this.score;
        },

        "disableButtons": function() {
            this.buttonOne.classList.add("disabled");
            this.buttonTwo.classList.add("disabled");
            this.buttonThree.classList.add("disabled");
            this.buttonFour.classList.add("disabled");
            this.buttonFive.classList.add("disabled");
        },

        "enableButtons": function() {
            this.buttonOne.classList.remove("disabled");
            this.buttonTwo.classList.remove("disabled");
            this.buttonThree.classList.remove("disabled");
            this.buttonFour.classList.remove("disabled");
            this.buttonFive.classList.remove("disabled");
        },

        /**
        * Returns testscore
        */
        "getScore": function() {
            return this.score;
        }
    };

    return test2;
})();
