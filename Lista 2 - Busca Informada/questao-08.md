# Questão 8

**a) Complexidade.** É quanto o método gasta para achar a solução, medido de duas formas. A complexidade de tempo é a quantidade de nós gerados ou expandidos. A complexidade de espaço é a quantidade de nós que ficam guardados na memória ao mesmo tempo. As duas são escritas em função de b (fator de ramificação), d (profundidade da solução mais rasa) e m (profundidade máxima da árvore). Por exemplo, a busca em largura é O(b^(d+1)) em tempo e espaço, e a gulosa e o A* são exponenciais no pior caso, mas uma boa heurística reduz muito esse custo.

**b) Completude.** Um método é completo quando ele sempre encontra uma solução, se existir alguma. Não precisa ser a melhor, basta achar uma. A largura e o A* são completos, se b for finito. A profundidade e a gulosa não são, porque podem descer por um caminho infinito ou ficar presas num ciclo, como a gulosa entre Iasi e Neamt no exemplo da aula.

**c) Quanto a ser ótimo.** Um método é ótimo quando a solução que ele encontra é sempre a de menor custo. Ser ótimo é mais forte do que ser completo: todo método ótimo é completo, mas um completo pode achar uma solução cara. O custo uniforme e o A* com heurística admissível são ótimos. A gulosa não é, e isso aparece na Romênia, onde ela acha 450 km em vez de 418 km.

**d) Admissibilidade.** É uma propriedade da heurística e não do método de busca. Uma heurística é admissível quando nunca superestima o custo real até a meta, ou seja, h(n) ≤ h*(n) para todo n. Ela importa porque é a condição para o A* ser ótimo. Se a heurística superestimar o custo de algum nó do caminho ótimo, o A* pode deixar esse nó na fronteira e devolver antes uma solução pior.

## Resumo de como cheguei na solução

Os três primeiros itens são os critérios de avaliação que já tinham aparecido na Lista 1, então reaproveitei o que tinha escrito lá e atualizei com exemplos das buscas informadas. Para a admissibilidade, fiz questão de deixar claro que ela é uma característica da heurística e não do algoritmo, porque no começo eu confundia isso. Também liguei ela com a otimalidade, que é o motivo de ela importar.
