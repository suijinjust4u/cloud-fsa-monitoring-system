const WS_URL = "ws://localhost:8000/ws";

class API {
  constructor() {
    this.ws = null;
    this.callbacks = [];
  }

  connect() {
    console.log("Connecting to WebSocket:", WS_URL);
    this.ws = new WebSocket(WS_URL);

    this.ws.onopen = () => {
      console.log("WebSocket connection opened.");
    };

    this.ws.onmessage = (event) => {
      try {
        const data = JSON.parse(event.data);
        this.callbacks.forEach((cb) => cb(data));
      } catch (e) {
        console.error("Error parsing message:", e);
      }
    };

    this.ws.onclose = () => {
      console.log("WebSocket connection closed. Reconnecting in 3s...");
      setTimeout(() => this.connect(), 3000);
    };

    this.ws.onerror = (e) => {
      console.error("WebSocket error: ", e);
    };
  }

  subscribe(callback) {
    this.callbacks.push(callback);
  }
}

const api = new API();
api.connect();
