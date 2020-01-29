from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    print(__name__ + "apples")
    return open("./static/index.html").read()


@app.route('/home')
def home():
    print("Finding home")
    return "Welcome home"


@app.route('/william')
def hide_and_seek():
    print("You found willasdiam!")
    return "you found me"


if __name__ == "__main__":
    # app.debug will not work if you run using an IDE. It must be run in your terminal    
    app.debug = True
    app.run()
