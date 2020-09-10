import json
import pprint

filename = "data/person.json"
with open(filename, 'r') as f:
    data = json.load(f)
pprint.PrettyPrinter().pprint(data)
