from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(15000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))   


#In this class we will define id and email for user
class User(db.Model, UserMixin):
    #User will be defined by id in order to see the difference between people with the same second name 
    id = db.Column(db.Integer, primary_key=True) 
    #email must be unique
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String)
    notes = db.relationship('Note')
