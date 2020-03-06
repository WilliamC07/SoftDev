from flask import Flask, render_template
from data import mongoConnection
app = Flask(__name__)

@app.route("/")
def root():
    return render_template("index.html", stuff=mongoConnection.meteorites_with_class("Acapulcoite"))


if __name__ == "__main__":
    app.debug = True
    app.run()
