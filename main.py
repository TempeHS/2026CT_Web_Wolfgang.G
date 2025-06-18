from flask import Flask
from flask import render_template

from flask import Flask
from flask import render_template, request

app = Flask(__name__)

@app.route('/index.html')
@app.route('/')
def index():
        card_data = (
                ("Contact us", "Contact information and location", "contact.html", "static/images/logo.png"),
                ("What is Carcinization", "What actually is Carcinization?", "whatis.html", "static/images/logo.png"),
                ("What causes Carcinization", "Why is everything evolving into a crab exactly", "whatcauses.html", "static/images/logo.png"),
                ("Who coined the phrase Carcinization", "Who discovered it?", "who.html", "static/images/logo.png"),
             
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

@app.route('/who.html')
def who():
        return render_template("who.html"), 200

@app.route('/will.html')
def will():
        return render_template("will.html"), 200

@app.route('/why.html')
def why():
        return render_template("why.html"), 200

@app.route('/donate.html', methods=['GET', 'POST'])
def donate():
    if request.method == 'POST':
        # Here you would process the donation (e.g., save info, integrate payment gateway)
        name = request.form.get('name')
        amount = request.form.get('amount')
        # For now, just thank the user
        return render_template("donate.html", thank_you=True, name=name, amount=amount)
    return render_template("donate.html", thank_you=False)

if __name__ == '__main__':
    app.run(debug=True)