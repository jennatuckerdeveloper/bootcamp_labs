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
            $('#returns').html(data.weather[0].main)
        }
    });
}

function searchWeatherZ() {
    $.ajax({
        url: "http://api.openweathermap.org/data/2.5/weather",
        data: {
            q: $('#entryz').val(),
            APPID: '9ef3311b380d2586bf47ff522529e7a9'
        },
        dataType: "jsonp",
        type: "post",
        success: function (data) {
            $('#returns').html(data.weather[0].main)
        }
    });
}


$('#search').click(searchWeather);
$('#searchz').click(searchWeatherZ);
