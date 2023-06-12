google.charts.load('current', {packages: ['corechart', 'line']});
google.charts.setOnLoadCallback(drawBasic);

const balance_dynamics_data = JSON.parse(
    document.currentScript.dataset.balanceDynamicsData
  );
const balance_dynamics_chart_element_id = document.currentScript.dataset.chartElementId;


function drawBasic() {
    var data = new google.visualization.DataTable();
    data.addColumn('number', 'День');
    data.addColumn('number', 'Баланс');

    data.addRows(balance_dynamics_data);

    var options = {

    hAxis: {
      title: 'День',
      minValue: 1,
      maxValue: 31
    },
    vAxis: {
      title: 'Баланс',
      minValue: 0
    },
    legend: { position: 'none' },
    height: 250,

    };

    var chart_element = document.getElementById(balance_dynamics_chart_element_id);
    var chart = new google.visualization.LineChart(chart_element);
    chart.draw(data, options);
}