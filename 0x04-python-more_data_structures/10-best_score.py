def best_score(a_dictionary):
    if not a_dictionary:
        return None
    
    max_score = max(a_dictionary.values())
    for k , v in a_dictionary.items():
        if v == max_score:
            return k
        