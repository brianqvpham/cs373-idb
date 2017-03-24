from flask import Blueprint, render_template
from blueprints.static_data import static_data

articles_bp = Blueprint('articles', __name__,)


@articles_bp.route('/articles/')
@articles_bp.route('/articles/<id>')
def show_article(id=None):
    if (not id):
        data = static_data['articles']
        return render_template('articles.html', articles=data)
    else:
        # Find correct country in countrys list
        print(id)
        article = list(filter(lambda x: x["id"] == id, static_data['articles']))[0]
        countries = list(filter(lambda x: x["id"] in article['countries'], static_data['countries']))
        organization = list(filter(lambda x: x["id"] == article['source'], static_data['sources']))[0]
        return render_template('article.html', countries=countries, article=article, organization=organization)
