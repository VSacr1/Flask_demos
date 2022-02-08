# Import everything we need 
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
import os 

#Declaring Flask object 
app = Flask(__name__)

# Set the connection string to connect to a database
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

# Declaring SQLAlchemy object
db = SQLAlchemy(app)

# Defining our tables 
class Countries(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable = False)
    cities = db.relationship('Cities', backref='country')

class Cities(db.Model):
    id = db.Column(db.Integer, primary_key = True )
    name = db.Column(db.String(30), nullable=False)
    country_id = db.Column(db.Integer, db.ForeignKey('countries.id'), nullable=False)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')