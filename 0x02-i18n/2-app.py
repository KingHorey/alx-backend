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
def home() -> None:
    """ render homepage """
    render_template('1-index.html', )


@babel.localeselector
def get_locale() -> str:
    """ sets locale """
    return request.accept_languages.best_match(app.config['LANGUAGES'])

