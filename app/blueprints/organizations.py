from flask import Blueprint, render_template, jsonify, request
from blueprints.static_data import static_data
from store import store

organizations_bp = Blueprint('organizations', __name__,)

@organizations_bp.route('/organizations/')
@organizations_bp.route('/organizations/<id>')
def show_organization(id=None):
    if (not id):
        data = store.Organization().get(None)
        return render_template('organizations.html', items=data)
    else:
        data = store.Organization().get(id, expand=['articles', 'country'])
        return render_template('organization.html', item=data)

@organizations_bp.route('/api/organizations/')
@organizations_bp.route('/api/organizations/<id>')
def get_organizations(id=None):
    args = request.args.to_dict()
    args['expand'] = request.args.getlist('expand')
    return jsonify(store.Organization().get(id, **args))
