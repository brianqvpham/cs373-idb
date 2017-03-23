from flask import Blueprint, render_template
from blueprints.static_data import static_data

articles_bp = Blueprint('articles', __name__,)


@articles_bp.route('/articles/', defaults={'page' :'articles'})
@articles_bp.route('/articles/<page>')
def show_article(page):
    # if page == 'articles':
    #     return render_template('%s.html' % page)
    # else:
    print(static_data['articles'])
        # Change this when creating separate pages for articles
    return render_template('articles.html', sources=static_data['articles'])
