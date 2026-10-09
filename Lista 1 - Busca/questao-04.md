# Questão 4

O que diferencia uma estratégia de busca A de uma estratégia B é a **ordem em que elas expandem os nós**, ou seja, qual nó da fronteira é escolhido para ser visitado primeiro. O slide da aula fala isso com essas palavras: "uma estratégia de busca é basicamente uma ordem de expansão dos nodos".

O resto do algoritmo é igual em todas. Todas tiram um nó da fronteira, olham se ele é a meta, geram os filhos com a função-sucessor e colocam esses filhos de volta na fronteira. O que muda é só a estrutura da fronteira:

| Estratégia | Fronteira | Quem sai primeiro |
|:--|:--|:--|
| Largura | fila (FIFO) | o mais raso, o que entrou primeiro |
| Custo uniforme | fila ordenada por g(x) | o de menor custo de caminho até ali |
| Profundidade | pilha (LIFO) | o mais fundo, o que entrou por último |
| Profundidade limitada | pilha com um teto l | o mais fundo, desde que não passe de l |
| Aprofundamento iterativo | pilha, reiniciada com l = 0, 1, 2... | o mais fundo dentro do limite da rodada |

Isso dá para ver no código da questão 8: a busca em largura e a busca em profundidade são a mesma função, e a única linha que muda é `fronteira.popleft()` contra `fronteira.pop()`.

Na aula o professor completou isso dizendo que o que difere os algoritmos são duas coisas: a forma como cada um expande a árvore e como isso afeta o desempenho deles nas métricas de avaliação. A segunda parte é consequência da primeira. Mudar a ordem de expansão muda quantos nós ficam guardados, se o algoritmo pode se perder num ramo infinito e se ele acha a solução mais barata.

## Critérios de avaliação

As estratégias são avaliadas por quatro critérios:

| Critério | Pergunta |
|:--|:--|
| Completude | Se existe solução, o algoritmo sempre encontra uma? |
| Otimalidade | A solução que ele encontra é a de menor custo? |
| Complexidade de tempo | Quantos nós ele gera ou explora até achar? |
| Complexidade de espaço | Quantos nós ele precisa guardar na memória ao mesmo tempo? |

Tempo e espaço são medidos em função de três números do problema:

- **b**: fator de ramificação, quantos filhos cada nó gera no máximo
- **d**: profundidade da solução de menor custo
- **m**: profundidade máxima do espaço de estados, que pode ser infinita

Completude e otimalidade são coisas separadas. Ser completo é achar alguma solução, mesmo que não seja a melhor. Ser ótimo é achar sempre a melhor. Um algoritmo pode ser completo sem ser ótimo, mas não dá para ser ótimo sem ser completo.

## Resumo de como cheguei na solução

Comecei pela definição do slide, que fala que a estratégia é a ordem de expansão. No começo achei que era resumido demais, mas quando montei a tabela das cinco estratégias da aula percebi que o único lugar onde elas se diferenciam é mesmo a fronteira: em todas o laço é tirar um nó, testar se é a meta e gerar os filhos. Depois conferi isso no meu código da questão 8, onde a largura e a profundidade ficaram com uma única linha diferente.

Para os critérios usei os quatro do slide e as três variáveis b, d e m. Fiz questão de separar completude de otimalidade porque o professor deu ênfase a isso na aula, com o exemplo do mapa da Romênia: achar uma rota qualquer de Arad para Bucareste já torna o algoritmo completo, e só achar a menor rota torna ele ótimo.
