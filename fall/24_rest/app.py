from flask import Flask, render_template
import urllib3
import json

app = Flask(__name__)

@app.route("/")
def root():
    # Please do not abuse my key :c
    url = "https://api.nasa.gov/planetary/apod?api_key=1a1rL9InSFCbzuRveSsAxGRO01VtH3lAR1NVHbXj"
    http = urllib3.PoolManager()
    response = http.request('GET', url)
    data= json.loads(response.data)

    return render_template("index.html", image_source=data["url"])


if __name__ == "__main__":
    app.debug = True
    app.run()