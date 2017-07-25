/**
 * Created by jennamtucker on 7/18/17.
 */

$(document).on('click', '.int', function(event){
    event.preventDefault();

    $('html, body').animate({
        scrollTop: $( $.attr(this, 'href') ).offset().top
    }, 500);
});