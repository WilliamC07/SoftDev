import json
from pymongo import MongoClient
import datetime
import pprint

TEAM_NAME = "tannedCows"

client = MongoClient('localhost', 27017)  # default mongo port is 27017
database = client[TEAM_NAME]
meteoriteLandings = database['meteoriteLandings']
commonLocations = database['commonLocations']

if meteoriteLandings.count() == 0:
    # Need to initialize the databsae
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
    meteoriteLandings.insert_many(cleaned_data)


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


def meteorites_with_class(class_name: str) -> list:
    """
    Lists all the meteorites classified with class_name given.
    :param class_name: See Example Entry at start of this file for names
    :return:
    """
    return list(meteoriteLandings.find({"recclass": class_name}))


def meteorites_found() -> list:
    """
    List of all the meteorites that were found (that means someone found it rather than someone saw it falling)
    :return: List of objects
    """
    return list(meteoriteLandings.find({"fall": "Found"}))


def meteorite_with_class_and_max_mass(class_name: str, max_mass: float):
    """
    Lists all the meteorites classified with class_name given limited by given maximum mass.
    :param class_name: See Example Entry at start of this file for names
    :param max_mass:
    :return:
    """
    return list(meteoriteLandings.find({"recclass": class_name, "mass": {"$lt": max_mass}}))


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
        if datetime.datetime.strptime(entry["year"], "%Y-%m-%dT%H:%M:%S.%f") < date:
            result.append(entry)
    return result


def meteorite_fell_near(location: str):
    """
    Finds all the meteorite that fell near your area given the location. Error of margin is 25 degree distance sqrt(a**2 + b**2)
    :param location: Location of where you are as string. Available values: "New York City", "Chicago","Los Angeles","Boston","Paris","London","Madrid","Moscow","Dubai","Mumbai"
    :return:
    """
    output = []
    given_longitude = commonLocations.find({"name": location})[0]['long']
    given_latitude = commonLocations.find({"name": location})[0]['lat']
    for entry in meteoriteLandings.find({}):
        entry_longitude, entry_latitude = entry["geolocation"]["coordinates"]
        entry_latitude = float(entry_latitude)
        entry_longitude = float(entry_longitude)
        if ((entry_longitude - given_longitude) ** 2 + (entry_latitude - given_latitude) ** 2) ** .5 < 25:
            output.append(entry)

    return output