from flask import Blueprint, render_template
from blueprints.static_data import static_data

countries_bp = Blueprint('countries', __name__,)


@countries_bp.route('/countries/', defaults={'page' :'countries'})
@countries_bp.route('/countries/<page>')
def show_country(page):
    # if page == 'countries':
    #     return render_template('%s.html' % page)
    # else:
    print(static_data['countries'])
        # Change this when creating separate pages for countries
    return render_template('countries.html', sources=static_data['countries'])
