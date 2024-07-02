#!/usr/bin/env python3

""" import flask package """
from typing import Callable

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home() -> Callable:
    """ render homepage """
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run()
