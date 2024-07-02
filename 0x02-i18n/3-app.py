#!/usr/bin/env python3

""" import flask packages """
from flask import Flask, render_template, request
from flask_babel import Babel, _


class Config:
    """ class for locale configs"""
    LANGUAGES = ["en", "fr"]
    DEFAULT_LOCALE = "en"
    DEFAULT_TZ = "UTC"


app = Flask(__name__)
babel = Babel(app)

app.config.from_object(Config)
app.url_map.strict_slashes = False


@app.route("/", methods=["GET"])
def home() -> str:
    """ render homepage """
    return render_template('1-index.html', home_title=_("Welcome to "
                                                        "Holberton"),
                           home_header=_("Hello world"))


@babel.localeselector
def get_locale() -> str:
    """ sets the locale """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0")
