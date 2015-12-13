from flask import render_template
from app import app
from app import models

app.config.from_object('config')


@app.route('/index')
def index():
    return "Hello"
