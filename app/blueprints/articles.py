from flask import Blueprint, render_template, jsonify
from blueprints.static_data import static_data
from repo import repo
from util import find

articles_bp = Blueprint('articles', __name__,)


@articles_bp.route('/articles/')
@articles_bp.route('/articles/<id>')
def show_article(id=None):
    if (not id):
        return render_template('articles.html', articles=repo.get_articles())
    else:
        article = repo.get_article(id)
        print(article)
        organizations = repo.get_organizations()
        organization = find(organizations, 'id', article['id'])
        countries = repo.get_countries()
        country = [find(countries, 'id', country_id) for country_id in article['countries']]
        return render_template('article.html', article=article, organization=organization)

@articles_bp.route('/api/articles/')
def get_articles():
    return jsonify(repo.get_articles())
