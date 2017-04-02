import pickle
import os

class PickleRepo():
    def __init__(self):
        self.pickle_file = os.path.dirname(__file__) + '/data/data.pickle'

    def get_articles(self):
        return pickle.load(open(self.pickle_file, 'rb'))['articles']

    def get_organizations(self):
        return pickle.load(open(self.pickle_file, 'rb'))['organizations']

    def get_countries(self):
        return pickle.load(open(self.pickle_file, 'rb'))['countries']


repo = PickleRepo()




