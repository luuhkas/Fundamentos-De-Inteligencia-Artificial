# Questão 2

Pra testar um argumento com tabela-verdade usei a ideia do slide do Wumpus: listar todas as interpretações e olhar só as linhas em que TODAS as premissas são V. Se a conclusão também for V em todas essas linhas, o argumento é válido. Se tiver uma linha só com premissas V e conclusão F, é inválido. Os três têm duas proposições, então são 2^2 = 4 linhas cada.

**a) Se neva, então faz frio. Não está nevando. Logo, não está frio.**

```
p : neva
q : faz frio

{p → q, ¬p} |= ¬q
```

|    | p | q | p → q | ¬p | ¬q |
|:--:|:-:|:-:|:-:|:-:|:-:|
| I1 | V | V | V | F | F |
| I2 | V | F | F | F | V |
| I3 | F | V | **V** | **V** | **F** |
| I4 | F | F | **V** | **V** | **V** |

As premissas são V juntas em I3 e I4. Em I4 a conclusão é V, mas em I3 é F: não neva, faz frio mesmo assim, e as duas premissas continuam verdadeiras. Então o argumento é INVÁLIDO.

Faz sentido, a premissa só fala o que acontece quando neva. Quando não neva ela não afirma nada (o slide fala isso da implicação: "caso contrário, não estou fazendo nenhuma afirmação"). Parece um modus tollens mas não é, o MT nega o consequente e aqui negaram o antecedente.

**b) Se eu durmo tarde, não acordo cedo. Acordo cedo. Logo, não durmo tarde.**

```
p : durmo tarde
q : acordo cedo

{p → ¬q, q} |= ¬p
```

|    | p | q | ¬q | p → ¬q | ¬p |
|:--:|:-:|:-:|:-:|:-:|:-:|
| I1 | V | V | F | F | F |
| I2 | V | F | V | V | F |
| I3 | F | V | F | **V** | **V** |
| I4 | F | F | V | V | V |

As duas premissas (p → ¬q e q) só são V juntas em I3, e nela ¬p é V. Argumento VÁLIDO. Esse sim é o modus tollens: o consequente é ¬q, e a segunda premissa diz q, que é a negação dele.

**c) Gosto de dançar ou cantar. Não gosto de dançar. Logo, gosto de cantar.**

```
p : gosto de dançar
q : gosto de cantar

{p ∨ q, ¬p} |= q
```

|    | p | q | p ∨ q | ¬p |
|:--:|:-:|:-:|:-:|:-:|
| I1 | V | V | V | F |
| I2 | V | F | V | F |
| I3 | F | V | **V** | **V** |
| I4 | F | F | F | V |

As premissas só são V juntas em I3, e nela q é V. Argumento VÁLIDO. Se um dos dois lados do "ou" é falso, sobra o outro. Na tabela de regras da aula isso tem nome, é o silogismo disjuntivo: α ∨ β, ¬α |= β.

## Resumo de como cheguei na solução

Primeiro formalizei cada argumento do jeito da questão 1 (letras, fórmulas, {premissas} |= conclusão), com a negação fora da letra. Depois montei a tabela com uma coluna pra cada premissa e uma pra conclusão, e marquei as linhas onde todas as premissas dão V. A resposta sai só dessas linhas: na b e na c sobrou uma linha só e a conclusão era V nela, então são válidos. Na a sobraram duas e numa delas a conclusão é F, e uma linha assim já basta pra dizer que é inválido. Conferi com a tabela de regras da aula: a b é o modus tollens e a c é o silogismo disjuntivo. A a não bate com nenhuma regra de lá, o que combina com o resultado.
