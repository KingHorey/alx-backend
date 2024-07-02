#!/usr/bin/env python3
""" Module for trying out Babel i18n """

from flask import Flask, render_template, request
from flask_babel import Babel, _


class Config:
    LANGUAGES = ["en", "fr"]
    DEFAULT_LOCALE = "en"
    DEFAULT_TZ = "UTC"


app = Flask(__name__)
babel = Babel(app)

app.config.from_object(Config)
app.url_map.strict_slashes = False


@app.route("/", methods=["GET"])
def home():
    render_template('1-index.html', home_title=_("Welcome to Holberton"),
                    home_header=_("Hello World"))


@babel.localeselector
def get_locale(locale="fr"):
    best_match = request.accept_languages.best_match(app.config['LANGUAGES'])
    return best_match if best_match else locale


if __name__ == "__main__":
    app.run(port=4000)
