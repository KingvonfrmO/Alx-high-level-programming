def element_at(my_list, idx):
    length = len(my_list)
    if idx == 0 and idx >= length:
        return 
    else:
        popped = my_list.pop(idx)
        return popped
    
    
    