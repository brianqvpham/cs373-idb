from flask import request, render_template


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


def process_resource_page(id, Model, template):
    data = Model.get(id)
    return render_template(template, item=data)


def process_resource_list_page(Model, template):
    args = request.args.to_dict()
    args['offset'] = int(args.get('offset', 0))
    data = Model.get(None, **args)
    current_path = request.path
    prev_url = '{0}?offset={1}'.format(
        current_path, max(args['offset'] - 10, 0))
    next_url = '{0}?offset={1}'.format(current_path, args['offset'] + 10)
    return render_template(template, items=data, next_url=next_url, prev_url=prev_url)
