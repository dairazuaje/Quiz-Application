from flask import Flask, render_template
from data.db import test_function

app = Flask(__name__)

# Routes to the home page
@app.route("/")
def home():
    test_function()
    return render_template("index.html")

@app.route("/addcard")
def add_card():
    return render_template("addcard.html")

app.run(debug=True)