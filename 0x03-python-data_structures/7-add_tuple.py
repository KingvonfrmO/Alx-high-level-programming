def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a = tuple_a[:2] + (0, 0)
    tuple_b = tuple_b[:2] + (0, 0)
    
    result_a = tuple_a[0] + tuple_b[0]
    result_b = tuple_a[1] + tuple_b[1]
    
    overall = (result_a, result_b)
    
    return overall