from flask import Blueprint, render_template, jsonify, url_for, request
from store import store

search_bp = Blueprint('search', __name__,)

def fill(data, baseURL):
    ret = []
    print(data)
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

# @search_bp.route('/search')
def search(query):
    # words = request.args.get('query', '').split(',')
    words = query.split(',')

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

def and_f(attr, fields):
    for field in fields:
        if all(word in o[field] for word in words):
            return True
    return False

def get_and_results(words, data, *fields):
    def f(o):
        for field in fields:
            if all(word in o[field] for word in words):
                return True
        return False
    return list(filter(f, data))

def get_or_results(words, data, *fields):
    def f(o):
        for field in fields:
            if any(word in o[field] for word in words):
                return True
        return False
    return list(filter(f, data))


