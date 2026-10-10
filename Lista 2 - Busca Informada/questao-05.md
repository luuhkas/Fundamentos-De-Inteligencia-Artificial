# Questão 5

Essa pergunta é a mesma da questão 2. Lá eu respondi pelo lado do que cada busca enxerga, o g(n) e o h(n). Aqui vou responder pelo lado do resultado, mostrando o que essa diferença causa num mesmo problema.

A diferença central continua sendo a mesma: a busca não informada escolhe o próximo nó usando só a formulação do problema, e a informada usa também uma estimativa h(n) de quanto falta até a meta.

O efeito disso aparece bem no grafo da questão 1, que resolvi com as cinco estratégias:

| Estratégia | Tipo | Nós expandidos | Custo do caminho |
|:--|:--|:--:|:--:|
| Largura | não informada | 8 | 55 |
| Profundidade | não informada | 3 | 55 |
| Custo uniforme | não informada | 8 | 43 |
| Gulosa | informada | 3 | 47 |
| A* | informada | 5 | 43 |

Dá para tirar três coisas dessa tabela:

1. **A informação reduz o trabalho.** O custo uniforme e o A* acharam o mesmo caminho ótimo, mas o A* expandiu 5 nós e o custo uniforme 8. O h(n) fez o A* deixar de lado B e F, que não levavam ao melhor caminho.
2. **Ter informação não garante a resposta certa.** A gulosa é informada, mas como olha só para o h(n), devolveu 47 em vez de 43. A busca informada só é ótima quando usa a heurística do jeito certo, como o A*, somando g(n) e h(n), e com uma heurística admissível.
3. **A qualidade depende da heurística.** Uma busca informada é tão boa quanto a estimativa que recebe. Com h(n) = 0 para todo nó, o A* vira o custo uniforme, que é uma busca cega. É isso que a questão 12 pergunta.

Resumindo: a busca não informada explora o espaço de estados sem direção e acaba visitando muita coisa que não interessa, e a informada usa conhecimento do problema para ir direto para a região mais promissora.

## Resumo de como cheguei na solução

Quando li a lista, percebi que a questão 5 repete a 2. Para não copiar a mesma resposta, escolhi mostrar a diferença na prática. Usei a tabela da questão 1, porque ali as cinco estratégias rodam no mesmo grafo e dá para comparar direto o número de nós expandidos e o custo do caminho. Montando a tabela, percebi que a resposta não é só "a informada é melhor": a gulosa também é informada e errou, e isso mostra que o importante é como a heurística é usada.
