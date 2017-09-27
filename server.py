""""Milk donation website"""
from jinja2 import StrictUndefined

from flask import (Flask, jsonify, render_template, redirect, request, flash, session)
from flask_debugtoolbar import DebugToolbarExtension

from model import connect_to_db, db, Order, User, Milk, Order_item, Milk_diet, Diet

app = Flask(__name__)

app.secret_key = "ABC"
#raises a error for undefined variable in jinja
app.jinja_env.undefined = StrictUndefined

if __name__ == "__main__":

    app.debug = True
    app.jinja_env.auto_reload = app.debug  # make sure templates are not cached

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(port=5000, host='0.0.0.0')
