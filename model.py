"""Model and database functions for Milkmaids"""
db = SQLAlchemy()


class Order(db.model):
    """Orders for website"""

    __tablename__ = "orders"

    order_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    #order_status =
    #order_date =


class User(db.model):
    """Users of website"""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(50), nullable=True)
    lastname = db.Column(db.String(50), nullable=True)
    username = db.Column(db.String(64), nullable=True)
    password_encypt = db.Column(db.String(64), nullable=True)
    address = db.Column(db.String(64), nullable=True)
    zipcode = db.Column(db.Integer, nullable=True)
    email = db.Column(db.String(64), nullable=True)


class Milk(db.model):
    """Milk for website"""

    __tablename__ = "milk"

    milk_id = db.Column(db.Integer, primary_key=True)
    milk_diet = db.Column(db.String(30),)
    #smoker =
    baby_age = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    price_per_oz = db.Column(db.Integer)
    #inventory =


class Order_item(db.model):
    """Items in Order"""

    __tablename__ = "order_items"

    order_item_id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.order_id'))
    milk_id = db.Column(db.Integer, db.ForeignKey('milk.milk_id'))
    quantity = db.Column(db.Integer)


class Milk_donation(db.model):
    """Milk donated to milk website"""

    __tablename__ = "milk_donation"

    milk_donation_id = db.Column(db.Integer, primary_key= True)
    diet_id = db.Column(db.String(30), db.ForeignKey('milk.milk_id'))



#Helper functions


def connect_to_db(app):
    """"Connect the database to the flask app"""