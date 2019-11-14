# Devin Lin, William Cao
# SoftDev Pd2
# K25 - Getting More REST
# 2019-11-14

from flask import Flask, render_template
from datetime import datetime
import urllib3
import json

app = Flask(__name__)


@app.route("/")
def root():
    url = "https://api.jikan.moe/v3/anime/36456"
    http = urllib3.PoolManager()
    response = http.request('GET', url)
    data = json.loads(response.data)

    return render_template("index.html", image_source=data["image_url"])


@app.route("/anime")
def anime():
    url = "https://api.jikan.moe/v3/anime/36456"
    http = urllib3.PoolManager()
    response = http.request('GET', url)
    data = json.loads(response.data)

    return render_template("anime.html", image_source=data["image_url"], title_jap=data["title_japanese"],
                           title_english=data["title"], synopsis=data["synopsis"])


@app.route("/currency_exchange")
def currency_exchange():
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    http = urllib3.PoolManager()
    response = http.request('GET', url)
    data = json.loads(response.data)
    exchange = data["rates"].items()
    timestamp = datetime.utcfromtimestamp(data["time_last_updated"]).strftime('%Y-%m-%d %H:%M');

    return render_template("currency_exchange.html", timestamp=timestamp, exchange_rates=exchange)


@app.route("/rick")
def rick():
    url = "https://rickandmortyapi.com/api/"
    http = urllib3.PoolManager()
    response = http.request('GET', url)
    data = json.loads(response.data)

    response1 = http.request('GET', data['characters'])
    data1 = json.loads(response1.data)
    all_characters = data1['results']
    return render_template("rickMorty.html", rick=all_characters[0]['image'], name=all_characters[0]['name'],
                           status=all_characters[0]['status'], species=all_characters[0]['species'],
                           gender=all_characters[0]['gender'])


if __name__ == "__main__":
    app.debug = True
    app.run()
