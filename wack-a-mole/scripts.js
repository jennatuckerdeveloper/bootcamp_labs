function play() {
    for (i = 1; i <= 16; i++) {
        var img = '<img class="hole" src="hole.jpg"/>';
        img = $(img).attr("id", "mole" + i);
        $('#ground').append(img);
    }
};

play();

var timer;
var t = 1000;

timer = setInterval(game, t);

var score = 0;
$('#number').html(score);
lst = [];

function game () {
    var holeZ = $('#ground').children('.hole');
    var mole = Math.floor(Math.random() * holeZ.length);
    var mle = $(holeZ[mole]);
    mle.attr("src", "mole.jpg").attr("class", "mole");
    // console.log(holeZ);
    // console.log(holeZ.length)
    if (holeZ.length === 0) {
        clearInterval(timer);
        alert("End of Game!  Your score is: " + score)
    }

     // Chris used this syntax to print readable objects from a list of objects:
    // $.each(lst, function (i, o){
    //     console.log($(o))
    // })
};


$('img').click(function () {
    if ($(this).attr("src") === "mole.jpg") {
        $(this).attr("src", "hole.jpg").attr("class", "hole");
        score = score + 10;
        $('#number').html(score);
        var lst_loc = lst.indexOf(this);
        lst.splice(lst_loc, 1);
    }
    $('#ground').css("border", "none");
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
    clearInterval(timer);
    for (i = 1; i <= 16; i++) {
        var mole = i;
        $('#mole' + mole).attr("src", "hole.jpg").attr("class", "hole");
    }
    ;
    $('#ground').css("border", "none");
    score = 0;
    $('#number').html(score);
    t = 1000;
    timer = setInterval(game, t);
    lst = [];

});


// Chris took the function out of the setInvertal and made
// it a variable, so that portion could also be reused.
