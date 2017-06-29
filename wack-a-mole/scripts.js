for (i = 1; i <= 16; i++) {
    var img = '<img src="hole.jpg"/>';
    img = $(img).attr("id", "mole" + i);
    $('#ground').append(img);
};

var timer;
var t = 1000;

timer = setInterval(game, t);

function game () {
    var mole = Math.floor(Math.random() * 16) + 1;
    $('#mole' + mole).attr("src", "mole.jpg");
};

$('img').click(function () {
    $(this).attr("src", "hole.jpg");
    clearInterval(timer);
    t = t - 20;
    timer = setInterval(game, t);
    console.log(t);
});

// Chris took the function out of the setInvertal and made
// it a variable, so that portion could also be reused.

