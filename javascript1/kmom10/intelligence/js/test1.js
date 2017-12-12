window.Test1 = (function() {
    "use strict";

    var test1 = {
        "score": 0,
        "answer": null,
        "currQuestion": 1,
        "question": document.getElementById("question"),
        "answerOne": document.getElementById("answerOne"),
        "answerX": document.getElementById("answerX"),
        "answerTwo": document.getElementById("answerTwo"),

        "buttonOne": document.getElementById("one"),
        "buttonX": document.getElementById("x"),
        "buttonTwo": document.getElementById("two"),
        "nextQuestion": document.getElementById("nextQuestion"),
        "result": document.getElementById("result"),

        "infoParagraph": document.getElementById("information"),
        "header": document.getElementById("header"),
        "startButton": document.getElementById("startButton"),

        "questions": {
            "one": {
                "question": "Vem är rikast av de tre?",
                "one": "Clark Kent",
                "x": "Bruce Wayne",
                "two": "Hugo Strange",
                "answer": "x"
            },
            "two": {
                "question": "Vilken av följande tidningar finns med i Superman?",
                "one": "Daily Planet",
                "x": "Aftonbladet",
                "two": "Expressen",
                "answer": "one"
            },
            "three": {
                "question": "Vilket utav de följande materialen är tyngst?",
                "one": "Vatten",
                "x": "Järn",
                "two": "Bly",
                "answer": "two"
            }
        },

        /**
        * Reset function, called by outer Test.reset()
        */
        "reset": function() {
            this.score = 0;
            this.currQuestion = 1;
            this.answer = null;
            this.displayQuestion();
            this.enableButtons();

            this.result.classList.add("hidden");
            this.nextQuestion.classList.add("hidden");
        },

        "displayInfo": function() {
            var that = this;
            this.header.innerHTML = "Tipsfrågor";
            this.infoParagraph.innerHTML = "Detta test går ut på att du ska svara på ett antal tipsfrågor. Varje fråga kommer att ha tre svarsalternativ: 1, X och 2. Svara genom att klicka på ett utav alternativen som visas.<br>När du svarat på alla frågor kommer du få reda på ditt resultat.";

            this.startButton.addEventListener("click", function() {
                that.displayOne();
                document.getElementById("startPage").className = ("hidden");
                document.getElementById("questions").className = ("");

                that.buttonOne.addEventListener("click", function() {
                    that.answer = "one";
                    that.checkAnswer();

                    that.disableButtons();
                });
                that.buttonX.addEventListener("click", function() {
                    that.answer = "x";
                    that.checkAnswer();

                    that.disableButtons();
                });

                that.buttonTwo.addEventListener("click", function() {
                    that.answer = "two";
                    that.checkAnswer();

                    that.disableButtons();
                });

                that.nextQuestion.addEventListener("click", function() {
                    that.displayQuestion();

                    document.getElementById("results").classList.add("hidden");
                    document.getElementById("nextQuestion").classList.add("hidden");

                    that.enableButtons();
                });
            });
        },

        /**
        * Disables answers
        */
        "disableButtons": function() {
            this.buttonOne.classList.add("disabled");
            this.buttonX.classList.add("disabled");
            this.buttonTwo.classList.add("disabled");
        },

        /**
        * Enables answers
        */
        "enableButtons": function() {
            this.buttonOne.classList.remove("disabled");
            this.buttonX.classList.remove("disabled");
            this.buttonTwo.classList.remove("disabled");
        },

        "checkAnswer": function() {
            var that = this;

            document.getElementById("results").classList.remove("hidden");
            document.getElementById("nextQuestion").classList.remove("hidden");

            if(this.currQuestion === 1) {
                this.buttonX.classList.add("correct");

                switch(this.answer) {
                    case "one":
                        that.buttonOne.classList.add("incorrect");
                        that.result.innerHTML = "Fel svar. Rätt svar var X: Bruce Wayne";
                        break;
                    case "x":
                        that.score += 3;
                        that.result.innerHTML = "Rätt svar!";
                        break;
                    case "two":
                        that.buttonTwo.classList.add("incorrect");
                        that.result.innerHTML = "Fel svar. Rätt svar var X: Bruce Wayne";
                        break;
                }
            }
            else if(this.currQuestion === 2) {
                this.buttonOne.classList.add("correct");

                switch(this.answer) {
                    case "one":
                        that.score += 3;
                        that.result.innerHTML = "Rätt svar!";
                        break;
                    case "x":
                        that.buttonX.classList.add("incorrect");
                        that.result.innerHTML = "Fel svar. Rätt svar var 1: Daily Planet";
                        break;
                    case "two":
                        that.buttonTwo.classList.add("incorrect");
                        that.result.innerHTML = "Fel svar. Rätt svar var 1: Daily Planet";
                        break;
                }
            }
            else if(this.currQuestion === 3) {
                document.getElementById("nextQuestion").innerHTML = "Visa Resultat";
                this.buttonTwo.classList.add("correct");

                switch(this.answer) {
                    case "one":
                        that.buttonOne.classList.add("incorrect");
                        that.result.innerHTML = "Fel svar. Rätt svar var 2: Bly";
                        break;
                    case "x":
                        that.buttonOne.classList.add("incorrect");
                        that.result.innerHTML = "Fel svar. Rätt svar var 2: Bly";
                        break;
                    case "two":
                        that.score += 3;
                        that.result.innerHTML = "Rätt svar!";
                        break;
                }
            }

            this.currQuestion++;
            this.answer = null;
        },

        "displayQuestion": function() {
            var that = this;
            this.buttonOne.classList.remove("incorrect");
            this.buttonOne.classList.remove("correct");

            this.buttonX.classList.remove("incorrect");
            this.buttonX.classList.remove("correct");

            this.buttonTwo.classList.remove("incorrect");
            this.buttonTwo.classList.remove("correct");

            switch(this.currQuestion) {
                case 1:
                    this.displayOne();
                    break;
                case 2:
                    this.displayTwo();
                    break;
                case 3:
                    this.displayThree();
                    break;
                case 4:
                    // All questions answered, go to finish page.
                    document.getElementById("questionsContainer").classList.add("hidden");
                    document.getElementById("resultsPage").classList.remove("hidden");

                    document.getElementById("testScore").innerHTML = that.score;
            }
        },

        "displayOne": function() {
            this.question.innerHTML = this.questions.one.question;
            this.answerOne.innerHTML = this.questions.one.one;
            this.answerX.innerHTML = this.questions.one.x;
            this.answerTwo.innerHTML = this.questions.one.two;
        },

        "displayTwo": function() {
            this.question.innerHTML = this.questions.two.question;
            this.answerOne.innerHTML = this.questions.two.one;
            this.answerX.innerHTML = this.questions.two.x;
            this.answerTwo.innerHTML = this.questions.two.two;
        },

        "displayThree": function() {
            this.question.innerHTML = this.questions.three.question;
            this.answerOne.innerHTML = this.questions.three.one;
            this.answerX.innerHTML = this.questions.three.x;
            this.answerTwo.innerHTML = this.questions.three.two;
        },

        /**
        * Returns testscore
        */
        "getScore": function() {
            return this.score;
        }
    };

    return test1;
})();
