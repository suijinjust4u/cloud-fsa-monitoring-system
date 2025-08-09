import random
from backend.simulation.energy_profiles import solar_profile, wind_profile, hybrid_profile
import time

class NodeSimulator:
    def __init__(self):
        self.node_ids = ["node_1", "node_2", "node_3"]
        self.counter = 0
    
    def generate_data(self):
        # Each node gets a profile + some noise, randomly introduce fault every 10 cycles
        self.counter += 1
        data = []
        for node_id in self.node_ids:
            if self.counter % 10 == 0:
                fault = True
            else:
                fault = False
            profile = random.choice([solar_profile, wind_profile, hybrid_profile])
            value = profile() + (random.random() - 0.5) * 10
            node_data = {
                "node_id": node_id,
                "timestamp": int(time.time()),
                "value": max(0, round(value, 2)),
                "fault": fault
            }
            data.append(node_data)
        return data
