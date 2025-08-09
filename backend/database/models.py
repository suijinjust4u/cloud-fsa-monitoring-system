# Minimal dummy DB models using dataclasses
from dataclasses import dataclass
from datetime import datetime

@dataclass
class NodeStatus:
    node_id: str
    state: str
    last_updated: datetime

@dataclass
class FaultEvent:
    node_id: str
    fault_time: datetime
    fault_type: str
