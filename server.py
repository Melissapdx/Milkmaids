""""Milk donation website"""
from jinja2 import StrictUndefined

from flask import (Flask, jsonify, render_template,
                redirect, request, flash, session)
from flask_debugtoolbar import DebugToolbarExtension

from model import connect_to_db, db, Order,User,Milk,Order_item,Milk_diet,Diet