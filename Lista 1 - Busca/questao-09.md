# Questão 9

O código está em [`codigo/questao-09.py`](codigo/questao-09.py) e a saída completa em [`codigo/saida-questao-09.txt`](codigo/saida-questao-09.txt).

## O mapa

O enunciado pede só as cidades que estão antes de Bucareste, então tirei do mapa Giurgiu, Urziceni, Hirsova, Eforie, Vaslui, Iasi e Neamt. Sobraram 13 cidades, com os vizinhos em ordem alfabética, igual nas outras questões.

```python
romenia = {
    "Arad":      {"Sibiu": 140, "Timisoara": 118, "Zerind": 75},
    "Bucharest": {"Fagaras": 211, "Pitesti": 101},
    ...
    "Zerind":    {"Arad": 75, "Oradea": 71},
}
```

## O que mudei nos algoritmos da questão 8

**Profundidade limitada.** Troquei a pilha da questão 8 por uma função recursiva. Na recursão a profundidade do nó é o tamanho do caminho menos 1, então colocar o limite ficou fácil: quando o nó chega no limite, a função não gera os filhos dele e volta. É o que o slide fala, "nodos na profundidade l não possuem sucessores".

```python
def profundidade_limitada(caminho, objetivo, limite, visitados):
    no = caminho[-1]
    visitados.append(no)
    if no == objetivo:
        return caminho
    if len(caminho) - 1 == limite:   # chegou no limite, nao expande
        return None
    for vizinho in romenia[no]:
        if vizinho not in caminho:   # nao volta pra cidade do proprio caminho
            resultado = profundidade_limitada(caminho + [vizinho], objetivo, limite, visitados)
            if resultado is not None:
                return resultado
    return None
```

**Aprofundamento iterativo.** É só um laço em volta da profundidade limitada, começando no limite 0 e subindo de um em um até achar ou até chegar no limite máximo.

```python
def aprofundamento_iterativo(inicio, objetivo, limite_maximo, iteracoes):
    visitados = []
    for limite in range(limite_maximo + 1):
        desta_vez = []
        caminho = profundidade_limitada([inicio], objetivo, limite, desta_vez)
        ...
```

**Como o limite é contado.** Usei o limite contando trechos, como no slide: limite 0 é só Arad, limite 1 vai até os vizinhos de Arad e assim por diante. Na aula o professor conta os níveis começando do 1, com a raiz sendo o nível 1. Para esta questão não muda o resultado, porque Bucareste está a 3 trechos de Arad, então nas duas formas de contar o limite 2 não alcança e os limites 4 e 7 alcançam.

## Profundidade limitada

| Limite | Visitados | Resultado | Caminho | Custo | Tempo médio |
|:--:|:--:|:--|:--|:--:|:--:|
| 2 | 9 | **não achou** | | | 1,98 µs |
| 4 | 4 | achou | Arad, Sibiu, Fagaras, Bucharest | 450 km | 0,87 µs |
| 7 | 4 | achou | Arad, Sibiu, Fagaras, Bucharest | 450 km | 0,87 µs |

Com **limite 2** ela visitou Arad, Sibiu, Fagaras, Oradea, Rimnicu Vilcea, Timisoara, Lugoj, Zerind e Oradea de novo, e desistiu. Existe solução, mas ela está na profundidade 3 e o limite não deixa chegar lá. É a situação l < d da questão 6, em que a profundidade limitada não é completa.

Com **limite 4 e limite 7** o resultado foi igual em tudo, até no tempo. A busca desce por Arad, Sibiu, Fagaras e acha Bucareste na profundidade 3, antes de chegar perto do limite. O limite só faz diferença quando é menor que a profundidade da solução.

Uma coisa curiosa: com limite 2 ela demorou mais que com limite 4. Com limite 2 ela precisa olhar a árvore toda até a profundidade 2 para ter certeza de que não tem solução, já com limite 4 ela acha logo no primeiro ramo.

## Aprofundamento iterativo

| Limite máximo | Rodadas (limite: visitados) | Visitados no total | Resultado | Custo | Tempo médio |
|:--:|:--|:--:|:--|:--:|:--:|
| 2 | 0: 1, 1: 4, 2: 9 | 14 | **não achou** | | 3,41 µs |
| 4 | 0: 1, 1: 4, 2: 9, 3: 4 | 18 | achou | 450 km | 4,45 µs |
| 7 | 0: 1, 1: 4, 2: 9, 3: 4 | 18 | achou | 450 km | 4,43 µs |

Com **limite máximo 2** ela fez as rodadas 0, 1 e 2 e nenhuma alcançou Bucareste, pelo mesmo motivo da limitada.

Com **limite máximo 4 e 7** ela parou na rodada do limite 3, que foi a primeira a alcançar Bucareste. Por isso os dois deram exatamente o mesmo resultado: o aprofundamento iterativo nunca chega a usar os limites 4, 5, 6 e 7, porque já achou antes. A pequena diferença de tempo entre eles é só variação da medida.

## Comparando os dois

Com o mesmo limite 4, a limitada visitou 4 nós e a iterativa visitou 18, porque a iterativa refez as rodadas 0, 1 e 2 antes de chegar na rodada 3. Isso também aparece no tempo: 0,87 µs contra 4,45 µs.

Em troca desse retrabalho, a iterativa garante que a solução encontrada é a mais rasa, ou seja, a de menos trechos. A limitada não garante isso: ela devolve a primeira solução que aparecer dentro do limite. Aqui as duas devolveram o mesmo caminho porque Sibiu e Fagaras vêm primeiro na ordem alfabética, mas foi coincidência.

E igual na questão 5, nenhuma das duas achou a rota mais curta em quilômetros, que é Arad, Sibiu, Rimnicu Vilcea, Pitesti, Bucareste, com 418 km. Ela tem 4 trechos, e as duas buscas não olham a distância, só a profundidade.

## Resumo de como cheguei na solução

Antes de mexer no código, conferi no mapa a que profundidade Bucareste está de Arad. São 3 trechos, por Sibiu e Fagaras. Isso já me deixou prever o resultado: o limite 2 ia falhar e os limites 4 e 7 iam dar a mesma coisa. Rodar o código serviu para confirmar.

Para a profundidade limitada, troquei a pilha da questão 8 por recursão, porque assim a profundidade de cada nó vem do tamanho do caminho e o limite vira um if só. O aprofundamento iterativo ficou sendo um laço que chama a limitada com o limite subindo.

O ponto em que mais travei foi o controle de estados repetidos. Primeiro pensei em usar o mesmo conjunto `conhecidos` da questão 8, mas percebi que com limite isso dá errado: se uma cidade é alcançada primeiro por um caminho longo e fica marcada como conhecida, ela não pode mais ser alcançada por um caminho mais curto, e aí pode faltar profundidade para chegar na meta. E se o conjunto não fosse zerado a cada rodada, uma cidade vista numa rodada ficaria proibida na seguinte. Troquei por uma regra mais simples, de não voltar para uma cidade que já está no caminho atual. Isso evita ficar em círculo entre Arad e Sibiu e não atrapalha as rodadas seguintes. Por causa dessa regra, Oradea aparece duas vezes no limite 2, uma vez vindo de Sibiu e outra vindo de Zerind.

Os tempos foram medidos do mesmo jeito da questão 8, com a média de 100 mil execuções.
