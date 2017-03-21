"""
Requests articles for every news source.
Stores article metadata in pickle file.
Articles stored as dicts.
"""

import urllib.request
import json
import pickle

api_link = "https://newsapi.org/v1/articles?source=" # Put source link here
api_key = "0291a4046bac4b3cb5429fd129fb37fa"
output_pickle_name = "articles.pickle" # Put pickle file name here
input_sources = "sources.pickle"



if __name__ == "__main__":
    articles = []
    sources = pickle.load(open(input_sources, 'rb'))
    for s in sources:
        # Construct api url to pull articles from
        url = api_link + s["id"]    # Add source id to url
        url = url + "&apiKey=" + api_key    # Add api key to url
       
        try:
            # Make api request
            req = urllib.request.Request(url)
            response = urllib.request.urlopen(req)
            string = response.read().decode('utf-8')
            json_obj = json.loads(string)
            returned_articles = json_obj["articles"]
            for article in returned_articles:
                # Iterate through list of returned articles.
                # Add them to our articles list.
                article["source"] = s["name"]     # Add source field to article
                article["country"] = s["country"]    # Add country field to article
                articles.append(article)
        except Exception as e:
            print("Caught exception while requesting articles.")
            print(str(e))
            break
    print(articles)
    with open(output_pickle_name, 'wb') as f:
        pickle.dump(articles, f)
    
