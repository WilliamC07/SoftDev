# Team Pizza Bagels
# Joseph Yusufov
# William Cao
# Devin Lin
# 2019-09-26

from flask import Flask
from flask import render_template
from flask import request


app = Flask(__name__) #create instance of class Flask

@app.route("/auth")
def authentication(): 
    """
    This only accepts GET requests
    """
    print("\n" + "BODY OF REQUEST >>>" + str(request))
    print("REQUEST ARGS >>>" + str(request.args) + "\n")
    return render_template("index.html", login_info=request.args, method_type=request.method)


@app.route('/')
def index():
    return render_template("landing.html")


if __name__ == "__main__":
    app.debug = True
    app.run()
