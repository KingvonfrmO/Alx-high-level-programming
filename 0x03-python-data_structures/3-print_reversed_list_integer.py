def print_reversed_list_integer(my_list=[]):
    my_list.reverse()
    length = len(my_list)
    for i in range(0, length):
        print("{}".format(my_list[i]),end = "\n")
        