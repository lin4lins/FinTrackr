google.charts.load('current', {packages: ['corechart', 'line']});
google.charts.setOnLoadCallback(drawBasic);

function drawBasic() {

      var data = new google.visualization.DataTable();
      data.addColumn('number', 'Day');
      data.addColumn('number', 'Amount');

      data.addRows([
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
        [24, 12.8],
        [26,  5.3],
        [30,  6.6],
        [30,  64.8],
        [31,  42.2]
      ]);

      var options = {

        hAxis: {
          title: 'Day',
          minValue: 1,
          maxValue: 31
        },
        vAxis: {
          title: 'Balance',
          minValue: 0
        },
        legend: { position: 'none' },
        height: 250,

      };

      var chart = new google.visualization.LineChart(document.getElementById('home_balance'));

      chart.draw(data, options);
    }