from pymongo import MongoClient
import json
import datetime

DATABASE_NAME = "HensAndCows"
client = MongoClient('localhost', 27017)

# Drop the existing database
if DATABASE_NAME in client.list_database_names():
    client.drop_database(DATABASE_NAME);

# Recreate the database
database = client[DATABASE_NAME]
meteoriteCollection = database['meteoriteLandings']
locationCollection = database['commonLocations']

# Populate the meteorite collection
"""
Name: Meteorite Landings
Description of its contents: name of meteorite, classification, mass, found years after it fell or if someone saw it
                             falling, year fell, location in latitude and longitude
Host: https://data.nasa.gov/resource/y77d-th95.json

Parsing-----------
Parsing the data.json file
Because the data is from NASA, it is relatively clean (no syntax error).
We parsed the json file, creating a list of dictionaries. All entries are thrown out if it is
missing either the mass, classification, or location where the meteorite fell.
We then inserted the now serialized data into mongo.
This is all done in the initialize.py file. It should only be called once.

Data description sources-----------
* "nametype" field documentation: https://data.nasa.gov/Space-Science/Meteorite-Landings/ak9y-cwf9
* "fall" field documentation: https://www.researchgate.net/publication/326053427_Meteorite_Landings

Example entry
{
"name": "Aachen",
"id": "1",
"nametype": "Valid",                -- 'valid' is for most meteorites and 'relict'
"recclass": "L5",                   -- Type of meteorite ("Acapulcoite", "Achondrite-ung", "Angrite", "Aubrite", "C", "C2-ung", "C3-ung", "CBa", "CI1", "CK4", "CM2", "CO3.2", "CO3.3", "CO3.4", "CO3.5", "CO3.6", "CR2", "CR2-an", "CV3", "Diogenite", "Diogenite-pm", "EH3", "EH3/4-an", "EH4", "EH5", "EH7-an", "EL6", "Eucrite", "Eucrite-br", "Eucrite-cm", "Eucrite-mmict", "Eucrite-pmict", "H", "H/L3.6", "H/L3.9", "H/L4", "H3", "H3-4", "H3-5", "H3-6", "H3.4", "H3.7", "H3.8", "H3/4", "H4", "H4-5", "H4-6", "H4-an", "H4/5", "H5", "H5-6", "H5-7", "H5/6", "H6", "H?", "Howardite", "Iron", "Iron, IAB-MG", "Iron, IAB-sHL", "Iron, IAB-sLL", "Iron, IAB-ung", "Iron, IIAB", "Iron, IID", "Iron, IIE", "Iron, IIE-an", "Iron, IIF", "Iron, IIIAB", "Iron, IVA", "Iron, ungrouped", "Iron?", "K3", "L", "L/LL4", "L/LL5", "L/LL6", "L3", "L3-4", "L3-6", "L3.4", "L3.6", "L3.7", "L3.7-6", "L4", "L4-6", "L5", "L5-6", "L5/6", "L6", "LL", "LL3-6", "LL3.00", "LL3.15", "LL3.2", "LL3.3", "LL3.4", "LL3.6", "LL3.8", "LL3.9", "LL4", "LL5", "LL6", "Lodranite", "Martian (chassignite)", "Martian (nakhlite)", "Martian (shergottite)", "Mesosiderite", "Mesosiderite-A1", "Mesosiderite-A3", "Mesosiderite-A3/4", "OC", "Pallasite", "Pallasite, PMG", "R3.8-6", "Stone-uncl", "Unknown", "Ureilite", "Ureilite-an", "Winonaite")
"mass": "21",                       -- Mass in grams
"fall": "Fell",                     -- Either "Fell" or "Found"
"year": "1880-01-01T00:00:00.000",  -- Year found/Year meteorite hit
"reclat": "50.775000",              -- Recorded latitude
"reclong": "6.083330",              -- Recorded longitude
"geolocation": {
    "type": "Point",                -- "Point" describes how geolocation is recorded
    "coordinates": [
        6.08333,
        50.775
        ]
    }
}

"""
with open("data.json", encoding='utf-8') as data_file:
    print(data_file)
    entries = json.load(data_file)
sterilized_data = []
for entry in entries:
    # Every meteorite requires: mass, classification, location where it fell
    if "mass" not in entry.keys() or entry["recclass"] == "Unknown" or "geolocation" not in entry.keys():
        print(f"Skipped id={entry['id']}")
        continue

    if "year" in entry.keys():
        # Remove the hours, minute seconds from displaying
        entry["year"] = entry["year"][0: entry["year"].find("T")]
    else:
        entry["year"] = "Unknown"

    sterilized_data.append(entry)
    # Convert mass to a floating point number (instead of string)
    entry["mass"] = float(entry["mass"])

# Insert to database
meteoriteCollection.insert_many(sterilized_data)

# Populate common location with latitude and longitude
locations = [
    {"name": "New York City", "lat": 40.7128, "long": 74.0060},
    {"name": "Chicago", "lat": 41.8781, "long": 87.6298},
    {"name": "Los Angeles", "lat": 34.0522, "long": 118.2437},
    {"name": "Boston", "lat": 42.3601, "long": 71.0589},
    {"name": "Paris", "lat": 48.8566, "long": 2.3522},
    {"name": "London", "lat": 51.5074, "long": 0.1278},
    {"name": "Madrid", "lat": 40.4168, "long": 3.7038},
    {"name": "Moscow", "lat": 55.7558, "long": 37.6173},
    {"name": "Dubai", "lat": 25.2048, "long": 55.2708},
    {"name": "Mumbai", "lat": 19.0760, "long": 72.8777},
]
locationCollection.insert_many(locations)

def get_class_names() -> list:
    return list(meteoriteCollection.find({}).distinct('recclass'))


def get_locations() -> list:
    return [x["name"] for x in locations]


def meteorites_with_class(class_name: str) -> list:
    """
    Lists all the meteorites classified with class_name given.
    :param class_name: See Example Entry at start of this file for names
    :return:
    """
    return list(meteoriteCollection.find({"recclass": class_name}))


def meteorites_found() -> list:
    """
    List of all the meteorites that were found (that means someone found it rather than someone saw it falling)
    :return: List of objects
    """
    return list(meteoriteCollection.find({"fall": "Found"}))

def meteorite_with_class_and_max_mass(class_name: str, max_mass: float):
    """
    Lists all the meteorites classified with class_name given limited by given maximum mass.
    :param class_name: See Example Entry at start of this file for names
    :param max_mass:
    :return:
    """
    return list(meteoriteCollection.find({"recclass": class_name, "mass": {"$lte": max_mass}}))

def meteorite_with_class_and_found_before_date(class_name: str, date: datetime.datetime):
    """
    List of all meteorites of given class that fell before the given time
    :param class_name: See Example Entry at start of this file for names
    :param date: Date in which meteorite fell before
    :return:
    """
    result = []
    for entry in meteorites_with_class(class_name):
        # Date formatting source
        # https://stackoverflow.com/a/969324/7154700
        # https://docs.python.org/3.7/library/datetime.html#strftime-strptime-behavior
        if datetime.datetime.strptime(entry["year"], "%Y-%m-%d") < date:
            result.append(entry)
    return result

def meteorite_fell_near(location: str):
    """
    Finds all the meteorite that fell near your area given the location. Error of margin is 25 degree distance sqrt(a**2 + b**2)
    :param location: Location of where you are as string. Available values: "New York City", "Chicago","Los Angeles","Boston","Paris","London","Madrid","Moscow","Dubai","Mumbai"
    :return:
    """
    output = []
    given_longitude = locationCollection.find({"name": location})[0]['long']
    given_latitude = locationCollection.find({"name": location})[0]['lat']
    for entry in meteoriteCollection.find({}):
        # pprint(entry)
        entry_longitude, entry_latitude = entry["geolocation"]["coordinates"]
        entry_latitude = float(entry_latitude)
        entry_longitude = float(entry_longitude)
        if ((entry_longitude - given_longitude) ** 2 + (entry_latitude - given_latitude) ** 2) ** .5 < 10:
            output.append(entry)
    return output


if __name__ == "__main__":
    print(get_class_names())
