def uniq_add(my_list=[]):
    unique = set()
    
    for i in my_list:
        unique.add(i)
        
    result = sum(unique)
    
    return result