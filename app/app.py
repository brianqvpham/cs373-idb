from flask import Flask, Blueprint
from models import db

blueprint = Blueprint('blueprint', __name__)

@blueprint.route('/')
def index():
    return "Hello World!"

def create_app():
    app = Flask(__name__)
    app.register_blueprint(blueprint)
    db.init_app(app)
    return app

if __name__ == "__main__":
    app = create_app()
    app.run()

