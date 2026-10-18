# le o mapa em texto e monta o grafo
# cada celula andavel vira um vertice (linha, coluna)
# a aresta para o vizinho custa o terreno do vizinho (custo de entrar nele)

# . plano   : arenoso   ^ rochoso   ~ pantano   # parede
# A agente   P premio   $ recompensa (os tres ficam em terreno plano)
CUSTO = {".": 1, ":": 4, "^": 10, "~": 20}
VALOR_RECOMPENSA = 15

# ordem fixa dos vizinhos pra execucao ser sempre igual: cima, direita, baixo, esquerda
DIRECOES = [(-1, 0), (0, 1), (1, 0), (0, -1)]


class Mapa:
    # le o mapa de um arquivo ou recebe as linhas prontas (mapa aleatorio)
    def __init__(self, arquivo=None, linhas=None):
        if linhas is None:
            with open(arquivo, encoding="utf-8") as f:
                linhas = [linha.rstrip("\n") for linha in f if linha.strip()]
        self.linhas = linhas

        self.terreno = {}
        self.recompensas = []
        self.inicio = None
        self.premio = None
        for l, linha in enumerate(self.linhas):
            for c, simbolo in enumerate(linha):
                if simbolo == "#":
                    continue
                if simbolo == "A":
                    self.inicio = (l, c)
                elif simbolo == "P":
                    self.premio = (l, c)
                elif simbolo == "$":
                    self.recompensas.append((l, c))
                if simbolo in CUSTO:
                    self.terreno[(l, c)] = simbolo
                else:
                    self.terreno[(l, c)] = "."

        # lista de adjacencia: grafo[vertice] = {vizinho: custo}
        self.grafo = {}
        for (l, c) in self.terreno:
            self.grafo[(l, c)] = {}
            for dl, dc in DIRECOES:
                vizinho = (l + dl, c + dc)
                if vizinho in self.terreno:
                    self.grafo[(l, c)][vizinho] = CUSTO[self.terreno[vizinho]]

    def custo(self, caminho):
        total = 0
        for i in range(len(caminho) - 1):
            total += self.grafo[caminho[i]][caminho[i + 1]]
        return total

    def coletadas(self, caminho):
        return [r for r in self.recompensas if r in caminho]


# heuristica usada pela gulosa, A* e RMA* (o menu troca entre as duas)
HEURISTICA = "manhattan"


def usa_heuristica(nome):
    global HEURISTICA
    HEURISTICA = nome


# as duas sao admissiveis: o agente so anda em 4 direcoes e cada passo custa no minimo 1
#   euclidiana = distancia em linha reta (a da aula, mapa da Romenia)
#   manhattan  = soma dos passos na vertical e na horizontal (nunca menor que a linha reta)
def h(a, b):
    if HEURISTICA == "euclidiana":
        return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5
    return abs(a[0] - b[0]) + abs(a[1] - b[1])
