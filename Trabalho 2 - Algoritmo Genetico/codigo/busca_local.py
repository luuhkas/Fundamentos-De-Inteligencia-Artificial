# busca local pra juntar com o AG (algoritmo memetico)
#
# ideia de Burke, Newall e Weare (1996), "A memetic algorithm for university exam
# timetabling": depois do cruzamento e da mutacao, cada filho passa por uma busca local
# (subida de encosta) que melhora ele antes de entrar na populacao. O artigo da UFT
# (Descardeci et al., 2017) tambem cita essa saida: uma funcao de "reparacao" depois
# dos operadores (Nunes et al., 2013).
#
# aqui: sorteia alguns genes do filho e, pra cada um, testa todos os slots onde o bloco
# pode comecar, ficando com o que der a maior fitness (subida de encosta)

import random


def subida_de_encosta(problema, individuo, genes=4):
    nota = problema.fitness(individuo)
    for i in random.sample(range(len(individuo)), genes):
        original = individuo[i]
        melhor_inicio = original
        for inicio in problema.genes[i][2]:
            if inicio == original:
                continue
            individuo[i] = inicio
            nova = problema.fitness(individuo)
            if nova > nota:
                nota = nova
                melhor_inicio = inicio
        individuo[i] = melhor_inicio
    return individuo
