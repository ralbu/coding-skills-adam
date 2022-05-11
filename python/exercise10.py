from math import floor

def calculate_avg_players(players):
    players_simple = {}


    for i in players:
        name = i['name']
        score = i['score']
        players_simple[name] = score
    players = players_simple

    scores = {}
    names = players.keys()
    fl_times = {}

    for p in names:
        first_letter = p.upper()[0]
        if first_letter in scores:
            scores[first_letter] += players[p]
            fl_times[first_letter] += 1
        else:
            scores[first_letter] = players[p]
            fl_times[first_letter] = 1 
        print(fl_times)
    for i in scores:
        scores[i] = floor(scores[i]/fl_times[i])

    result = scores

    return result