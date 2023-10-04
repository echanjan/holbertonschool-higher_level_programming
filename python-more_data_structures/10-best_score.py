#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is not None:
        best_value = max(a_dictionary.values(), default=None)
        if best_value is not None:
            return next(key for key, value in a_dictionary.items() if value == best_value)

    return None
