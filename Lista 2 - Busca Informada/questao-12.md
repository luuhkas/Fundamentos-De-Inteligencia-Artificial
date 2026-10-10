# Questão 12

**Sim, é correto.** A busca de custo uniforme é o A* com a heurística h(n) = 0 para todo nó.

O A* escolhe o nó da fronteira com menor f(n) = g(n) + h(n). Se h(n) = 0 em todo lugar, sobra f(n) = g(n), que é exatamente o critério do custo uniforme: expandir o nó com menor custo de caminho desde o início.

E a heurística nula é admissível, porque 0 ≤ h*(n) sempre, já que nenhum custo é negativo. Ela também é consistente, porque 0 ≤ c(n, n') + 0. Então o custo uniforme herda as garantias do A*: é completo e ótimo, nas mesmas condições.

Isso também ajuda a entender o que o h(n) faz no A*. A heurística nula é a menos informada possível. Qualquer outra heurística admissível domina ela, então, pelo que vimos na questão 7, o A* com uma heurística de verdade nunca expande mais nós do que o custo uniforme. Foi o que aconteceu na questão 1: os dois acharam o mesmo caminho de custo 43, mas o A* expandiu 5 nós e o custo uniforme 8.

Pela questão 10 dá para ver de outra forma: com w = 0, a função f(n) = (2 − w)·g(n) + w·h(n) vira 2·g(n), que é o custo uniforme, e com w = 1 vira o A*.

## Resumo de como cheguei na solução

Comparei as duas funções de avaliação: o custo uniforme usa g(n) e o A* usa g(n) + h(n), então bastava zerar o h(n). Depois conferi se a heurística zero é válida, ou seja, admissível e consistente, porque senão não faria sentido dizer que é um caso do A* com as mesmas garantias. Para mostrar que isso não é só uma curiosidade, usei os números da questão 1, onde dá para ver quanto a heurística economizou em relação ao caso h = 0.
