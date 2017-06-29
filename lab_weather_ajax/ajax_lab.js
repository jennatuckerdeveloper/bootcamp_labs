function searchWeather() {
    $.ajax({
        url: "http://api.openweathermap.org/data/2.5/weather",
        data: {
            q: $('#entry').val(),
            APPID: '9ef3311b380d2586bf47ff522529e7a9'
        },
        dataType: "jsonp",
        type: "post",
        success: function (data) {
            console.log(data);
            var vis = data.weather[0].id.toString();
            if (vis === '803' || vis === '804') {
                $('#icon').html('<img src="8034.png"/>');
                $('#content').css('background-image', 'url(' + "80x.jpg" + ')');
            } else if (vis === '800') {
                $('#icon').html('<img src="800.png"/>');
                $('#content').css('background-image', 'url(' + "800.jpg" + ')');
            } else if (vis === '801') {
                $('#icon').html('<img src="801.png"/>');
                $('#content').css('background-image', 'url(' + "80x.jpg" + ')');
            } else if (vis === '802') {
                $('#icon').html('<img src="802.png"/>');
                $('#content').css('background-image', 'url(' + "80x.jpg" + ')');
            } else if (vis.slice(0, 1) === '3') {
                $('#icon').html('<img src="300.png"/>');
                $('#content').css('background-image', 'url(' + "300400.jpg" + ')');
            } else if (vis.slice(0, 1) === '5') {
                $('#icon').html('<img src="500.png"/>');
                $('#content').css('background-image', 'url(' + "300400.jpg" + ')');
            } else if (vis.slice(0, 1) === '2') {
                $('#icon').html('<img src="200.png"/>');
                $('#content').css('background-image', 'url(' + "200.jpg" + ')');
            } else if (vis.slice(0, 1) === '6') {
                $('#icon').html('<img src="600.png"/>');
                $('#content').css('background-image', 'url(' + "600.jpg" + ')');
            } else if (vis.slice(0, 1) === '7') {
                $('#icon').html('<img src="700.png"/>');
                $('#content').css('background-image', 'url(' + "700.jpg" + ')');
            }
            $('#returns').html(data.weather[0].main)
        }
    });
}



function searchWeatherZ() {
    $.ajax({
        url: "http://api.openweathermap.org/data/2.5/weather",
        data: {
            zip: $('#entry').val(),
            APPID: '9ef3311b380d2586bf47ff522529e7a9'
        },
        dataType: "jsonp",
        type: "post",
        success: function (data) {
            console.log(data);
            var vis = data.weather[0].id.toString();
            if (vis === '803' || vis === '804') {
                $('#icon').html('<img src="8034.png"/>');
                $('#content').css('background-image', 'url(' + "80x.jpg" + ')');
            } else if (vis === '800') {
                $('#icon').html('<img src="800.png"/>');
                $('#content').css('background-image', 'url(' + "800.jpg" + ')');
            } else if (vis === '801') {
                $('#icon').html('<img src="801.png"/>');
                $('#content').css('background-image', 'url(' + "80x.jpg" + ')');
            } else if (vis === '802') {
                $('#icon').html('<img src="802.png"/>');
                $('#content').css('background-image', 'url(' + "80x.jpg" + ')');
            } else if (vis.slice(0, 1) === '3') {
                $('#icon').html('<img src="300.png"/>');
                $('#content').css('background-image', 'url(' + "300400.jpg" + ')');
            } else if (vis.slice(0, 1) === '5') {
                $('#icon').html('<img src="500.png"/>');
                $('#content').css('background-image', 'url(' + "300400.jpg" + ')');
            } else if (vis.slice(0, 1) === '2') {
                $('#icon').html('<img src="200.png"/>');
                $('#content').css('background-image', 'url(' + "200.jpg" + ')');
            } else if (vis.slice(0, 1) === '6') {
                $('#icon').html('<img src="600.png"/>');
                $('#content').css('background-image', 'url(' + "600.jpg" + ')');
            } else if (vis.slice(0, 1) === '7') {
                $('#icon').html('<img src="700.png"/>');
                $('#content').css('background-image', 'url(' + "700.jpg" + ')');
            }
            $('#returns').html(data.weather[0].main);
        }
    });
}



$('#search').click(searchWeather);
$('#searchz').click(searchWeatherZ);


