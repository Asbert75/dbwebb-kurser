/**
 * @preserve 31994a7d02101f94e4e07d6c5f3db7ba
 *
 * 31994a7d02101f94e4e07d6c5f3db7ba
 * javascript1
 * lab4
 * eroa16
 * 2016-11-24 15:22:08
 * v2.2.21 (2016-10-07)
 *
 * Generated 2016-11-24 16:22:09 by dbwebb lab-utility v2.2.21 (2016-10-07).
 * https://github.com/mosbth/lab
 */

(function(dbwebb){
    "use strict";

    var ANSWER = null;

    console.log("Ready to begin.");


/** ======================================================================
 * Lab 4 - javascript1
 *
 * Practice basics on objects.
 *
 */



/** ----------------------------------------------------------------------
 * Section 1 . Create object
 *
 * Start by creating an empty object called 'person' by using the object
 * literal.
 *
 */

var person = {};


/**
 * Exercise 1.1
 *
 * Give your person-object the property 'firstName' with a value of 'Isaac'.
 * Add a method called 'print1()' that returns a presentation of the object,
 * like this: 'My name is Isaac.' Use 'this.firstName' to construct the
 * string.
 *
 * Answer with the result from calling 'person.print1()'.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */

person.firstName = "Isaac";
person.print1 = function() {
    return "My name is " + this.firstName + ".";
};




ANSWER = person.print1();

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("1.1", ANSWER, false);

/**
 * Exercise 1.2
 *
 * Add properties 'lastName' and 'nationality' to your person-object. Their
 * values should be 'Newton' and 'England'.
 *
 * Create the method 'person.print2()' which should say: 'My name is Isaac
 * Newton from England.'.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */

person.lastName = "Newton";
person.nationality = "England";

person.print2 = function() {
    return "My name is " + this.firstName + " " + this.lastName + " from " + this.nationality + ".";
};




ANSWER = person.print2();

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("1.2", ANSWER, false);

/**
 * Exercise 1.3
 *
 * Add the property 'born' with the value of a Date object: '1643-01-04'.
 * Create a method 'print3()' that says exactly the same as 'print2()'
 * followed by 'I was born 1643.'.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */

person.born = new Date("1643-01-04");
person.print3 = function() {
    return this.print2() + " I was born " + this.born.getFullYear() + ".";
};




ANSWER = person.print3();

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("1.3", ANSWER, false);

/**
 * Exercise 1.4
 *
 * Create a second person, called 'person2' by using built-in function
 * 'Object.create()'. The person2 should have the following properties:
 * 'Henri, Becquerel, France, 1852-12-15'.
 *
 * Print out details on the second person using 'person2.print3()'.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */

var person2 = Object.create(person);
person2.firstName = "Henri";
person2.lastName = "Becquerel";
person2.nationality = "France";
person2.born = new Date("1852-12-15");




ANSWER = person2.print3();

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("1.4", ANSWER, false);

/** ----------------------------------------------------------------------
 * Section 2 . More on objects
 *
 * Even more on objects!
 *
 */



/**
 * Exercise 2.1
 *
 * Create a object called 'shape' with the properties: 'x', 'y', 'height',
 * 'width' and 'print'. Create a new object from 'shape' called 'shape1' and
 * initiate the properties with: x:39, y:71, height:17, width: 20.
 *
 * Use the 'print' method to print out the assigned values as: 'x:?, y:?,
 * height:?, width:?'
 *
 * Write your code below and put the answer into the variable ANSWER.
 */

var shape = {};
shape.x = 0;
shape.y = 0;
shape.height = 0;
shape.width = 0;
shape.print = function() {
    return 'x:' + this.x + ', y:' + this.y + ', height:' + this.height + ', width:' + this.width;
};


var shape1 = Object.create(shape);
shape1.x = 39;
shape1.y = 71;
shape1.height = 17;
shape1.width = 20;





ANSWER = shape1.print();

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("2.1", ANSWER, true);

/**
 * Exercise 2.2
 *
 * Create a method 'shape.init(x, y, height, width)' that helps you to
 * initiate a object. Try it out by re-initing 'shape1' using the method.
 *
 * Answer with 'shape1.print()'.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */

shape.init = function(x, y, height, width) {
    this.x = x;
    this.y = y;
    this.height = height;
    this.width = width;
};

shape1.init(39, 71, 17, 20);




ANSWER = shape1.print();

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("2.2", ANSWER, false);

/**
 * Exercise 2.3
 *
 * Create another object from 'shape' called 'shape2' and initiate the
 * properties with: x:56, y:12, height:18, width: 15.
 *
 * Use the 'print' method to print out the assigned values.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */

var shape2 = Object.create(shape);
shape2.init(56, 12, 18, 15);




ANSWER = shape2.print();

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("2.3", ANSWER, false);

/**
 * Exercise 2.4
 *
 * Create a method in 'shape' that calculates and returns the area of the
 * shape. Try it out by calling it for 'shape1' and 'shape2'.
 *
 * Answer with both values, separated by ', ' (notice the space after the
 * comma).
 *
 * Write your code below and put the answer into the variable ANSWER.
 */

shape.calcArea = function() {
    return this.height * this.width;
};




ANSWER = shape1.calcArea() + ", " + shape2.calcArea();

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("2.4", ANSWER, false);

/**
 * Exercise 2.5
 *
 * Create a method 'shape.overlapPoint(posX, posY)' that checks if a position
 * x, y is within the current shape. Or, the shape overlaps that position. The
 * shapes position x and y is top left of the shape. Return true or false.
 * Test by checking if x:58, y:87 is within 'shape1' and if x:55, y:11 is
 * within 'shape2'.
 *
 * Return the result separated by ', ' (notice the space after the comma).
 *
 * Write your code below and put the answer into the variable ANSWER.
 */

 // x = width
 // y = height

shape.overlapPoint = function(posX, posY) {
    var xMin = this.x;
    var xMax = this.x + this.width;
    var yMin = this.y;
    var yMax = this.y + this.height;

    if ((posX < xMax) && (posX > xMin)) {
        if ((posY < yMax) && (posY > yMin)) {
            return true;
        }
    }
    else {
        return false;
    }
};




ANSWER = shape1.overlapPoint(58, 87) + ", " + shape2.overlapPoint(55, 11);

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("2.5", ANSWER, true);

/**
 * Exercise 2.6
 *
 * Create a method 'shape.overlapShape()' that takes a shape as argument and
 * checks if the shapes overlaps (colliding bodies). Return true or false.
 * Create a new 'shape3' and initiate the properties with: x:49, y:80,
 * height:17, width: 20.
 *
 * Return the result from checking 'shape1.overlapShape(shape3)'.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */

shape.overlapShape = function(aShape) {
    if (
        ((this.x + this.width > aShape.x) && (this.y + this.height > aShape.y)) &&
        ((this.x + this.width < aShape.x + aShape.width) || (this.y + this.height < aShape.y + aShape.height))
        ) {
        return true;
    }
    else {
        return false;
    }
};

var shape3 = Object.create(shape);
shape3.init(49, 80, 17, 20);


ANSWER = shape1.overlapShape(shape3);

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("2.6", ANSWER, false);

/**
 * Exercise 2.7
 *
 * Create a method 'shape.move(moveX, moveY)' which moves the shape from its
 * current position by adding 'x += moveX' and 'y += moveY'. Try it out by
 * moving 'shape3' using 'moveX: 20, moveY: 17'.
 *
 * Re-check if the bodies 'shape1' and 'shape3' collides.
 *
 * Write your code below and put the answer into the variable ANSWER.
 */

shape.move = function(moveX, moveY) {
    this.x += moveX;
    this.y += moveY;
};

shape3.move(20, 17);




ANSWER = shape1.overlapShape(shape3);

// I will now test your answer - change false to true to get a hint.
dbwebb.assert("2.7", ANSWER, false);


    console.log(dbwebb.exitWithSummary());

}(window.dbwebb));
