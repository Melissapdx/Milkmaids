""""Milk donation website"""
from jinja2 import StrictUndefined
from flask import Response, Flask, jsonify, json, render_template, redirect, request, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from model import connect_to_db, db, Order, User, Milk, Order_item, Milk_diet, Diet
from decimal import *

app = Flask(__name__, static_url_path='/static')

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


@app.route("/register", methods=["POST"])
def register_process():
    """Process registration, add to database if user does not exist"""

    email = request.form.get("email")
    password = request.form.get("password")
    firstname = request.form.get("firstname")
    lastname = request.form.get("lastname")
    address = request.form.get("address")
    zipcode = request.form.get("zipcode")

    user_check = User.query.filter_by(email=email).all()

    if user_check == []:
        new_user = User(email=email, password=password, firstname=firstname,
                        lastname=lastname, address=address, zipcode=zipcode)
        db.session.add(new_user)
    ## add flash and redirect to sign in page if exists
    else:
        flash('Looks like you already have an account. Sign in!')
        return redirect("/login")

    db.session.commit()

    return redirect("/")

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


@app.route("/logout")
def logout_handler():
    """logs users out"""

    session.pop("User ID", None)
    flash("You are currently logged out")
    return redirect("/")


@app.route("/userhome/<user_id>")
def user_homepage(user_id):
    """Displays user homepage"""

    user = User.query.filter_by(user_id=user_id).one()

    flash("Welcome!")
    return render_template("user_homepage.html", user=user)


@app.route("/shop")
def get_milk():
    """Get information on milk products to display to user"""
    milk_products = db.session.query(Milk, Milk_diet).join(Milk_diet).all()
    
    # TODO use map
    milk_output = []
    for (milk, diet) in milk_products:
        milk_output.append({
            "milk_id": milk.milk_id,
            "smoker": milk.smoker,
            "baby_age": milk.baby_age,
            "user_id": milk.user_id,
            "price_per_oz": milk.price_per_oz,
            "inventory": milk.inventory,
            "date": milk.date.isoformat(),
            "diet_name": diet.milk_diet.diet_name
        })

    return render_template("shop.html", milk_output=milk_output)


@app.route('/add_to_cart')
def add_to_cart():
    """
    Add a Milk item to cart
    """
    milk = request.args.get('milk', None)
    # TODO change to map id
    milk = int(milk)
    if milk is None:
        return
    if 'cart' in session:
        cart = session['cart']
        cart['order'].append(milk)
    else:
        cart = session['cart'] = {}
        cart['order'] = [milk]

    session['cart'] = cart
    html = "Item added to cart!"
    return (html)


@app.route("/cart")
def display_cart():
    """
    Display items in shopping cart by quering milk_ids that are sent from ajax call.
    cart_items = {[
        diet_name,
        baby_age,
        smoker,
        how_many_oz,
        price_per_oz,
    ]}
    total_cost = sum of items' cost
    """
    #get cart from session
    cart = session.get("cart", {})
    cart_items = []
    milk_ids = cart.get("order")
    if milk_ids:
        for milk_item in milk_ids:
            milk_query = db.session.query(Milk, Milk_diet).join(Milk_diet).filter_by(milk_id=milk_item).one()
            cart_items.append(milk_query)
        milk_prices = []
        #calculate total cost of each milk item by multiplying ounces and inventory
        for item in cart_items:
            milk_cost = item.Milk.price_per_oz * item.Milk.inventory
            milk_prices.append(milk_cost)
        # calculates cost of total user orders
        count = 0
        for price in milk_prices:
            count += price
        order_cost = count
        session['order_cost'] = order_cost
        return render_template("cart.html", cart_items=cart_items, order_cost=order_cost)
    else:
        return render_template("cart.html", cart_items=cart_items)


@app.route("/checkout")
def checkout():
    """User checkout via stripe. Database is queried by User ID and user's shipping information is printed.
    Total order_cost is calculated by adding shipping, merchandise cost and tax.
    """
    user = session.get("User ID")
    order_cost = session.get("order_cost")
    shipping = 9
    total_cost = shipping + order_cost
    user_query = User.query.filter_by(user_id=user).first()
    if user:
        fname = user_query.firstname
        lname = user_query.lastname
        address = user_query.address
        zipcode = user_query.zipcode
        return render_template("checkout.html", address=address, zipcode=zipcode, fname=fname, lname=lname, order_cost=order_cost, shipping=shipping, total_cost=total_cost)
    else:
        flash('Please login or signup')
        return redirect("/login")

if __name__ == "__main__":

    app.debug = True
    app.jinja_env.auto_reload = app.debug  # make sure templates are not cached

    connect_to_db(app)

    # Use the DebugToolbar
    # DebugToolbarExtension(app)

    app.run(port=5000, host='0.0.0.0')
