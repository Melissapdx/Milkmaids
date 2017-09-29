""""Milk donation website"""
from jinja2 import StrictUndefined

from flask import (Flask, jsonify, render_template, redirect, request, flash, session)
from flask_debugtoolbar import DebugToolbarExtension

from model import connect_to_db, db, Order, User, Milk, Order_item, Milk_diet, Diet

app = Flask(__name__)

app.secret_key = "ABC"
#raises a error for undefined variable in jinja
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def index():
    """Homepage"""
    return render_template("index.html")


@app.route("/register", methods=["GET"])
def register_form():
    """display register form"""

    return render_template("account.html")


@app.route("/login")
def login_form():
    """Displays login form"""

    return render_template("account.html")


@app.route("/login", methods=["POST"])
def login_handler():
    """handles login form inputs and verifies login"""

    email = request.form.get("email_2")
    password = request.form.get("password_2")

    user = User.query.filter_by(email=email).first()
    #verify user login
    if user:
        if user.password == password:
            session["User ID"] = user.user_id
        else:
            flash("Incorrect password, Please enter correct password")
            return redirect("/login")
    else:
        flash("Email doesn't exist. Please sign up!")
        return redirect("/login")
    return redirect("/userhome/%s" % user.user_id)


@app.route("/userhome/<user_id>")
def user_homepage(user_id):
    """Displays user homepage"""
    user = User.query.filter_by(user_id=user_id).one()
    print user

    flash("Welcome!")
    return render_template("user_homepage.html", user=user)


if __name__ == "__main__":

    app.debug = True
    app.jinja_env.auto_reload = app.debug  # make sure templates are not cached

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(port=5000, host='0.0.0.0')
