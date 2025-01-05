import time
import json

class AuditTrail:
    def __init__(self):
        self.logs = []

    def log_action(self, action, user_id, details):
        log_entry = {
            "timestamp": time.time(),
            "action": action,
            "user_id": user_id,
            "details": details
        }
        self.logs.append(log_entry)

    def get_logs(self):
        return json.dumps(self.logs, indent=4)

    def __repr__(self):
        return "AuditTrail()"
