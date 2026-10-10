# Questão 16

O grafo tem **dois nós com o nome F**: um em cima, entre B e H, com estimativa 5, e outro embaixo, entre D e G, com estimativa 3. Como são estados diferentes, chamei o de baixo de **F'** para não misturar.

| Nó | h(n) | Vizinhos (custo) |
|:--:|:--:|:--|
| A | 14 | B 5, C 4 |
| B | 17 | A 5, F 10 |
| C | 12 | A 4, D 8 |
| D | 5 | C 8, E 3, F 2, F' 2 |
| E | 3 | D 3, G 2 |
| F | 5 | B 10, D 2, H 8 |
| F' | 3 | D 2, G 3 |
| G | 1 | E 2, F' 3, H 1 |
| H | 0 | F 8, G 1 (objetivo) |

As arestas não têm seta, então valem nos dois sentidos. Convenções, iguais às da questão 1: os sucessores entram em ordem alfabética, o nó de onde se veio também é gerado (como no exemplo da Romênia da aula), o teste de meta é feito quando o nó sai da fronteira, e os empates são resolvidos pelo nó mais perto da raiz e, depois, pelo mais à esquerda. Na fronteira, o número entre parênteses indica por onde o nó foi gerado quando o mesmo estado aparece mais de uma vez.

## A*

Cada nó da fronteira aparece com o seu f = g + h.

| Passo | Sai da fronteira | Fronteira depois do passo |
|:--:|:--|:--|
| 0 | | A 14 |
| 1 | A (0 + 14 = 14) | B 22, C 16 |
| 2 | C (4 + 12 = 16) | B 22, A 22, D 17 |
| 3 | D (12 + 5 = 17) | B 22, A 22, C 32, E 18, F 19, F' 17 |
| 4 | F' (14 + 3 = 17) | B 22, A 22, C 32, E 18, F 19, D 21, G(F') 18 |
| 5 | E (15 + 3 = 18) | B 22, A 22, C 32, F 19, D 21, G(F') 18, D 23, G(E) 18 |
| 6 | G vindo de E (17 + 1 = 18) | B 22, A 22, C 32, F 19, D 21, G(F') 18, D 23, E 22, F' 23, H(E) 18 |
| 7 | G vindo de F' (17 + 1 = 18) | B 22, A 22, C 32, F 19, D 21, D 23, E 22, F' 23, H(E) 18, E 22, F' 23, H(F') 18 |
| 8 | H vindo de E (18 + 0 = 18) | é a meta |

**Caminho:** A, C, D, E, G, H, com custo 4 + 8 + 3 + 2 + 1 = **18**.

Os empates foram resolvidos assim:

- **Passo 5:** E e G(F') tinham f = 18. E está na profundidade 3 e G(F') na 4, então saiu E.
- **Passo 6:** os dois G tinham f = 18 e a mesma profundidade. O que vem de E está mais à esquerda na árvore, porque E é gerado antes de F' pelo D.
- **Passos 7 e 8:** pelo mesmo motivo, o G vindo de F', que está numa profundidade menor, sai antes dos dois H, e entre os H sai o mais à esquerda.

Existe outro caminho com o mesmo custo, A, C, D, F', G, H, que também dá 4 + 8 + 2 + 3 + 1 = 18. Por isso o A* gerou o H duas vezes com f = 18. Qualquer um dos dois seria ótimo, e o desempate escolheu o de E.

## Busca gulosa

Cada nó da fronteira aparece só com o seu h.

| Passo | Sai da fronteira | Fronteira depois do passo |
|:--:|:--|:--|
| 0 | | A 14 |
| 1 | A (14) | B 17, C 12 |
| 2 | C (12) | B 17, A 14, D 5 |
| 3 | D (5) | B 17, A 14, C 12, E 3, F 5, F' 3 |
| 4 | E (3) | B 17, A 14, C 12, F 5, F' 3, D 5, G 1 |
| 5 | G (1) | B 17, A 14, C 12, F 5, F' 3, D 5, E 3, F' 3, H 0 |
| 6 | H (0) | é a meta |

**Caminho:** A, C, D, E, G, H, com custo **18**.

No passo 4 houve empate entre E e F', os dois com h = 3 e na mesma profundidade. Ganhou E, que está mais à esquerda.

## Comparando

| | A* | Gulosa |
|:--|:--:|:--:|
| Nós que saíram da fronteira | 8 | 6 |
| Tamanho da fronteira no fim | 11 | 8 |
| Custo do caminho | 18 | 18 |

Aqui a gulosa teve sorte. A heurística é boa nesse grafo, e todos os nós no caminho até H tinham h menor do que os que ficavam para trás, então ela foi direto e ainda acertou o ótimo. O A* fez dois passos a mais porque, quando o f empata, ele precisa conferir os dois caminhos de custo 18. Mas só o A* garante que 18 é o melhor, porque nada na gulosa impede que ela escolha um caminho caro quando a heurística engana.

## Resumo de como cheguei na solução

O primeiro problema foi o nome repetido: tem dois F no desenho, com estimativas diferentes. Tratei como dois estados e chamei o de baixo de F', porque misturar os dois mudaria todos os valores de h.

Depois montei a tabela de vizinhos e simulei as duas buscas escrevendo a fronteira completa depois de cada passo, que é o que a questão pede. No A* foi onde tive mais trabalho, porque apareceram vários empates em f = 18 e precisei decidir quem saía primeiro. Usei a mesma regra da questão 6, de preferir o nó mais perto da raiz e depois o mais à esquerda. Também percebi que a gulosa e o A* chegaram no mesmo custo, e conferi somando os caminhos na mão que existem dois caminhos de 18 até H, então os dois resultados estão certos.
