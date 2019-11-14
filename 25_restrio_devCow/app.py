# Devin Lin, William Cao
# SoftDev Pd2
# K25 - Getting More REST
# 2019-11-14

from flask import Flask, render_template
from datetime import datetime
import urllib
import json

app = Flask(__name__)


@app.route("/")
def root():
    url = urllib.request.urlopen("https://api.jikan.moe/v3/anime/36456")
    response = url.read()
    data = json.loads(response)

    return render_template("index.html", image_source=data["image_url"])


@app.route("/anime")
def anime():
    url = urllib.request.urlopen("https://api.jikan.moe/v3/anime/36456")
    response = url.read()
    data = json.loads(response)

    return render_template("anime.html", image_source=data["image_url"], title_jap=data["title_japanese"],
                           title_english=data["title"], synopsis=data["synopsis"])


@app.route("/currency_exchange")
def currency_exchange():
    url = urllib.request.urlopen("https://api.exchangerate-api.com/v4/latest/USD")
    response = url.read()
    data = json.loads(response)
    exchange = data["rates"].items()
    timestamp = datetime.utcfromtimestamp(data["time_last_updated"]).strftime('%Y-%m-%d %H:%M');

    return render_template("currency_exchange.html", timestamp=timestamp, exchange_rates=exchange)


@app.route("/rick")
def rick():
    url = urllib.request.urlopen("https://rickandmortyapi.com/api/")
    response = url.read()
    data = json.loads(response)

    url1 = urllib.request.urlopen(data['characters'])
    response1 = url1.read()
    data1 = json.loads(response1)
    all_characters = data1['results']
    return render_template("rickMorty.html", rick=all_characters[0]['image'], name=all_characters[0]['name'],
                           status=all_characters[0]['status'], species=all_characters[0]['species'],
                           gender=all_characters[0]['gender'])


if __name__ == "__main__":
    app.debug = True
    app.run()
