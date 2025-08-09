# Cloud-Based FSA‑Driven Intelligent Monitoring System  
_For Renewable Energy‑Powered Distributed Networks_  
_with Ollama (Mistral 7B) AI Integration_

## 📌 Overview
This project is a **full-stack web and AI system** for **real-time monitoring** of distributed renewable energy nodes (solar, wind, hybrid), using:
- **Finite State Automata (FSA)** for modeling node states (Normal, Faulted, Recovering).
- **Simulation module** generating realistic energy and fault data.
- **FastAPI backend** serving REST + WebSocket endpoints for live updates.
- **Frontend dashboard** (HTML/CSS/JS) for visualizing node status, power output charts, and interacting with AI assistant.
- **Ollama Mistral 7B integration** for natural language Q&A about the **live system data**.

---

## 🏗 Features
- **Real-time status updates** via WebSockets.
- **Live power output graph** using Chart.js.
- **Color‑coded node states** (Green: Normal, Orange: Recovering, Red: Faulted).
- **AI Assistant** (Ollama Mistral 7B running locally) to answer questions based on **current system data**.
- Modular Python backend for easy extension to physical IoT devices or database storage.

---

## 📂 Project Structure
cloud-fsa-monitoring-system/
│
├── backend/
│ ├── app.py # FastAPI app (REST + WebSocket)
│ ├── fsa/ # FSA logic
│ │ ├── fsa_model.py
│ │ └── state_definitions.py
│ ├── simulation/ # Data simulators for solar/wind/hybrid
│ │ ├── node_simulator.py
│ │ ├── energy_profiles.py
│ │ └── network_sim.py
│ ├── anomaly_detection/ # Fault/anomaly detection
│ │ └── detector.py
│ ├── utils/
│ │ ├── config.py
│ │ └── ollama_client.py # Ollama integration (Mistral 7B)
│ └── database/ # (Optional) DB models
│
├── frontend/
│ ├── index.html # Dashboard UI
│ ├── styles/style.css # Dashboard styles
│ └── scripts/ # Frontend JS
│ ├── api.js # WebSocket connection
│ ├── graph.js # Live chart rendering
│ └── main.js # UI updates + chat logic
│
├── requirements.txt # Python backend dependencies
└── README.md # This file
text

---

## ⚙️ Requirements

- **Python 3.9+**
- **Ollama installed locally** → [https://ollama.com](https://ollama.com)
- **Mistral 7B model**:
ollama pull mistral:7b
text
- Mac/Linux recommended (tested on macOS).

---

## 📦 Install & Setup

1️⃣ **Clone repository**
git clone <your-github-repo-url>
cd cloud-fsa-monitoring-system
text

2️⃣ **Create Python virtual environment & install dependencies**
python3 -m venv venv
source venv/bin/activate # Mac/Linux
pip install -r requirements.txt
text

3️⃣ **Run Ollama in background**
ollama serve
text

4️⃣ **Verify Mistral 7B model is available**
ollama run mistral:7b "Hello"
text

5️⃣ **Start the backend (FastAPI)**
uvicorn backend.app:app --reload --port 8000
text
➡ This serves:
- WebSocket: `ws://localhost:8000/ws`
- API: `http://localhost:8000`
- API Docs: `http://localhost:8000/docs`

6️⃣ **Start the frontend**
cd frontend
python3 -m http.server 8080
text
➡ Open in browser: `http://localhost:8080`

---

## 💻 Usage

### **Live Dashboard**
- Displays **node status table** (real-time).
- Updates **line chart** with power outputs every 2 seconds.

### **Ask AI (Ollama Chat)**
- Enter natural language questions into the chat input.
- Mistral 7B will respond based on the **current real system data**.
- Examples:
  - "Which nodes are faulted right now?"
  - "Summarize the current network status."
  - "What’s the average output of all nodes?"

---

## 🤖 How Ollama Integration Works

- Backend gathers **latest simulated data** from `NodeSimulator`.
- Passes **formatted data + user question** to `ollama_client.py`.
- Mistral 7B responds, grounded only in the provided real data.
- The response is sent back to the frontend and displayed in the chat log.

---

## 🛠 Troubleshooting

**Problem:** WebSocket errors / data not showing  
**Solution:** Ensure backend is running on `8000` and frontend on another port (e.g., `8080`). Don’t run `python3 -m http.server` on 8000 — that overrides backend.

**Problem:** AI chat says “Error connecting to server”  
**Solution:** Verify `ollama serve` is running and that `mistral:7b` is downloaded.

**Problem:** Chart not updating  
**Solution:** Open browser console (`F12`) → check if payload from `/ws` contains `nodes` and `states`. If not, backend may be crashing.

---

## 🚀 Next Steps / Extensions
- Connect to real IoT sensor data instead of simulation.
- Add historical trend analysis.
- Store logs/events in a database.
- Enhance AI assistant with analytics (e.g., fault prediction).

---

## 📜 License
Your choice (MIT recommended for open use).

---

**Author:** SUJIN S P  
**Location:** TAMIL NADU  
**Specialty:** AI-Integrated Renewable Energy Monitoring Systems
