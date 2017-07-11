$('.ui.checkbox').checkbox();

$(document).on('change', '[type="checkbox"]', function() {
    var food = $(this).val();
    console.log(food);
    if ($(this).is(':checked')) {
        $('ul').append("<li class=item id=" + food + ">" + food + "</li>");
        console.log("hey");
}   if (!$(this).is(':checked')) {
        $('[id=' + food + ']').remove();
        console.log('yo');
    }
});

//It doesn't seem like you can put a click event on a checkbox

class="error"
#error-message