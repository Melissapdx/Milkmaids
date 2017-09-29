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

    for row in open("seed_data/user.data"):
        row = row.rstrip()
        user_id, firstname, lastname, username, password, address, zipcode, email = row.split('|')
        user = User(user_id=user_id, firstname=firstname, lastname=lastname,
                    username=username, password=password, address=address, zipcode=zipcode, email=email)

        #add user to database
        db.session.add(user)
#commit user to database
    db.session.commit()


def load_milk():
    """Load items from milk data into database"""

    #Milk.query.delete()

    for row in open("seed_data/milk.data"):
        row = row.rstrip()
        milk_id, smoker, baby_age, user_id, price_per_oz, inventory, date = row.split('|')
        milk = Milk(milk_id=milk_id, smoker=smoker, baby_age=baby_age,
                    user_id=user_id, price_per_oz=price_per_oz, inventory=inventory, date=date)

        db.session.add(milk)
    db.session.commit()


def load_milk_diet():
    """"Load milk diet data"""

    #Milk_diet.query.delete()

    for row in open("seed_data/milk_diet.data"):
        row = row.rstrip()
        milk_diet_id, milk_id, diet_id = row.split('|')
        milk_diet = Milk_diet(milk_diet_id=milk_diet_id, milk_id=milk_id, diet_id=diet_id)

        db.session.add(milk_diet)
    db.session.commit()


def load_diet():
    """Load diet name information"""

    #Diet.query.delete()

    for row in open("seed_data/diet.data"):
        row = row.rstrip()
        diet_id, diet_name = row.split('|')
        diet = Diet(diet_id=diet_id, diet_name=diet_name)

        db.session.add(diet)
    db.session.commit()


def set_val_user_id():
    """Set value for the next user_id after seeding database"""

    # Get the Max user_id in the database
    result = db.session.query(func.max(User.user_id)).one()
    max_id = int(result[0])

    # Set the value for the next user_id to be max_id + 1
    query = "SELECT setval('users_user_id_seq', :new_id)"
    db.session.execute(query, {'new_id': max_id + 1})
    db.session.commit()

if __name__ == "__main__":
    connect_to_db(app)
# In case tables haven't been created, create them
    db.drop_all()
    db.create_all()

#import different types of data
    load_users()
    load_milk()
    load_diet()
    load_milk_diet()
    set_val_user_id()
