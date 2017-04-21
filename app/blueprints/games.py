import urllib.request
import json

def get_games():
    # Get data from API request
    source = 'http://gamelookup.me/api/games/'
    req = urllib.request.Request(source)
    response = urllib.request.urlopen(req)
    string = response.read().decode('utf-8')
    json_obj = json.loads(string)

    # Parse data and make lists of themes and ratings
    result = {}
    result['games'] = json_obj['games_list']
    result['themes'] = []
    result['ratings'] = []
    for game in json_obj['games_list']:
        if game['theme'] not in result['themes']:
            result['themes'].append(game['theme'])

        if game['avg_score'] not in result['ratings']:
            result['ratings'].append(game['avg_score'])

    result['themes'].sort()
    result['ratings'].sort()
    return result

def query_games(games, **kwargs):
    result = games
    for key in kwargs:
        result = list(filter(lambda game: game[key] == kwargs[key], result))
    return result
    
