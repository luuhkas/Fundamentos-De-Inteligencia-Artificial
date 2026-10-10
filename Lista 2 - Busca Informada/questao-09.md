# Questão 9

A busca gulosa é uma busca pela melhor escolha (best-first) que avalia cada nó **só pela heurística**:

```
f(n) = h(n)
```

A cada passo ela tira da fronteira o nó que parece estar mais perto da meta, sem considerar quanto já gastou para chegar nele. Ela ignora o g(n). O nome vem daí: ela "quer" chegar logo na meta e sempre pega o que parece mais perto naquele momento.

## Como funciona, passo a passo

1. Coloca o estado inicial na fronteira.
2. Tira da fronteira o nó com o menor h(n).
3. Se ele for a meta, devolve o caminho até ele.
4. Senão, gera os sucessores, calcula o h de cada um e coloca todos na fronteira.
5. Volta para o passo 2.

## Exemplo da aula: de Arad até Bucareste

Usando h(n) = distância em linha reta até Bucareste:

| Passo | Expandido | Sucessores gerados (h) | Escolhido |
|:--:|:--|:--|:--|
| 1 | Arad (366) | Sibiu 253, Timisoara 329, Zerind 374 | Sibiu |
| 2 | Sibiu (253) | Arad 366, Fagaras 176, Oradea 380, Rimnicu Vilcea 193 | Fagaras |
| 3 | Fagaras (176) | Sibiu 253, Bucareste 0 | Bucareste |

Caminho: Arad, Sibiu, Fagaras, Bucareste, com 140 + 99 + 211 = **450 km**. Ela chega rápido, expandindo só 3 nós, mas não é a rota ótima, que é por Rimnicu Vilcea e Pitesti, com 418 km. Ela pegou Fagaras porque 176 é menor que 193, sem perceber que o trecho de Fagaras até Bucareste é longo.

## Propriedades

| Critério | Busca gulosa |
|:--|:--|
| Completa? | **Não.** Pode ficar presa em ciclo. No exemplo da aula, saindo de Iasi para Fagaras, ela vai para Neamt porque o h dele é menor, de Neamt só pode voltar para Iasi, e de Iasi escolhe Neamt de novo, para sempre |
| Ótima? | **Não.** Como mostra o exemplo da Romênia |
| Tempo | O(b^m) no pior caso, mas uma boa heurística reduz muito |
| Memória | O(b^m), porque guarda todos os nós na fronteira |

A vantagem dela é ser rápida quando a heurística é boa, como no exemplo da Romênia. A desvantagem é não ter nenhuma garantia.

## Resumo de como cheguei na solução

Escrevi a definição a partir do slide, que diz que ela "não considera nenhuma função de custo, apenas a função heurística", e coloquei o algoritmo em passos para deixar claro que a única coisa que muda em relação às outras buscas é o critério de escolha na fronteira. Depois refiz o exemplo de Arad até Bucareste da aula numa tabela e conferi os 450 km somando os trechos. Para a completude, usei o exemplo de Iasi e Neamt que o professor explicou na aula, porque ele mostra bem o problema de olhar só para frente: a busca não tem nenhuma memória de quanto já andou e fica indo e voltando.
