from flask import Blueprint, render_template, jsonify, url_for, request
from blueprints.static_data import static_data
from store import store
from util import process_resource_page

articles_bp = Blueprint('articles', __name__,)


@articles_bp.route('/articles/')
@articles_bp.route('/articles/<id>')
def show_article(id=None):
    if id:
        template = 'article.html'
    else:
        template = 'articles.html'
    return process_resource_page(id, store.Article, template, expand=['organization', 'countries'])

@articles_bp.route('/api/articles/')
@articles_bp.route('/api/articles/<id>')
def get_articles(id=None):
    args = request.args.to_dict()
    args['expand'] = request.args.getlist('expand')
    return jsonify(store.Article().get(id, **args))


