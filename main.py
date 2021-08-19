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
    return render_template("add.html")

if __name__ == "__main__":
    app.run(debug=True)

