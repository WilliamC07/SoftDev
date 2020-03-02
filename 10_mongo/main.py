# Manfred Tan && William Cao: Team tannedCows
# SoftDev pd1
# K10: Import/Export Bank
# 2020-03-04
from pymongo import MongoClient
import datetime
from pprint import pprint

"""
Name: Meteorite Landings
Description of its contents: name of meteorite, classification, mass, found years after it fell or if someone saw it 
                             falling, year fell, location in latitude and longitude
Host: https://data.nasa.gov/resource/y77d-th95.json

* "nametype" field documentation: https://data.nasa.gov/Space-Science/Meteorite-Landings/ak9y-cwf9
* "fall" field documentation: https://www.researchgate.net/publication/326053427_Meteorite_Landings

* We removed all entry (not reflected in .json) that do not have year fell and mass known

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

client = MongoClient('localhost', 27017)  # default mongo port is 27017
db = client["tannedCows"]
meteoriteLandings = db['meteoriteLandings']

def print_header(header: str):
    print("\n\n-----")
    print(header)
    print("-----")


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
    :param location: Location of where you are as string. Available values: "New York City"
    :return:
    """
    output = []
    given_longitude = -73.935242
    given_latitude = 40.730610
    for entry in meteoriteLandings.find({}):
        pprint(entry)
        entry_longitude, entry_latitude = entry["geolocation"]["coordinates"]
        entry_latitude = float(entry_latitude)
        entry_longitude = float(entry_longitude)
        if ((entry_longitude - given_longitude) ** 2 + (entry_latitude - given_latitude) ** 2) ** .5 < 25:
            output.append(entry)

    return output


print_header("First two meteorites with class 'L5'")
pprint(meteorites_with_class("L5")[:2])

print_header("First two meteorites that were found rather than someone saw it falling")
pprint(meteorites_found()[:2])

print_header("First two meteorite with class 'L' with maximum mass 1234.0")
pprint(meteorite_with_class_and_max_mass("L", 1234.0)[:2])

print_header("First two meteorite of class 'LL5' that fell before year 2000")
year_2000 = datetime.datetime(2000, 1, 1)
pprint(meteorite_with_class_and_found_before_date("LL5", year_2000)[:2])

print_header("Meteorites that fell near NYC")
pprint(meteorite_fell_near("New York City")[:2])
