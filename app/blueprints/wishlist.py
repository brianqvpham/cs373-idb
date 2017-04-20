from flask import Blueprint, render_template, jsonify, request
from blueprints.games import get_games, query_games

wishlist_bp = Blueprint('wishlist', __name__)
game_data = None

@wishlist_bp.route('/wishlist/')
def show_wishlist():
    global game_data

    """ 
    # Initialize game data if neccessary
    if game_data == None:
        game_data = get_games()
    """

    # Using mock data since other group's website is down
    game_data = {}
    game_data["themes"] = ["Action", "Adventure", "Roleplay", "Scifi"]
    game_data["ratings"] = ["E", "M", "T"]
    return render_template('wishlist.html', themes=game_data["themes"], ratings=game_data["ratings"])

@wishlist_bp.route('/wishlist/<op_1>')
def show_wishlist_result(op_1=None):
   # TODO 

    """ 
        for g in game_d["games_list"]:
            if g["theme"] not in games["themes"]:
                games["themes"].append(g["theme"])
            if g["avg_score"] not in games["rating"]:
                # append score
                games["rating"].append(g["avg_score"])
            if g["theme"] not in theme_rating:
                # games["theme_rating"] has the form of
                # {"theme_a":
                #      {"rating_1" : [{game_1}, {game_2},..],
                #       "rating_2": []..}
                #  "theme_b":
                #      {"rating_3: [{game_3}] }
                
                theme_rating[g["theme"]] = {}
                theme_rating[g["theme"]][g["avg_score"]] = [g]
                
            elif g["avg_score"] not in theme_rating[g["theme"]]:
                theme_rating[g["theme"]][g["avg_score"]] = [g]
            else:
                theme_rating[g["theme"]][g["avg_score"]].append(g)
        for t in theme_rating:
            print(t + "\n")
            for s in theme_rating[t]:
                print("score: " + s + "\n") """
