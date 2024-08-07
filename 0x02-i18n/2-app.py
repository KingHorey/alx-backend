#!/usr/bin/env python3

""" import flask packages """
from typing import Callable, Any
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """ class for locale configs"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
babel = Babel(app)

app.config.from_object(Config)


@app.route("/")
def home() -> Callable:
    """ render homepage """
    return render_template('1-index.html')


@babel.localeselector
def get_locale() -> Any:
    """ sets locale """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run()
