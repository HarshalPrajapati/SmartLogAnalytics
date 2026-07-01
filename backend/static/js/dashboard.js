let pieChart;
let barChart;

async function loadCharts() {

    const response = await fetch("/api/chart-data");
    const data = await response.json();
    document.getElementById("lastUpdated").textContent = "Last Updated: " + new Date().toLocaleTimeString();

    if (pieChart) {
        pieChart.destroy();
    }

    if (barChart) {
        barChart.destroy();
    }

    pieChart = new Chart(
        document.getElementById("pieChart"),
        {
            type: "pie",
            data: {
                labels: data.labels,
                datasets: [{
                    data: data.counts,
                    backgroundColor: [
                        "#198754",
                        "#ffc107",
                        "#dc3545"
                    ]
                }]
            },
            options: {
                responsive: true,
                plugins: {
                    legend: {
                        position: "bottom"
                    }
                }
            }
        }
    );

    barChart = new Chart(
        document.getElementById("barChart"),
        {
            type: "bar",
            data: {
                labels: data.labels,
                datasets: [{
                    label: "Log Count",
                    data: data.counts,
                    backgroundColor: [
                        "#198754",
                        "#ffc107",
                        "#dc3545"
                    ]
                }]
            },
            options: {
                responsive: true,
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        }
    );
}

loadCharts();

// Refresh every 30 seconds
setInterval(loadCharts, 30000);