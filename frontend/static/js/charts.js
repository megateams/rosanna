// donut and bar graph
    //   donut
    document.addEventListener("DOMContentLoaded", function() {
        var donutCtx = document.getElementById("genderDonutChart").getContext("2d");
        var donutData = {
            labels: ["Boys", "Girls"],
            datasets: [{
                data: [65, 35], // Replace with your actual data
                backgroundColor: ["red", "#f9b855"],
            }]
        };
        var donutChart = new Chart(donutCtx, {
            type: "doughnut",
            data: donutData,
            options: {
                responsive: true,
                maintainAspectRatio: false,
                legend: {
                    position: "bottom"
                },
                title: {
                    display: true,
                    text: "Gender Distribution"
                }
            }
        });
        // donut

        // bargraph
        var barCtx = document.getElementById("genderBarChart").getContext("2d");
        var barData = {
            labels: ["Baby", "Middle","Top","P.1", "P.2", "P.3", "P.4", "P.5", "P.6", "P.7"],
            datasets: [{
                label: "Boys",
                data: [20,15,27,30, 35, 40, 45, 50, 55, 60], // Replace with your actual data for boys
                backgroundColor: "blue",
                // borderColor: "rgba(54, 162, 235, 1)",
                borderWidth: 1
            },
            {
                label: "Girls",
                data: [19,32,11,25, 30, 35, 40, 45, 50, 55], // Replace with your actual data for girls
                backgroundColor: "green",
                // borderColor: "rgba(255, 99, 132, 1)",
                borderWidth: 1
            }]
        };
        var barChart = new Chart(barCtx, {
            type: "bar",
            data: barData,
            options: {
                responsive: true,
                maintainAspectRatio: false,
                scales: {
                    x: {
                        grid: {
                            display: false
                        }
                    },
                    y: {
                        beginAtZero: true,
                        grid: {
                            color: "rgba(0,0,0,0.1)"
                        },
                        ticks: {
                            stepSize: 10
                        }
                    }
                },
                plugins: {
                    legend: {
                        position: "top"
                    },
                    title: {
                        display: true,
                        text: "Gender Distribution by Class"
                    }
                }
            }
        });
        // bargraph
    });  
// donut and bar graph

// line graph
document.addEventListener("DOMContentLoaded", function() {
    var ctx = document.getElementById("paymentChart").getContext("2d");
    var paymentData = {
      labels: ["February", "March", "April", "May"],
      datasets: [{
        label: "Payments",
        data: [1500, 2000, 1800, 2300], // Replace with your actual payment data
        fill: false,
        borderColor: "#007",
        borderWidth: 1,
        pointBackgroundColor: "#fff",
        pointRadius: 4,
        pointHoverRadius: 6
      },
      {
        label: "Fees",
        data: [700, 1300, 2800, 4000], // Replace with your actual payment data
        fill: false,
        borderColor: "#0f0",
        borderWidth: 1,
        pointBackgroundColor: "#fff",
        pointRadius: 4,
        pointHoverRadius: 6
      },
      {
        label: "Expenses",
        data: [900, 1000, 1500, 2900], // Replace with your actual payment data
        fill: false,
        borderColor: "#f00",
        borderWidth: 1,
        pointBackgroundColor: "#fff",
        pointRadius: 4,
        pointHoverRadius: 6
      }]
    };
    var paymentChart = new Chart(ctx, {
      type: "line",
      data: paymentData,
      options: {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
          x: {
            grid: {
              display: false
            }
          },
          y: {
            beginAtZero: true,
            grid: {
              color: "#999"
            },
            ticks: {
              stepSize: 500
            }
          }
        },
        plugins: {
          legend: {
            position: "top"
          },
          title: {
            display: true,
            color: 'black',
            text: "Payment Overview"
          }
        }
      }
    });
  });
// line graph
