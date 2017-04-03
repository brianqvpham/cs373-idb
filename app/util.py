def map_model(model):
    map = {
        "country": "countries",
        "countries": "countries",
        "organization": "organizations",
        "organizations": "organizations",
        "article": "articles",
        "articles": "articles"
    }
    return map[model]

def find(data, attr, value):
    return next((o for o in data if o[attr] == value), None)
