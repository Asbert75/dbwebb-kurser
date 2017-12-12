(function() {
    'use strict';

    function Flag(country, flagId, flagCode) {
        var that = this;
        this.flagCode = flagCode;
        this.country = country;
        this.flagId = flagId;
        this.target = document.getElementById(country);
        this.link = document.getElementById(this.flagId);

        this.draw = function() {
            that.target.innerHTML = flagCode;
            console.log("Drawing flag.");
        };

        this.undraw = function() {
            that.target.innerHTML = " ";
            console.log("Removing Flag.");
        };

        this.initialize = function() {
            console.log("Initializing " + this.country + " flag!");

            this.link.addEventListener("click", function() {
                console.log(this.target);
                that.draw();
            });

            this.target.addEventListener("click", function() {
                that.undraw();
            });
        };
    }

    var sweFlag = new Flag('swedish', 'drawSweden', '<div id="swedishFlag"><div id="sweHorizontal"></div><div id="sweVertical"></div></div>');
    var fraFlag = new Flag('french', 'drawFrance', '<div id="frenchFlag"><div id="frenchLeft"></div><div id="frenchRight"></div></div>');
    var irlFlag = new Flag('irish', 'drawIreland', '<div id="irishFlag"><div id="irishLeft"></div><div id="irishRight"></div></div>');
    var idnFlag = new Flag('indonesian', 'drawIndonesia', '<div id="indonesianFlag"><div id="indonesianBottom"></div></div>');

    console.log(sweFlag);

    var flags = [];
    flags[0] = sweFlag;
    flags[1] = fraFlag;
    flags[2] = irlFlag;
    flags[3] = idnFlag;

    flags.forEach(function(flag) { flag.initialize();});

})();
