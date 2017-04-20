#from flask import Blueprint, render_template, jsonify, request
from game_data import get_games

#wishlist_bp = Blueprint('wishlist', __name__)
game_d = None
games = {}
theme_rating = {}

#@wishlist_bp.route('/wishlist/', methods=['GET'])
def show_selection():
    global game_d
    global games 
    global theme_rating
    # name a template
    
    if game_d == None:
        game_d = get_games()
        games["themes"] = []
        games["rating"] = []
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
                print("score: " + s + "\n")


show_selection()
        
