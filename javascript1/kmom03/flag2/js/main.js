(function(){
    'use strict';

    // var myContent = document.getElementById('content');
    var flag = document.getElementById("flag");


    var sweLink = document.getElementById("drawSweden");
    var fraLink = document.getElementById("drawFrance");
    var irlLink = document.getElementById("drawIreland");
    var idnLink = document.getElementById("drawIndonesia");

    sweLink.addEventListener("click", function() {
        console.log("Drawing Swedish Flag");
        drawFlag("sweden");
    });

    fraLink.addEventListener("click", function() {
        console.log("Drawing French Flag");
        drawFlag("france");
    });

    irlLink.addEventListener("click", function() {
        console.log("Drawing Irish Flag");
        drawFlag("ireland");
    });

    idnLink.addEventListener("click", function() {
        console.log("Drawing Indonesian Flag");
        drawFlag("indonesia");
    });

    flag.addEventListener("click", function() {
        console.log("Removing Flag");
        flag.innerHTML = "";
    });

    function drawFlag(country) {
        console.log("Drawing flag for " + country);

        switch (country) {
            case "sweden":
                flag.innerHTML = '<div id="swedishFlag"><div id="sweHorizontal"></div><div id="sweVertical"></div></div>';
                break;

            case "france":
                flag.innerHTML = '<div id="frenchFlag"><div id="frenchLeft"></div><div id="frenchRight"></div></div>';
                break;

            case "ireland":
                flag.innerHTML = '<div id="irishFlag"><div id="irishLeft"></div><div id="irishRight"></div></div>';
                break;

            case "indonesia":
                flag.innerHTML = '<div id="indonesianFlag"><div id="indonesianBottom"></div></div>';
                break;

            default:
                console.log("Flag not available.");
                break;
        }
    }

    console.log('Sandbox is ready!');
})();
