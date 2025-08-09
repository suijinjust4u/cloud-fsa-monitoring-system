const tableBody = document.querySelector("#node-table tbody");

// Subscribe to live backend data and update dashboard
api.subscribe(updateDashboard);

function updateDashboard(payload) {
  // For debugging, you can uncomment:
  // console.log("Dashboard data:", payload);

  if (!payload || !payload.nodes || !payload.states) {
    console.warn("Invalid payload structure:", payload);
    return;
  }

  const { nodes, states } = payload;

  tableBody.innerHTML = "";

  nodes.forEach((node) => {
    const tr = document.createElement("tr");
    const status = states[node.node_id] || "Unknown";

    // Color code status text
    let color = "green";
    if (status === "Faulted") color = "red";
    else if (status === "Recovering") color = "orange";

    tr.innerHTML = `
      <td>${node.node_id}</td>
      <td style="color: ${color}">${status}</td>
      <td>${node.value} kW</td>
    `;

    tableBody.appendChild(tr);
  });

  updateChart(nodes);
}

/* ------- Ollama Chat Functionality ------- */

const chatLog = document.getElementById("chat-log");
const chatInput = document.getElementById("chat-input");
const sendChatBtn = document.getElementById("send-chat");

sendChatBtn.onclick = async function () {
  const question = chatInput.value.trim();
  if (!question) return;
  appendChat("You", question);
  chatInput.value = "";
  appendChat("Ollama", "...");

  try {
    // Adjust URL if backend is on a different host/port
    const response = await fetch("http://localhost:8000/ollama-query", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ query: question }),
    });

    const data = await response.json();
    chatLog.lastChild.innerHTML = `<b>Ollama:</b> ${data.response || data.error}`;
    chatLog.scrollTop = chatLog.scrollHeight; // Scroll to bottom
  } catch (error) {
    chatLog.lastChild.innerHTML =
      "<b>Ollama:</b> Error connecting to server.";
  }
};

function appendChat(sender, message) {
  const div = document.createElement("div");
  div.innerHTML = `<b>${sender}:</b> ${message}`;
  chatLog.appendChild(div);
  chatLog.scrollTop = chatLog.scrollHeight; // Scroll to bottom
}
