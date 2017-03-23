from flask import Blueprint, render_template

countries_bp = Blueprint('countries', __name__,)


@countries_bp.route('/countries/', defaults={'page' :'countries'})
@countries_bp.route('/countries/<page>')
def show_country(page):
    if page == 'countries':
        return render_template('%s.html' % page)
    else:
        # Change this when creating separate pages for countries
        return render_template('countries.html')
