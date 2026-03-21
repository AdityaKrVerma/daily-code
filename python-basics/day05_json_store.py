## Create day05_json_store.py that 
## writes a small dictionary to JSON and reads it back.

import json

data = {
    "name": "Aditya",
    "age": 30,
    "city": "Ashley",
    "skills": ["Python", "Data"]
}

filename = "data.json"

with open(filename, 'w') as file:
    json.dump(data, file, indent=4)
    print(f"Dictionary written to {filename}")

with open(filename, 'r') as file:
    loaded_data = json.load(file)
    print("Data read from file:")
    print(loaded_data)

print(f"Type check: {type(loaded_data)}")