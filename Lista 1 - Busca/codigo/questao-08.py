# Lista 1 - Questao 8
# busca em largura e em profundidade no mapa da questao 7 (School ate Museum)

from collections import deque
import time

# grafo nao direcionado, cada aresta aparece nos dois lados
# vizinhos em ordem alfabetica pra execucao ser sempre igual
mapa = {
    "Bank":   {"Club": 1.1, "Home": 1.3, "Lake": 1.0, "Museum": 1.7, "Park": 1.8, "School": 1.0},
    "Club":   {"Bank": 1.1, "Home": 1.2, "School": 1.4},
    "Home":   {"Bank": 1.3, "Club": 1.2, "Museum": 2.7},
    "Lake":   {"Bank": 1.0, "Park": 1.6, "School": 0.9},
    "Museum": {"Bank": 1.7, "Home": 2.7, "Park": 1.6},
    "Park":   {"Bank": 1.8, "Lake": 1.6, "Museum": 1.6},
    "School": {"Bank": 1.0, "Club": 1.4, "Lake": 0.9},
}


def custo(caminho):
    total = 0
    for i in range(len(caminho) - 1):
        total += mapa[caminho[i]][caminho[i + 1]]
    return total


def busca_largura(inicio, objetivo):
    fronteira = deque([[inicio]])   # fila
    conhecidos = {inicio}
    visitados = []
    while fronteira:
        caminho = fronteira.popleft()   # sai o que entrou primeiro
        no = caminho[-1]
        visitados.append(no)
        if no == objetivo:
            return caminho, visitados
        for vizinho in mapa[no]:
            if vizinho not in conhecidos:
                conhecidos.add(vizinho)
                fronteira.append(caminho + [vizinho])
    return None, visitados


def busca_profundidade(inicio, objetivo):
    fronteira = [[inicio]]   # pilha
    conhecidos = {inicio}
    visitados = []
    while fronteira:
        caminho = fronteira.pop()   # sai o que entrou por ultimo
        no = caminho[-1]
        visitados.append(no)
        if no == objetivo:
            return caminho, visitados
        # empilha ao contrario pra o primeiro em ordem alfabetica sair primeiro
        for vizinho in reversed(list(mapa[no])):
            if vizinho not in conhecidos:
                conhecidos.add(vizinho)
                fronteira.append(caminho + [vizinho])
    return None, visitados


def executa(nome, busca):
    caminho, visitados = busca("School", "Museum")

    # uma execucao so e rapida demais pra medir, entao repito 100 mil vezes
    repeticoes = 100000
    inicio = time.perf_counter()
    for _ in range(repeticoes):
        busca("School", "Museum")
    total = time.perf_counter() - inicio

    print(nome)
    print("  ordem de visita:", " -> ".join(visitados))
    print("  nos visitados:", len(visitados))
    print("  caminho:", " -> ".join(caminho))
    print("  custo: %.1f km" % custo(caminho))
    print("  tempo de uma execucao: %.2f microssegundos" % (total / repeticoes * 1e6))
    print("  tempo das 100 mil: %.4f s" % total)
    print()


executa("BUSCA EM LARGURA", busca_largura)
executa("BUSCA EM PROFUNDIDADE", busca_profundidade)
