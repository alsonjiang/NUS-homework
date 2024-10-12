import sympy as sp

# Function to compute REF
def row_echelon_form(matrix):
    # Convert the input to a sympy Matrix
    M = sp.Matrix(matrix)
    # Use sympy's rref() function to get the REF
    M_ref, _ = M.rref()
    return M_ref

# Example usage
matrix = [
    [1, 2, -1, -4],
    [2, 3, -1, -11],
    [-2, 0, -3, 22]
]

ref_matrix = row_echelon_form(matrix)
print("Row Echelon Form (REF):")
sp.pprint(ref_matrix)
