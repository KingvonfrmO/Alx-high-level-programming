def delete_at(my_list=[], idx=0):
    length = len(my_list)
    if idx < 0 and idx >= length:
        return my_list
    else:
        my_list.remove(idx)

        