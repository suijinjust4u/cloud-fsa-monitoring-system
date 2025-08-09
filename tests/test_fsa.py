import pytest
from backend.fsa.fsa_model import FiniteStateAutomata

def test_fsa_transitions():
    fsa = FiniteStateAutomata()
    node_id = "test_node"

    # Initial state
    assert fsa.get_state(node_id) == "Normal"

    # Valid transition
    fsa.transition(node_id, "Faulted")
    assert fsa.get_state(node_id) == "Faulted"

    # Invalid transition (direct Normal -> Recovering)
    fsa.transition(node_id, "Normal")  # From Faulted only to Recovering or Faulted
    assert fsa.get_state(node_id) == "Faulted"  # State unchanged

    # Valid transition to Recovering
    fsa.transition(node_id, "Recovering")
    assert fsa.get_state(node_id) == "Recovering"

    # Valid transition back to Normal
    fsa.transition(node_id, "Normal")
    assert fsa.get_state(node_id) == "Normal"
