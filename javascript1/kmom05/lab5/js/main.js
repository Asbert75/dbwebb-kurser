(function(){
    'use strict';
    var verbose = false;

    var myContent = document.getElementById('content');

    var box1 = document.getElementById('box1');

    function printDimensions(element) {
        var width = element.offsetWidth;
        var height = element.offsetHeight;
        console.log("Width: " + width + "px. Height: " + height + "px.");
    }

    function printWindowDimensions() {
        var width = window.innerWidth;
        var height = window.innerHeight;
        console.log("Width: " + width + "px. Height: " + height + "px.");
    }

    function getWindowDimensions() {
        var width = window.innerWidth;
        var height = window.innerHeight;
        return [width, height];
    }

    function getProperty(element, property) {
        var prop, styles;

        styles = window.getComputedStyle(element);
        prop = styles.getPropertyValue(property);

        return prop;
    }

    function centerElement(element) {
        var width = element.offsetWidth;
        var height = element.offsetHeight;

        element.style.position = "absolute";
        element.style.top = "50%";
        element.style.left = "50%";
        element.style.marginTop = -(height/2) + "px";
        element.style.marginLeft = -(width/2) + "px";
    }

    function printPos(element) {
        var rect = element.getBoundingClientRect();
        console.log("Top: " + rect.top + "px Right: " + rect.right + "px Bottom: " + rect.bottom + "px Left: " + rect.left + "px");
    }

    console.log("Box top: " + getProperty(box1, "top") + " and left: " + getProperty(box1, "left"));
    printWindowDimensions();
    printDimensions(box1);

    centerElement(box1);
    console.log("Box size: " + getProperty(box1, "width") + " * " + getProperty(box1, "height"));
    printPos(box1);


    window.addEventListener("resize", function() {
        centerElement(box1);
    });


    function toggleOutline(target) {
        target.classList.toggle("selected");
    }

    window.addEventListener("click", function(event) {
        var target = event.target;
        toggleOutline(target);
        if(verbose) console.log(event);
    });


    function toggleCircle() {
        if(verbose) console.log("E was pressed.");
        var targets = document.getElementsByClassName("selected");

        for (var i = 0; i < (targets.length); i++) {
                targets[i].classList.toggle("circle");
        }
    }

    document.addEventListener("keydown", function(event) {
		var key;
		key = event.keyCode || event.which;
        if (key == 69) {
            toggleCircle();
        }
    });



    function changeSize(target, width, height) {
        target.style.width = width + "px";
        target.style.height = height + "px";

        centerElement(target);
    }

    box1.addEventListener("click", function() {
        changeSize(box1, 300, 300);
    });


    function by10(key) {
        var targets = document.querySelectorAll(".selected");

        Array.prototype.forEach.call(targets, function(element) {
            var w = element.offsetWidth;
            var h = element.offsetHeight;

            if (key == 81) { // Q pressed
                w += 10;
                h += 10;
                element.style.width = w + "px";
                element.style.height = h + "px";

                element.style.marginTop = -(h/2) + "px";
                element.style.marginLeft = -(w/2) + "px";
            }
            else if (key == 87) { // W pressed
                w -= 10;
                h -= 10;
                element.style.width = w + "px";
                element.style.height = h + "px";

                element.style.marginTop = -(h/2) + "px";
                element.style.marginLeft = -(w/2) + "px";
            }
        });
    }

    function swapColor() {
        var targets = document.getElementsByClassName("selected");
        // grön->gul->röd->blå->
        Array.prototype.forEach.call(targets, function (element) {
            if(element.classList.contains("green")) {
                element.classList.add("purple");
                element.classList.remove("green");
            }
            else if(element.classList.contains("purple")) {
                element.classList.add("red");
                element.classList.remove("purple");
            }
            else if(element.classList.contains("red")) {
                element.classList.add("blue");
                element.classList.remove("red");
            }
            else if(element.classList.contains("blue")) {
                element.classList.add("green");
                element.classList.remove("blue");
            }
            else {
                element.classList.add("green");
            }
        });
    }


    function placeRandom(element) {
        var dimensions = getWindowDimensions();
        var maxWidth = dimensions[0];
        var maxHeight = dimensions[1];

        var eleWidth = element.offsetWidth;
        var eleHeight = element.offsetHeight;

        var width = Math.random() * maxWidth;
        var height = Math.random() * maxHeight;

        if((eleWidth + width) > maxWidth) {
            width = width - eleWidth;
        }

        if((width - eleWidth) < 0) {
            width = width + eleWidth;
        }

        if((eleHeight + height) > maxHeight) {
            height = height - eleHeight;
        }

        if((height - eleHeight) < 0) {
            height = height + eleHeight;
        }

        return [width, height];
    }

    function duplicateSelected() {
        var targets = document.querySelectorAll(".selected");
        var targetCount = 0;

        Array.prototype.forEach.call(targets, function (element) {
            targetCount += 1;
            var clone = element.cloneNode();

            var dimensions = placeRandom(element);
            var width = dimensions[0];
            var height = dimensions[1];

            clone.style.zIndex = (element.style.zIndex + 1);
            clone.style.top = height + "px";
            clone.style.left = width + "px";

            myContent.appendChild(clone);
        });

        console.log("Duplicates created: " + targetCount);
    }


    function changeZ(key) {
        var targets = document.querySelectorAll(".selected");
        var index;

        Array.prototype.forEach.call(targets, function (element) {
            index = parseInt(element.style.zIndex);
            if (isNaN(index)) {
                index = 0;
            }

            if (key == 65) {
                element.style.zIndex = index+1;
            }
            else if (key == 83) {
                element.style.zIndex = index-1;
            }
        });
    }

    function removeSelected() {
        var targets = document.querySelectorAll(".selected");

        Array.prototype.forEach.call(targets, function (element) {
            if(element.parentNode == myContent) {
                myContent.removeChild(element);
            }
        });
    }

    function moveSelected(key) {
        var targets = document.querySelectorAll(".selected");
        var top;
        var left;

        Array.prototype.forEach.call(targets, function (element) {
            top = element.style.top;
            left = element.style.left;

            if (top.indexOf("%") !== -1) {
                // If value is in % do this
                top = parseFloat(top);
                left = parseFloat(left);

                switch (key) {
                    case 38: // UP
                        top -= 0.5;
                        element.style.top = top + "%";
                        break;
                    case 39: // RIGHT
                        left += 0.5;
                        element.style.left = left + "%";
                        break;
                    case 40: // DOWN
                        top += 0.5;
                        element.style.top = top + "%";
                        break;
                    case 37: // LEFT
                        left -= 0.5;
                        element.style.left = left + "%";
                        break;
                }
            }
            else if (top.indexOf("px") !== -1) {
                // If value is in px do this
                top = parseFloat(top);
                left = parseFloat(left);

                switch (key) {
                    case 38: // UP
                        top -= 20;
                        element.style.top = top + "px";
                        break;
                    case 39: // RIGHT
                        left += 20;
                        element.style.left = left + "px";
                        break;
                    case 40: // DOWN
                        top += 20;
                        element.style.top = top + "px";
                        break;
                    case 37: // LEFT
                        left -= 20;
                        element.style.left = left + "px";
                        break;
                }
            }
        });
    }

    function deselect() {
        var targets = document.querySelectorAll(".selected");

        Array.prototype.forEach.call(targets, function (element) {
            element.classList.remove("selected");
        });
    }

    function selectAll() {
        var targets = document.getElementsByTagName("*");
        var targetCount = 0;

        Array.prototype.forEach.call(targets, function (element) {
            targetCount += 1;
            element.classList.add("selected");
        });

        console.log("Targets selected: " + targetCount);
    }

    function clearClass(target) {
        target.classList.remove("green");
        target.classList.remove("red");
        target.classList.remove("purple");
        target.classList.remove("blue");

        target.classList.remove("box");
        target.classList.remove("circle");
    }

    function randomizeColor(target) {
        var colors = ["green", "red", "purple", "blue"];
        var color = Math.round(Math.random() * 3);

        target.classList.add(colors[color]);
    }

    function randomizeShape(target) {
        var shapes = ["box", "circle"];
        var shape = Math.round(Math.random());

        target.classList.add(shapes[shape]);
    }

    function randomizePlacement(target) {
        var dimensions = placeRandom(box1);
        var width = dimensions[0];
        var height = dimensions[1];

        target.style.top = height + "px";
        target.style.left = width + "px";
    }

    function createRandomElement() {
        var clone = box1.cloneNode();

        clone.className = "size200";

        randomizeColor(clone);
        randomizeShape(clone);
        randomizePlacement(clone);

        myContent.appendChild(clone);
    }


    document.addEventListener("keydown", function(event) {
        var key;
        var target;
        key = event.keyCode || event.which;

        target = event.target;
        console.log(event);

        switch (key) {
            case 81:
                if(verbose) console.log("Sent Q");
                by10(81);
                break;

            case 87:
                if(verbose) console.log("Sent W");
                by10(87);
                break;

            case 82:
                if(verbose) console.log("Sent R");
                swapColor();
                break;

            case 84:
                if(verbose) console.log("Sent T");
                duplicateSelected();
                break;

            case 65:
                if(verbose) console.log("Sent A");
                changeZ(key);
                break;

            case 83:
                if(verbose) console.log("Sent S");
                changeZ(key);
                break;

            case 89:
                if(verbose) console.log("Sent Y");
                removeSelected();
                break;

            case 38:
                if(verbose) console.log("Sent UP ARROW");
                moveSelected(key);
                break;

            case 40:
                if(verbose) console.log("Sent DOWN ARROW");
                moveSelected(key);
                break;

            case 39:
                if(verbose) console.log("Sent RIGHT ARROW");
                moveSelected(key);
                break;

            case 37:
                if(verbose) console.log("Sent LEFT ARROW");
                moveSelected(key);
                break;

            case 85:
                if(verbose) console.log("Sent U");
                deselect();
                break;

            case 73:
                if(verbose) console.log("Sent I");
                selectAll();
                break;

            case 80:
                if(verbose) console.log("Sent P");
                createRandomElement();
                break;

            case 68:
                if(verbose) console.log("Sent D");
                animateObjectChange();
                break;

            case 71:
                if(verbose) console.log("Sent G");
                clearImages();
                mirrorImage();
                break;

            default:
                break;
        }
    });

    function fadeRemove(target) {
        target.classList.add("animateSize");
        target.style.width = "2px";
        target.style.height = "2px";

        window.setTimeout(function() {
            target.parentNode.removeChild(target);
        }, 2000);
    }


    document.addEventListener("dblclick", function(event) {
        var tar = event.target;
        fadeRemove(tar);
    });


    function animateObjectChange() {
        var targets = document.querySelectorAll(".selected");

        Array.prototype.forEach.call(targets, function (element) {
            var interv = window.setInterval(function() {
                clearClass(element);
                randomizeShape(element);
                randomizeColor(element);
                randomizePlacement(element);
            }, 200);

            window.setTimeout(function() {
                window.clearInterval(interv);
            }, 1000);
        });
    }

    function clearImages() {
        var targets = document.querySelectorAll(".imageContainer");

        Array.prototype.forEach.call(targets, function (element) {
            while (element.firstChild) {
                element.removeChild(element.firstChild);
            }
            fadeRemove(element);
        });
    }

    function mirrorImage() {
        var imageContainer = document.createElement("div");
        myContent.appendChild(imageContainer);
        imageContainer.classList.add("imageContainer");
        imageContainer.classList.add("animateSize");

        var images = [];

        for (var im = 0; im < 16; im++) {
            images[im] = document.createElement("div");

            randomizeColor(images[im]);
            randomizeShape(images[im]);
            images[im].style.width = images[im].style.height = "112.5px";
            images[im].classList.add("image" + im);
        }

        window.setTimeout(function() {
            imageContainer.style.width = imageContainer.style.height = "500px";

            window.setTimeout(function() {
                images.forEach(function(element) {
                    imageContainer.appendChild(element);
                });
            }, 1000);
        }, 1500);

    }

})();
