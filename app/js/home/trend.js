google.charts.load("current", {packages: ["corechart"]});
google.charts.setOnLoadCallback(drawChart);

function drawChart() {
    var data = google.visualization.arrayToDataTable([
        ['День', 'Баланс'],
        [1,  37.8],
        [2,  30.9],
        [3,  25.4],
        [4,  11.7],
        [5,  11.9],
        [6,   8.8],
        [7,   7.6],
        [8,  12.3],
        [9,  16.9],
        [10, 12.8],
        [11,  5.3],
        [12,  6.6],
        [13,  64.8],
        [14,  42.2],
        [21,  16.9],
        [26,  20.8],
        [27,  32.6],
    ]);

    var options = {
        title: '',
        legend: 'none',
        crosshair: {trigger: 'both', orientation: 'both'},
        trendlines: {
            0: {
                type: 'polynomial',
                degree: 2,
                visibleInLegend: true,
            }
        },
        hAxis: {
          title: 'День',
          minValue: 1,
        },
        vAxis: {
          title: 'Баланс',
          minValue: 0
        },
        height: 250
    };

    var chart_element = document.getElementById('polynomial_trend');
    var chart = new google.visualization.ScatterChart(chart_element);
    chart.draw(data, options);
}