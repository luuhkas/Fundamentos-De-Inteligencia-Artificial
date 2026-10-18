# RMA* (Reward Maximization A*) adaptado de:
# CAO, XU, ZHANG, CHOSET, REN. Heuristic Search for the Orienteering Problem
# with Time-Varying Reward. SoCS 2024 (Algoritmo 1 do artigo)
#
# adaptacao pro trabalho:
#   - a recompensa nao muda com o tempo, entao o label nao guarda o tempo
#   - o label e (vertice, g, R): g = lucro (valor dos $ pegos - custo andado), R = $ ja pegos
#   - o caminho termina sempre no destino e pode repetir vertice (voltar de um beco)

import heapq
from mapa import h, VALOR_RECOMPENSA


def alcancaveis(grafo, inicio):
    vistos = {inicio}
    pilha = [inicio]
    while pilha:
        no = pilha.pop()
        for vizinho in grafo[no]:
            if vizinho not in vistos:
                vistos.add(vizinho)
                pilha.append(vizinho)
    return vistos


def rma_estrela(mapa, destino):
    grafo = mapa.grafo
    vistos = alcancaveis(grafo, mapa.inicio)
    if destino not in vistos:
        return None, [], 0
    # recompensa em sala fechada nunca vai ser pega, entao nem entra na heuristica
    premios = [r for r in mapa.recompensas if r in vistos]

    # limite superior do lucro que ainda da pra ter: pega todos os $ que faltam
    # e paga no minimo a distancia de manhattan ate o destino (por isso e admissivel)
    def heuristica(no, R):
        return VALOR_RECOMPENSA * (len(premios) - len(R)) - h(no, destino)

    # l1 domina l2 no mesmo vertice se tem lucro maior ou igual pegando menos ou os mesmos $
    # (quem pegou menos ainda pode ir buscar o resto, entao l2 nunca fica melhor que l1)
    def dominado(no, g, R):
        for g1, R1 in frente[no]:
            if g1 >= g and R1 <= R:
                return True
        return False

    def podado(no, g, R, f):
        if melhor is not None and f <= melhor[0]:
            return True   # nao tem como passar a melhor solucao ja achada
        return dominado(no, g, R)

    R0 = frozenset([mapa.inicio]) if mapa.inicio in premios else frozenset()
    g0 = VALOR_RECOMPENSA * len(R0)
    aberta = [(-(g0 + heuristica(mapa.inicio, R0)), -g0, [mapa.inicio], R0)]   # linhas 1-3
    frente = {no: [] for no in grafo}   # linha 4, labels ja expandidos que ninguem domina
    melhor = None   # linha 5, (lucro, caminho) da melhor solucao ate agora
    ordem = []   # nos expandidos, na ordem em que foram expandidos
    gerados = 1

    while aberta:   # linha 6
        f, g, caminho, R = heapq.heappop(aberta)   # linha 7, sai o de MAIOR f
        f, g = -f, -g
        no = caminho[-1]
        if podado(no, g, R, f):   # linhas 8-9
            continue
        # linha 10, entra na frente e tira quem ele domina
        frente[no] = [(g1, R1) for g1, R1 in frente[no] if not (g >= g1 and R <= R1)]
        frente[no].append((g, R))
        if no == destino and (melhor is None or g > melhor[0]):   # linhas 11-12
            melhor = (g, caminho)
        ordem.append(no)
        for vizinho, custo in grafo[no].items():   # linhas 13-19
            novo_g = g - custo
            novo_R = R
            if vizinho in premios and vizinho not in R:
                novo_g += VALOR_RECOMPENSA
                novo_R = R | {vizinho}
            novo_f = novo_g + heuristica(vizinho, novo_R)   # linha 20
            if not podado(vizinho, novo_g, novo_R, novo_f):   # linhas 21-25
                heapq.heappush(aberta, (-novo_f, -novo_g, caminho + [vizinho], novo_R))
                gerados += 1

    if melhor is None:
        return None, ordem, gerados
    return melhor[1], ordem, gerados   # linha 26
