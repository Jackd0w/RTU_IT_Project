from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()
DB_NAME = "database.db"

def create():

    app = Flask(__name__, template_folder='templates')
    app.config['SECRET_KEY'] = 'qkjkdgnsdfrjgakdsfmn'
    app.config['SQL_Alchemy_URI'] = f'sqlite:///{DB_NAME}'


    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    from .models import User, Note

    return app

    def create_database(app):
        if not path('website/' + DB_NAME):
            db.create_all(app=app)
            print("Create Database")