from flask import Blueprint, render_template, jsonify, request
from blueprints.static_data import static_data
from store import store
from util import process_resource_page, process_resource_list_page

organizations_bp = Blueprint('organizations', __name__,)

@organizations_bp.route('/organizations/', methods=['GET'])
def show_organizations():
    template = 'organizations.html'
    return process_resource_list_page(store.OrganizationStore(), template)

@organizations_bp.route('/organizations/<id>', methods=['GET'])
def show_organization(id):
    template = 'organization.html'
    return process_resource_page(id, store.OrganizationStore(), template)

@organizations_bp.route('/api/organizations/')
@organizations_bp.route('/api/organizations/<id>')
def get_organizations(id=None):
    args = request.args.to_dict()
    args['expand'] = request.args.getlist('expand')
    return jsonify(store.OrganizationStore().get(id, **args))
