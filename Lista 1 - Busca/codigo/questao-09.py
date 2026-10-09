# Lista 1 - Questao 9
# profundidade limitada e aprofundamento iterativo no mapa da Romenia
# de Arad ate Bucharest, com limites 2, 4 e 7

import time

# so as cidades antes de Bucharest
# (Giurgiu, Urziceni, Hirsova, Eforie, Vaslui, Iasi e Neamt ficaram de fora)
romenia = {
    "Arad":           {"Sibiu": 140, "Timisoara": 118, "Zerind": 75},
    "Bucharest":      {"Fagaras": 211, "Pitesti": 101},
    "Craiova":        {"Drobeta": 120, "Pitesti": 138, "Rimnicu Vilcea": 146},
    "Drobeta":        {"Craiova": 120, "Mehadia": 75},
    "Fagaras":        {"Bucharest": 211, "Sibiu": 99},
    "Lugoj":          {"Mehadia": 70, "Timisoara": 111},
    "Mehadia":        {"Drobeta": 75, "Lugoj": 70},
    "Oradea":         {"Sibiu": 151, "Zerind": 71},
    "Pitesti":        {"Bucharest": 101, "Craiova": 138, "Rimnicu Vilcea": 97},
    "Rimnicu Vilcea": {"Craiova": 146, "Pitesti": 97, "Sibiu": 80},
    "Sibiu":          {"Arad": 140, "Fagaras": 99, "Oradea": 151, "Rimnicu Vilcea": 80},
    "Timisoara":      {"Arad": 118, "Lugoj": 111},
    "Zerind":         {"Arad": 75, "Oradea": 71},
}


def custo(caminho):
    total = 0
    for i in range(len(caminho) - 1):
        total += romenia[caminho[i]][caminho[i + 1]]
    return total


def profundidade_limitada(caminho, objetivo, limite, visitados):
    no = caminho[-1]
    visitados.append(no)
    if no == objetivo:
        return caminho
    if len(caminho) - 1 == limite:   # chegou no limite, nao expande
        return None
    for vizinho in romenia[no]:
        if vizinho not in caminho:   # nao volta pra cidade do proprio caminho
            resultado = profundidade_limitada(caminho + [vizinho], objetivo, limite, visitados)
            if resultado is not None:
                return resultado
    return None


def aprofundamento_iterativo(inicio, objetivo, limite_maximo, iteracoes):
    visitados = []
    for limite in range(limite_maximo + 1):
        desta_vez = []
        caminho = profundidade_limitada([inicio], objetivo, limite, desta_vez)
        visitados += desta_vez
        iteracoes.append((limite, len(desta_vez), caminho is not None))
        if caminho is not None:
            return caminho, visitados
    return None, visitados


def cronometra(funcao):
    repeticoes = 100000
    inicio = time.perf_counter()
    for _ in range(repeticoes):
        funcao()
    return (time.perf_counter() - inicio) / repeticoes * 1e6


def mostra(caminho, visitados, tempo):
    print("    nos visitados:", len(visitados))
    print("    ordem:", " -> ".join(visitados))
    if caminho is None:
        print("    resultado: nao achou")
    else:
        print("    caminho:", " -> ".join(caminho))
        print("    profundidade:", len(caminho) - 1)
        print("    custo:", custo(caminho), "km")
    print("    tempo: %.2f microssegundos" % tempo)
    print()


print("PROFUNDIDADE LIMITADA")
for limite in (2, 4, 7):
    visitados = []
    caminho = profundidade_limitada(["Arad"], "Bucharest", limite, visitados)
    tempo = cronometra(lambda: profundidade_limitada(["Arad"], "Bucharest", limite, []))
    print("  limite", limite)
    mostra(caminho, visitados, tempo)

print("APROFUNDAMENTO ITERATIVO")
for limite in (2, 4, 7):
    iteracoes = []
    caminho, visitados = aprofundamento_iterativo("Arad", "Bucharest", limite, iteracoes)
    tempo = cronometra(lambda: aprofundamento_iterativo("Arad", "Bucharest", limite, []))
    print("  limite maximo", limite)
    for l, quantos, achou in iteracoes:
        print("    limite %d: %d nos visitados, %s" % (l, quantos, "achou" if achou else "nao achou"))
    mostra(caminho, visitados, tempo)
