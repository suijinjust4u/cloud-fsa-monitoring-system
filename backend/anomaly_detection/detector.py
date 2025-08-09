class AnomalyDetector:
    def __init__(self):
        self.current_states = {}  # node_id -> state

    def analyze(self, node_data):
        # Simple logic: if fault flag or value below threshold mark as Faulted
        if node_data.get("fault") or node_data.get("value", 0) < 10:
            self.current_states[node_data['node_id']] = "Faulted"
        else:
            # If previously faulted, mark recovering
            prev = self.current_states.get(node_data['node_id'], "Normal")
            if prev == "Faulted":
                self.current_states[node_data['node_id']] = "Recovering"
            else:
                self.current_states[node_data['node_id']] = "Normal"
