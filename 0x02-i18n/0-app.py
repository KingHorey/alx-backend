#!/usr/bin/env python3

from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False



@app.route("/")
def home():
	render_template('0-index.html')
