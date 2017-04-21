from flask import request, render_template, redirect


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
    args['page'] = int(args.get('page', 0))
    args['limit'] = int(args.get('limit', 10))
    data = Model.get(None, **args)
    current_path = request.path
    prev_url = '{0}?page={1}&limit={2}'.format(
        current_path, max(args['page'] - 1, 0), args['limit'])
    next_url = '{0}?page={1}&limit={2}'.format(current_path, args['page'] + 1, args['limit'])
    page = args['page']
    pages = range(max(page - 2, 0), page+3)
    page_links = []
    for n in pages:
        page_links.append({
            "num": n + 1,
            "link": '{0}?page={1}&limit={2}'.format(current_path, n, args['limit']),
            "className": 'active' if n == page else ''
            })
    return render_template(template, items=data, next_url=next_url, prev_url=prev_url, page_links=page_links)






