# Define states and events for clarity (not used directly here but for extension)

STATES = ["Normal", "Faulted", "Recovering"]

EVENTS = {
    "fault_detected": "Faulted",
    "fault_cleared": "Recovering",
    "recovery_complete": "Normal",
}
