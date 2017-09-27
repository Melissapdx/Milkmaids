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