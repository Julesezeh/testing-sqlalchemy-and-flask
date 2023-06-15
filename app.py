from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Log(db.Model):
    id =  db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, unique=True)
    date = db.Column(db.DateTime)
    
@app.route("",methods=["GET"])
def index():
    pass 

