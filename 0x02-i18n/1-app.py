from flask import Flask, render_template
from flask_babel import Babel


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
	render_template('1-index.html')
