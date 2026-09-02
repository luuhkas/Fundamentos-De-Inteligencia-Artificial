# Questão 2

Defini os dez termos com minhas palavras. Pra não sair repetindo o slide, amarrei todos eles num exemplo só: um pedaço da árvore de busca do mapa da Romênia, saindo de Arad até Bucareste.

Nesse pedaço, cada bolinha é um nó e o estado dela é só a cidade. As linhas são as ações, e quem gerou elas foi a função-sucessor. O desenho todo é a árvore de busca. O caminho Arad, Sibiu, Fagaras, Bucareste é uma solução, e somando 140 + 99 + 211 dá 450 km, que é o custo do caminho dela.

**a) Estado**

É a foto de como o mundo está num momento, só com o que interessa pro problema. No mapa da Romênia o estado é só a cidade onde eu estou (não preciso guardar o resto do mapa). No aspirador de pó é a posição do robô mais a sujeira de cada lado.

**b) Espaço de estados**

São todos os estados que dá pra alcançar saindo do inicial e aplicando as ações. O aspirador tem 8, as 8 rainhas passam de 10 elevado a 14. Ele existe mesmo que eu nunca gere ele inteiro, e na maioria dos problemas eu nunca gero.

**c) Árvore de busca**

É o registro do caminho que o algoritmo percorreu. Não é a mesma coisa que o espaço de estados: o espaço é um grafo (dá pra chegar no mesmo estado por vários caminhos) e a árvore é o jeito que AQUELE algoritmo foi abrindo esse grafo. Por isso o mesmo estado pode aparecer repetido em ramos diferentes.

**d) Nó de busca**

É a estrutura que representa um ponto da árvore. Ele não É o estado, ele CARREGA o estado, mais o pai, a ação que gerou ele, o custo g(x) e a profundidade. É essa informação extra que deixa eu remontar o caminho da solução no final.

**e) Estado objetivo**

É o estado que passa no teste de meta, ou seja, o problema resolvido. Pode ser explícito (cidade == Bucareste) ou implícito, quando é uma propriedade em vez de um valor (chequemate(x), ou nenhuma rainha sendo atacada).

**f) Ação**

É o que leva de um estado pro outro, e é a única forma de andar pelo espaço de estados. No aspirador são quatro: esquerda, direita, aspirar ou não fazer nada.

**g) Função-sucessor**

Dado um estado, ela devolve todos os pares ação e estado que resulta. É ela que vai gerando o espaço de estados conforme precisa. É o coração da modelagem: se ela gera estado inválido o algoritmo perde tempo, e se ela deixa de gerar um estado válido o algoritmo pode nunca achar a solução.

**h) Fator de branching (b)**

Quantos filhos cada nó gera, em média. É o que faz o custo explodir, porque a busca cresce como b elevado à profundidade. Na tabela da aula, com b = 10, sair da profundidade 8 pra 12 vai de 31 horas pra 35 anos.

**i) Custo do caminho**

É a soma do custo de cada passo, o g(x). É aditivo e nenhum passo custa negativo. Dependendo do problema é distância, tempo, ou só 1 por ação (e quando é 1 por ação, custo do caminho vira sinônimo de profundidade).

**j) Solução do problema**

É a sequência de ações que sai do estado inicial e chega no objetivo. A solução ÓTIMA é a de menor custo entre todas. Vale separar as duas: achar uma solução qualquer é completude, achar a mais barata é otimalidade, e nem todo algoritmo que faz a primeira faz a segunda.

## Resumo de como cheguei na solução

Escrevi cada definição a partir de um exemplo concreto da aula e depois generalizei, em vez de copiar o slide. Também tomei o cuidado de marcar os três pares que se confundem e que na minha leitura são o ponto da questão: estado e nó (a cidade é o estado, a bolinha na árvore é o nó), espaço de estados e árvore de busca (o espaço é um grafo, a árvore é como um algoritmo específico abriu ele), e solução e solução ótima.
