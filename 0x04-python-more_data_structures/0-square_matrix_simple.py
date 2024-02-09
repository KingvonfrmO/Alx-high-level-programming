def square_matrix_simple(matrix=[]):
    row = len(matrix)
    column = len(matrix[0])
    result_matrix = [row[:] for row in matrix]
    
    for i in range(0, row):
        for j in range(0, column):
            matrix[i][j]= (matrix[i][j])**2
    
    return result_matrix