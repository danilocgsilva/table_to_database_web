from flask import render_template, redirect, url_for, Flask
from connection_string import connection_string

flask_app = Flask(__name__)

flask_app.config['SQLALCHEMY_DATABASE_URI'] = connection_string
flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
