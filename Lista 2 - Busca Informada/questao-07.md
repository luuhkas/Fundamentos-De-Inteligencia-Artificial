# Questão 7

## O que significa h1 dominar h2

Sendo h1 e h2 duas heurísticas **admissíveis** para o mesmo problema, h1 domina h2 quando, para todo nó n:

```
h1(n) ≥ h2(n)
```

Ou seja, h1 dá sempre um valor maior ou igual ao de h2. Como as duas são admissíveis, nenhuma passa do custo real h*(n), então a ordem fica assim:

```
h2(n) ≤ h1(n) ≤ h*(n)
```

h1 está mais perto do custo verdadeiro. É uma estimativa mais informada, que erra menos para baixo.

Um detalhe: no slide da aula a desigualdade aparece como "h2(n) ≤ h1(n)" na frase que diz que h2 domina h1, o que fica invertido em relação à conclusão do próprio slide. Pela definição do Russell e Norvig, quem domina é a heurística de valores **maiores**, e é isso que faz sentido com o exemplo da aula, em que a soma das distâncias domina o número de peças fora do lugar.

## O que isso quer dizer para a eficiência do A*

**O A* usando h1 nunca expande mais nós do que o A* usando h2.** Na maioria dos casos expande bem menos.

O motivo é que o A* expande, com certeza, todo nó com f(n) < C*, em que C* é o custo da solução ótima. Como f(n) = g(n) + h(n), isso é o mesmo que todo nó com h(n) < C* − g(n). Se h1(n) ≥ h2(n), qualquer nó que passa nesse corte com h1 também passa com h2, mas o contrário não acontece. Então o conjunto de nós que o A* abre com h1 está contido no conjunto que ele abre com h2.

O exemplo da aula é o 8-puzzle, com h1 = número de peças fora do lugar e h2 = soma das distâncias de cada peça até a posição final. A soma das distâncias domina, porque toda peça fora do lugar está a pelo menos 1 movimento de distância. Na tabela que o professor mostrou, para uma solução de profundidade 10, o A* gerou 93 nós com a heurística das peças fora do lugar e 39 com a das distâncias. O fator de ramificação efetivo caiu de 1,38 para 1,22.

Eu vi isso acontecer na questão 17 desta lista. Lá a heurística h2 que propus domina h1, e o A* visitou 8 nós com h2 contra 15 com h1, chegando na mesma solução.

A conclusão do slide é que vale mais a pena usar a heurística admissível de valores maiores, desde que ela não seja cara demais de calcular.

## Resumo de como cheguei na solução

Comecei pela definição do slide e estranhei a desigualdade, porque ela dizia que h2 domina h1 com h2 ≤ h1, e logo abaixo dizia que h2 é melhor. Fui conferir no Russell e Norvig e confirmei que o certo é a heurística dominante ter os valores maiores, então escrevi a definição assim e deixei o detalhe registrado.

Para explicar a eficiência, em vez de só dizer que é "melhor", tentei entender o porquê. A chave foi lembrar que o A* abre todo nó com f menor que o custo da solução ótima. Com uma heurística maior, menos nós ficam abaixo desse corte. Usei os números do 8-puzzle da aula como exemplo e depois liguei com a questão 17, onde comparei as duas heurísticas na prática e o número de nós visitados caiu quase pela metade.
