(function(){
    'use strict';
    /*globals Hangman*/

    var characterList = document.getElementsByTagName("input");
    var wordContainer = document.getElementById("wordContainer");
    var wrongLetters = document.getElementById("wrongLetters");
    var message = document.getElementById("winMessage");
    var messageContainer = document.getElementById("winContainer");
    var resetButton = document.getElementById("newGame");

    wrongLetters.innerHTML = "()";

    var guessedCharacters = [];
    var wrongGuesses = 0;

    var theWord = Hangman.getWord();
    var wordArray = theWord.split("");
    var hiddenWord = Array(wordArray.length);



    resetButton.addEventListener("click", function() { window.location.reload(); });
    resetButton.style.display = "none";


    for (var j = 0; j < wordArray.length; j++) {
            hiddenWord[j] = "-";
            wordContainer.innerHTML += "- ";
    }

    for (var i = 0; i < characterList.length; i++) {
        characterList[i].addEventListener("click", function() {
            var letter = this.value;
            if(theWord.indexOf(letter) !== -1) {
                findOccurrences(letter);
            }
            else {
                wrongGuesses++;
                guessedCharacters.push(letter);
            }

            this.className = "inactive";
            wrongLetters.innerHTML = "(" + guessedCharacters.join("") + ")";
            wordContainer.innerHTML = hiddenWord.join(" ");

            buildHangman();
        });
    }


    function findOccurrences(letter) {
        for (var i = 0; i < theWord.length; i++) {
            if(theWord.charAt(i) === letter) {
                hiddenWord[i] = letter;
            }
        }

        if (hiddenWord.indexOf("-") === -1) {
            // Game won
            messageContainer.style.background = "green";
            message.innerHTML = "CONGRATULATIONS. YOU WON!";
            inactivateAll();
        }
    }


    function lostGame() {
        messageContainer.style.background = "red";
        message.innerHTML = "YOU LOST!";
        inactivateAll();
    }


    function inactivateAll() {
        for (var i = 0; i < characterList.length; i++) {
            characterList[i].className = "inactive";
        }

        resetButton.style.display = "inline";
    }


    function buildHangman() {
        switch(wrongGuesses) {
            case 1:
                Hangman.show("hill");
                break;
            case 2:
                Hangman.show("gallow");
                break;
            case 3:
                Hangman.show("rope");
                break;
            case 4:
                Hangman.show("head");
                break;
            case 5:
                Hangman.show("body");
                break;
            case 6:
                Hangman.show("rightarm");
                break;
            case 7:
                Hangman.show("leftarm");
                break;
            case 8:
                Hangman.show("rightleg");
                break;
            case 9:
                Hangman.show("leftleg");
                lostGame();
                break;
        }
    }


    function init() {
        Hangman.hide("hill");
        Hangman.hide("gallow");
        Hangman.hide("rope");
        Hangman.hide("head");
        Hangman.hide("body");
        Hangman.hide("rightarm");
        Hangman.hide("leftarm");
        Hangman.hide("rightleg");
        Hangman.hide("leftleg");
    }


    init();

})();
