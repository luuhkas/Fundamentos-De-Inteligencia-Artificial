# Questão 14

Um método de busca é monotônico quando a função de avaliação **nunca diminui ao longo de um caminho**. No A*, isso quer dizer que, se n' é sucessor de n:

```
f(n') ≥ f(n)
```

Isso acontece quando a heurística é **consistente**, que por isso também é chamada de heurística monotônica. Partindo da condição de consistência:

```
h(n) ≤ c(n, n') + h(n')
```

e somando g(n) dos dois lados:

```
g(n) + h(n) ≤ g(n) + c(n, n') + h(n')
       f(n) ≤ g(n') + h(n')
       f(n) ≤ f(n')
```

porque g(n') = g(n) + c(n, n'). Então, com heurística consistente, o f só cresce ou fica igual conforme a busca desce na árvore.

## Por que isso importa

- **Os nós saem da fronteira em ordem crescente de f.** O A* desenha os "contornos" do slide: primeiro abre tudo com f até um valor, depois tudo até o seguinte, e assim por diante, até chegar no contorno do custo ótimo C*.
- **Cada estado só precisa ser expandido uma vez.** A primeira vez que um estado sai da fronteira, ele já chegou pelo melhor caminho possível. É o que o slide fala: com heurística consistente "os vértices precisam ser visitados apenas uma vez".
- **Dá para usar busca em grafo sem perder a otimalidade**, descartando estados repetidos, como comentei na questão 4.

## Exemplo

No exemplo da Romênia da aula o f nunca diminui no caminho ótimo: Arad 366, Sibiu 393, Rimnicu Vilcea 413, Pitesti 417 e Bucareste 418, sempre crescendo. Já no grafo da questão 16 a heurística não é consistente no arco de B para F: f(B) = 5 + 17 = 22 e f(F) = 15 + 5 = 20, ou seja, o f caiu de 22 para 20 ao descer de B para F. Ali o método não é monotônico.

## Resumo de como cheguei na solução

O slide da heurística consistente diz que, com ela, "f(n) não decresce ao longo de qualquer caminho", e foi daí que liguei monotonicidade com consistência. Para não deixar só a afirmação, fiz a conta somando g(n) dos dois lados da desigualdade, e o f(n) ≤ f(n') saiu direto. Depois procurei um exemplo de cada caso: o caminho ótimo da Romênia do slide, onde o f só sobe, e o arco de B para F da questão 16, que eu já tinha visto que quebra a consistência na questão 3. Fiz a conta do f nos dois nós e confirmei que ele diminui.
