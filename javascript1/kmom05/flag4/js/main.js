(function() {
    'use strict';
    var content = document.getElementById("body");

    function swapBG() {
        var targets = document.querySelectorAll("button");

        Array.prototype.forEach.call(targets, function(button) {
            button.addEventListener("click", function(event) {
                var color = event.target.id;

                switch(color) {
                    case "red":
                        content.style.backgroundColor = "#C74444";
                        break;
                    case "blue":
                        content.style.backgroundColor = "#4486C7";
                        break;
                    case "green":
                        content.style.backgroundColor = "#44c767";
                        break;
                }
            });
        });
    }

    function Flag(country, flagId, flagCode) {
        this.flagCode = flagCode;
        this.country = country;
        this.flagId = flagId;

        this.draw = function(target) {
            target.innerHTML = flagCode;
        };

        this.undraw = function(target) {
            target.innerHTML = "?";
        };
    }

    var sweFlag = new Flag('swedish', 'drawSweden', '<div id="swedishFlag"><div id="sweHorizontal"></div><div id="sweVertical"></div></div>');
    var fraFlag = new Flag('french', 'drawFrance', '<div id="frenchFlag"><div id="frenchLeft"></div><div id="frenchRight"></div></div>');
    var irlFlag = new Flag('irish', 'drawIreland', '<div id="irishFlag"><div id="irishLeft"></div><div id="irishRight"></div></div>');
    var idnFlag = new Flag('indonesian', 'drawIndonesia', '<div id="indonesianFlag"><div id="indonesianBottom"></div></div>');
    var japFlag = new Flag('japanese', 'drawJapan', '<div id="japaneseFlag"><div id="japaneseMid"></div></div>');

    var blocks = new Array(10);
    var selectedBlocks = new Array(2);
    var selectedCards = new Array(2);

    var foundMatches = 0;

    var cells = document.querySelectorAll("td");
    var clicks = 0;

    function initializeGame() {
        for (var i = 0; i < 10; i++) {
            cells[i].id = i;

            cells[i].onclick = function() {
                displayCard(this.id);
            };

            var rand = Math.floor(Math.random() * 5);

            while (isDuplicate(rand)) {
                rand = Math.floor(Math.random() * 5);
            }

            blocks[i] = rand;
        }
    }

    function reset() {
        for (var b = 0; b < blocks.length; b++) {
            blocks[b] = undefined;
        }

        for (var sb = 0; sb < selectedBlocks.length; sb++) {
            selectedBlocks[sb] = undefined;
        }

        for (var sc = 0; sc < selectedCards.length; sc++) {
            selectedCards[sc] = undefined;
        }

        foundMatches = 0;
        clicks = 0;

        for (var i = 0; i < 10; i++) {
            cells[i].innerHTML = "?";
        }

        initializeGame();
    }

    function toggleClicks() {
        var cards = document.querySelectorAll("td");

        Array.prototype.forEach.call(cards, function(card) {
            card.classList.toggle("unclickable");
        });
    }

    function isDuplicate(num) {
        var idCount = 0;

        for (var i = 0; i < 10; i++) {
            if (blocks[i] == num) {
                idCount++;
            }
        }

        if (idCount > 1) {
            return true;
        }
        else {
            return false;
        }
    }

    function drawFlags(targetCard, blockPos) {
        var flagId = blocks[blockPos];

        switch(flagId) {
            case 0:
                sweFlag.draw(targetCard);
                break;
            case 1:
                fraFlag.draw(targetCard);
                break;
            case 2:
                irlFlag.draw(targetCard);
                break;
            case 3:
                idnFlag.draw(targetCard);
                break;
            case 4:
                japFlag.draw(targetCard);
                break;
        }
    }

    function checkForMatch(id){
		if (clicks == 1) {
			selectedCards[0] = blocks[id];
			selectedBlocks[0] = id;
		}
		else if (clicks == 2) {
			selectedCards[1] = blocks[id];
			selectedBlocks[1] = id;

			if (selectedCards[0] == selectedCards[1]) {
				console.log("Match! Keep on clicking to match the other flags.");
                foundMatches++;

                if (foundMatches == 5) {
                    window.setTimeout(function() {
                        if (window.confirm("Congratulations. You have finished the game!\nWould you like to reset the game?")) {
                            reset();
                        }
                    }, 1000);
                }
			}
			else {
				console.log("No match! Flipping cards back.");

				toggleClicks();

				window.setTimeout(function() {
					for (var i = 0; i < 2; i++) {
						for (var c = 0; c < 10; c++) {
							if (blocks[c] === selectedCards[i]) {
								var cont = document.getElementById(selectedBlocks[i]);
								cont.innerHTML = "?";
								cont.onclick = function() {
                                    displayCard(this.id);
                                };
							}
						}
					}

					toggleClicks();

				}, 1500);
			}

			clicks = 0;

		}
	}

    function displayCard(id) {
        var card = document.getElementById(id);

        card.onclick = function() {
            window.alert("You cannot select that card again.");
        };

        clicks++;
        console.log("Clicks: " + clicks);

        drawFlags(card, id);
        checkForMatch(id);
    }

    initializeGame();
    swapBG();

}());
