import os

from flask import Flask
from flask import session
from flask import render_template
from flask import redirect
from flask import url_for
from flask import request


app = Flask(__name__)
# Need SECRET KEY for session
# In future, we need to save to .env file
secret = os.urandom(12)
print("Secret key: {}".format(secret))
app.secret_key = secret


def credentials_middleware(username, password):
    """
    Will attempt to login the user with the given credentials.
    Returns view to welcome page if credentials are correct; error page otherwise
    :param username:
    :param password:
    """
    print("entering middleware with username: {} password: {}".format(username, password))

    errors = []
    if username != 'user':
        errors.append("Incorrect Username")
    if password != 'pass':
        errors.append("Incorrect Password")

    if len(errors):
        return render_template("error.html", errors=errors)
    else:
        session['username'] = username
        print("\n\nCurrent session: {}".format(str(session)))
        return render_template("welcome.html")


@app.route("/")
def home():
    print("\n\nUser has entered website")

    if session.get('username') is None:
        # User has not logged in before
        print("User needs to login because user has not logged in before")
        return redirect(url_for("login"))
    else:
        print("User has already logged in")
        print("Session data username: {}".format(session['username']))
        return render_template("welcome.html")


@app.route('/login', methods=['GET'])
def login():
    print("\n\nUser entered login view")

    if request.method == 'GET' and len(request.args) != 0:
        username = request.args["username"]
        password = request.args["password"]
        print("User is logging in with username: {} password: {}".format(username, password))
        return credentials_middleware(username, password)
    else:
        print("User needs to fill out login information")
        return render_template("login.html")


@app.route('/logout', methods=['GET'])
def logout():
    print("\n\nRemoving username from session (logout)")
    session.pop('username')
    print("Current session: {}".format(session))
    # Don't redirect back to root since we know the user is not logged in
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.debug = True
    app.run()
