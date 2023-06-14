#!/usr/bin/python3
def best_score(a_dictionary):
    # dictionary is none or empty return none
    if not a_dictionary:
        return None
    mx = max(a_dictionary.values())
    for key, value in a_dictionary.items():
        if mx == value:
            return key
