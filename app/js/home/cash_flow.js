google.charts.load('current', {packages: ['corechart', 'bar']});
google.charts.setOnLoadCallback(drawMultSeries);

function drawMultSeries() {
    var data = google.visualization.arrayToDataTable([
       ['Type', 'Value', { role: 'style' }],
       ['Income', 219.45, '#28CB7C' ],
       ['Expense', 196.30, '#E74C3C'],
    ]);

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
      bar: {groupWidth: "75%"},
      legend: { position: "none" },
      height: 250,

    };

    var chart = new google.visualization.BarChart(document.getElementById('home_cash_flow'));
    chart.draw(view, options);
}