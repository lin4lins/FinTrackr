google.charts.load("current", {packages:["corechart"]});
google.charts.setOnLoadCallback(drawChart);

const expense_structure_data = JSON.parse(
    document.currentScript.dataset.expenseStructureData
  );
const expense_chart_element_id = document.currentScript.dataset.chartElementId;

function drawChart() {
  var data = google.visualization.arrayToDataTable(expense_structure_data);

  var options = {
    title: 'Категорії',
    is3D: true,
    height: 250,
  };

  var chart_element = document.getElementById(expense_chart_element_id);
  var chart = new google.visualization.PieChart(chart_element);
  chart.draw(data, options);
}