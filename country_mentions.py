
import pickle

# articles will be a list of dicts
article_list = pickle.load( open( "articles.pickle", "rb" ) ) 

countries_list = pickle.load( open( "countries.pickle", "rb" ) )




list_of_countries = 

for ar in article_list:
    description = ar["description"]
    countries_mentioned = get_mentions(description)
    

def get_mentions(description):
    # parse description
    # loop through words in description & check if they are in the list of countries
