def find(data, attr, value):
    print(value)
    return next((o for o in data if o[attr] == value), None)
