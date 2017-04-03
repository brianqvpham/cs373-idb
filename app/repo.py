import pickle
import os
import copy
from util import find, map_model

class PickleRepo():
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
                    expanded = [self.get(f, id=x["id"]) for x in field]
                else:
                    expanded = self.get(f, id=field["id"])
                o[f] = expanded

    def get(self, model, **kwargs) :
        model = map_model(model)
        resource = self.data[model]
        if 'id' in kwargs:
            resource = copy.deepcopy(find(resource, 'id', kwargs['id']))
        else:
            resource = copy.deepcopy(resource)
        if 'expand' in kwargs:
            self.expand(resource, kwargs['expand'])
        return resource

repo = PickleRepo()




