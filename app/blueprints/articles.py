from flask import Blueprint, render_template, jsonify, url_for, request
from blueprints.static_data import static_data
from store import store
from util import find

articles_bp = Blueprint('articles', __name__,)


@articles_bp.route('/articles/')
@articles_bp.route('/articles/<id>')
def show_article(id=None):
    if (not id):
        return render_template('articles.html', articles=repo.get_articles())
    else:
        article = repo.get_article(id)
        organizations = repo.get_organizations()
        organization = find(organizations, 'id', article['org_id'])
        print(organization)
        countries = repo.get_countries()
        countries = [find(countries, 'id', country_id) for country_id in article['countries']]
        return render_template('article.html', article=article, organization=organization, countries=countries)


@articles_bp.route('/api/articles/')
@articles_bp.route('/api/articles/<id>')
def get_articles(id=None):
    args = request.args.to_dict()
    args['expand'] = request.args.getlist('expand')
    return jsonify(store.Article().get(id, **args))


