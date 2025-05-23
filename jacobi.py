import numpy as np
import sympy as sp

def newton_system():
    # Tamanho do vetor c
    n = int(input("Digite o tamanho do vetor c: "))

    # Definir variáveis simbólicas
    c_syms = sp.symbols(f'c1:{n+1}')  # cria (c1, c2, ..., cn)

    # Receber expressões para cada componente de F
    F_exprs = []
    for i in range(n):
        expr = input(f"Digite a expressão para F{i+1} em termos de {c_syms}: ")
        expr = expr.replace('e', 'E')  # substitui 'e' por 'E'
        F_exprs.append(sp.sympify(expr, locals={'E': sp.E}))  # E → número de Euler

    # Derivar simbolicamente para obter J
    J_exprs = [[sp.diff(f, c) for c in c_syms] for f in F_exprs]

    # Receber chute inicial
    c0 = []
    for i in range(n):
        val = float(input(f"Digite o valor inicial de c{i+1}: "))
        c0.append(val)

    # Número de iterações
    n_iter = int(input("Digite o número de iterações: "))

    # Iterações de Newton
    c_vals = np.array(c0, dtype=float)

    for k in range(n_iter):
        print(f"\n--- Iteração {k+1} ---")

        # Avaliar F em c_vals
        F_vals = np.array([float(f.subs(dict(zip(c_syms, c_vals)))) for f in F_exprs])
        print("F(c):")
        print(F_vals)

        # Avaliar J em c_vals
        J_vals = np.zeros((n, n))
        for i in range(n):
            for j in range(n):
                J_vals[i][j] = float(J_exprs[i][j].subs(dict(zip(c_syms, c_vals))))
        print("J(c):")
        print(J_vals)

        # Resolver J * delta = -F
        try:
            delta = np.linalg.solve(J_vals, -F_vals)
        except np.linalg.LinAlgError:
            print("Erro: matriz Jacobiana singular.")
            return

        print("delta:")
        print(delta)

        # Atualizar c
        print("c antes da atualização:")
        print(c_vals)

        c_vals = c_vals + delta

        print("c após a atualização:")
        print(c_vals)

    print("\nResultado final de c:")
    print(c_vals)

newton_system()

# Solução: [ 8.77128645  0.25969545 -1.37228132]