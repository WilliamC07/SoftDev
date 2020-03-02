import json
from pymongo import MongoClient

TEAM_NAME = "tannedCows"

client = MongoClient('localhost', 27017)  # default mongo port is 27017
database = client[TEAM_NAME]
collection = database['meteoriteLandings']

with open("data.json") as data_file:
    collection.insert_many(json.load(data_file))

client.close()
