import os
from flask_sqlalchemy import SQLAlchemy

database_username = os.environ.get('DATABASE_USERNAME')
database_password = os.environ.get('DATABASE_PASSWORD')
database_name = os.environ.get('DATABASE_NAME')
database_host = os.environ.get('DATABASE_HOST')
connection_string = f"mysql://{database_username}:{database_password}@{database_host}:3306/{database_name}"
