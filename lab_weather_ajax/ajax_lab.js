/*
Chris converted everything into one data type.
He used the Google maps API to make city and zip into lat/long.
 */

// This comes from JS global objects and built-in functions.

if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(showPosition);
}

function showPosition(pos) {
    var lat = pos.coords.latitude;
    var lon = pos.coords.longitude;
    console.log(lat, lon);
    landingPage(lat, lon)
}


function landingPage(lat, lon) {
    $.ajax({
        url: "http://api.openweathermap.org/data/2.5/weather",
        data: {
            lat: lat,
            lon: lon,
            APPID: '9ef3311b380d2586bf47ff522529e7a9'
        },
        type: "get",
        success: function (response) {
            update_page(response)
        }
    });
}

var select_background = function(vis) {
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
};

var convert_temp = function(temp) {
    var far = (temp * 9/5 - 459.67).toFixed(1);
            var cel = (temp = temp - 273.15).toFixed(1);
            $('#temp').html(far + ' degrees F').append('<br>', cel, ' degrees C')
};

var update_page = function (response) {
        console.log(response);
        var vis = response.weather[0].id.toString();
        select_background(vis);
        $('#returns').html(response.weather[0].main);
        var temp = response.main.temp;
        convert_temp(temp)
};


function searchWeather() {
    $.ajax({
        url: "http://api.openweathermap.org/data/2.5/weather",
        data: {
            q: $('#entry').val(),
            APPID: '9ef3311b380d2586bf47ff522529e7a9'
        },
        type: "get",
        success: function (response) {
            update_page(response)
        }
    });
}


$('#search').click(searchWeather);


