# Alex Thompson (Thumb Thompson)
# William Cao (Cow)
# SoftDev1 pd2
# K10 -- <Jinja Tuning/Flask&Jinja/Learning to use jinja>
# 2019-09-23

from flask import Flask
from flask import render_template
from flask import request


app = Flask(__name__) #create instance of class Flask

@app.route("/auth")
def hello_world():
    print(request)
    print(request.args)
    return render_template("index.html", login_info=request.args)


@app.route('/')
def index():
    return render_template("landing.html")


if __name__ == "__main__":
    app.debug = True
    app.run()
