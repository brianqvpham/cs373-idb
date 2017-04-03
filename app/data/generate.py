import urllib.request
import json
import pickle
import os
import uuid

path = os.path.abspath(__file__)
dir_path = os.path.dirname(path)

country_to_name = {"au" : "Australia", "de" : "Germany",
                   "gb" : "United Kingdom of Great Britain and Northern Ireland",
                   "in" : "India",
                   "it" : "Italy",
                   "us" : "United States of America"}

def find(data, attr, value):
    return next((o['id'] for o in data if o[attr] == value), None)

def get_country_mentions(des, countries):
    country_names = [c['name'] for c in countries]
    mentions = []
    if des:
        for word in des.split():
            if word in countries:
                mentions.append(word)
    return [{"id": find(countries, 'name', c)['id']} for c in mentions]

def get_countries():
    source = "https://restcountries.eu/rest/v2/all" # Put source link here
    req = urllib.request.Request(source)
    response = urllib.request.urlopen(req)
    string = response.read().decode('utf-8')
    json_obj = json.loads(string)
    for c in json_obj:
        c["id"] = c["numericCode"]

    return json_obj

def get_organizations(countries):
    source = "https://newsapi.org/v1/sources?language=en" # Put source link here
    req = urllib.request.Request(source)
    response = urllib.request.urlopen(req)
    string = response.read().decode('utf-8')
    json_obj = json.loads(string)
    organizations = json_obj['sources']
    for o in organizations:
        country_name = country_to_name[o['country']]
        country_id = next((c['id'] for c in countries if c['name'] == country_name), None)
        o['country'] = {"id": country_id}
    return organizations

def get_articles(countries, orgs):
    api_link = "https://newsapi.org/v1/articles?source=" # Put source link here
    api_key = "0291a4046bac4b3cb5429fd129fb37fa"
    articles = []
    for o in orgs:
        # Construct api url to pull articles from
        url = api_link + o["id"]    # Add source id to url
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
                article["organization"] = {"id": o["id"]}     # Add source field to article
                articles.append(article)
                desc = article['description'] if article['description'] else ''
                title = article['title'] if article['title'] else ''
                all_words = desc + " " + title
                countries_mentioned = get_country_mentions(all_words, countries)
                if countries_mentioned:
                    article["countries"] = countries_mentioned
                else:
                    article["countries"] = [{"id": o['country']['id']}]
                article['id'] = str(uuid.uuid1())

        except Exception as e:
            print("Caught exception while requesting articles.")
            print(str(e))
            break
    return articles

def main():
    outfile = dir_path + '/data.pickle'
    data = {}
    data['countries'] = get_countries()
    data['organizations'] = get_organizations(data['countries'])
    data['articles'] = get_articles(data['countries'], data['organizations'])

    for c in data['countries']:
        articles = [{"id": x['id']} for x in data['articles'] if any(y['id'] == c['id'] for y in x['countries'])]
        organizations = [{"id": x['id']} for x in data['organizations'] if x['country']['id'] == c['id']]
        c['articles'] = articles
        c['organizations'] = organizations

    for o in data['organizations']:
        articles = [{"id": x['id']} for x in data['articles'] if x['organization']['id'] == o['id']]
        o['articles'] = articles

    with open(outfile, 'wb') as f:
        pickle.dump(data, f)

if __name__ == '__main__':
    main()
