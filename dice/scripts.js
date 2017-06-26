// JavaScript JS Objects

// var val = Math.floor(Math.random() * 6) + 1;
// var held = false;
// 'use strict';
'use strict';

var round = 1;


function die(id) {
    this.id = id;
    this.val = 0;
    this.held = false;
    this.setVal = function() {
        if (!this.held) {
            this.val = Math.floor(Math.random() * 6) + 1;
            this.render();
        }

    }
    this.render = function() {document.getElementById(this.id).innerHTML=this.val.toString()};

};

function checkRound() {
    if (die1.val === 3 && die2.val === 3) {
        round = 1;
        changeRound();
        document.getElementById('message').innerHTML='Angry Dice send you back to round 1.';
        releaseHold();
    }
    if (round === 1 && die1.val + die2.val === 3) {
        round = 2;
        changeRound();
        releaseHold();
    } else if (round === 2 && (die1.val === 3 || die2.val === 3) && (die1.val === 4 || die2.val === 4) && (die1.val + die2.val === 7)) {
        round = 3;
        changeRound();
        releaseHold();
    } else if (round === 3 && die1.val + die2.val === 11) {
        document.getElementById('message').innerHTML = 'You win!!!';
        changeRound();
        releaseHold();
    }
}

function changeRound() {
    document.getElementById('roundNumber').innerHTML = round.toString();
};

function releaseHold() {
    die1.held = false;
    die2.held = false;
    document.getElementById(die1.id).style.borderColor='black';
    document.getElementById(die2.id).style.borderColor='black';

};

var die1 = new die('die1');
var die2 = new die('die2');

document.getElementById('roll').addEventListener('click', function(e) {e.preventDefault();
    die1.setVal();
    die2.setVal();
    checkRound();
});

var dieDivs = document.getElementsByClassName('dieClick');
// gives us an array of the elements with the class

Array.from(dieDivs).forEach(function (e) {
    e.addEventListener('click', function () {
        if (this.id === 'die1' && !die1.held) {
            die1.held = true;
            this.style.borderColor='blue';
        }
        else if (this.id === "die2" && !die2.held) {
            die2.held = true;
            this.style.borderColor='blue';
        }
        else if (this.id === 'die2' && die2.held) {
            die2.held = false;
            this.style.borderColor='black';
        }
        else if (this.id === 'die1' && die1.held) {
            die1.held = false;
            this.style.borderColor='black';
        }
        console.log(die1.held)
        console.log(die2.held)
    })
});

//
// console.log(die1);
// console.log(die2);

