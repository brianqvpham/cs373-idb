"""
Requests source ids from api.
Stores a dict of source-ids to source names in pickle file.
"""

import urllib.request
import json
import pickle

source = "https://newsapi.org/v1/sources?language=en" # Put source link here
output_pickle_name = "sources.pickle" # Put pickle file name here



if __name__ == "__main__":
    req = urllib.request.Request(source)
    response = urllib.request.urlopen(req)
    string = response.read().decode('utf-8')
    json_obj = json.loads(string)
    source_list = json_obj["sources"]
    sources = {}
    for s in source_list:
        sources[s["id"]] = s["name"]
    print(sources)
    with open(output_pickle_name, 'wb') as f:
        pickle.dump(sources, f)
    
