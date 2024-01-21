def max_integer(my_list=[]):
    length = len(my_list)
    if length == 0:
        return None
    else:
        max_value = max(my_list)
        return max_value