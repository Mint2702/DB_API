from flask import Flask

app = Flask(__name__)

from application import routes

app.run(debug=True)