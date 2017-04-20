import urllib.request
import json

def get_games():
    source = "http://gamelookup.me/api/games/"
    req = urllib.request.Request(source)
    response = urllib.request.urlopen(req)
    string = response.read().decode('utf-8')
    json_obj = json.loads(string)
            
    return json_obj
