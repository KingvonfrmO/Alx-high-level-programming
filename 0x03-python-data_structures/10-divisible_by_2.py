def divisible_by_2(my_list=[]):
    length = len(my_list)
    new_list = []
    for i in range(0, length):
        if my_list[i] % 2 == 0:
            result = True
            new_list.append(result)
        else:
            result = False
            new_list.append(result)
    
    return new_list