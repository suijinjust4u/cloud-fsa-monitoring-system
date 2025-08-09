from backend.anomaly_detection.detector import AnomalyDetector

def test_detector():
    detector = AnomalyDetector()
    node_data_normal = {"node_id": "n1", "value": 50, "fault": False}
    node_data_fault = {"node_id": "n1", "value": 5, "fault": True}

    detector.analyze(node_data_normal)
    assert detector.current_states["n1"] == "Normal"

    detector.analyze(node_data_fault)
    assert detector.current_states["n1"] == "Faulted"
