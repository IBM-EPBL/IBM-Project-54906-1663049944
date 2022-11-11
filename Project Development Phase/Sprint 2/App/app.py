from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "ABC@123"

@app.route("/")
def index():
  return render_template("index.html")
  
@app.route("/login")
def login():
  return render_template("login.html")
