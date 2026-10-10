# Questão 19

## Modelagem

Representei cada estado como uma sequência de 7 posições, com P para peça preta, B para branca e _ para o lugar vazio:

```
Estado inicial:   P P P _ B B B
Meta:             B B B P P P   (com o vazio em qualquer posição)
```

O enunciado não fala onde o vazio tem que ficar no final, então considerei meta qualquer estado em que, lendo da esquerda para a direita e pulando o vazio, as peças ficam B B B P P P.

Os três movimentos são sempre uma peça indo para o lugar vazio:

| Movimento | Distância até o vazio | Custo |
|:--|:--:|:--:|
| deslizar | 1 casa | 1 |
| pular por cima de 1 peça | 2 casas | 1 |
| pular por cima de 2 peças | 3 casas | 2 |

## A heurística proposta

**h(n) = número de pares (preta, branca) em que a preta está à esquerda da branca.**

São os pares que ainda estão "na ordem errada". Contando:

- No estado inicial P P P _ B B B, cada uma das 3 pretas está à esquerda de cada uma das 3 brancas, então h = 3 × 3 = **9**.
- Na meta, todas as brancas estão à esquerda de todas as pretas, então h = **0**.

Exemplo de um estado no meio: em B P B _ P P B, os pares preta antes de branca são a primeira P com o B da posição 3 e com o último B, e as duas P do meio com o último B. Então h = 4.

## Por que ela é admissível

A ideia é ver quanto cada movimento consegue diminuir o h, e comparar com o custo dele:

- **Deslizar:** a peça só troca de lugar com o vazio. Ela não passa por cima de ninguém, então a ordem das peças não muda. Custa 1 e o h diminui **0**.
- **Pular 1 peça:** a peça que pula troca de ordem com uma peça. Isso pode desfazer no máximo 1 par errado. Custa 1 e o h diminui **no máximo 1**.
- **Pular 2 peças:** a peça que pula troca de ordem com duas peças. Pode desfazer no máximo 2 pares errados. Custa 2 e o h diminui **no máximo 2**.

Em todos os casos, **cada unidade de custo desfaz no máximo um par errado**. Para chegar na meta é preciso desfazer todos os h(n) pares, então qualquer solução custa pelo menos h(n):

```
h(n) ≤ h*(n)
```

A heurística nunca superestima, então é admissível. Pelo mesmo argumento ela também é consistente: um movimento de custo c muda o h em no máximo c, então h(n) ≤ c + h(n').

## Conferindo

Para ter certeza, escrevi um programa pequeno ([`codigo/questao-19.py`](codigo/questao-19.py), saída em [`codigo/saida-questao-19.txt`](codigo/saida-questao-19.txt)) que gera todos os estados alcançáveis a partir do inicial (são 140) e calcula o custo real mínimo de cada um até a meta. Em todos os 140, o h ficou menor ou igual ao custo real. No estado inicial, h = 9 e o custo real ótimo é 14, então a estimativa é otimista, como tem que ser.

Uma heurística mais simples também seria admissível: o número de peças brancas que não estão nas 3 primeiras posições. Cada uma dessas precisa de pelo menos um movimento, de custo pelo menos 1. Mas no estado inicial ela vale só 3, contra 9 da de pares, então a de pares está bem mais perto dos 14 reais e é mais informativa.

## Resumo de como cheguei na solução

Comecei pensando na heurística mais óbvia, contar quantas peças estão fora do lado certo, porque é parecida com a das peças fora do lugar do 8-puzzle da aula. Funcionava, mas dava só 3 no estado inicial, muito longe do custo real. Aí pensei no que o problema realmente pede: inverter a ordem das peças. Isso me lembrou de contar pares fora de ordem, e daí veio a heurística dos pares preta antes de branca.

A parte mais importante foi justificar a admissibilidade. Analisei cada um dos três movimentos e percebi que o custo deles bate exatamente com o máximo de pares que conseguem desfazer: o pulo de 2 peças custa 2 e desfaz no máximo 2 pares. Isso garante que nenhuma unidade de custo desfaz mais de um par. Por último, como eu não tinha certeza de que não tinha esquecido algum caso, testei em todos os estados possíveis com um programa e a desigualdade valeu em todos.
