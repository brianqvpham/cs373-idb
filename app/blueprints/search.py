from flask import Blueprint, render_template, jsonify, url_for, request
from store import store

search_bp = Blueprint('search', __name__,)

def fill(data, baseURL):
    ands = [{
        **o,
        "link": "{}/{}".format(baseURL, o["id"]),
    } for o in data["and"]]
    ors = [{
        **o,
        "link": "{}/{}".format(baseURL, o["id"]),
    } for o in data["or"]]

    return {
            "and": ands,
            "or": ors
            }


@search_bp.route('/api/search')
def search_route():
    query = request.args.get('query', '')
    return jsonify(search(query))


def search(query=None):
    words = query.split(' ')

    organizations = store.OrganizationStore().search(words)
    organizations = fill(organizations, '/api/organizations')
    articles = store.ArticleStore().search(words)
    articles = fill(articles, '/api/articles')
    countries = store.CountryStore().search(words)
    countries = fill(countries, '/api/countries')

    return {
        "and": {
            "organizations": organizations["and"],
            "articles": articles["and"],
            "countries": countries["and"]
            },
        "or": {
            "organizations": organizations["or"],
            "articles": articles["or"],
            "countries": countries["or"]
            }
        }

