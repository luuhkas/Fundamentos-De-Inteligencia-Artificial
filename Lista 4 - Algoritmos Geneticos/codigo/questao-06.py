# Lista 4 - Questao 6
# AG pra achar a rota de menor custo passando uma vez por cada uma das 5 cidades
# cromossomo = ordem das cidades, a rota volta pra primeira no final

import random
import itertools

random.seed(3)   # semente fixa pra execucao ser sempre igual

distancia = {(1, 2): 2, (1, 3): 9, (1, 4): 3, (1, 5): 6, (2, 3): 4,
             (2, 4): 3, (2, 5): 8, (3, 4): 7, (3, 5): 3, (4, 5): 3}


def d(a, b):
    return distancia[(min(a, b), max(a, b))]


def custo(rota):
    total = 0
    for i in range(5):
        total += d(rota[i], rota[(i + 1) % 5])   # o % 5 fecha a volta
    return total


def fitness(rota):
    return 1 / custo(rota)   # menor custo = maior fitness


def cruzamento_ordem(pai1, pai2, a, b):
    # o filho fica com o pedaco [a, b) do pai1 e completa com o resto na ordem do pai2
    meio = pai1[a:b]
    resto = [c for c in pai2 if c not in meio]
    return resto[:a] + meio + resto[a:]


def mutacao(rota, i, j):
    nova = rota[:]
    nova[i], nova[j] = nova[j], nova[i]   # troca duas cidades de lugar
    return nova


def mostra(rota):
    return "-".join(str(c) for c in rota) + "-" + str(rota[0])


populacao = [[1, 3, 2, 5, 4], [1, 4, 3, 2, 5]]

for geracao in range(1, 6):
    pai1, pai2 = populacao
    print("GERACAO", geracao)
    print("  pais:", mostra(pai1), "custo", custo(pai1), " |", mostra(pai2), "custo", custo(pai2))

    a = random.randint(0, 3)
    b = random.randint(a + 1, 5)
    filho1 = cruzamento_ordem(pai1, pai2, a, b)
    filho2 = cruzamento_ordem(pai2, pai1, a, b)
    print("  cruzamento mantendo as posicoes", a + 1, "a", b)
    print("  filhos:", mostra(filho1), "custo", custo(filho1), " |", mostra(filho2), "custo", custo(filho2))

    i, j = random.sample(range(5), 2)
    k, l = random.sample(range(5), 2)
    filho1 = mutacao(filho1, i, j)
    filho2 = mutacao(filho2, k, l)
    print("  mutacao: troca das posicoes", i + 1, "e", j + 1, "no filho 1 e", k + 1, "e", l + 1, "no filho 2")
    print("  filhos mutados:", mostra(filho1), "custo", custo(filho1), " |", mostra(filho2), "custo", custo(filho2))

    # ficam os 2 melhores entre pais e filhos
    populacao = sorted([pai1, pai2, filho1, filho2], key=custo)[:2]
    print("  sobrevivem:", mostra(populacao[0]), "custo", custo(populacao[0]), " |", mostra(populacao[1]), "custo", custo(populacao[1]))
    print()

# conferindo com todas as rotas possiveis (a cidade 1 fixa no comeco)
melhor = min(([1] + list(p) for p in itertools.permutations([2, 3, 4, 5])), key=custo)
print("melhor rota testando todas:", mostra(melhor), "custo", custo(melhor))
