from flask import render_template, redirect, url_for, Flask
from model_view.Index import Index
from model_view.Registration import Registration
from db import connection_string
from flask_sqlalchemy import SQLAlchemy

flask_app = Flask(__name__)

flask_app.config['SQLALCHEMY_DATABASE_URI'] = connection_string
flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(flask_app)

@flask_app.route('/', endpoint='index', methods=["GET"])
def index():
    index_data = Index()
    return render_template('index.html', view_data=index_data)

@flask_app.route('/upload', endpoint='upload', methods=["POST"])
def upload():
    return redirect(url_for('index'))

@flask_app.route('/registration', endpoint='registration', methods=['GET'])
def registration():
    registration_data = Registration()
    return render_template('registration.html', view_data=registration_data)

if __name__ == '__main__':
    flask_app.run(debug=True)
