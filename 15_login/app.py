from flask import Flask
from flask import session
from flask import render_template
from flask import redirect
from flask import url_for
from flask import request
app = Flask(__name__)

#def check_sess()

def check_creds(username, password):
    error = []
    if (password != 'pass'):
        error.append('pass')
    if (username != 'user'):
        error.append('user')
    return error

@app.route("/")
def home():
    if (session.get('username') == None):
        print ('no username')
        return redirect(url_for("login"))
    #else:
        #cred_errors = check_creds(session.get('username'),session.get('password'))
        #if (cred_errors == [])
        #    return redirect(url_for("welcome"))


@app.route('/login',methods = ['GET'])
def login():
    print(request.args('username'))
    return render_template("login.html")



@app.route("/welcome")
def welcome():
    return "You are logged in"

@app.route('/bad_login')
def bad_login():
    pass

if __name__ == "__main__":
    app.debug = True
    app.run()
