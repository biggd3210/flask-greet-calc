from flask import Flask, request

app = Flask(__name__)

@app.route('/welcome')
def general_welcome():
    return "welcome"

@app.route('/welcome/home')
def welcome_home():
    return "welcome home"

@app.route('/welcome/back')
def welcome_back():
    return "welcome back"