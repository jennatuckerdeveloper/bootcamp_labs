function play() {
    for (i = 1; i <= 16; i++) {
        var img = '<img src="hole.jpg"/>';
        img = $(img).attr("id", "mole" + i);
        $('#ground').append(img);
    }
};

play();

var timer;
var t = 1000;

timer = setInterval(game, t);

var board = [];
var score = 0;
$('#number').html(score);

function game () {
    var mole = Math.floor(Math.random() * 16) + 1;
    $('#mole' + mole).attr("src", "mole.jpg");
    board.push($('#mole' + mole));

};

// Chris used this to print readable objects from game:
// $.each(board, function (i, o){
//     console.log($(o))
// })

$('img').click(function () {
    if ($(this).attr("src") === "mole.jpg") {
        $(this).attr("src", "hole.jpg");
        score = score + 10;
        $('#number').html(score);
        
    }
;

    clearInterval(timer);
    t = t - 20;
    timer = setInterval(game, t);
});

$('#stop').click(function() {
    clearInterval(timer);
    $('#ground').css("border", "solid 4px").css("border-color", "black");

});

$('#start').click(function() {
    t = 1000;
    timer = setInterval(game, t);
    for (i=1; i<=16; i++) {
        var mole = i;
        $('#mole' + mole).attr("src", "hole.jpg");
    }
    $('#ground').css("border", "none");
});




// Chris took the function out of the setInvertal and made
// it a variable, so that portion could also be reused.

// If all 16 divs are mole pics, end game, present message
// Do not change a picture of a mole to a mole
