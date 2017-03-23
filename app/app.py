from flask import Flask, Blueprint, render_template
from models import db
from blueprints.articles import articles_bp
from blueprints.sources import sources_bp
from blueprints.countries import countries_bp

blueprint = Blueprint('blueprint', __name__)


@blueprint.route('/')
#@blueprint.route('/<page>')
def index(page='home'):
    data = {}
    return render_template('{0}.html'.format(page), **data)


def create_app():
    app = Flask(__name__)
    app.register_blueprint(blueprint)
    app.register_blueprint(articles_bp)
    app.register_blueprint(sources_bp)
    app.register_blueprint(countries_bp)
    db.init_app(app)
    return app

if __name__ == "__main__":
    app = create_app()
    app.run()
