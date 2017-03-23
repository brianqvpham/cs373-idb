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
        # Find correct article in articles list
        data = list(filter(lambda x: x["id"] == id, static_data['articles']))[0]
        return render_template('article.html', article=data)
