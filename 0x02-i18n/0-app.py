#!/usr/bin/env python3

""" import flask package """
from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def home() -> str:
	""" render homepage """
	return render_template('0-index.html')


if __name__ == "__main__":
	app.run(port=5000, host="0.0.0.0")
