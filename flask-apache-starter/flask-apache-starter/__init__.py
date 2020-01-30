#Tiffany Cao, William Cao
#SoftDev1 pd1
#K
#2019

from flask import Flask, render_template
import os
app = Flask(__name__)

DIR = os.path.dirname(__file__)
DIR += '/'

@app.route('/')
def hello_world():
    return render_template("index.html")

if __name__ == "__main__":
    app.debug = True
    app.run()
