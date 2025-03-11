from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    backend_data ="Random Person"
    return render_template("index.html",front_end_data = backend_data), 200

if __name__ == '__main__':
    app.run(debug=True)