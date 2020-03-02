import json
from pymongo import MongoClient

TEAM_NAME = "tannedCows"

client = MongoClient('localhost', 27017)  # default mongo port is 27017
database = client[TEAM_NAME]
collection = database['meteoriteLandings']

with open("data.json") as data_file:
    entries = json.load(data_file)

# Turn mass into floating point for comparison
cleaned_data = []
for entry in entries:
    # We need mass and classification
    if "mass" not in entry.keys() or entry["recclass"] == "Unknown" or "geolocation" not in entry.keys():
        print(f"Skipped id={entry['id']}")
        continue

    cleaned_data.append(entry)
    entry["mass"] = float(entry["mass"])

# insert to mongo
collection.insert_many(cleaned_data)

client.close()
