import json
import os

LOG_FILE = "incident_logs.json"


def save_incident(
    question,
    threat,
    severity,
    confidence
):

    incident = {
        "question": question,
        "threat": threat,
        "severity": severity,
        "confidence": confidence
    }

    if os.path.exists(LOG_FILE):

        with open(LOG_FILE, "r") as f:
            logs = json.load(f)

    else:
        logs = []

    logs.append(incident)

    with open(LOG_FILE, "w") as f:
        json.dump(
            logs,
            f,
            indent=4
        )