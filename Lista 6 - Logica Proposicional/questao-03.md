# Questão 3

Tabela-verdade é o jeito mais direto de testar uma fórmula: eu listo todas as interpretações possíveis das proposições simples e calculo o valor da fórmula em cada uma. Como as duas fórmulas só têm o p, são 2^1 = 2 interpretações (o slide fala que n símbolos dão 2^n linhas). Pelo slide, tautologia é a fórmula que dá V em TODAS as interpretações e contradição (insatisfatível) é a que dá F em todas.

**a) p ∨ ¬p é uma tautologia**

|    | p | ¬p | p ∨ ¬p |
|:--:|:-:|:-:|:-:|
| I1 | V | F | **V** |
| I2 | F | V | **V** |

Deu V nas duas linhas, então é tautologia. O ∨ só dá F com os dois lados F, e p e ¬p nunca são falsos juntos. É o princípio do terceiro excluído do começo da aula: ou p é V ou é F, não tem terceira opção.

**b) p ∧ ¬p é uma contradição**

|    | p | ¬p | p ∧ ¬p |
|:--:|:-:|:-:|:-:|
| I1 | V | F | **F** |
| I2 | F | V | **F** |

Deu F nas duas linhas, então é contradição. O ∧ só dá V com os dois lados V, e p e ¬p nunca são verdadeiros ao mesmo tempo. Esse é o princípio da não contradição.

Uma coisa que notei: o slide de insatisfatibilidade repete a tabela de p ∨ ¬p e diz que ela é insatisfatível, mas a tabela ali mostra V nas duas linhas. O próprio professor percebeu na aula e corrigiu na hora: "tem que ser E, o p e não p, aí sim é insatisfatível". Ou seja, o exemplo certo de insatisfatível é esse p ∧ ¬p da letra b.

## Resumo de como cheguei na solução

Montei as tabelas do jeito do slide de validade, com as interpretações I1 e I2 nas linhas e uma coluna pra cada pedaço da fórmula: p, depois ¬p pela tabela da negação, depois a fórmula pela tabela do ∨ ou do ∧. Com a coluna final pronta só comparei com a definição: tudo V é tautologia, tudo F é contradição. Depois liguei cada resultado com os dois princípios do começo da aula, porque na verdade as duas fórmulas são esses princípios escritos em lógica.
