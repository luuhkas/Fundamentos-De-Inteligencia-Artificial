# Questão 3

## O que é uma heurística

É uma função h(n) que estima o custo do caminho mais barato entre o estado n e a meta mais próxima. Ela usa algum conhecimento do problema para dar esse palpite. Pelo slide, os valores precisam ser não negativos, quanto menor o valor mais promissor é o estado, e na meta h vale 0.

O exemplo da aula é a distância em linha reta. Para ir de Santa Helena a Curitiba, h(Santa Helena) é a distância em linha reta entre as duas cidades. Ela não é o caminho real, porque ninguém anda em linha reta pela estrada, mas é uma boa estimativa de quanto falta.

## Heurística admissível

É a que **nunca superestima** o custo real até a meta. Para todo nó n:

```
h(n) ≤ h*(n)
```

em que h*(n) é o custo verdadeiro do melhor caminho de n até a meta. Por isso se diz que uma heurística admissível é otimista: ela pode achar que falta menos do que realmente falta, mas nunca mais.

A distância em linha reta é admissível porque a menor distância entre dois pontos é a reta, então nenhuma estrada pode ser mais curta que ela.

## Heurística consistente

É a que respeita a desigualdade triangular entre um nó e cada sucessor dele. Para todo nó n e todo sucessor n' gerado por uma ação com custo c(n, n'):

```
h(n) ≤ c(n, n') + h(n')
```

Ou seja, a estimativa direta de n até a meta não pode ser maior do que dar um passo até n' e usar a estimativa de lá. Na aula o professor deu o exemplo com números: se h(n') = 10 e o passo custa 15, então h(n) pode ser no máximo 25. Se fosse maior, a heurística estaria se contradizendo, porque estaria dizendo que de n falta mais do que de n' mais o passo até ele.

A consequência prática é que, com uma heurística consistente, o f(n) = g(n) + h(n) nunca diminui ao longo de um caminho. É por isso que o A* com heurística consistente nunca precisa expandir o mesmo estado duas vezes.

## Toda heurística consistente é também admissível?

**Sim.** Dá para ver isso seguindo um caminho ótimo de n até a meta, n → n1 → n2 → ... → meta, e aplicando a consistência em cada passo:

```
h(n)  ≤ c(n, n1) + h(n1)
      ≤ c(n, n1) + c(n1, n2) + h(n2)
      ≤ ...
      ≤ c(n, n1) + c(n1, n2) + ... + h(meta)
```

Como h(meta) = 0, o lado direito é exatamente o custo desse caminho ótimo, que é h*(n). Então h(n) ≤ h*(n), e a heurística é admissível.

**O contrário não vale.** Achei um exemplo na própria lista, no grafo da questão 16. Lá h(B) = 17, o arco B para F custa 10 e h(F) = 5. Como 17 > 10 + 5 = 15, a heurística não é consistente nesse arco. Mas o caminho real mais barato de B até H custa 18, então h(B) = 17 continua sendo admissível. É o que o slide fala: "nem toda heurística admissível é consistente".

## Resumo de como cheguei na solução

Montei as três definições a partir dos slides e da explicação do professor sobre a desigualdade triangular, que foi o que me fez entender a consistência. A fórmula sozinha não dizia muito, mas o exemplo dele com 10 e 15 deixou claro que a ideia é a heurística não se contradizer entre um nó e o vizinho.

Para a última pergunta, o slide só afirma que toda consistente é admissível, então fui atrás do porquê. Pesquisando no livro do Russell e Norvig vi que dá para provar aplicando a consistência passo a passo ao longo do caminho ótimo, e escrevi essa conta. Para mostrar que o contrário não vale, em vez de inventar um exemplo, testei a desigualdade nos grafos da própria lista. No da questão 16 ela falhou no arco de B para F, e conferindo o custo real vi que mesmo assim h(B) não superestima. Então ali tem uma heurística admissível que não é consistente.
