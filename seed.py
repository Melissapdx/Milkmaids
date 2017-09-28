""""File to seed database from seed_data"""

from sqlalchemy import func
from model import Order
from model import User
from model import Milk
from model import Order_item
from model import Milk_diet
from model import Diet

from model import connect_to_db, db
from server import app
from datetime import datetime


def load_users():
    """"Load users from user.data into database"""
    print "User"
    User.query.delete()

    for row in open("seed_data/user.data"):
        row = row.rstrip()
        print row
        user_id, firstname, lastname, username, password, address, zipcode, email = row.split('|')
        user = User(user_id=user_id, firstname=firstname, lastname=lastname,
        username=username, password=password, address=address, zipcode=zipcode, email=email)

        #add user to database
        db.session.add(user)
#commit user to database
    db.session.commit()

if __name__ == "__main__":
    connect_to_db(app)
# In case tables haven't been created, create them
    db.create_all()

#import different types of data
    load_users()
