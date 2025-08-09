class FiniteStateAutomata:
    def __init__(self):
        # States per node_id
        self.current_states = {}
        self.transitions = {
            "Normal": ["Normal", "Faulted"],
            "Faulted": ["Recovering", "Faulted"],
            "Recovering": ["Normal", "Faulted"]
        }
    
    def transition(self, node_id, new_state):
        current = self.current_states.get(node_id, "Normal")
        if new_state in self.transitions.get(current, []):
            self.current_states[node_id] = new_state
        # else ignore invalid transitions

    def get_state(self, node_id):
        return self.current_states.get(node_id, "Normal")
