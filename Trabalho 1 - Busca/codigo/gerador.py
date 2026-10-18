# gera um mapa aleatorio no mesmo formato dos arquivos de texto da pasta mapas
# so aceita mapa que cumpre o enunciado: >= 30 vertices e os 4 terrenos
# o premio pode cair num lugar sem caminho, ai o programa tem que perceber

import random

# chance de cada celula de dentro ser: parede, plano, arenoso, rochoso, pantano
SIMBOLOS = ["#", ".", ":", "^", "~"]
PESOS = [28, 44, 12, 9, 7]


def gera_mapa(semente=None, altura=12, largura=20, recompensas=6):
    sorteio = random.Random(semente)
    while True:
        grade = []
        for l in range(altura):
            linha = []
            for c in range(largura):
                if l in (0, altura - 1) or c in (0, largura - 1):
                    linha.append("#")   # borda sempre e parede
                else:
                    linha.append(sorteio.choices(SIMBOLOS, PESOS)[0])
            grade.append(linha)

        livres = [(l, c) for l in range(altura) for c in range(largura) if grade[l][c] != "#"]
        terrenos = set(grade[l][c] for l, c in livres)
        if len(livres) < 30 + recompensas or len(terrenos) < 4:
            continue   # nao cumpre o enunciado, sorteia de novo

        # agente, premio e recompensas ficam em celulas sorteadas (em terreno plano)
        sorteados = sorteio.sample(livres, 2 + recompensas)
        l, c = sorteados[0]
        grade[l][c] = "A"
        l, c = sorteados[1]
        grade[l][c] = "P"
        for l, c in sorteados[2:]:
            grade[l][c] = "$"
        # confere de novo os 4 terrenos, porque A, P e $ podem ter coberto algum
        if len(set("".join("".join(linha) for linha in grade)) & set(".:^~")) == 4:
            return ["".join(linha) for linha in grade]
