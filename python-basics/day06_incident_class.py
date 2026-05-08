import day06_alert_class

class Incident:
    def __init__(self, id, name, owner, status):
        self.incident_id = id
        self.service_name = name
        self.owner = owner
        self.status = status

    def display(self):
        print(f"Incident ID:{self.incident_id}, Service:{self.service_name}, Owner:{self.owner}, Status:{self.status}")

if __name__=="__main__":
    incident = Incident("INC001","Authentication Service","Aidan","Open")
    incident.display()