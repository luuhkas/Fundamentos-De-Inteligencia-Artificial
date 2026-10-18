# Trabalho 1 - Busca
# menu: escolhe o mapa e o destino, anima um algoritmo ou mostra o comparativo
# rodar de dentro da pasta codigo: python3 main.py

import os
from mapa import Mapa, usa_heuristica
from visual import mostra_mapa, anima
from comparativo import ALGORITMOS, tabela, grafico, compara_heuristicas, compara_aleatorios
from gerador import gera_mapa

PASTA = os.path.dirname(os.path.abspath(__file__))
PASTA_MAPAS = os.path.join(PASTA, "..", "mapas")
PASTA_IMAGENS = os.path.join(PASTA, "..", "imagens")


def escolhe_mapa():
    arquivos = sorted(os.listdir(PASTA_MAPAS))
    for i, nome in enumerate(arquivos):
        print("%d - %s" % (i + 1, nome))
    print("%d - mapa aleatorio" % (len(arquivos) + 1))
    opcao = int(input("mapa: ")) - 1
    if opcao == len(arquivos):
        return Mapa(linhas=gera_mapa()), "aleatorio"
    return Mapa(os.path.join(PASTA_MAPAS, arquivos[opcao])), arquivos[opcao][:-4]


def escolhe_destino(mapa):
    mostra_mapa(mapa, mapa.premio)
    while True:
        texto = input("Digite a coordenada de destino 'linha coluna' (enter = premio %s): " % (mapa.premio,))
        if texto.strip() == "":
            return mapa.premio
        l, c = texto.split()
        destino = (int(l), int(c))
        if destino in mapa.terreno:
            return destino
        print("esse ponto e parede ou fora do mapa")


mapa, nome_mapa = escolhe_mapa()
destino = escolhe_destino(mapa)
heuristica = "manhattan"
while True:
    print()
    print("heuristica atual: %s" % heuristica)
    for i, (nome, _) in enumerate(ALGORITMOS):
        print("%d - animar %s" % (i + 1, nome))
    print("6 - comparativo (tabela + grafico)")
    print("7 - trocar destino")
    print("8 - trocar heuristica (euclidiana / manhattan)")
    print("9 - comparar as duas heuristicas")
    print("10 - trocar de mapa (desenhado ou aleatorio)")
    print("11 - comparar em 30 mapas aleatorios")
    print("0 - sair")
    opcao = input("opcao: ")
    if opcao == "0":
        break
    elif opcao == "6":
        print("heuristica: %s" % heuristica)
        resultados = tabela(mapa, destino)
        grafico(resultados, os.path.join(PASTA_IMAGENS, "comparativo-%s-%s.png" % (nome_mapa, heuristica)))
    elif opcao == "7":
        destino = escolhe_destino(mapa)
    elif opcao == "8":
        if heuristica == "manhattan":
            heuristica = "euclidiana"
        else:
            heuristica = "manhattan"
        usa_heuristica(heuristica)
    elif opcao == "9":
        compara_heuristicas(mapa, destino, heuristica,
                            os.path.join(PASTA_IMAGENS, "heuristicas-%s.png" % nome_mapa))
    elif opcao == "10":
        mapa, nome_mapa = escolhe_mapa()
        destino = escolhe_destino(mapa)
    elif opcao == "11":
        medias = compara_aleatorios(30)
        grafico(medias, os.path.join(PASTA_IMAGENS, "comparativo-aleatorios-%s.png" % heuristica),
                "média dos 5 algoritmos em 30 mapas aleatórios (só os mapas com caminho)")
    elif opcao in ("1", "2", "3", "4", "5"):
        nome, busca = ALGORITMOS[int(opcao) - 1]
        rota, ordem, gerados = busca(mapa, destino)
        if rota is None:
            print(nome + ": nao existe caminho ate o destino (parede, beco ou sala fechada)")
        print("nos expandidos: %d   nos gerados: %d" % (len(ordem), gerados))
        titulo = nome
        if opcao in ("3", "4", "5"):
            titulo = "%s   (heurística %s)" % (nome, heuristica)
        anima(mapa, rota, ordem, destino, titulo)
