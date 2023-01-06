from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def first_flask():
    return "My first Flask Framework!"

@app.route("/1")
def first_flask_1():
    return "First route in Flask!"  

@app.route("/2")
def first_flask_math():
    equation = 4 ** 5
    return str(equation)      

@app.route("/3")
def html_page():
    return render_template("flask.html")   
 