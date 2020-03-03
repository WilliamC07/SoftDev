import json
from pymongo import MongoClient

TEAM_NAME = "tannedCows"

client = MongoClient('localhost', 27017)  # default mongo port is 27017
database = client[TEAM_NAME]
collection = database['meteoriteLandings']

with open("data.json", encoding='utf-8') as data_file:
    print(data_file)
    entries = json.load(data_file)


# Turn mass into floating point for comparison
cleaned_data = []
for entry in entries:
    # We need mass, classification, and location where meteorite fell
    if "mass" not in entry.keys() or entry["recclass"] == "Unknown" or "geolocation" not in entry.keys():
        print(f"Skipped id={entry['id']}")
        continue

    cleaned_data.append(entry)
    entry["mass"] = float(entry["mass"])

# insert to mongo
collection.insert_many(cleaned_data)


# making locations database
# added example locations. We can use mapquest to implement more, but these will do for now.
database['commonLocations'].insert_many([
    {"name":"New York City","lat":40.7128,"long":74.0060},
    {"name":"Chicago","lat":41.8781,"long":87.6298},
    {"name":"Los Angeles","lat":34.0522,"long":118.2437},
    {"name":"Boston","lat":42.3601,"long":71.0589},
    {"name":"Paris","lat":48.8566,"long":2.3522},
    {"name":"London","lat":51.5074,"long":0.1278},
    {"name":"Madrid","lat":40.4168,"long":3.7038},
    {"name":"Moscow","lat":55.7558,"long":37.6173},
    {"name":"Dubai","lat":25.2048,"long":55.2708},
    {"name":"Mumbai","lat":19.0760,"long":72.8777},
])

#{"name":"","lat":,"long":},
client.close()
