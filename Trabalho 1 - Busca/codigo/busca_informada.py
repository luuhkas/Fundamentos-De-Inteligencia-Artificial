# busca gulosa e A* ate um alvo, mais a regra que decide se vale desviar pra recompensa

import heapq
from mapa import h, VALOR_RECOMPENSA


def gulosa(grafo, inicio, alvo):
    fronteira = [(h(inicio, alvo), [inicio])]   # ordenada so por h
    conhecidos = {inicio}
    ordem = []   # nos expandidos, na ordem em que foram expandidos
    gerados = 1
    while fronteira:
        _, caminho = heapq.heappop(fronteira)
        no = caminho[-1]
        if no == alvo:
            return caminho, ordem, gerados
        ordem.append(no)
        for vizinho in grafo[no]:
            if vizinho not in conhecidos:
                conhecidos.add(vizinho)
                heapq.heappush(fronteira, (h(vizinho, alvo), caminho + [vizinho]))
                gerados += 1
    return None, ordem, gerados


def a_estrela(grafo, inicio, alvo):
    fronteira = [(h(inicio, alvo), 0, [inicio])]   # ordenada por f = g + h
    melhor_g = {inicio: 0}
    ordem = []   # nos expandidos, na ordem em que foram expandidos
    gerados = 1
    while fronteira:
        _, g, caminho = heapq.heappop(fronteira)
        no = caminho[-1]
        if g > melhor_g[no]:
            continue   # ja achei um caminho mais barato pra esse no
        if no == alvo:
            return caminho, ordem, gerados
        ordem.append(no)
        for vizinho, custo in grafo[no].items():
            novo_g = g + custo
            if vizinho not in melhor_g or novo_g < melhor_g[vizinho]:
                melhor_g[vizinho] = novo_g
                heapq.heappush(fronteira, (novo_g + h(vizinho, alvo), novo_g, caminho + [vizinho]))
                gerados += 1
    return None, ordem, gerados


# a parte da heuristica que avalia o desvio:
#   desvio = h(atual, $) + h($, destino) - h(atual, destino)
#   so vale ir no $ se o valor dele for maior que o desvio estimado
# entre os que valem, escolhe o de maior ganho; se nenhum vale, vai direto pro destino
def escolhe_alvo(atual, faltam, destino):
    alvo = destino
    melhor_ganho = 0
    for r in sorted(faltam):
        desvio = h(atual, r) + h(r, destino) - h(atual, destino)
        ganho = VALOR_RECOMPENSA - desvio
        if ganho > melhor_ganho:
            alvo = r
            melhor_ganho = ganho
    return alvo


def viagem_heuristica(mapa, busca, destino):
    atual = mapa.inicio
    faltam = set(mapa.recompensas)
    rota = [atual]
    ordem = []   # nos expandidos, na ordem em que foram expandidos
    gerados = 0
    while atual != destino:
        alvo = escolhe_alvo(atual, faltam, destino)
        caminho, nos, g = busca(mapa.grafo, atual, alvo)
        ordem += nos
        gerados += g
        if caminho is None:
            if alvo == destino:
                return None, ordem, gerados
            faltam.discard(alvo)   # recompensa sem caminho (sala fechada), desiste dela
            continue
        rota += caminho[1:]
        atual = caminho[-1]
        for no in caminho:
            faltam.discard(no)
    return rota, ordem, gerados
