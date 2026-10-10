# Questão 10

A função é:

```
f(n) = (2 − w)·g(n) + w·h(n)
```

Para entender o que cada w faz, substituí os três valores pedidos:

| w | f(n) | Que busca é |
|:--:|:--|:--|
| 0 | 2·g(n) | **custo uniforme** |
| 1 | g(n) + h(n) | **A\*** |
| 2 | 2·h(n) | **busca gulosa** |

**w = 0.** Sobra f(n) = 2·g(n). Multiplicar todos os valores por 2 não muda qual nó é o menor da fronteira, então a ordem de expansão é exatamente a do custo uniforme, que só olha o custo do caminho até ali.

**w = 1.** Fica f(n) = g(n) + h(n), que é a função do A*.

**w = 2.** Sobra f(n) = 2·h(n). Pelo mesmo motivo do w = 0, o fator 2 não muda a ordem, e a busca vira a gulosa, que só olha a heurística.

## Para que valores de w ele é garantidamente ótimo

Supondo que h é admissível, ele é ótimo para **0 ≤ w ≤ 1**.

Para ver isso, tirei o (2 − w) em evidência. Para w < 2:

```
f(n) = (2 − w) · [ g(n) + (w / (2 − w)) · h(n) ]
```

O fator (2 − w) da frente é positivo e não muda a ordem da fronteira. Então a busca se comporta como um A* com a heurística h'(n) = (w / (2 − w))·h(n).

- Se **w ≤ 1**, o peso w / (2 − w) fica entre 0 e 1. Com w = 0 ele vale 0, com w = 0,5 vale 1/3 e com w = 1 vale 1. Então h'(n) ≤ h(n) ≤ h*(n), h' continua admissível e a busca é ótima.
- Se **w > 1**, o peso passa de 1. Com w = 1,5, por exemplo, vale 3. Aí h'(n) pode ficar maior que o custo real e deixa de ser admissível, então a otimalidade não é mais garantida. No limite w = 2 vira a gulosa, que não é ótima.

Resumindo: de 0 até 1 a busca vai do custo uniforme até o A*, e as duas pontas são ótimas. De 1 até 2 ela vai ficando cada vez mais gulosa e perde a garantia.

## Resumo de como cheguei na solução

Primeiro substituí os três valores de w que a questão pede, o que já respondeu metade dela. A parte que precisei entender melhor foi por que 2·g(n) é o mesmo que o custo uniforme, e a resposta é que multiplicar tudo por uma constante positiva não muda quem é o menor da fronteira.

Para a otimalidade, a ideia de colocar (2 − w) em evidência veio de tentar escrever a função no formato g + h do A*. Fazendo isso, a pergunta virou "quando a heurística multiplicada pelo peso continua admissível?", e isso acontece quando o peso é no máximo 1, ou seja, quando w ≤ 1. Testei alguns valores de w no meio do intervalo para conferir se o peso se comportava como eu esperava.
