# Reimportando após reset
import numpy as np
from scipy.linalg import lu, solve_triangular

# Matrizes L e U serão recalculadas a partir de A original
A = np.array([
    [10, 2, -1],
    [-3, -5, 2],
    [1, 1, 6]
], dtype=float)

# Novo vetor b
b_new = np.array([9, -3, 33], dtype=float)

# Fatoração LU novamente
P, L, U = lu(A)

# Aplicar permutação de P em b_new
Pb_new = P @ b_new

# Resolver Ly = Pb_new
y_new = solve_triangular(L, Pb_new, lower=True)

# Resolver Ux = y_new
x_new = solve_triangular(U, y_new)

print(y_new, x_new)
