# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
import model as m

# -- Initialization section --
app = Flask(__name__)

# -- Routes section --
@app.route('/')
@app.route('/index', methods=["GET", "POST"])
# write an app that takes in two words and renders them in some stylistic way
def index():
    if request.method == "GET":
        return render_template("index.html")
    else:
        print(request.form)
        word1 = m.result(request.form["first"], request.form["firstStyle"])
        word2 = m.result(request.form["second"], request.form["secondStyle"])
        return render_template("index.html", firstWord=word1, secondWord=word2)

# future fixes?