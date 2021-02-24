from flask import Flask

def create():
    app = Flask(__name__, template_folder='templates')
    app.config['SECRET_KEY'] = 'qkjkdgnsdfrjgakdsfmn'

    return app