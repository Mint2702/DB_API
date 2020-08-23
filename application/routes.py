from flask import Flask

from application import app


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/home')
def home():
    return 'Home!'