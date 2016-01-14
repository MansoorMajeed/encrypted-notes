from flask import render_template
from app import app
from app import models

app.config.from_object('config')

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/login')
def login():
    return "login"

@app.route('/signup')
def signup():
    return "signup"

@app.route('/notes')
def notes():
    return "your notes"


