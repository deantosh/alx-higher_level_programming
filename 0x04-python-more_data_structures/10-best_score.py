#!/usr/bin/python3
def best_score(a_dictionary):
    # details of best scorer
    name_best_scorer = None
    score = 0

    if a_dictionary == None:
        return name_best_scorer

    for name in a_dictionary.keys():
        if a_dictionary[name] > score:
            score = a_dictionary[name]
            name_best_scorer = name

    return name_best_scorer
