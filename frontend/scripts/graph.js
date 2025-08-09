let ctx = document.getElementById("powerChart").getContext("2d");
let powerChart = null;

// Initialize the chart with datasets for each node ID
function initChart(nodeIds) {
  const datasets = nodeIds.map((nid) => ({
    label: nid,
    data: [],
    fill: false,
    borderColor: getRandomColor(),
    tension: 0.1,
  }));

  powerChart = new Chart(ctx, {
    type: "line",
    data: {
      labels: [],
      datasets: datasets,
    },
    options: {
      animation: false,
      responsive: true,
      scales: {
        x: {
          type: "category", // Using category axis with string labels
          title: {
            display: true,
            text: "Time",
          },
        },
        y: {
          beginAtZero: true,
          title: { display: true, text: "Power Output (kW)" },
        },
      },
      plugins: {
        legend: {
          display: true,
          position: "top",
        },
      },
    },
  });
}

// Update the chart with new data from each simulation tick
function updateChart(nodes) {
  // Initialize chart once, using the current node IDs as dataset labels
  if (!powerChart) {
    initChart(nodes.map((node) => node.node_id));
  }

  if (nodes.length === 0) {
    return;
  }

  const timeLabel = new Date(nodes[0].timestamp * 1000).toLocaleTimeString();

  // Maintain fixed number of visible points (e.g., last 20)
  if (powerChart.data.labels.length >= 20) {
    powerChart.data.labels.shift();
    powerChart.data.datasets.forEach((ds) => ds.data.shift());
  }

  powerChart.data.labels.push(timeLabel);

  nodes.forEach((node) => {
    let dataset = powerChart.data.datasets.find((ds) => ds.label === node.node_id);
    if (dataset) {
      dataset.data.push(node.value);
    }
  });

  powerChart.update();
}

// Helper to generate random colors for each line/dataset
function getRandomColor() {
  const letters = "0123456789ABCDEF";
  let color = "#";
  for (let i = 0; i < 6; i++) {
    color += letters[Math.floor(Math.random() * 16)];
  }
  return color;
}
