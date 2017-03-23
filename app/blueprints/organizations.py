from flask import Blueprint, render_template
from blueprints.static_data import static_data

organizations_bp = Blueprint('organizations', __name__,)


@organizations_bp.route('/organizations/', defaults={'page' :'organizations'})
@organizations_bp.route('/organizations/<page>')
def show_org(page):
    # if page == 'organizations':
        # return render_template('%s.html' % page)
    # else:
    print(static_data['sources'])
    # Change this when creating separate pages for organizations
    return render_template('organizations.html', sources=static_data['sources'])
    # return 'hey'
