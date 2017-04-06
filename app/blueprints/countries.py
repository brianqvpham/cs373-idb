from flask import Blueprint, render_template, jsonify, request
from blueprints.static_data import static_data
from store import store
from util import process_resource_page

countries_bp = Blueprint('countries', __name__,)

@countries_bp.route('/countries/')
@countries_bp.route('/countries/<id>')
def show_country(id=None):
    if id:
        template = 'country.html'
    else:
        template = 'countries.html'
    return process_resource_page(id, store.CountryStore(), template, expand=['articles', 'organizations'])

@countries_bp.route('/api/countries/')
@countries_bp.route('/api/countries/<id>')
def get_countries(id=None):
    args = request.args.to_dict()
    args['expand'] = request.args.getlist('expand')
    json = jsonify(store.CountryStore().get(id, **args))
    print(3)
    return json
