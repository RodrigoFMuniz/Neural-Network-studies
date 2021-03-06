import numpy as np

taxa_acerto = 0.95
taxa_aprendizagem = 0.01
valor = 0
geracao = 1

entradas = np.array([-1, 7, 5, -4, 6, 5, -10])
pesos = np.array([0.8, 0.1, 0, 0.02, 0.6, -0.74, 0.32])
# pesos = np.array([0.786,0.206,0.076])
print(entradas)
print(pesos)


def soma(e, p):
    return np.dot(e, p)


def step_function(n):
    if n >= 0:
        return 1
    return 0


def ajuste_peso(entrada, err, peso, taxa_aprendizagem):
    return peso + (taxa_aprendizagem*entrada*err)


def calc_err(pesos):
    return


while valor < taxa_acerto:
    print(f'Geração: {geracao}')
    s = soma(entradas, pesos)
    sf = step_function(s)
    print(f'Valor da stepfunction {sf}')
    if sf >= 1:
        print(f'Resultado atingido na geração: {geracao}')
        valor = sf
    else:
        for ind, p in enumerate(pesos):
            pesos[ind] = ajuste_peso(entradas[ind], 0.15, p, taxa_aprendizagem)
            print(f'Geração {geracao} => Novo peso {ind}: {pesos[ind]}')
        geracao += 1
        if geracao == 1000:
            break
