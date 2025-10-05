from flask import render_template, redirect, url_for, request
from model_view.Index import Index
from model_view.Registration import Registration
from model_view.Sidebar import Sidebar
from flask_app import flask_app
from repositories.DatabaseRepository import DatabaseRepository
from db import db
from models.Database import Database

@flask_app.route('/', endpoint='index', methods=["GET"])
def index():
    index_data = Index()
    return render_template(
        'index.html',
        view_data=index_data,
        sidebar=Sidebar()
    )

@flask_app.route('/upload', endpoint='upload', methods=["POST"])
def upload():
    return redirect(url_for('index'))

@flask_app.route('/registration', endpoint='registration', methods=['GET'])
def registration():
    registration_data = Registration()
    return render_template(
        'registration.html', 
        view_data=registration_data, 
        sidebar=Sidebar()
    )

@flask_app.route('/registration', endpoint='registration_persists', methods=['POST'])
def registration_persists():
    username = request.form['username']
    password = request.form['password']
    host = request.form['host']
    database_name = request.form['database']
    friendly_name = request.form['database']
    
    database_repository = DatabaseRepository(db.session)
    
    database = Database(
        user_name=username,
        password=password,
        host=host,
        database_name=database_name,
        friendly_name=friendly_name
    )
    
    database_repository.create(database)
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    flask_app.run(debug=True)
