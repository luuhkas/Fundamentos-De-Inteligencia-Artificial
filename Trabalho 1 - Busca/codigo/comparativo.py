# roda os algoritmos e monta a tabela e o grafico de comparacao
# tempo medido e a media de varias execucoes, porque uma so e rapida demais
# modelo do professor (aula 2): 10.000 nos gerados por segundo e 1 KB por no

import heapq
import itertools
import textwrap
import time
import tracemalloc
import matplotlib.pyplot as plt
from mapa import Mapa, VALOR_RECOMPENSA, usa_heuristica
from gerador import gera_mapa
from busca_cega import largura, profundidade, viagem_cega
from busca_informada import gulosa, a_estrela, viagem_heuristica
from rma_estrela import rma_estrela, alcancaveis
from visual import FUNDO, TEXTO, EXPANDIDO

ALGORITMOS = [
    ("Largura", lambda m, d: viagem_cega(m, largura, d)),
    ("Profundidade", lambda m, d: viagem_cega(m, profundidade, d)),
    ("Gulosa", lambda m, d: viagem_heuristica(m, gulosa, d)),
    ("A*", lambda m, d: viagem_heuristica(m, a_estrela, d)),
    ("RMA*", lambda m, d: rma_estrela(m, d)),
]


def mede(mapa, busca, destino, repeticoes=20):
    tracemalloc.start()
    rota, ordem, gerados = busca(mapa, destino)
    _, pico = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    inicio = time.perf_counter()
    for _ in range(repeticoes):
        busca(mapa, destino)
    tempo = (time.perf_counter() - inicio) / repeticoes
    return rota, len(ordem), gerados, tempo, pico


def tabela(mapa, destino):
    resultados = []
    print("%-13s %6s %3s %6s %10s %8s %10s %10s %10s %10s" % (
        "algoritmo", "custo", "$", "lucro", "expandidos", "gerados",
        "tempo(ms)", "memoria", "prof.tempo", "prof.mem"))
    for nome, busca in ALGORITMOS:
        rota, expandidos, gerados, tempo, pico = mede(mapa, busca, destino)
        modelo_tempo = "%.3f s" % (gerados / 10000)
        modelo_mem = "%d KB" % gerados
        if rota is None:
            print("%-13s %6s %3s %6s %10d %8d %10.3f %7.1f KB %10s %10s" % (
                nome, "-", "-", "-", expandidos, gerados, tempo * 1000, pico / 1024,
                modelo_tempo, modelo_mem) + "   SEM CAMINHO")
            continue
        custo = mapa.custo(rota)
        pegas = len(mapa.coletadas(rota))
        lucro = VALOR_RECOMPENSA * pegas - custo
        print("%-13s %6d %3d %6d %10d %8d %10.3f %7.1f KB %10s %10s" % (
            nome, custo, pegas, lucro, expandidos, gerados, tempo * 1000, pico / 1024,
            modelo_tempo, modelo_mem))
        resultados.append((nome, expandidos, tempo * 1000, lucro))
    return resultados


# roda gulosa, A* e RMA* com cada uma das duas heuristicas
# "A* direto" vai so ate o destino, sem recompensa, pra ver o efeito da heuristica sozinha
def compara_heuristicas(mapa, destino, atual, arquivo=None, trava=True):
    linhas = [("A* direto", lambda m, d: a_estrela(m.grafo, m.inicio, d))] + ALGORITMOS[2:]
    dados = {}
    print("%-10s %-11s %10s %6s %6s" % ("algoritmo", "heuristica", "expandidos", "custo", "lucro"))
    for nome, busca in linhas:
        for heuristica in ("euclidiana", "manhattan"):
            usa_heuristica(heuristica)
            rota, ordem, gerados = busca(mapa, destino)
            if rota is None:
                print("%-10s %-11s %10d   SEM CAMINHO" % (nome, heuristica, len(ordem)))
                continue
            custo = mapa.custo(rota)
            lucro = VALOR_RECOMPENSA * len(mapa.coletadas(rota)) - custo
            print("%-10s %-11s %10d %6d %6d" % (nome, heuristica, len(ordem), custo, lucro))
            dados[(nome, heuristica)] = len(ordem)
    usa_heuristica(atual)
    if not dados:
        print("nenhum algoritmo achou caminho, sem grafico")
        return

    # um painel por algoritmo, cada um com a sua escala (senao o RMA* esconde os outros)
    # no estilo das figuras do artigo: caixa, grade clara, contorno preto e legenda embaixo
    nomes = [nome for nome, _ in linhas]
    fig, eixos = plt.subplots(1, len(nomes), figsize=(13, 4.8), facecolor=FUNDO)
    fig.subplots_adjust(left=0.06, right=0.98, top=0.9, bottom=0.24, wspace=0.35)
    for ax, nome in zip(eixos, nomes):
        valores = [dados.get((nome, "euclidiana"), 0), dados.get((nome, "manhattan"), 0)]
        barras = ax.bar(["Euclidiana", "Manhattan"], valores, color=["#D4D4D4", EXPANDIDO], width=0.6,
                        edgecolor=TEXTO, linewidth=0.8)
        for barra, valor in zip(barras, valores):
            ax.text(barra.get_x() + barra.get_width() / 2, valor, "%d" % valor,
                    ha="center", va="bottom", fontsize=9, color=TEXTO)
        estilo_artigo(ax, nome)
    eixos[0].set_ylabel("nós expandidos", fontsize=10, color=TEXTO)
    fig.text(0.06, 0.03, textwrap.fill("Figura: nós expandidos com cada heurística. \"A* direto\" vai ao destino "
             "sem passar pelas recompensas, o que isola o efeito da heurística: a Manhattan domina a euclidiana.", 150),
             fontsize=10, color=TEXTO, va="bottom")
    if arquivo:
        fig.savefig(arquivo, dpi=130, facecolor=FUNDO)
    if trava:
        plt.show()
    else:
        fig.show()


# custo uniforme saindo de um vertice: menor custo ate todos os outros
def custo_uniforme(grafo, inicio):
    custo = {inicio: 0}
    fila = [(0, inicio)]
    while fila:
        c, no = heapq.heappop(fila)
        if c > custo[no]:
            continue
        for vizinho, passo in grafo[no].items():
            if vizinho not in custo or c + passo < custo[vizinho]:
                custo[vizinho] = c + passo
                heapq.heappush(fila, (c + passo, vizinho))
    return custo


# forca bruta: testa todas as ordens de recompensas e devolve o maior lucro possivel
def lucro_otimo(mapa, destino):
    premios = [r for r in mapa.recompensas if r in alcancaveis(mapa.grafo, mapa.inicio)]
    distancia = {p: custo_uniforme(mapa.grafo, p) for p in [mapa.inicio] + premios}
    melhor = -distancia[mapa.inicio][destino]   # ir direto sem pegar nada
    for k in range(1, len(premios) + 1):
        for ordem in itertools.permutations(premios, k):
            paradas = [mapa.inicio] + list(ordem)
            custo = distancia[ordem[-1]][destino]
            for i in range(len(paradas) - 1):
                custo += distancia[paradas[i]][paradas[i + 1]]
            melhor = max(melhor, VALOR_RECOMPENSA * k - custo)
    return melhor


# roda os 5 algoritmos em varios mapas aleatorios e mostra a media
def compara_aleatorios(quantidade=30):
    soma = {nome: [0, 0, 0.0, 0] for nome, _ in ALGORITMOS}   # expandidos, lucro, tempo, vezes no otimo
    com_caminho = 0
    for semente in range(quantidade):
        mapa = Mapa(linhas=gera_mapa(semente))
        if mapa.premio not in alcancaveis(mapa.grafo, mapa.inicio):
            continue   # todos respondem "sem caminho" nesse mapa
        com_caminho += 1
        otimo = lucro_otimo(mapa, mapa.premio)
        for nome, busca in ALGORITMOS:
            inicio = time.perf_counter()
            rota, ordem, gerados = busca(mapa, mapa.premio)
            tempo = time.perf_counter() - inicio
            lucro = VALOR_RECOMPENSA * len(mapa.coletadas(rota)) - mapa.custo(rota)
            soma[nome][0] += len(ordem)
            soma[nome][1] += lucro
            soma[nome][2] += tempo * 1000
            if lucro == otimo:
                soma[nome][3] += 1

    print("%d mapas aleatorios: %d com caminho, %d sem caminho" % (quantidade, com_caminho, quantidade - com_caminho))
    print("%-13s %16s %12s %15s %13s" % ("algoritmo", "expandidos(media)", "lucro(media)", "tempo(ms,media)", "achou o otimo"))
    medias = []
    for nome, _ in ALGORITMOS:
        expandidos, lucro, tempo, otimos = soma[nome]
        medias.append((nome, expandidos / com_caminho, tempo / com_caminho, lucro / com_caminho))
        print("%-13s %16.1f %12.1f %15.3f %10d/%d" % (
            nome, expandidos / com_caminho, lucro / com_caminho, tempo / com_caminho, otimos, com_caminho))
    return medias


# eixo no estilo das figuras do artigo: caixa completa, grade clara atras das barras
def estilo_artigo(ax, titulo):
    ax.set_title(titulo, fontsize=11, color=TEXTO)
    ax.set_facecolor(FUNDO)
    ax.grid(axis="y", color="#DDDDDD", linewidth=0.8)
    ax.set_axisbelow(True)
    ax.tick_params(labelsize=9, colors=TEXTO)
    ax.margins(y=0.15)
    for borda in ax.spines.values():
        borda.set_color(TEXTO)
        borda.set_linewidth(0.8)


def grafico(resultados, arquivo=None, titulo="comparativo no mapa escolhido", trava=True):
    if not resultados:
        print("nenhum algoritmo achou caminho, sem grafico")
        return
    nomes = [r[0] for r in resultados]
    cores = [EXPANDIDO if n == "RMA*" else "#D4D4D4" for n in nomes]
    fig, eixos = plt.subplots(1, 3, figsize=(14, 4.8), facecolor=FUNDO)
    fig.subplots_adjust(left=0.05, right=0.98, top=0.9, bottom=0.24, wspace=0.28)

    for ax, indice, painel, formato in [(eixos[0], 1, "nós expandidos", "%d"),
                                        (eixos[1], 2, "tempo (ms)", "%.2f"),
                                        (eixos[2], 3, "lucro (recompensas − custo)", "%+g")]:
        valores = [r[indice] for r in resultados]
        barras = ax.bar(nomes, valores, color=cores, width=0.6, edgecolor=TEXTO, linewidth=0.8)
        for barra, valor in zip(barras, valores):
            y = barra.get_height()
            ax.text(barra.get_x() + barra.get_width() / 2, y, formato % round(valor, 2), ha="center",
                    va="bottom" if y >= 0 else "top", fontsize=9, color=TEXTO)
        estilo_artigo(ax, painel)
        ax.axhline(0, color=TEXTO, linewidth=0.8)
        ax.tick_params(axis="x", labelsize=8)

    fig.text(0.05, 0.03, textwrap.fill("Figura: %s. Em azul, o RMA*; em cinza, os demais algoritmos. "
             "Lucro = 15 × recompensas pegas − custo do caminho." % titulo, 160), fontsize=10, color=TEXTO, va="bottom")
    if arquivo:
        fig.savefig(arquivo, dpi=130, facecolor=FUNDO)
    if trava:
        plt.show()
    else:
        fig.show()
