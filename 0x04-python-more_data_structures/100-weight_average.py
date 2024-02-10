def weight_average(my_list=[]):
    
    multiplication_sum = 0
    total_weight = 0
    
    for i in range(len(my_list)):
            multiplication_sum += my_list[i][0] * my_list[i][1]
            total_weight += my_list[i][1]
            
    return multiplication_sum / total_weight
