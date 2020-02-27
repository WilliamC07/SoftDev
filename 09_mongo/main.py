# William Cao && Justin Shaw
# SoftDev pd1
# K09 -- Yummy Mongo Py
# 2020-02-28

from pymongo import MongoClient
import pprint

client = MongoClient('localhost', 27017)  # default mongo port is 27017
db = client['restaurants']
collection = db['restaurants-collection']

"""
Sample:
[{'_id': ObjectId('5e5753ec7b30a03ac513f3bc'),
  'address': {'building': '200',
              'coord': [-74.0142077, 40.7148476],
              'street': 'West Street',
              'zipcode': '10282'},
  'borough': 'Manhattan',
  'cuisine': 'American',
  'grades': [{'date': {'date': 1395014400000}, 'grade': 'A', 'score': 3},
             {'date': {'date': 1362614400000}, 'grade': 'A', 'score': 2},
             {'date': {'date': 1330646400000}, 'grade': 'A', 'score': 2}],
  'name': 'Goldman Sachs',
  'restaurant_id': '41469754'
},
{'_id': ObjectId('5e5753ec7b30a03ac513f6d9'),
  'address': {'building': '2',
              'coord': [-74.0160502, 40.71546439999999],
              'street': 'River Terrace',
              'zipcode': '10282'},
  'borough': 'Manhattan',
  'cuisine': 'American',
  'grades': [{'date': {'date': 1392940800000}, 'grade': 'A', 'score': 0},
             {'date': {'date': 1360713600000}, 'grade': 'A', 'score': 8},
             {'date': {'date': 1346716800000}, 'grade': 'A', 'score': 2},
             {'date': {'date': 1313020800000}, 'grade': 'A', 'score': 2}],
  'name': 'Le Pain Quotidien',
  'restaurant_id': '41507371'
}]
"""


def print_header(header: str):
    print("\n\n-----")
    print(header)
    print("-----")


def restaurants_in_borough(borough: str):
    return list(collection.find({"borough": borough.capitalize()}))


def restaurants_in_zip_code(code: str):
    return list(collection.find({"address.zipcode": code}))


def restaurants_in_zip_code_with_grade(code: str, grade_requested: str):
    restaurants = []
    for restaurant in collection.find({"address.zipcode": code}):
        for grade in restaurant["grades"]:
            if grade["grade"] != grade_requested:
                break
        else:
            restaurants.append(restaurant)
    return restaurants


def restaurants_in_zip_code_with_score_below(code: str, score_requested: int):
    restaurants = []
    for restaurant in collection.find({"address.zipcode": code}):
        for grade in restaurant["grades"]:
            if grade["score"] >= score_requested:
                break
        else:
            restaurants.append(restaurant)
    return restaurants


def restaurants_with_improving_score():
    restaurants = []
    for restaurant in collection.find():
        previous = -1
        for grade in restaurant["grades"]:
            score = grade["score"]
            if score is not None and score < previous:
                break
            else:
                previous = grade["score"]
        else:
            restaurants.append(restaurant)
    return restaurants


print_header("Restaurants in the Bronx (2)")
pprint.pprint(restaurants_in_borough("Bronx")[0:2])  # get first two so we don't spam the terminal

print_header("Restaurants in zipcode 10282 (stuyvesant zipcode) (2)")
pprint.pprint(restaurants_in_zip_code("10282")[0:2])  # get first two so we don't spam the terminal

print_header("Restaurants in zipcode 10282 (stuyvesant zipcode) with only grade A (2)")
pprint.pprint(restaurants_in_zip_code_with_grade("10282", "A")[0:2])

print_header("Restaurants in zipcode 10282 (stuyvesant zipcode) with only grade less than 10 (2)")
pprint.pprint(restaurants_in_zip_code_with_score_below("10282", 10)[0:2])

print_header("Restaurants with improving scores or consistent (3)")
pprint.pprint(restaurants_with_improving_score()[0:3])
