import random
import numpy as np
import sys


def gerar_individuo() -> list:
    individuo = [random.randint(0,7) for _ in range(8)]
    #individuo = random.randint(range(8), 8)
    return individuo


def etapa_populacao_inicial(tam: int) -> list:
    populacao = []
    for _ in range(tam):
        populacao.append(gerar_individuo())
    return etapa_aptidao(populacao)


def calcular_fitness(individuo: list) -> float:
    rainhas_ataque = 0
    for i in range(len(individuo)):
        for j in range(i+1,len(individuo)):
            linha = abs(i - j)
            coluna = abs(individuo[i] - individuo[j])
            if linha == 0 or coluna == 0 or linha == coluna:
                rainhas_ataque += 1
    if rainhas_ataque == 0:    
        return 1.1
    else:
        return 1 / rainhas_ataque

    
def etapa_aptidao(populacao: list) -> list:
    return sorted(populacao, key=lambda x:calcular_fitness(x), reverse=True)


def selecao_roleta(populacao: list) -> list:
    escolha = random.random()
    populacao_fitness = [calcular_fitness(rainha) for rainha in populacao]
    total = sum(populacao_fitness)
    anterior = 0
    index = 0
    for i in range(len(populacao_fitness)):
        pedaco = populacao_fitness[i] / total
        anterior += pedaco
        if anterior >= escolha:
            index = i
            break
    return populacao.pop(index)
    

def etapa_selecao(taxa_cruzamento: float, populacao: list):
    selecao_populacao = []
    buffer_populacao = populacao.copy()
    quantidade_cromossomos = int(len(buffer_populacao) * taxa_cruzamento)
    quantidade_cromossomos += quantidade_cromossomos % 2
    while len(selecao_populacao) < quantidade_cromossomos:
        selecao_populacao.append(selecao_roleta(buffer_populacao))
    return selecao_populacao


def etapa_cruzamento(tipo_cruzamento: str, selecao_populacao: list) -> list:
    nova_populacao = []
    if tipo_cruzamento == 'CORTE':
        while len(selecao_populacao) > 0:
            pai = selecao_populacao.pop(0)
            mae = selecao_populacao.pop(0)
            corte = random.randint(3,6)
            filho_1 = pai[:corte] + mae[corte:]
            filho_2 = mae[:corte] + pai[corte:]
            nova_populacao.append(filho_1)
            nova_populacao.append(filho_2)
    else:
        while len(selecao_populacao) > 0:
            pai = selecao_populacao.pop(0)
            mae = selecao_populacao.pop(0)
            corte_lista = random.sample(range(7),2)
            filho_1 = pai.copy()
            filho_2 = mae.copy()
            for i in corte_lista:
                aux = filho_1[i]
                filho_1[i] = filho_2[i]
                filho_2[i] = aux
            nova_populacao.append(filho_1)
            nova_populacao.append(filho_2)
    return nova_populacao
        


def etapa_mutacao(taxa_mutacao: float, nova_populacao: list) -> list:
    for individuo in nova_populacao:
        if random.random() < taxa_mutacao:
            individuo[random.randint(0,7)] = random.randint(0,7)
    return nova_populacao


def etapa_atualizacao(taxa_sobrevivencia: float, populacao: list, nova_populacao: list) -> list:
    sobreviventes = int(taxa_sobrevivencia * len(populacao))
    etapa_aptidao(nova_populacao)
    return populacao[:sobreviventes] + nova_populacao[:len(populacao)-sobreviventes]


def vetor_para_matriz(individuo: list) -> None:
    tabuleiro = np.zeros((8, 8), dtype=int)
    for i in range(8):
        tabuleiro[i][individuo[i]] = 1
    print(tabuleiro)


def algoritmo_genetico(tipo_cruzamento = 'SWAP', geracoes = 100, tam_populacao = 200, taxa_cruzamento = 0.5, taxa_mutacao = 0.01, taxa_sobrevivencia = 0.5) -> int:
    populacao_inicial = etapa_populacao_inicial(tam_populacao)
    populacao = etapa_aptidao(populacao_inicial)
    for _ in range(geracoes):   
        selecao_populacao = etapa_selecao(taxa_cruzamento, populacao)
        nova_populacao = etapa_cruzamento(tipo_cruzamento, selecao_populacao)
        nova_populacao = etapa_mutacao(taxa_mutacao, nova_populacao)
        populacao = etapa_atualizacao(taxa_sobrevivencia, populacao, nova_populacao)
        populacao = etapa_aptidao(populacao)
        if calcular_fitness(populacao[0]) >= 1.1:
            print(populacao[0])
            return 1
    return 0


def configuracao(argumentos: list) -> list:
    config = []
    try:     
        if len(argumentos) == 7:
            config = [argumentos[1]] + [int(arg) for arg in argumentos[2:4]] + [float(arg) for arg in argumentos[4:]]
    except BaseException:
        print('Configuração inválida\nIniciando Configuração padrão')
    return config


if __name__ == '__main__':
    otimo = 0
    iteracao = 50
    for i in range(iteracao):
        print(f'Rodando: {i}')
        otimo += algoritmo_genetico(*configuracao(sys.argv))
    sucesso = otimo / iteracao
    falhas = 1 - sucesso
    print(f'Sucesso: {sucesso}\nFalhas: {falhas}')
