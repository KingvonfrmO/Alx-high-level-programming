def print_matrix_integer(matrix=[[]]):
    row = len(matrix)
    column = len(matrix[0]) if row > 0 else 0
    
    for r in range(row):
        for c in range(column):
            print("{}".format(matrix[r][c]), end=" ")
        print()