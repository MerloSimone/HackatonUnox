// Fetch data from the server using PHP
async function fetchData() {
    try {
        const response = await fetch('data.php');
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error fetching data:', error);
    }
}

// Process data and create the bar chart
async function createBarChart() {
    const data = await fetchData();

    const categories = data.map(item => item.summary);
    const counts = data.map(item => item.messageCount);

    const ctx = document.getElementById('categoryChart').getContext('2d');

    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: categories,
            datasets: [{
                label: 'Message Count',
                data: counts,
                backgroundColor: 'rgba(75, 192, 192, 0.5)',
                borderColor: 'rgba(75, 192, 192, 1)',
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
}

// Call the function to create the bar chart
createBarChart();
