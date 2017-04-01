import pickle
import os

class PickleRepo():
    def __init__(self):
        self.pickle_folder = os.path.dirname(__file__) + '/data'

    def get_articles(self):
        articles = pickle.load(open(self.pickle_folder + '/articles.pickle', 'rb'))
        print(articles)
        return articles

repo = PickleRepo()




