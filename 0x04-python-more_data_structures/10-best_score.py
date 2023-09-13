#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None

    return max([v for k, v in a_dictionary.items()])
