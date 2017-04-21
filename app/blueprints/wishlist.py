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
    theme = request.args.get('theme')
    rating = request.args.get('avg_score')
    if theme is not None:
        args['theme'] = theme
    if rating is not None:
        args['avg_score'] = rating
    
    filtered_games = query_games(game_data['games'], **args)#theme=theme, avg_score=rating)
    print(filtered_games)
    
    """
    # Using mock data since other group's website is down
    game_data = {}
    game_data['themes'] = ['Action', 'Adventure', 'Roleplay', 'Scifi']
    game_data['ratings'] = ['E', 'M', 'T']
    """

    return render_template('wishlist.html', themes=game_data['themes'], 
                           ratings=game_data['ratings'],
                           fil_games=filtered_games,
                           theme=theme,
                           avg_score=rating)
