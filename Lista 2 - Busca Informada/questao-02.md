# Questão 2

A diferença está na informação que cada uma usa para escolher qual nó da fronteira expandir.

**Busca não informada (ou cega).** Usa só o que está na formulação do problema: o estado inicial, a função-sucessor, o teste de meta e o custo dos passos. Ela não tem nenhuma noção de "estou chegando perto". Na Lista 1, a busca em largura não sabia que Fagaras estava mais perto de Bucareste do que Zerind, ela só abria os nós na ordem da fila. No máximo ela olha o g(n), o custo do caminho desde o início até o nó, como faz a busca de custo uniforme. O g(n) é uma referência ao passado: diz quanto já foi gasto, mas não diz nada sobre quanto falta.

**Busca informada (ou heurística).** Usa, além disso, um conhecimento específico do problema na forma de uma função heurística h(n), que estima o custo do nó n até a meta. É uma referência ao futuro. Com ela, a busca consegue dar preferência aos nós que parecem mais promissores e deixar de lado ramos que claramente se afastam do objetivo.

| | Não informada | Informada |
|:--|:--|:--|
| O que olha para escolher | ordem de chegada ou g(n) | h(n), sozinho ou somado com g(n) |
| Conhecimento do problema | só a formulação | formulação mais uma estimativa até a meta |
| Exemplos | largura, profundidade, custo uniforme, aprofundamento iterativo | gulosa, A* |
| Comportamento | espalha a busca por todo o espaço de estados | direciona a busca para perto da meta |

Na prática isso faz muita diferença. Na Lista 1, a largura visitou 9 cidades na Romênia e achou 450 km. O A* da aula, usando a distância em linha reta como h(n), foi direto pela região de Rimnicu Vilcea e Pitesti e achou os 418 km, que é a rota ótima.

## Resumo de como cheguei na solução

Comecei pelo slide que fala que as buscas cegas "utilizam apenas o custo de caminho do nó atual ao nó inicial (função g)", e daí veio a ideia de separar as duas pelo que cada uma enxerga: o passado, com g(n), e o futuro, com h(n). Para não ficar só na definição, usei o mapa da Romênia, que já tinha simulado na Lista 1, porque ali dá para comparar as duas no mesmo problema: a largura achou 450 km e o A* da aula achou 418 km.
