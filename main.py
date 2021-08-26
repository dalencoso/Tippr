from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
import math

def round_down(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n * multiplier) / multiplier

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/login")
def login():
    if request.method=='POST':
        username = request.form['email']
        password = request.form['psw']
        return render_template('loginboot.html', user=username, pword=password)
    return render_template("loginboot.html")

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route("/add", methods=["POST", "GET"])
def add():
    if request.method=='GET':
        return render_template("add.html")
    if request.method=='POST':
        names = request.form.getlist('names')
        hours = request.form.getlist('hoursworked')
        totaltips = request.form['tips']
        totalhours = 0.0
        for hour in hours:
            totalhours = totalhours + float(hour)

        tipsperhour = float(totaltips)/totalhours

        personaltips = []
        count = 0
        for a in range(len(names)):
            personaltips.append(round_down(tipsperhour * float(hours[a]), 2))

        data = zip(names, personaltips)
        data = list(data)


        return render_template('addresults.html', data=data, totalhours=totalhours, totaltips=totaltips)

@app.route('/addresults', methods=["POST", "GET"])
def results():
    if request.method=='POST':
        names = request.form['textbox']
        return render_template('addresults.html', names=names, tips=tips)
    return render_template("addresults.html")

if __name__ == "__main__":
    app.run(debug=True)

