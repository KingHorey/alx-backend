#!/usr/bin/env python3

""" import flask and flask_babel """

from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """ class for locale configs"""
    LANGUAGES = ["en", "fr"]
    DEFAULT_LOCALE = "en"
    DEFAULT_TZ = "UTC"


app = Flask(__name__)
babel = Babel(app)

app.config.from_object(Config)
app.url_map.strict_slashes = False


@app.route("/")
def home() -> str:
    """ home route"""
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0")
