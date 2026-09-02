# Lista 1 - Busca

**Fundamentos De Inteligência Artificial** - UTFPR Campus Santa Helena

Docente: Thiago França Naves

Lucas Silva Maués - RA 2476878

## Questão 1

Simulei a busca em largura e a busca em profundidade na árvore da lista para achar os nós 10 e 20.

![Questão 1](questao-01.png)

### Resumo de como cheguei na solução

Comecei passando a árvore do desenho para uma lista de filhos de cada nó, na ordem da esquerda para a direita. Essa ordem importa: é ela que decide quem entra primeiro na fronteira, então se eu trocasse, a simulação inteira sairia diferente.

Depois montei uma tabela por busca, uma linha por passo, anotando quem visitei, o que aquele nó expandiu e como a memória ficou. Os dois algoritmos são o mesmo laço. O que muda é só a fronteira: fila na largura, sai quem entrou primeiro, e pilha na profundidade, sai quem entrou por último.

Montando as tabelas apareceram duas coisas que eu não tinha percebido. Folha é visitada mas não expande nada, porque não tem filho para conhecer, e por isso o número de expandidos fica sempre menor que o de visitados. E os dois testam a meta em momentos diferentes: a largura visita, expande e só depois testa, já a profundidade visita, testa e só expande se não for a solução. É daí que vem o +1 do O(b^(d+1)) da largura.

Para o tempo e a memória usei o modelo da aula, 10.000 nós gerados por segundo e 1 KB por nó. O tempo saiu dos nós gerados.

A memória é contada diferente nos dois. Na largura é o total de gerados, porque ela guarda tudo. Na profundidade é o maior valor da coluna de memória, porque ela vai apagando os ramos que já falharam.
