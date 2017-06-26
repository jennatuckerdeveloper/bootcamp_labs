// variables
// var variable-name = data-type;

var name = 'Chris';

// data types
// strings
var string = "This is a string.";
//arrays
var array = ['we would call this a list in python', 22, 44, [4, 3.3], {'key': 'value'}];
// Javascript objects
var jsObj = {
    'key1': 'value1',
    'key2': 'value2'
};
// NO comma after the last JS object value.
// keys don't necessarily have to be in quotations in JS
// JS objects look like python dictionaries.
// Python dictionaries are JV objects or classes.
// You won't get the variables built in the way you do in Python.
// You can build methods into JS objects.
var integer = 331030850;
// float
var float = 3.14;
// bools

// Functions
// JS was written within like a week.
// Back in the early 90's.
// Kind of a joke.
// Java was popular at the time, and Javascript wanted to ride the coattails of its popularity.
// Javascript has evolved quite a bit.
// There are a lot of ways to do things.
function myFunction(arg1, arg2) {
    console.log(arg1 + arg2);
}
// function myFunction(arg1, arg2) {
//     alert(arg1 + arg2);
// };
myFunction(4, 5)
// alert is a pop-up
// JS at the top of the page stops the page from rendering
// Always put JS at the bottom of the body
var greeting = function (nm) {
    console.log(nm);
};
// greeting(name)

// bools
// true and false are lower case
// || is or
// && is and
// === is equals

function testBool1() {
    var bool = (true && !true);
    console.log(bool)
}

// control flow

var num = Math.floor(Math.random() * 100) + 1;
function guessNumber(guess) {
    if (guess > num) {
        console.log('You guessed higher than the random number.')
    } else if (guess < num) {
        console.log('You guessed lower than the random number.')
    } else {
        console.log('You win! The number was ' + num)
    }
}

guessNumber(32, num);

// event listeners
// MDN Mozilla Developer Network, great JS documentation

document.getElementById('guess').addEventListener('click', function (event) {
    event.preventDefault();
    console.log('I have been clicked!');
    var ourGuess = document.getElementById('ValueGuess').value;
    guessNumber(ourGuess);
});

