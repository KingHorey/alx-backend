#!/usr/bin/env python3

""" import flask packages """
from typing import Any
from flask import Flask, render_template, request
from flask_babel import Babel, gettext


class Config:
    """ class for locale configs"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)


app.config.from_object(Config)
app.url_map.strict_slashes = False


@app.route("/")
def home() -> str:
    """ render homepage """
    return render_template('3-index.html', home_title=gettext("Welcome to "
                                                              "Holberton"),
                           home_header=gettext("Hello world!"))


def get_locale() -> Any:
    """ sets the locale """
    print(request.accept_languages.best_match(app.config['LANGUAGES']))
    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel = Babel(app, locale_selector=get_locale)


if __name__ == "__main__":
    app.run()
