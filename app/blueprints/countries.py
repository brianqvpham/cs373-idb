from flask import Blueprint, render_template, jsonify, request
from blueprints.static_data import static_data
from store import store
from util import process_resource_page, process_resource_list_page

countries_bp = Blueprint('countries', __name__,)

@countries_bp.route('/countries/', methods=['GET'])
def show_countries():
    template = 'countries.html'
    return process_resource_list_page(store.CountryStore(), template)

@countries_bp.route('/countries/<id>', methods=['GET'])
def show_country(id):
    template = 'country.html'
    return process_resource_page(id, store.CountryStore(), template)

@countries_bp.route('/api/countries/')
@countries_bp.route('/api/countries/<id>')
def get_countries(id=None):
    args = request.args.to_dict()
    return jsonify(store.CountryStore().get(id, **args))
