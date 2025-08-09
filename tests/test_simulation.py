from backend.simulation.node_simulator import NodeSimulator

def test_simulate_data():
    sim = NodeSimulator()
    data = sim.generate_data()
    assert isinstance(data, list)
    assert len(data) > 0
    for d in data:
        assert "node_id" in d
        assert "value" in d
        assert "fault" in d
