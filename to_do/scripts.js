$('#add').click(function () {
    tditem = $('#todo').val();
    $('#tdlist').append('<li></li>');
    $('li:last').append(document.createTextNode(tditem));
});

