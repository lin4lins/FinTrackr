google.charts.load("current", {packages:["corechart"]});
google.charts.setOnLoadCallback(drawChart);
function drawChart() {
  var data = google.visualization.arrayToDataTable([
    ['Task', 'Hours per Day'],
    ['Work',     11],
    ['Eat',      2],
    ['Commute',  2],
    ['Watch TV', 2],
    ['Sleep',    7]
  ]);

  var options = {
    title: 'Категорії',
    is3D: true,
    height: 250,
  };

  var chart_element = document.getElementById('income_structure');
  var chart = new google.visualization.PieChart(chart_element);
  chart.draw(data, options);
}