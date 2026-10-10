# Questão 13

A principal desvantagem do A* é o **consumo de memória**.

Ele guarda na memória todos os nós gerados. Os da fronteira ficam lá porque podem ser escolhidos depois, e os já expandidos ficam para ele poder voltar para outro ramo, o backtracking que o professor mostrou no exemplo da Romênia, quando o A* larga Rimnicu Vilcea e volta para Fagaras. O custo de memória é O(b^d), o mesmo da busca em largura. Na prática, o A* costuma ficar sem memória bem antes de ficar sem tempo.

Isso aparece até nos exemplos pequenos desta lista:

| Questão | Nós visitados pelo A* | Nós que ficaram esperando na fronteira |
|:--|:--:|:--:|
| 15 (mapa de A até R) | 10 | 16 |
| 17a (robô, com h1) | 15 | 20 |

Mesmo achando a solução rápido, ele termina com mais nós guardados na fronteira do que nós que realmente visitou. Num problema grande essa fronteira cresce exponencialmente.

O slide fala que as principais variantes do A* existem justamente para resolver isso:

- **IDA\*** (Iterative Deepening A*): faz o mesmo que o aprofundamento iterativo da Lista 1, mas o limite de cada rodada é o valor de f, e não a profundidade. Gasta muito menos memória.
- **SMA\*** (Simplified Memory-Bounded A*): fixa um número máximo de nós na memória. Quando enche, descarta o nó com o pior f.

Uma segunda desvantagem é que **o desempenho depende totalmente da heurística**. Com uma heurística ruim, perto de zero, ele vira um custo uniforme e expande muita coisa. E achar uma heurística boa, que seja admissível e ainda informativa, nem sempre é fácil.

## Resumo de como cheguei na solução

O slide da análise do A* diz que ele "guarda todos os nós expandidos na memória, para possibilitar o backtracking", e o das variantes fala que IDA* e SMA* são "tentativas para minimizar a quantidade de memória gasta pelo A*, uma de suas principais desvantagens". Juntei as duas frases para responder. Para não ficar só na teoria, contei nas minhas simulações das questões 15 e 17 quantos nós ficaram na fronteira no final, e em todas sobrou mais nó esperando do que nó visitado, o que mostra bem o problema da memória mesmo em casos pequenos.
