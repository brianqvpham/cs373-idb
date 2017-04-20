from flask import Blueprint, render_template, jsonify, request
from blueprints.games import get_games, query_games

wishlist_bp = Blueprint('wishlist', __name__)
game_data = None

@wishlist_bp.route('/wishlist/')
def show_wishlist():
    global game_data

    # Initialize game data if neccessary
    if game_data == None:
        game_data = get_games()
    

    # Parse args if exist
    args = {}
    for key in game_data:
        # Try every criteria in game_data except for games 
        if key != 'games':
            cur_arg = request.args.get(key)
            if cur_arg is not None:
                args[key] = cur_arg

    filtered_games = query_games(game_data, **args)
    
    
    """
    # Using mock data since other group's website is down
    game_data = {}
    game_data['themes'] = ['Action', 'Adventure', 'Roleplay', 'Scifi']
    game_data['ratings'] = ['E', 'M', 'T']
    """

    return render_template('wishlist.html', themes=game_data['themes'], 
                           ratings=game_data['ratings'],
                           fil_games=filtered_games)
