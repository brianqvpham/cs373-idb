from flask import Blueprint, render_template

sources_bp = Blueprint('sources', __name__,)


@sources_bp.route('/sources/', defaults={'page' :'sources'})
@sources_bp.route('/sources/<page>')
def show_source(page):
    if page == 'sources':
        return render_template('%s.html' % page)
    else:
        # Change this when creating separate pages for sources
        return render_template('sources.html')
