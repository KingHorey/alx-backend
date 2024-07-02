#!/usr/bin/env python3
""" Module for trying out Babel i18n """
from typing import Any

import pytz
from flask import Flask, render_template, request, g
from flask_babel import Babel, _


class Config:
    """ class for locale configs"""
    LANGUAGES = ["en", "fr"]
    DEFAULT_LOCALE = "en"
    DEFAULT_TZ = "UTC"


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

app = Flask(__name__)
babel = Babel(app)

app.config.from_object(Config)
app.url_map.strict_slashes = False


@app.route("/", methods=["GET"])
def home() -> None:
    """ render homepage """
    render_template('1-index.html', home_title=_("Welcome to Holberton"),
                    home_header=_("Hello World"))


@babel.localeselector
def get_locale() -> str:
    """ sets the locale """
    lang = request.args.get("locale")
    if lang in app.config['LANGUAGES']:
        return lang
    if g.user:
        lang = g.user.get("locale")
        if lang in app.config['LANGUAGES']:
            return lang
    else:
        best_match = request.accept_languages.best_match(
            app.config['LANGUAGES'])
        return best_match if best_match else app.config['DEFAULT_LOCALE']


@app.before_request
def before_request() -> None:
    """ run before other requests """
    g.user = get_user()


def get_user() -> dict:
    """ get user information, if exists """
    user_id = request.args.get("login_as")
    if user_id in users and int(user_id):
        return users.get(int(user_id))
    return {}


@babel.timezoneselector
def get_timezone() -> Any:
    """ set the timezone """
    tzone = request.args.get("timezone")
    if tzone:
        try:
            verified_zone = pytz.timezone(tzone)
            return verified_zone
        except pytz.exceptions.UnknownTimeZoneError:
            return app.config['DEFAULT_TZ']
    if g.user:
        tzone = g.user.get("timezone")
        try:
            verified_zone = pytz.timezone(tzone)
            return verified_zone
        except pytz.exceptions.UnknownTimeZoneError:
            return app.config['DEFAULT_TZ']
    else:
        return app.config['DEFAULT_TZ']


if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0")
