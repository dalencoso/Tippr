from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta

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
        names = request.form.getlist('textbox')
        return render_template('addresults.html', names=names)

@app.route('/addresults', methods=["POST", "GET"])
def results():
    if request.method=='POST':
        names = request.form['textbox']
        return render_template('addresults.html', names=names)
    return render_template("addresults.html")

@app.route('/api/<name>/<token>')
def api(name, token):
    return f"<h1>{name} {token}</h1>"

if __name__ == "__main__":
    app.run(debug=True)

