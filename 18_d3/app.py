"""

William Cao, Henry Liu, Ethan Chen -- HEW
SoftDev pd1
K18 -- Come Up For Air
2020-04-21

"""
import csv
from flask import Flask, render_template, jsonify
app = Flask(__name__)


@app.route("/")
def root():
    return render_template("index.html")


@app.route("/data", methods={'GET'})
def data():
    """
    GET the initial claims for the United States.

    returns a JSON as an array of objects ({count: number, date: string})
    Example return:
    [
        {count: "208000", date: "1967-01-07"},
        {count: "207000", date: "1967-01-14"}
    ]
    """
    payload = []
    with open("data.csv") as csv_file:
        reader = csv.reader(csv_file)
        # skip the first row, which is the header row
        next(reader)
        for entry in reader:
            payload.append({'date': entry[0], 'count': int(entry[1])})

    return jsonify(payload)


if __name__ == "__main__":
    app.debug = True
    app.run()
