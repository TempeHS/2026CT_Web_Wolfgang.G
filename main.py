from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/index.html')
@app.route('/')
def index():
        card_data = (
                ("What is Carcinization", "Lorem Ipsum", "Take me there", "Static/images/logo.png"),
                ("What is Carcinization", "Lorem Ipsum", "Take me there", "Static/images/logo.png"),
                ("What is Carcinization", "Lorem Ipsum", "Take me there", "Static/images/logo.png"),
                ("What is Carcinization", "Lorem Ipsum", "Take me there", "Static/images/logo.png"),
                ("What is Carcinization", "Lorem Ipsum", "Take me there", "Static/images/logo.png"),
                ("What is Carcinization", "Lorem Ipsum", "Take me there", "Static/images/logo.png"),
        ) 
        return render_template("index.html", cards=card_data), 200

if __name__ == '__main__':
    app.run(debug=True)