# Lista 2 - Questao 19
# confere se a heuristica dos pares (preta antes de branca) e admissivel
# P = peca preta, B = peca branca, _ = vazio

import heapq

inicial = "PPP_BBB"


def eh_meta(estado):
    return estado.replace("_", "") == "BBBPPP"


def sucessores(estado):
    vazio = estado.index("_")
    lista = []
    # distancia ate o vazio e custo: deslizar, pular 1 peca, pular 2 pecas
    for distancia, custo in ((1, 1), (2, 1), (3, 2)):
        for peca in (vazio - distancia, vazio + distancia):
            if 0 <= peca < 7:
                novo = list(estado)
                novo[vazio] = novo[peca]
                novo[peca] = "_"
                lista.append(("".join(novo), custo))
    return lista


def h(estado):
    pecas = estado.replace("_", "")
    pares = 0
    for i in range(len(pecas)):
        for j in range(i + 1, len(pecas)):
            if pecas[i] == "P" and pecas[j] == "B":
                pares += 1
    return pares


# gera todos os estados que da pra alcancar
estados = set()
pilha = [inicial]
while pilha:
    estado = pilha.pop()
    if estado not in estados:
        estados.add(estado)
        for novo, _ in sucessores(estado):
            pilha.append(novo)

# custo real minimo de cada estado ate a meta (custo uniforme saindo das metas)
custo_real = {}
fila = [(0, e) for e in estados if eh_meta(e)]
heapq.heapify(fila)
while fila:
    custo, estado = heapq.heappop(fila)
    if estado in custo_real:
        continue
    custo_real[estado] = custo
    for novo, c in sucessores(estado):
        if novo not in custo_real:
            heapq.heappush(fila, (custo + c, novo))

print("estados alcancaveis:", len(estados))
print("estado inicial: h =", h(inicial), " custo real =", custo_real[inicial])

erros = [e for e in estados if h(e) > custo_real[e]]
print("estados em que h passa do custo real:", len(erros))
