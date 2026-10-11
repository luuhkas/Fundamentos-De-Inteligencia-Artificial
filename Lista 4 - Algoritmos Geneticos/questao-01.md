# Questão 1

## O que são meta-heurísticas

Uma meta-heurística é um **método de busca de alto nível, genérico, que pode ser adaptado para uma grande quantidade de problemas diferentes**. É assim que o slide da aula define: "um algoritmo de alto nível customizável a uma ampla quantidade de problemas".

A diferença para a heurística da Lista 2 ajudou a entender o nome. A heurística, como a distância em linha reta no mapa da Romênia, é feita **para um problema específico** e usa informação daquele problema para estimar quanto falta até a meta. A meta-heurística fica um nível acima: ela é uma **estratégia geral de como procurar**, e não depende do problema. Na aula o professor explicou que ela "não necessariamente vai pegar informações do problema", mas precisa de uma função de avaliação para dizer se um estado é bom ou ruim. Para usar num problema novo, basta trocar duas coisas: como a solução é representada e como ela é avaliada.

Os algoritmos genéticos são o exemplo que vimos na aula. A mesma estrutura, com população, seleção, cruzamento e mutação, serve para achar o máximo de uma função, a rota do caixeiro viajante e a posição das 8 rainhas. Só muda o cromossomo e o fitness. Outros exemplos de meta-heurística são a têmpera simulada (simulated annealing), a busca tabu e a otimização por colônia de formigas.

Elas são métodos de **busca local**: em vez de montar uma árvore com o caminho até a meta, como nas Listas 1 e 2, elas trabalham direto com soluções completas e vão melhorando essas soluções. O caminho até a solução não importa, só a solução final.

## Vantagens de usar meta-heurísticas

1. **Servem para espaços de busca enormes ou infinitos.** O caixeiro viajante com 10 cidades já tem 362.880 caminhos, como vimos na aula de busca informada. Com mais cidades, uma busca que olha tudo levaria séculos. A meta-heurística não precisa olhar o espaço inteiro, ela explora só as regiões mais promissoras.
2. **Acham soluções boas em pouco tempo**, mesmo sem garantir a ótima. Em problemas NP-completos, como o caixeiro viajante, uma solução perto da ótima achada rápido costuma valer mais que a ótima achada tarde demais.
3. **Conseguem escapar de ótimos locais.** No exemplo da aula, a função f(x) = x·sen(10πx) + 1 tem vários picos, e muitos algoritmos param no primeiro pico que acham. A meta-heurística tem mecanismos para "pular" para outra região, como a mutação no algoritmo genético.
4. **São reaproveitáveis.** O mesmo algoritmo, com pouca adaptação, resolve problemas bem diferentes. Isso economiza o trabalho de inventar um algoritmo novo para cada problema.
5. **Não precisam de propriedades matemáticas do problema.** Não exigem que a função seja contínua ou que dê para derivar, só que dê para avaliar uma solução e dar uma nota para ela.

A desvantagem, para ser justo, é que elas **não garantem a solução ótima**, e o resultado pode mudar de uma execução para outra, porque dependem de sorteios. Na questão 6 desta lista, rodei o mesmo algoritmo com várias sementes, e na maioria ele chegou na rota ótima em 5 gerações, mas em uma delas não chegou.

## Resumo de como cheguei na solução

Comecei pela definição do slide e pela explicação do professor na aula, comparando com a heurística que estudamos na Lista 2. Foi essa comparação que fez o "meta" do nome fazer sentido para mim: a heurística é do problema, e a meta-heurística é do método.

Para as vantagens, juntei o que o slide fala sobre espaços de busca grandes com o exemplo da função de vários picos, que mostra o problema dos ótimos locais. Também lembrei do caixeiro viajante da aula de busca informada, que mostra como o espaço explode. Por último coloquei a desvantagem, porque achei que responder só as vantagens deixaria a resposta incompleta, e usei o que aconteceu na questão 6 como exemplo.
