google.charts.load("current", {packages: ["corechart"]});
google.charts.setOnLoadCallback(drawChart);

const trend_data = JSON.parse(
    document.currentScript.dataset.trendData
  );
const trend_chart_element_id = document.currentScript.dataset.chartElementId;

function drawChart() {
    var data = new google.visualization.DataTable();
    data.addColumn('number', 'День');
    data.addColumn('number', 'Баланс');
    data.addRows(trend_data);

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

    var chart_element = document.getElementById(trend_chart_element_id);
    var chart = new google.visualization.ScatterChart(chart_element);
    chart.draw(data, options);
}