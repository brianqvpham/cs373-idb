from flask import Blueprint, render_template

organizations_bp = Blueprint('organizations', __name__,)


@organizations_bp.route('/organizations/', defaults={'page' :'organizations'})
@organizations_bp.route('/organizations/<page>')
def show_source(page):
    if page == 'organizations':
        return render_template('%s.html' % page)
    else:
        # Change this when creating separate pages for organizations
        return render_template('organizations.html')
