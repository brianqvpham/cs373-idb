import pickle
import os
from util import find

class PickleRepo():
    def __init__(self):
        self.pickle_file = os.path.dirname(__file__) + '/data/data.pickle'
        self.data = pickle.load(open(self.pickle_file, 'rb'))

    def get_articles(self):
        return self.data['articles']

    def get_article(self, id):
        articles = self.get_articles()
        article = find(articles, 'id', id)
        print(article)
        return article

    def get_organizations(self):
        return self.data['organizations']

    def get_countries(self):
        return self.data['countries']


repo = PickleRepo()




