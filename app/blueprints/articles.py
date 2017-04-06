from flask import Blueprint, render_template, jsonify, url_for, request
from blueprints.static_data import static_data
from store import store
from util import process_resource_page, process_resource_list_page

articles_bp = Blueprint('articles', __name__,)

@articles_bp.route('/articles/', methods=['GET'])
def show_articles():
    template = 'articles.html'
    return process_resource_list_page(store.ArticleStore(), template)

@articles_bp.route('/articles/<id>')
def show_article(id=None):
    template = 'article.html'
    return process_resource_page(id, store.ArticleStore(), template)

@articles_bp.route('/api/articles/')
@articles_bp.route('/api/articles/<id>')
def get_articles(id=None):
    args = request.args.to_dict()
    return jsonify(store.ArticleStore().get(id, **args))


