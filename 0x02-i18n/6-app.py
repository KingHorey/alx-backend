#!/usr/bin/env python3
""" Module for trying out Babel i18n """

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
def home() -> str:
    """ render homepage """
    return render_template('1-index.html', home_title=_("Welcome to "
                                                        "Holberton"),
                           home_header=_("Hello world"))


@babel.localeselector
def get_locale() -> str:
    """ gets and sets the locale definition """
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
    """ checks for the login id"""
    user_id = request.args.get("login_as")
    if user_id in users and int(user_id):
        return users.get(int(user_id))
    return {}


if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0")
