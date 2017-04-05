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

def process_resource_page(id, Model, template, expand=[]):
    if (not id):
        args = request.args.to_dict()
        offset = int(args.get('offset', 0))
        data = Model().get(None, **args)
        current_path = request.path
        prev_url = '{0}?offset={1}'.format(current_path, max(offset - 10, 0))
        next_url = '{0}?offset={1}'.format(current_path, offset + 10)
        return render_template(template, items=data, next_url=next_url, prev_url=prev_url)
    else:
        data = Model().get(id, expand=expand)
        return render_template(template, item=data)

