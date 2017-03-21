"""
Requests source ids from api.
Sources are dicts with keys mapping to data about sources.
Source dicts are stored within a list.
"""

import urllib.request
import json
import pickle

# Mapping from country abbreciation to name
country_to_name = {"au" : "Australia", "de" : "Germany", 
                   "gb" : "Great Britain", "in" : "India", 
                   "it" : "Italy",
                   "us" : "United States of America"}
source = "https://newsapi.org/v1/sources?language=en" # Put source link here
output_pickle_name = "sources.pickle" # Put pickle file name here



if __name__ == "__main__":
    req = urllib.request.Request(source)
    response = urllib.request.urlopen(req)
    string = response.read().decode('utf-8')
    json_obj = json.loads(string)
    source_list = json_obj["sources"]
    for s in source_list:
        s["country"] = country_to_name[s["country"]]
    print(source_list)
    with open(output_pickle_name, 'wb') as f:
        pickle.dump(source_list, f)
    
