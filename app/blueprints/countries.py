from flask import Blueprint, render_template
from blueprints.static_data import static_data

countries_bp = Blueprint('countries', __name__,)

@countries_bp.route('/countries/')
@countries_bp.route('/countries/<id>')
def show_country(id=None):
    if (not id):
        data = static_data['countries']
        return render_template('countries.html', countries=data)
    else:
        country = list(filter(lambda x: x["id"] == id, static_data['countries']))[0]
        articles = list(filter(lambda x: x["id"] in country['articles'], static_data['articles']))
        sources = list(filter(lambda x: x["id"] in country['sources'], static_data['sources']))
        return render_template('country.html', country=country, articles=articles, sources=sources)
