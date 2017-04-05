from flask import Blueprint, render_template, jsonify, request
from blueprints.static_data import static_data
from store import store
from util import process_resource_page

organizations_bp = Blueprint('organizations', __name__,)

@organizations_bp.route('/organizations/')
@organizations_bp.route('/organizations/<id>')
def show_organization(id=None):
    if id:
        template = 'organization.html'
    else:
        template = 'organizations.html'
    return process_resource_page(id, store.Organization, template, expand=['country', 'articles'])

@organizations_bp.route('/api/organizations/')
@organizations_bp.route('/api/organizations/<id>')
def get_organizations(id=None):
    args = request.args.to_dict()
    args['expand'] = request.args.getlist('expand')
    return jsonify(store.Organization().get(id, **args))
