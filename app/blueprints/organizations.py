from flask import Blueprint, render_template, jsonify, request
from blueprints.static_data import static_data
from repo import repo

organizations_bp = Blueprint('organizations', __name__,)

@organizations_bp.route('/organizations/')
@organizations_bp.route('/organizations/<id>')
def show_country(id=None):
    if (not id):
        data = static_data['sources']
        return render_template('organizations.html', organizations=data)
    else:
        organization = list(filter(lambda x: x["id"] == id, static_data['sources']))[0]
        articles = list(filter(lambda x: x["id"] in organization['articles'], static_data['articles']))
        country = list(filter(lambda x: x["id"] == organization['country'], static_data['countries']))[0]
        return render_template('organization.html', country=country, articles=articles, organization=organization)

@organizations_bp.route('/api/organizations/')
def get_organizations():
    args = request.args.to_dict()
    args['expand'] = request.args.getlist('expand')
    return jsonify(repo.get('organizations', **args))
