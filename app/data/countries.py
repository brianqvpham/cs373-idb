import urllib.request
import json
import pickle

source = "https://restcountries.eu/rest/v2/all" # Put source link here
output_pickle_name = "countries.pickle" # Put pickle file name here



if __name__ == "__main__":
    req = urllib.request.Request(source)
    response = urllib.request.urlopen(req)
    string = response.read().decode('utf-8')
    json_obj = json.loads(string)
    print(json_obj)
    with open(output_pickle_name, 'wb') as f:
        pickle.dump(json_obj, f)
    
