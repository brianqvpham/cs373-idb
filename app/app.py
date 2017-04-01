from flask import Flask, Blueprint, render_template
from models import db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import db
from blueprints.articles import articles_bp
from blueprints.organizations import organizations_bp
from blueprints.countries import countries_bp
from blueprints.static_data import static_data

import os
import subprocess

blueprint = Blueprint('blueprint', __name__)

@blueprint.route('/')
def index():
    data = {}
    return render_template('home.html', **data)

@blueprint.route('/about/')
def about():
    return render_template('about.html')

@blueprint.route('/tests/')
def tests():
    test_script = 'tests.py'
    script_dir = os.path.dirname(__file__)
    try:
        result = subprocess.run(['python3.5',
                                os.path.join(script_dir, test_script)],
                                stdout = subprocess.PIPE,
                                stderr=subprocess.STDOUT, check=True).stdout
    except subprocess.CalledProcessError as e:
        result = e.output
    return result.decode('utf-8')

def create_app():
    app = Flask(__name__)
    app.register_blueprint(blueprint)
    app.register_blueprint(articles_bp)
    app.register_blueprint(organizations_bp)
    app.register_blueprint(countries_bp)
    db.init_app(app)
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)

