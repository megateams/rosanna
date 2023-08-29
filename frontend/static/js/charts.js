// donut and bar graph
    //   donut
    // document.addEventListener("DOMContentLoaded", function() {
        
        
        // donut
        

        // bargraph
        
        // bargraph
    // });  
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
            },
            ticks: {
              color:"black",
            }
          },
          y: {
            beginAtZero: true,
            grid: {
              color: "#999"
            },
            ticks: {
              stepSize: 500,
              color: "black",
            }
          }
        },
        plugins: {
          legend: {
            position: "top",
            labels: {
              color: "black"
            }
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


