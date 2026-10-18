# busca em largura e em profundidade
# param no primeiro vertice visitado que esteja em "alvos" (uma recompensa ou o destino)
# expandido = visitado e gerou os filhos, entao o alvo e visitado mas nao expandido

from collections import deque


def largura(grafo, inicio, alvos):
    fronteira = deque([[inicio]])   # fila
    conhecidos = {inicio}
    ordem = []   # nos expandidos, na ordem em que foram expandidos
    gerados = 1
    while fronteira:
        caminho = fronteira.popleft()   # sai o que entrou primeiro
        no = caminho[-1]
        if no in alvos:
            return caminho, ordem, gerados
        ordem.append(no)
        for vizinho in grafo[no]:
            if vizinho not in conhecidos:
                conhecidos.add(vizinho)
                fronteira.append(caminho + [vizinho])
                gerados += 1
    return None, ordem, gerados


def profundidade(grafo, inicio, alvos):
    fronteira = [[inicio]]   # pilha
    conhecidos = {inicio}
    ordem = []   # nos expandidos, na ordem em que foram expandidos
    gerados = 1
    while fronteira:
        caminho = fronteira.pop()   # sai o que entrou por ultimo
        no = caminho[-1]
        if no in alvos:
            return caminho, ordem, gerados
        ordem.append(no)
        # empilha ao contrario pra o primeiro vizinho (cima) sair primeiro
        for vizinho in reversed(list(grafo[no])):
            if vizinho not in conhecidos:
                conhecidos.add(vizinho)
                fronteira.append(caminho + [vizinho])
                gerados += 1
    return None, ordem, gerados


# a busca cega nao sabe se a recompensa compensa, entao pega toda que aparecer:
# busca ate o destino, mas se visitar uma recompensa antes, vai ate ela e recomeca dali
def viagem_cega(mapa, busca, destino):
    atual = mapa.inicio
    faltam = set(mapa.recompensas)
    rota = [atual]
    ordem = []   # nos expandidos, na ordem em que foram expandidos
    gerados = 0
    while atual != destino:
        caminho, nos, g = busca(mapa.grafo, atual, faltam | {destino})
        ordem += nos
        gerados += g
        if caminho is None:
            return None, ordem, gerados
        rota += caminho[1:]
        atual = caminho[-1]
        for no in caminho:
            faltam.discard(no)
    return rota, ordem, gerados
