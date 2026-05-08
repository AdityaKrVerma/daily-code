## Create day06_alert_class.py with an Alert class
## containing id, severity, message, and a display() method.

class Alert:

    def __init__(self, id, severity, message):
        self.id = id
        self.severity = severity
        self.message = message

    def display(self):
        print(f"ID: {self.id}, Severity: {self.severity}, Message: {self.message}")

if __name__ == "__main__":
    alerts = [
        Alert(1, "Medium", "High CPU Usage"),
        Alert(2, "Low", "Connected display incompatible"),
        Alert(3, "High", "Unauthorized access")
    ]

    for alert in alerts:
        alert.display()