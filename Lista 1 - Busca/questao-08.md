# Questão 8

Fiz em Python. O código está em [`codigo/questao-08.py`](codigo/questao-08.py) e a saída completa em [`codigo/saida-questao-08.txt`](codigo/saida-questao-08.txt).

O mapa da questão 7 virou um dicionário em que cada lugar aponta para os vizinhos e a distância até eles:

```python
mapa = {
    "Bank":   {"Club": 1.1, "Home": 1.3, "Lake": 1.0, "Museum": 1.7, "Park": 1.8, "School": 1.0},
    "Club":   {"Bank": 1.1, "Home": 1.2, "School": 1.4},
    ...
    "School": {"Bank": 1.0, "Club": 1.4, "Lake": 0.9},
}
```

As duas buscas são praticamente a mesma função. A única diferença é a fronteira: na largura é uma fila e sai quem entrou primeiro, na profundidade é uma pilha e sai quem entrou por último.

```python
def busca_largura(inicio, objetivo):
    fronteira = deque([[inicio]])   # fila
    ...
        caminho = fronteira.popleft()   # sai o que entrou primeiro

def busca_profundidade(inicio, objetivo):
    fronteira = [[inicio]]   # pilha
    ...
        caminho = fronteira.pop()   # sai o que entrou por ultimo
```

Na fronteira eu guardo o caminho inteiro até o nó, e não só o nó. Assim, quando a busca chega em Museum, o caminho já está pronto para imprimir e para somar os quilômetros. Também usei um conjunto `conhecidos` para o mesmo lugar não entrar duas vezes na fronteira, porque o mapa tem ciclos (School, Bank, Lake, School) e sem isso a profundidade não terminaria.

## Como medi o tempo

Uma execução sozinha leva cerca de 2 microssegundos, e nessa escala qualquer coisa que o computador estiver fazendo ao mesmo tempo atrapalha a medida. Por isso rodei cada busca **100 mil vezes** seguidas com `time.perf_counter()` e dividi o total pelo número de repetições para ter o tempo médio de uma execução.

## Resultado

```
BUSCA EM LARGURA
  ordem de visita: School -> Bank -> Club -> Lake -> Home -> Museum
  nos visitados: 6
  caminho: School -> Bank -> Museum
  custo: 2.7 km
  tempo de uma execucao: 2.07 microssegundos
  tempo das 100 mil: 0.2070 s

BUSCA EM PROFUNDIDADE
  ordem de visita: School -> Bank -> Home -> Museum
  nos visitados: 4
  caminho: School -> Bank -> Museum
  custo: 2.7 km
  tempo de uma execucao: 1.71 microssegundos
  tempo das 100 mil: 0.1715 s
```

| Algoritmo | Nós visitados | Caminho | Custo | Tempo médio | Tempo das 100 mil |
|:--|:--:|:--|:--:|:--:|:--:|
| Largura | 6 | School, Bank, Museum | 2,7 km | 2,07 µs | 0,2070 s |
| Profundidade | 4 | School, Bank, Museum | 2,7 km | **1,71 µs** | **0,1715 s** |

**A busca em profundidade foi a mais rápida**, cerca de 17% mais rápida que a largura. A ordem de visita do código foi a mesma que eu tinha simulado à mão na questão 7, então o resultado bate.

O motivo é o mesmo da questão 7: ela visitou 4 nós e a largura visitou 6, e o tempo acompanha o número de nós que passam pela fronteira. Rodei o programa mais de uma vez e os números mudaram um pouco nas casas decimais, mas a profundidade ficou na frente em todas.

Não dá para concluir que a profundidade é sempre mais rápida. O mapa tem só 7 lugares e Museum está a 2 trechos de School, então os dois tempos ficaram muito próximos. Num mapa grande quem decide é a complexidade da questão 6, O(b^m) contra O(b^(d+1)), e aí depende de onde a meta está.

## Resumo de como cheguei na solução

Comecei escrevendo a busca em largura, seguindo o laço que a aula mostra: tirar um nó da fronteira, ver se é a meta e colocar os vizinhos na fronteira. Depois copiei a função para fazer a profundidade e troquei só a fila por uma pilha. Quando rodei a profundidade pela primeira vez, ela foi para Lake antes de Bank, porque a pilha tira o último que entrou. Para ela seguir a ordem alfabética, igual à minha simulação à mão, coloquei os vizinhos na pilha de trás para frente com `reversed`.

O controle dos lugares já conhecidos eu coloquei porque o mapa tem ciclo e eu já tinha visto isso na questão 3, com os jarros voltando para o estado inicial.

Para o tempo, a primeira medida que fiz foi de uma execução só, e o número mudava muito de uma vez para outra. Pesquisando, vi que o certo para medir algo tão rápido é repetir várias vezes e tirar a média, então usei 100 mil repetições. Com isso os tempos ficaram estáveis e deu para comparar os dois.
