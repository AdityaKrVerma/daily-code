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
    alert = Alert(1, "Medium", "High CPU Usage")
    alert.display()