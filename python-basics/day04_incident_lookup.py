## Create day04_incident_lookup.py that 
## maps incident IDs to status strings using a dictionary

incident_map = {
    "INC001":"Open",
    "INC002":"Closed",
    "INC003":"Resolved",
    "INC004":"In Progress"
}

def get_incident_status(incident):
    return incident_map.get(incident, "Incident not found")

current_id = "INC003"
status = get_incident_status(current_id)

print(f"Incident {current_id} status: {status}")
print(f"Incident INC008 status: {get_incident_status("INC008")}")