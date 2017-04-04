import pickle
import os
import copy
from util import find, map_model

class PickleStore():
    def __init__(self):
        self.pickle_file = os.path.dirname(__file__) + '/data/data.pickle'
        self.data = pickle.load(open(self.pickle_file, 'rb'))

    def expand(self, model, fields):
        if type(model) is not list:
            model = [model]
        for o in model:
            for f in fields:
                field = o[f]
                if type(field) is list:
                    expanded = [PickleStore.get(self, f, x["id"]) for x in field]
                else:
                    expanded = PickleStore.get(self, f, field["id"])
                o[f] = expanded

    def get(self, model, id, **kwargs):
        model = map_model(model)
        resource = self.data[model]
        if id:
            resource = copy.deepcopy(find(resource, 'id', id))
        else:
            resource = copy.deepcopy(resource)
        if 'expand' in kwargs:
            self.expand(resource, kwargs['expand'])
        return resource

class Article(PickleStore):
    def __init__(self):
        super().__init__()

    def get(self, id, **kwargs):
        return super().get('articles', id, **kwargs)

class Organization(PickleStore):
    def __init__(self):
        super().__init__()

    def get(self, id, **kwargs):
        return super().get('organizations', id, **kwargs)

class Country(PickleStore):
    def __init__(self):
        return super().__init__()

    def get(self, id, **kwargs):
        return super().get('countries', id, **kwargs)

