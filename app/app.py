from flask import Flask
from models import db

def create_app():
    app = Flask(__name__)
    db.init_app(app)

if __name__ == '__main__':
    app = create_app()

