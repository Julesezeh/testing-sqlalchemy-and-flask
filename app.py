from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

db = SQLAlchemy(app)

@app.route("",methods=["GET"])
def index():
    pass 

