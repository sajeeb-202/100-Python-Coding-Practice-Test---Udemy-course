def transpose_matrix(matrix):
    # Handle empty matrix
    if matrix == []:
        return []
    
    # Check that all rows have the same length
    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise ValueError("All rows in the matrix must have the same length.")
    
    # Transpose using zip
    transposed = list(map(list, zip(*matrix)))
    return transposed