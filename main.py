from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/index.html')
@app.route('/')
def index():
        card_data = (
                ("Contact us", "Contact information and location", "contact.html", "static/images/logo.png"),
                ("What is Carcinization", "What actually is Carcinization?", "whatis.html", "static/images/logo.png"),
                ("What causes Carcinization", "Why is everything evolving into a crab exactly", "whatcauses.html", "static/images/logo.png"),
                ("Who coined the phrase Carcinization", "Who discovered it?", "Take me there", "static/images/logo.png"),
                ("Will humans evolve into crabs", "And how soon will they?", "Take me there", "static/images/logo.png"),
                ("Why should I care", "What affect does this even have on humanity", "Take me there", "static/images/logo.png"),
        ) 
        return render_template("index.html", cards=card_data), 200

@app.route('/contact.html')
def contact():
        return render_template("contact.html"), 200

@app.route('/sources.html')
def sources():
        return render_template("sources.html"), 200

@app.route('/whatis.html')
def whatis():
        return render_template("whatis.html"), 200

@app.route('/whatcauses.html')
def whatcauses():
        return render_template("whatcauses.html"), 200


if __name__ == '__main__':
    app.run(debug=True)