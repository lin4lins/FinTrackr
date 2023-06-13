google.charts.load('current', {packages: ['corechart', 'bar']});
google.charts.setOnLoadCallback(drawCashFlow);

const cash_flow_data = JSON.parse(
    document.currentScript.dataset.cashFlowData
  );
const cash_flow_chart_element_id = document.currentScript.dataset.chartElementId;

function drawCashFlow() {
    var data = google.visualization.arrayToDataTable(cash_flow_data);

    var view = new google.visualization.DataView(data);
    view.setColumns([0, 1,
                     { calc: "stringify",
                       sourceColumn: 1,
                       type: "string",
                       role: "annotation" },
                     2]);

    var options = {
      hAxis: {
        title: '',
        minValue: 0,
      },
      bar: {groupWidth: "80%"},
      legend: { position: "none" },
      height: 250,

    };

    var chart_element = document.getElementById(cash_flow_chart_element_id);
    var chart = new google.visualization.BarChart(chart_element);
    chart.draw(view, options);
}