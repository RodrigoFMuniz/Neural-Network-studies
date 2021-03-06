"""
Modelo de problema

A   B   S
0   0   0
0   1   0
1   0   0
1   1   1

re -> resposta esperada
rc -> resposta calculada
taxa_aprend = taxa de aprendizagem
"""

import numpy as np

taxa_aprendizagem = 0.01
valor = 0
geracao = 1

# AND
# entradas = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
# saidas = np.array([0, 0, 0, 1])

# OR
entradas = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
saidas = np.array([0, 1, 1, 1])

# XOR
# entradas = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
# saidas = np.array([0, 1, 1, 0])
pesos = np.array([0.0, 0.0])
# pesos = np.array([0.786,0.206,0.076])
print(entradas)
print(pesos)


def step_function(n):
    return 1 if n >= 1 else 0


def calcula_saida(registro):
    print(registro)
    s = registro.dot(pesos)
    return step_function(s)


def ajuste_pesos(entrada, err, peso, taxa_aprendizagem):
    return peso + (taxa_aprendizagem*entrada*err)


def erro(saida_esperada, saida_calculada):
    return saida_esperada - saida_calculada


def treinar():
    erro_total = 1
    geracao = 0
    print(f"Número de saídas: {len(saidas)}")
    print(f"Número de pesos: {len(pesos)}")
    while erro_total != 0:
        geracao += 1
        print(f'Geração: {geracao}')
        erro_total = 0
        for i in range(len(saidas)):
            print(f'Entrada: {i}')
            saida_calculada = calcula_saida(np.asarray(entradas[i]))
            err = erro(saidas[i], saida_calculada)
            erro_total += err
            print("erro", err)
            for j in range(len(pesos)):
                pesos[j] = ajuste_pesos(
                    peso=pesos[j], err=err, entrada=entradas[i][j], taxa_aprendizagem=taxa_aprendizagem)
                print(f"Peso atualizado, {pesos[j]}")
            print(f"Erro total: {erro_total}")


treinar()

print(calcula_saida(entradas[0]))
print(calcula_saida(entradas[1]))
print(calcula_saida(entradas[2]))
print(calcula_saida(entradas[3]))
