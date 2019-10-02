from flask import Flask
from flask import session
from flask import redirect
from flask import url_for
app = Flask(__name__)

#def check_sess()

def check_creds(user, pass):
    error = []
    if (pass != 'pass'):
        error.append('pass')
    if (user != 'user'):
        error.append('user')
    return error

@app.route("/")
def home():
    if check
        return redirect('http://localhost:5000/login')
    else:
        return render_template('')

@app.route('/login')
def login():
    return "logged in successfully"

@app.route('/bad_login')
def bad_login():


if __name__ == "__main__":
    app.debug = True
    app.run()
