from flask import Flask, render_template
from model_view.Index import Index

app = Flask(__name__)

@app.route('/')
def index():
    index_data = Index()
    return render_template('index.html', view_data=index_data)

if __name__ == '__main__':
    app.run(debug=True)
