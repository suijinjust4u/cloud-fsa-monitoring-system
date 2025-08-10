# Cloud-Based FSA‑Driven Intelligent Monitoring System  
_For Renewable Energy‑Powered Distributed Networks_  
_with Ollama (Mistral 7B) AI Integration_

## 📌 Overview
This is a **full-stack intelligent monitoring platform** for distributed renewable energy networks.  
It includes:

- **Finite State Automata (FSA)** to model operational states of each energy node (Normal, Faulted, Recovering)
- **Simulation** of solar, wind, and hybrid node output with random faults
- **FastAPI backend** serving REST & WebSocket data feeds
- **Frontend dashboard** (HTML/CSS/JavaScript + Chart.js)
- **Ollama (Mistral 7B)** for **natural language Q&A** grounded in **live system data**

---

## 🏗 Features
- **Real-time WebSocket updates** of node status and power output.
- **Live line chart** using Chart.js.
- **Ollama-powered AI assistant** for natural language queries about the network.
- Simulation easily replaceable with **real IoT data**.

---

## 📂 Project Structure
cloud-fsa-monitoring-system/
│
├── backend/
│ ├── app.py # FastAPI app (REST + WebSocket endpoints)
│ ├── fsa/ # Core FSA logic
│ ├── simulation/ # Data simulation modules
│ ├── anomaly_detection/ # Real-time anomaly detection
│ ├── utils/ollama_client.py # Ollama integration
│ └── database/ # Optional DB models
│
├── frontend/
│ ├── index.html
│ ├── styles/style.css
│ └── scripts/ # JS: api.js, graph.js, main.js
│
├── requirements.txt
└── README.md
text

---

## ⚙️ Requirements
- **Python 3.9+**
- **Ollama** installed locally → [https://ollama.com](https://ollama.com)
- **Mistral 7B model** pulled locally:
ollama pull mistral:7b
text

---

## 📦 Installation

1️⃣ **Clone repo**
git clone <your-repo-url>
cd cloud-fsa-monitoring-system
text

2️⃣ **Set up Python environment**
python3 -m venv venv
source venv/bin/activate # On Mac/Linux
pip install -r requirements.txt
text

3️⃣ **Start Ollama**
ollama serve
text

---

## ▶️ Running the System

### **Step 1 — Start Backend API (FastAPI)**
From the project root:
uvicorn backend.app:app --reload --host 0.0.0.0 --port 8000
text
- `--reload` → automatically reload on code changes
- `--host 0.0.0.0` → accessible on LAN if needed
- Backend docs: [http://localhost:8000/docs](http://localhost:8000/docs)
- WebSocket: `ws://localhost:8000/ws`

---

### **Step 2 — Serve Frontend**
In a **new terminal**, from the `frontend` folder:
cd frontend
python3 -m http.server 8080
text
Now open: [http://localhost:8080](http://localhost:8080)

---

### **Step 3 — Using the Dashboard**
- **Live Table**: Node IDs, operational states, power output
- **Live Graph**: Power output plotted over time
- **Chatbox**: Ask the AI assistant questions about the current network  
  (Model: `mistral:7b` running locally in Ollama)

Example questions:
Which nodes are faulted right now?
Summarize the current network status.
text

---

## 🛠 Troubleshooting
**WebSocket errors / No live updates**  
→ Ensure backend is running on port `8000` and frontend is on `8080`.

**AI Chat shows “Error connecting to server”**  
→ Ensure `ollama serve` is running and `mistral:7b` is installed.

**Chart not updating**  
→ Open browser DevTools → Console → check payloads from `/ws`.

---

## 💬 Example Full Run Commands

Terminal 1: Run Ollama
ollama serve
Terminal 2: Start FastAPI backend
uvicorn backend.app:app --reload --host 0.0.0.0 --port 8000
Terminal 3: Serve frontend
cd frontend
python3 -m http.server 8080
text

---

## 🚀 Extend & Customize
- Replace simulation with live sensor/IoT devices
- Store historical data in a database
- Extend Ollama prompt for advanced analytics

---

**Author:** _[Your Name]_  
**Location:** Bengaluru  
**Specialty:** AI-Integrated Renewable Energy Monitoring Systems
