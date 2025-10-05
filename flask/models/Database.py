from db import db

class Database(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    host = db.Column(db.String(255), nullable=False)
    database_name = db.Column(db.String(255), nullable=False)
    friendly_name = db.Column(db.String(255), nullable=False)
