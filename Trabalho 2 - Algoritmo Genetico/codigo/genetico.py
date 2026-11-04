# algoritmo genetico que monta a grade
#
# cromossomo = vetor de inteiros, um gene por BLOCO de aulas (como no artigo da UFPB,
# onde cada gene e uma aula e o valor e o slot dela). O valor do gene e o slot onde o
# bloco comeca. Ex.: AED I tem 6 aulas = 2 blocos de 3, entao ocupa 2 genes.

import random
from dados import divide_em_blocos, inicios_possiveis
from avaliacao import avalia


class Problema:
    def __init__(self, disciplinas, indisponivel, modo="enunciado"):
        self.disciplinas = disciplinas
        self.indisponivel = indisponivel
        self.modo = modo
        self.genes = []   # (disciplina, tamanho do bloco, slots onde o bloco pode comecar)
        for d in disciplinas:
            for tamanho in divide_em_blocos(d.aulas_semana):
                self.genes.append((d, tamanho, inicios_possiveis(tamanho)))

    def decodifica(self, cromossomo):
        grade = {d.codigo: [] for d in self.disciplinas}
        for (d, tamanho, _), inicio in zip(self.genes, cromossomo):
            for i in range(tamanho):
                grade[d.codigo].append(inicio + i)
        return grade

    def fitness(self, cromossomo):
        return avalia(self.decodifica(cromossomo), self.disciplinas, self.indisponivel, self.modo)[0]

    def aleatorio(self):
        return [random.choice(possiveis) for _, _, possiveis in self.genes]


# ---------------- selecao ----------------

def roleta(populacao, notas):
    total = sum(notas)
    giro = random.uniform(0, total)
    acumulado = 0
    for individuo, nota in zip(populacao, notas):
        acumulado += nota
        if acumulado >= giro:
            return individuo
    return populacao[-1]


def torneio(populacao, notas, k=3):
    melhor = random.randrange(len(populacao))
    for _ in range(k - 1):
        outro = random.randrange(len(populacao))
        if notas[outro] > notas[melhor]:
            melhor = outro
    return populacao[melhor]


# truncamento: so os 40% melhores podem ser pais, todos com a mesma chance (UFPB)
def truncamento(populacao, notas, limiar=0.4):
    ordem = sorted(range(len(populacao)), key=lambda i: notas[i], reverse=True)
    corte = max(2, int(len(populacao) * limiar))
    return populacao[random.choice(ordem[:corte])]


SELECOES = {"roleta": roleta, "torneio": torneio, "truncamento": truncamento}


# ---------------- cruzamento ----------------

def um_ponto(pai, mae):
    corte = random.randint(1, len(pai) - 1)
    return pai[:corte] + mae[corte:], mae[:corte] + pai[corte:]


def dois_pontos(pai, mae):
    a, b = sorted(random.sample(range(1, len(pai)), 2))
    return pai[:a] + mae[a:b] + pai[b:], mae[:a] + pai[a:b] + mae[b:]


def uniforme(pai, mae):
    filho1, filho2 = [], []
    for g1, g2 in zip(pai, mae):
        if random.random() < 0.5:   # mascara de cruzamento sorteada gene a gene
            filho1.append(g1)
            filho2.append(g2)
        else:
            filho1.append(g2)
            filho2.append(g1)
    return filho1, filho2


CRUZAMENTOS = {"um_ponto": um_ponto, "dois_pontos": dois_pontos, "uniforme": uniforme}


# ---------------- mutacao ----------------

# cada gene tem chance taxa de mudar o bloco pra outro slot possivel
def mutacao(problema, individuo, taxa):
    for i, (_, _, possiveis) in enumerate(problema.genes):
        if random.random() < taxa:
            individuo[i] = random.choice(possiveis)
    return individuo


# ---------------- ciclo do AG ----------------

def executa(problema, selecao="torneio", cruzamento="um_ponto", tam_populacao=200,
            geracoes=800, taxa_cruzamento=0.75, taxa_mutacao=0.02, elite=1,
            busca_local=None, semente=None, mostra=False):
    if semente is not None:
        random.seed(semente)
    seleciona = SELECOES[selecao]
    cruza = CRUZAMENTOS[cruzamento]

    populacao = [problema.aleatorio() for _ in range(tam_populacao)]
    notas = [problema.fitness(c) for c in populacao]
    historico = []   # (melhor, media) de cada geracao
    melhor, nota_melhor, geracao_melhor = None, -1, 0

    for geracao in range(geracoes):
        # guarda o melhor de todos
        i = max(range(tam_populacao), key=lambda j: notas[j])
        if notas[i] > nota_melhor:
            melhor, nota_melhor, geracao_melhor = populacao[i][:], notas[i], geracao
        historico.append((nota_melhor, sum(notas) / tam_populacao))
        if mostra and geracao % 100 == 0:
            print("geracao %4d   melhor %.4f   media %.4f" % (geracao, nota_melhor, historico[-1][1]))

        # elitismo: os melhores passam direto pra proxima geracao
        ordem = sorted(range(tam_populacao), key=lambda j: notas[j], reverse=True)
        nova = [populacao[j][:] for j in ordem[:elite]]

        while len(nova) < tam_populacao:
            pai = seleciona(populacao, notas)
            mae = seleciona(populacao, notas)
            if random.random() < taxa_cruzamento:
                filho1, filho2 = cruza(pai, mae)
            else:
                filho1, filho2 = pai[:], mae[:]
            for filho in (filho1, filho2):
                mutacao(problema, filho, taxa_mutacao)
                if busca_local is not None:
                    busca_local(problema, filho)
                if len(nova) < tam_populacao:
                    nova.append(filho)

        populacao = nova
        notas = [problema.fitness(c) for c in populacao]

    # criterio de parada: numero de geracoes (o enunciado pede pelo menos 500)
    i = max(range(tam_populacao), key=lambda j: notas[j])
    if notas[i] > nota_melhor:
        melhor, nota_melhor, geracao_melhor = populacao[i][:], notas[i], geracoes
    return melhor, nota_melhor, geracao_melhor, historico
