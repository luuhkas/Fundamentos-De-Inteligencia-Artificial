# Questão 4

O A* expande sempre o nó da fronteira com o menor f(n) = g(n) + h(n). Para ele ser completo e ótimo, algumas condições precisam valer.

## Completude

O A* é completo, ou seja, sempre acha uma solução quando ela existe, se:

1. **o fator de ramificação b for finito**, ou seja, cada nó tem uma quantidade finita de filhos;
2. **todo passo custar pelo menos um valor positivo ε**, ou seja, não existem ações com custo zero ou negativo.

A segunda condição evita que a busca fique presa gerando infinitos nós com o mesmo f, por exemplo andando em círculo por arcos de custo zero. Com as duas valendo, só existe uma quantidade finita de nós com f menor que o custo da solução, então em algum momento o A* chega nela.

## Otimalidade

O A* é ótimo, ou seja, a primeira solução que ele tira da fronteira é a de menor custo, se a heurística for:

- **admissível**, quando ele é usado como busca em árvore, que é como o professor fez na aula, deixando os estados repetidos aparecerem de novo na árvore;
- **consistente**, quando ele é usado como busca em grafo, guardando os estados já expandidos para não expandir de novo.

Na aula o professor falou que a admissível garante achar a solução e a consistente garante a ótima. Pesquisando no Russell e Norvig, entendi que a diferença está justamente nesse ponto da árvore e do grafo. Na busca em árvore a admissibilidade já basta. Na busca em grafo, se a heurística não for consistente, o A* pode descartar um estado que chegou primeiro por um caminho caro e depois perder o caminho barato até ele. A consistência garante que o primeiro caminho que chega a um estado já é o melhor, então nada se perde.

Outra condição que vem junto: **o teste de meta tem que ser feito quando o nó sai da fronteira, e não quando ele é gerado.** Foi o que o professor mostrou no exemplo da Romênia. Bucareste entrou na fronteira com f = 450 vindo de Fagaras, mas o A* não parou ali. Continuou por Pitesti e só parou quando Bucareste saiu da fronteira com f = 418. Se ele testasse na geração, teria devolvido os 450 km.

## Resumo

| Propriedade | Condição |
|:--|:--|
| Completo | b finito e custo de cada passo ≥ ε > 0 |
| Ótimo (busca em árvore) | h admissível |
| Ótimo (busca em grafo) | h consistente |
| Nos dois casos | teste de meta quando o nó sai da fronteira |

## Resumo de como cheguei na solução

O slide fala que o A* é "completo desde que a heurística seja consistente ou admissível", e na aula o professor separou os dois: admissível para achar e consistente para garantir a ótima. Fiquei com dúvida porque o próprio slide, no exemplo da Romênia, diz "solução ótima (dado que h(n) é admissível)". Fui ver no Russell e Norvig, e lá a explicação é que depende de o A* ser rodado como árvore ou como grafo. Isso fechou as duas falas.

Para a completude, o slide não fala das condições sobre b e o custo dos passos, então tirei elas do livro e tentei entender o porquê de cada uma em vez de só copiar. A do teste de meta eu percebi revendo o exemplo da Romênia na aula, que é justamente o momento em que o A* passa do caminho de 450 km para o de 418 km.
