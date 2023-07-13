def transpose_matrix(matrix):
    # Transpose the matrix by converting rows to columns
    return list(map(list, zip(*matrix)))

def get_matrix_minor(matrix, row_index, column_index):
    # Get the minor matrix of a given matrix by removing the specified row and column
    return [row[:column_index] + row[column_index+1:] for row in (matrix[:row_index]+matrix[row_index+1:])]

def get_matrix_determinant(matrix):
    # Base case for 2x2 matrix
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    determinant = 0
    # Expand the determinant using the first row
    for column in range(len(matrix)):
        determinant += ((-1)**column) * matrix[0][column] * get_matrix_determinant(get_matrix_minor(matrix, 0, column))
    
    return determinant

def calculate_matrix_inversion(matrix):
    # Check if the matrix is square
    rows, cols = len(matrix), len(matrix[0])
    if rows != cols:
        raise ValueError("The matrix is not square. Cannot calculate the inverse.")
    
    # Find the determinant
    determinant = get_matrix_determinant(matrix)

    # Base case for 2x2 matrix
    if len(matrix) == 2:
        return [[matrix[1][1]/determinant, -1 * matrix[0][1]/determinant],
                [-1 * matrix[1][0]/determinant, matrix[0][0]/determinant]]
    
    # Find the matrix of cofactors
    cofactors = []
    for row in range(len(matrix)):
        cofactor_row = []
        for column in range(len(matrix)):
            minor = get_matrix_minor(matrix, row, column)
            cofactor_row.append(((-1)**(row + column)) * get_matrix_determinant(minor))
        cofactors.append(cofactor_row)

    cofactors = transpose_matrix(cofactors)
    # Divide each element of the cofactor matrix by the determinant to obtain the inverse
    for row in range(len(cofactors)):
        for column in range(len(cofactors)):
            cofactors[row][column] = cofactors[row][column]/determinant
    
    return cofactors