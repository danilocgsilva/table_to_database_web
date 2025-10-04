from flask import Flask, render_template, redirect, url_for
from model_view.Index import Index
from model_view.Registration import Registration

app = Flask(__name__)

@app.route('/', endpoint='index', methods=["GET"])
def index():
    index_data = Index()
    return render_template('index.html', view_data=index_data)

@app.route('/upload', endpoint='upload', methods=["POST"])
def upload():
    return redirect(url_for('index'))

@app.route('/registration', endpoint='registration', methods=['GET'])
def registration():
    registration_data = Registration()
    return render_template('registration.html', view_data=registration_data)

if __name__ == '__main__':
    app.run(debug=True)
