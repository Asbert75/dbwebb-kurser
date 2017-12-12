/**
 * Showing off how to display/hide parts of a SVG-image.
 */
window.Hangman = (function() {
    "use strict";

    var hangman = {

        "theWord": " ",

        "words": ["runt", "battlerite", "xylophone", "abruptly", "axolotl", "envious", "violent"],

        // Get all elements as their id
        "partAsElement": {
            "hill":     document.getElementById('hang_hill'),
            "gallow":   document.getElementById('hang_construction'),
            "body":     document.getElementById('hang_body'),
            "rightarm": document.getElementById('hang_rightarm'),
            "leftarm":  document.getElementById('hang_leftarm'),
            "rightleg": document.getElementById('hang_rightleg'),
            "leftleg":  document.getElementById('hang_leftleg'),
            "rope":     document.getElementById('hang_rope'),
            "head":     document.getElementById('hang_head')
        },

        // Create an array with all valid parts
        "validParts": [
            "hill",
            "gallow",
            "body",
            "rightarm",
            "leftarm",
            "rightleg",
            "leftleg",
            "rope",
            "head"
        ],

        "isValid": function (part) {

            if (this.validParts.indexOf(part) === -1) {
                console.log("The part is not valid: " + part);
                return false;
            }
            return true;
        },

        "hide": function (part) {

            if (this.isValid(part)) {
                this.partAsElement[part].style.display = "none";
            }

        },

        "show": function (part) {

            if (this.isValid(part)) {
                this.partAsElement[part].style.display = "inline";
            }

        },

        "wordlist": function () {
            console.log(this.words);
        },

        "randomizeWord": function () {
            this.theWord = this.words[(Math.floor(Math.random() * this.words.length))];
        },

        "getWord": function () {
            this.randomizeWord();
            return this.theWord;
        },

        "peek": function () {
            console.log(this.theWord);
        }
    };

    return hangman;
})();
