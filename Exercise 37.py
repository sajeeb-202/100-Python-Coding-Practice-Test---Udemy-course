def multiply_matrices(matrix1, matrix2):
    # Handle empty matrices
    if not matrix1 or not matrix2:
        return "Matrices cannot be multiplied due to incompatible dimensions."

    # Number of columns in matrix1
    cols_m1 = len(matrix1[0])
    # Number of rows in matrix2
    rows_m2 = len(matrix2)

    # Check compatibility
    if cols_m1 != rows_m2:
        return "Matrices cannot be multiplied due to incompatible dimensions."

    # Number of rows in matrix1 and columns in matrix2
    rows_m1 = len(matrix1)
    cols_m2 = len(matrix2[0])

    # Initialize result matrix with zeros
    result = [[0 for _ in range(cols_m2)] for _ in range(rows_m1)]

    # Matrix multiplication
    for i in range(rows_m1):
        for j in range(cols_m2):
            for k in range(cols_m1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result