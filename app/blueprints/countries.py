from flask import Blueprint, render_template, jsonify, request
from blueprints.static_data import static_data
from store import store

countries_bp = Blueprint('countries', __name__,)

@countries_bp.route('/countries/')
@countries_bp.route('/countries/<id>')
def show_country(id=None):
    if (not id):
        data = store.Country().get(None)
        return render_template('countries.html', items=data)
    else:
        data = store.Country().get(id, expand=['articles', 'organizations'])
        return render_template('country.html', item=data)

@countries_bp.route('/api/countries/')
@countries_bp.route('/api/countries/<id>')
def get_countries(id=None):
    args = request.args.to_dict()
    args['expand'] = request.args.getlist('expand')
    return jsonify(store.Country().get(id, **args))
