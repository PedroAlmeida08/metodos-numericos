import numpy as np

# Matriz A original e vetor b
A = np.array([
    [0, 2, 5],
    [2, 1, 1],
    [3, 1, 0]
], dtype=float)

b = np.array([1, 1, 2], dtype=float)

# Permutação: trocar linha 0 com linha 2 (para evitar pivô zero)
P = np.array([
    [0, 0, 1],
    [0, 1, 0],
    [1, 0, 0]
], dtype=float)

PA = P @ A
Pb = P @ b

# Inicializa L e U
L = np.identity(3)
U = PA.copy()

# Etapa 1: Eliminação de Gauss manual
# Zerando elemento (1,0)
L[1, 0] = U[1, 0] / U[0, 0]
U[1] = U[1] - L[1, 0] * U[0]

# Zerando elemento (2,1)
L[2, 1] = U[2, 1] / U[1, 1]
U[2] = U[2] - L[2, 1] * U[1]

# Sistema: LUx = Pb

# Resolver Ly = Pb (substituição direta)
y = np.zeros(3)
y[0] = Pb[0]
y[1] = Pb[1] - L[1, 0]*y[0]
y[2] = Pb[2] - L[2, 1]*y[1]

# Resolver Ux = y (substituição reversa)
x = np.zeros(3)
x[2] = y[2] / U[2, 2]
x[1] = (y[1] - U[1, 2]*x[2]) / U[1, 1]
x[0] = (y[0] - U[0, 1]*x[1] - U[0, 2]*x[2]) / U[0, 0]

# Exibir resultados
print("PA:\n", PA)
print("Pb:\n", Pb)
print("L:\n", L)
print("U:\n", U)
print("y:\n", y)
print("x (solução):\n", x)
