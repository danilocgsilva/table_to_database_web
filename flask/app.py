from flask import Flask, render_template, redirect, url_for
from model_view.Index import Index

app = Flask(__name__)

@app.route('/', endpoint='index', methods=["GET"])
def index():
    index_data = Index()
    return render_template('index.html', view_data=index_data)

@app.route('/upload', endpoint='upload', methods=["POST"])
def upload():
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
