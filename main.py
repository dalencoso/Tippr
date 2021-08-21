from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/add", methods=["POST", "GET"])
def add():
    if request.method=='GET':
        return render_template("addtest.html")
    if request.method=='POST':
        names = request.form['mytext[]']
        return render_template('addresults.html', names=names)

@app.route('/addresults', methods=["POST", "GET"])
def results():
    if request.method=='GET':
        return render_template("addresults.html")
    if request.method=='POST':
        names = request.form['flname']
        return render_template('addresults.html', names=names)








if __name__ == "__main__":
    app.run(debug=True)

