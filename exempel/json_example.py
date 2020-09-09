import json


filename = "data/person.json"
with open(filename, 'r') as f:
    data = json.load(f)
    print(data)
