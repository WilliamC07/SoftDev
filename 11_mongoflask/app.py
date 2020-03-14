from flask import Flask, render_template, request
from data import mongoConnection
import json
from pymongo import MongoClient
import datetime
import pprint

app = Flask(__name__)

@app.route("/")
def root():
    return render_template("index.html",
                           meteorite_classes=mongoConnection.get_class_names(),
                           locations=mongoConnection.get_locations())

@app.route('/meteorites-with-class')
def meteorites_with_class() -> list:
    class_name = request.args['class_name']
    return render_template("result.html",
                           selection=f"Meteorites with class \"{class_name}\"",
                           meteorites=mongoConnection.meteorites_with_class(class_name))

@app.route('/meteorites-found')
def meteorites_found() -> list:
    return render_template("result.html",
                           selection=f"Meteorites that were found (i.e. someone found it rather than someone saw it falling)",
                           meteorites=mongoConnection.meteorites_found())

@app.route('/meteorites-max')
def meteorite_with_class_and_max_mass():
    max_mass = float(request.args['max_mass'])
    class_name = request.args['class_name']
    return render_template("result.html",
                           selection=f"Meteorites with class \"{class_name}\" and less than {max_mass} grams",
                           meteorites=mongoConnection.meteorite_with_class_and_max_mass(class_name, max_mass))

@app.route('/meteorites-date')
def meteorite_with_class_and_found_before_date():
    date = datetime.datetime.strptime(request.args['date'], "%Y-%m-%d")
    class_name = request.args['class_name']
    string_date = date.__format__("%Y-%m-%d")
    return render_template("result.html",
                           selection=f"Meteorites with class \"{class_name}\" that fell before {string_date}",
                           meteorites=mongoConnection.meteorite_with_class_and_found_before_date(class_name, date))

@app.route('/meteorites-fell-near')
def meteorite_fell_near():
    location = request.args['location']
    return render_template("result.html",
                           selection=f"Meteorites that fell near {location}. Error of margin is 25 degrees",
                           meteorites=mongoConnection.meteorite_fell_near(location))

if __name__ == "__main__":
    app.debug = True
    app.run()
