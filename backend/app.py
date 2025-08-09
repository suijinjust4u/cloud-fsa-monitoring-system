from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from backend.fsa.fsa_model import FiniteStateAutomata
from backend.simulation.node_simulator import NodeSimulator
from backend.anomaly_detection.detector import AnomalyDetector
from backend.utils.ollama_client import ask_ollama_with_data

import asyncio

app = FastAPI()

# Enable CORS for frontend client on any origin (customize for production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_methods=["*"],
    allow_headers=["*"],
)

fsa = FiniteStateAutomata()
simulator = NodeSimulator()
detector = AnomalyDetector()
connected_websockets = []

@app.get("/")
async def root():
    return {"message": "FSA-based Renewable Energy Monitoring API"}

@app.get("/simulate")
async def simulate():
    data = simulator.generate_data()
    for node_data in data:
        detector.analyze(node_data)
        fsa.transition(node_data['node_id'], detector.current_states.get(node_data['node_id'], "Normal"))
    return {"nodes": data}

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    connected_websockets.append(websocket)
    try:
        while True:
            data = simulator.generate_data()
            for node_data in data:
                detector.analyze(node_data)
                state = detector.current_states.get(node_data['node_id'], "Normal")
                fsa.transition(node_data['node_id'], state)
            await websocket.send_json({
                "nodes": data,
                "states": fsa.current_states
            })
            await asyncio.sleep(2)
    except WebSocketDisconnect:
        connected_websockets.remove(websocket)

class OllamaRequest(BaseModel):
    query: str

@app.post("/ollama-query")
async def ollama_query(request: OllamaRequest):
    """
    Process user question, gather current node data + state, and send it to Ollama for grounded reply.
    """
    try:
        # Generate the latest node data snapshot
        data = simulator.generate_data()
        
        # Update detector and FSA states based on latest data
        for node_data in data:
            detector.analyze(node_data)
            state = detector.current_states.get(node_data['node_id'], "Normal")
            fsa.transition(node_data['node_id'], state)
        
        fsa_data = {
            "nodes": data,
            "states": fsa.current_states.copy()
        }
        
        answer = ask_ollama_with_data(request.query, fsa_data)
        return {"response": answer}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
