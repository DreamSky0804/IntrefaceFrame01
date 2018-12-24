from flask import jsonify
from flask import render_template

from supermarket import supermarket

@supermarket.route("/")
def index():
    return render_template("index.html")


@supermarket.route("/hello", methods=['GET', ])
def hello():
    return jsonify(msg="hello world!")
