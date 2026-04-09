def add_matrices(matrix1, matrix2):
    # Case 1: Both matrices are empty
    if matrix1 == [] and matrix2 == []:
        return []
    
    # Case 2: One matrix is empty and the other is not
    if matrix1 == [] or matrix2 == []:
        return "Matrices must have the same dimensions"
    
    # Check number of rows
    if len(matrix1) != len(matrix2):
        return "Matrices must have the same dimensions"
    
    # Check number of columns in each row
    for row1, row2 in zip(matrix1, matrix2):
        if len(row1) != len(row2):
            return "Matrices must have the same dimensions"
    
    # Perform element-wise addition
    result = []
    for i in range(len(matrix1)):
        row_sum = []
        for j in range(len(matrix1[i])):
            row_sum.append(matrix1[i][j] + matrix2[i][j])
        result.append(row_sum)
    
    return result