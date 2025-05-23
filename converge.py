import numpy as np
import ast

def norma(vetor, tipo='infinito'):
    if tipo == 'infinito':
        return np.linalg.norm(vetor, np.inf)
    elif tipo == '1':
        return np.linalg.norm(vetor, 1)
    elif tipo == '2':
        return np.linalg.norm(vetor, 2)
    else:
        raise ValueError("Tipo de norma inválido. Use 'infinito', '1' ou '2'.")

def analisa_convergencia(c_solucoes, k, tipo_norma='infinito'):
    normas_diff = []
    for i in range(1, k+1):
        diff = c_solucoes[i] - c_solucoes[i-1]
        n = norma(diff, tipo_norma)
        normas_diff.append(n)
        print(f"||c^({i}) - c^({i-1})||_{tipo_norma} = {n:.6f}")
    return normas_diff

def menu_norma():
    print("Escolha o tipo da norma para calcular a convergência:")
    print("1 - Norma Infinito (max)")
    print("2 - Norma 1")
    print("3 - Norma 2")
    while True:
        escolha = input("Digite o número da opção desejada (1, 2 ou 3): ").strip()
        if escolha == '1':
            return 'infinito'
        elif escolha == '2':
            return '1'
        elif escolha == '3':
            return '2'
        else:
            print("Opção inválida. Tente novamente.")

def ler_array_console(indice):
    while True:
        entrada = input(f"Informe o vetor c^({indice}) como lista de números, ex: [1.0, 2.0, 3.0]: ").strip()
        try:
            lista = ast.literal_eval(entrada)
            if isinstance(lista, (list, tuple)) and all(isinstance(x, (int, float)) for x in lista):
                return np.array(lista, dtype=float)
            else:
                print("Entrada inválida: informe uma lista ou tupla de números.")
        except:
            print("Entrada inválida: use o formato correto, ex: [1.0, 2.0, 3.0]")

if __name__ == "__main__":
    while True:
        try:
            k = int(input("Informe o valor inteiro de k (k >= 1): "))
            if k >= 1:
                break
            else:
                print("Por favor, informe um número inteiro maior ou igual a 1.")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")

    c_solucoes = []
    for i in range(k+1):
        vetor = ler_array_console(i)
        c_solucoes.append(vetor)

    # Verifica se todos os vetores tem o mesmo tamanho
    tamanhos = [len(v) for v in c_solucoes]
    if len(set(tamanhos)) != 1:
        print("Erro: todos os vetores c^(k) devem ter o mesmo tamanho.")
        exit(1)

    tipo_norma = menu_norma()

    analisa_convergencia(c_solucoes, k, tipo_norma)
