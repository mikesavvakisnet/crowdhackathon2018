
// Ajax Temp, Hum, Air Quality
setInterval(function(){
    $.ajax({
        url: '/api/sensit',
        method: 'get',

        success: function (data) {
            $("#tempValue").html( data.temp );
            $("#humValue").html( data.hum );
            $("#airQValue").html( data.airQ );
        }
    });
},1000);

// Charts
$.ajax({
    url: '/api/sensit/temp/average',
    method: 'get',

    success: function (data) {
        // Charts
        dataDailySalesChart = {
            labels: ['M', 'T', 'W', 'T', 'F', 'S', 'S'],
            series: [
                [   data.monday,
                    data.tuesday,
                    data.wednesday,
                    data.thursday,
                    data.friday,
                    data.saturday,
                    data.sunday
                ]
            ]
        };

        optionsDailySalesChart = {
            lineSmooth: Chartist.Interpolation.cardinal({
                tension: 0
            }),
            low: 0,
            high: 40, // creative tim: we recommend you to set the high sa the biggest value + something for a better look
            chartPadding: {
                top: 0,
                right: 0,
                bottom: 0,
                left: 0
            },
        }

        new Chartist.Line('#dailySalesChart', dataDailySalesChart, optionsDailySalesChart);

        $("#avgTemp").html( data.last );
    }
});

// Charts
$.ajax({
    url: '/api/sensit/hum/average',
    method: 'get',

    success: function (data) {
        // Charts
        var dataWebsiteViewsChart = {
            labels: ['J', 'F', 'M', 'A', 'M', 'J', 'J', 'A', 'S', 'O', 'N', 'D'],
            series: [
                [
                    data.january,
                    data.february,
                    data.march,
                    data.april,
                    data.may,
                    data.june,
                    data.july,
                    data.august,
                    data.september,
                    data.october,
                    data.november,
                    data.december
                ]
            ]

        };
        var optionsWebsiteViewsChart = {
            axisX: {
                showGrid: false
            },
            low: 0,
            high: 100,
            chartPadding: {
                top: 0,
                right: 5,
                bottom: 0,
                left: 0
            }
        };
        var responsiveOptions = [
            ['screen and (max-width: 640px)', {
                seriesBarDistance: 5,
                axisX: {
                    labelInterpolationFnc: function(value) {
                        return value[0];
                    }
                }
            }]
        ];
        Chartist.Bar('#websiteViewsChart', dataWebsiteViewsChart, optionsWebsiteViewsChart, responsiveOptions);

        $("#avgHum").html( data.last );
    }
});

// Light Lamp
setInterval(function(){
    $.ajax({
        url: '/api/sensit/lightlamp',
        method: 'get',

        success: function (data) {
            $("#lightValue").html( data.status );
        }
    });
},1000);

// Nodes Status
setInterval(function(){
    $.ajax({
        url: '/api/sensit/nodes',
        method: 'get',

        success: function (data) {
            $("#batteryValue").html( data.battery );
            $("#trustValue").html( data.trust );
            $("#locValue").html( data.loc )
        }
    });
},1000);