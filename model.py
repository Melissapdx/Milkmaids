"""Model and database functions for Milkmaids"""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Order(db.Model):
    """Orders for website"""

    __tablename__ = "orders"

    order_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    order_status = db.Column(db.String(30))
    order_date = db.Column(db.DateTime)
    total_price = db.Column(db.Integer)

    #define relationship to user
    user = db.relationship("User", backref="orders")

    def __repr__(self):
        """Provide representation when printed"""

        return "<Order order_id=%s user_id=%s order_status=%s order_date=%s>" % (self.order_id, self.user_id, self.order_status, self.order_date)


class User(db.Model):
    """Users of website"""

    __tablename__ = "users"

    user_id = db.Column(db.Integer,autoincrement=True, primary_key=True)
    firstname = db.Column(db.String(50), nullable=True)
    lastname = db.Column(db.String(50), nullable=True)
    username = db.Column(db.String(64), nullable=True)
    password = db.Column(db.String(64), nullable=True)
    address = db.Column(db.String(64), nullable=True)
    zipcode = db.Column(db.Integer, nullable=True)
    email = db.Column(db.String(64), nullable=True)

    def __repr__(self):
        """Provide representation when printed"""

        return "<User user_id=%s firstname=%s lastname=%s username=%s password=%s address=%s zipcode=%s email=%s>" % (self.user_id, self.firstname, self.lastname, self.username, self.password, self.address, self.zipcode, self.email)


class Milk(db.Model):
    """Milk donations for website"""

    __tablename__ = "milk"

    milk_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    smoker = db.Column(db.Boolean)
    baby_age = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    price_per_oz = db.Column(db.Integer)
    inventory = db.Column(db.Integer)
    date = db.Column(db.DateTime)

    #define relationship to user
    user = db.relationship("User", backref="milk")

    def __repr__(self):
        """Provide representation when printed"""

        return "<Milk milk_id=%s smoker=%s baby_age=%s user_id=%s price_per_oz=%s inventory=%s date=%s>" % (self.milk_id, self.smoker, self.baby_age, self.user_id, self.price_per_oz, self.inventory, self.date)


class Order_item(db.Model):
    """Items in Order"""

    __tablename__ = "order_items"

    order_item_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.order_id'))
    milk_id = db.Column(db.Integer, db.ForeignKey('milk.milk_id'))
    quantity = db.Column(db.Integer)

    #define relationship to user
    milk_order = db.relationship("Order", backref="order_items")
    milk_item = db.relationship("Milk", backref="order_items")

    def __repr__(self):
        """Provide representation when printed"""

        return "<Order_item order_item_id=%s order_id=%s milk_id=%s quantity=%s>" % (self.order_item_id, self.order_id, self.milk_id, self.quantity)


class Milk_diet(db.Model):
    """Milk donated to milk website"""

    __tablename__ = "milk_diet"

    milk_diet_id = db.Column(db.Integer,autoincrement=True, primary_key=True)
    milk_id = db.Column(db.Integer, db.ForeignKey('milk.milk_id'))
    diet_id = db.Column(db.Integer, db.ForeignKey('diet.diet_id'))

    #define relationship to user
    milk = db.relationship("Milk", backref="milk_diet")
    milk_diet = db.relationship("Diet", backref="milk_diet")

    def __repr__(self):
        """Provide representation when printed"""
        return "<Milk_diet milk_diet_id=%s milk_id=%s diet_id=%s>" % (self.milk_diet_id, self.milk_id, self.diet_id)


class Diet(db.Model):
    """Stores diet information about milk"""

    __tablename__ = "diet"

    diet_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    diet_name = db.Column(db.String(64))

    def __repr__(self):
        """Provide representation when printed"""

        return "<Diet diet_id=%s,diet_name=%s>" % (self.diet_id, self.diet_name)


#Helper functions
def example_data():
    """Example data for tests.py"""
    user = User(email="person@gmail.com",
                password="admin")
    db.session.add(user)
    db.session.commit()


def connect_to_db(app,db_uri="postgresql:///milkmaids"):
    """"Connect the database to the flask app"""

    #Configure to PstgresSql database
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    from server import app
    connect_to_db(app)
    print "Connected to db"
