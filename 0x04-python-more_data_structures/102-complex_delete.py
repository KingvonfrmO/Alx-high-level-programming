def complex_delete(a_dictionary, value):
    key_to_del = []
    
    for k, v in a_dictionary.items():
        if v == value:
            key_to_del.append(k)
            
    for k in key_to_del:
        del a_dictionary[k]
    
    return a_dictionary