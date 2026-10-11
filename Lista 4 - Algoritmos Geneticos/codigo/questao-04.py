# Lista 4 - Questao 4
# uma geracao de um AG com 6 individuos de 6 bits, maximizando f(x) = x^2
# selecao por roleta, cruzamento de um ponto (taxa 80%) e mutacao bit a bit (taxa 5%)

import random

random.seed(7)   # semente fixa pra execucao ser sempre igual

populacao = ["001100", "010101", "111000", "000111", "101011", "101000"]


def aptidao(cromossomo):
    x = int(cromossomo, 2)
    return x * x


def mostra(titulo, pop):
    print(titulo)
    for c in pop:
        print("  ", c, "x =", int(c, 2), "f(x) =", aptidao(c))
    soma = sum(aptidao(c) for c in pop)
    print("   soma =", soma, " media = %.1f" % (soma / len(pop)), " melhor =", max(aptidao(c) for c in pop))
    print()


mostra("POPULACAO INICIAL", populacao)

# roleta: cada individuo ocupa uma faixa proporcional a aptidao
total = sum(aptidao(c) for c in populacao)
faixas = []
inicio = 0
for c in populacao:
    fim = inicio + aptidao(c)
    faixas.append((c, inicio, fim))
    print("faixa de", c, ": [%d, %d)  probabilidade %.1f%%" % (inicio, fim, 100 * aptidao(c) / total))
    inicio = fim
print()

selecionados = []
for i in range(6):
    r = random.uniform(0, total)
    for c, ini, fim in faixas:
        if ini <= r < fim:
            selecionados.append(c)
            print("roleta sorteou %.1f -> %s" % (r, c))
            break
print()

# cruzamento de um ponto, em pares
filhos = []
for i in range(0, 6, 2):
    pai1, pai2 = selecionados[i], selecionados[i + 1]
    r = random.random()
    corte = random.randint(1, 5)
    if r < 0.8:
        f1 = pai1[:corte] + pai2[corte:]
        f2 = pai2[:corte] + pai1[corte:]
    else:
        f1, f2 = pai1, pai2   # nao cruzou, filhos iguais aos pais
    print("pais", pai1, pai2, " r = %.2f  corte depois do bit %d ->" % (r, corte), f1, f2)
    filhos += [f1, f2]
print()

# mutacao: cada bit tem 5% de chance de inverter
nova = []
for c in filhos:
    bits = list(c)
    for i in range(6):
        if random.random() < 0.05:
            bits[i] = "1" if bits[i] == "0" else "0"
            print("mutacao no bit", i + 1, "de", c)
    nova.append("".join(bits))
print()

mostra("NOVA POPULACAO", nova)
