import json
from pymongo import MongoClient

data = None
with open("primer-dataset.json") as data_file:
    data = data_file.read().replace("$date", "date")  # mongodb keys cannot start with '$'

client = MongoClient('localhost', 27017)  # default mongo port is 27017
db = client['restaurants']
# should probably not use hyphen in collection name
# https://stackoverflow.com/questions/24711939/mongodb-collection-hyphenated-name
restaurants = db['restaurants-collection']
restaurants.insert_many(json.loads(data))
