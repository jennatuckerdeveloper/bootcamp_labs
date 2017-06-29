$('#add').click(function () {
    tditem = $('#todo').val();
    $('#tdlist').append('<li></li>');
    $('li:last').append('<input class="checkbox" type="checkbox">');
    $('li:last').append(document.createTextNode(tditem));
});

