# Questão 6

Primeiro uma tabela com os quatro algoritmos, e depois o que está por trás de cada linha, porque quase todo "sim" da tabela só vale se alguma condição for verdadeira.

| Algoritmo | Completo? | Ótimo? | Tempo | Memória |
|:--|:--|:--|:--:|:--:|
| Largura | Sim, se b for finito | Sim, se todas as ações custarem o mesmo | O(b^(d+1)) | O(b^(d+1)) |
| Profundidade | Não | Não | O(b^m) | O(b·m) |
| Profundidade limitada | Não, se l < d | Não | O(b^l) | O(b·l) |
| Aprofundamento iterativo | Sim, se b for finito | Sim, se cada passo custar 1 | O(b^d) | O(b·d) |

Lembrando: b é o fator de ramificação, d a profundidade da solução mais rasa, m a profundidade máxima da árvore e l o limite escolhido.

## Busca em largura

**Completude.** Ela é completa porque varre a árvore nível por nível, então se existe uma solução numa profundidade finita ela chega lá em algum momento. A condição é que b seja finito. Se um nó tivesse infinitos filhos, ela nunca terminaria o primeiro nível.

**Otimalidade.** Ela acha a solução mais rasa, e isso só é a mais barata se o custo do caminho nunca diminuir quando a profundidade aumenta. O caso mais comum é quando todas as ações custam o mesmo. Quando os custos são diferentes, ela pode errar. Foi o que aconteceu na questão 5: ela achou 450 km em 3 trechos e deixou passar a rota de 418 km em 4 trechos.

**Tempo e memória.** Os dois são O(b^(d+1)), porque ela guarda todos os nós que gerou. O +1 aparece porque ela visita, expande e só depois testa se é a meta, então gera um nível a mais do que precisava. A memória é o que inviabiliza ela: pela tabela da aula, com b = 10 e d = 6 já são 10 GB, e com d = 12 chegam a 10 petabytes.

## Busca em profundidade

**Completude.** Não é completa. Se a árvore for infinita, ou se o espaço de estados tiver ciclos e ela não controlar os estados repetidos, ela pode descer para sempre por um ramo e nunca voltar para o ramo onde estava a solução. Ela fica completa num espaço de estados finito e quando se evita repetir estado, mas isso não é garantido no caso geral.

**Otimalidade.** Não é ótima. Ela devolve a primeira solução que aparecer no ramo em que entrou, e nada garante que essa seja a mais barata.

**Tempo e memória.** O tempo é O(b^m), que é muito ruim quando m é bem maior que d. A memória é o ponto forte: O(b·m), linear, porque ela só guarda o caminho atual e os irmãos ainda não visitados, e apaga os ramos que já terminaram. No exemplo do slide são 118 KB contra os 10 petabytes da largura.

## Busca em profundidade limitada

É a profundidade com um teto l: os nós na profundidade l não têm filhos gerados. Isso resolve o problema da árvore infinita, mas cria dois novos.

**Completude.** Só é completa se l ≥ d. Se o limite for menor que a profundidade da solução, ela devolve "não achei" mesmo existindo solução. Às vezes o próprio problema dá um limite seguro: no mapa da Romênia, com 20 cidades, nenhum caminho sem repetir cidade passa de 19 trechos.

**Otimalidade.** Não é ótima, principalmente quando l > d, porque ela continua sendo uma busca em profundidade e devolve a primeira solução que encontrar dentro do limite.

**Tempo e memória.** O(b^l) de tempo e O(b·l) de memória. Ou seja, quanto menor o limite, mais barato, desde que ele não fique abaixo de d.

## Aprofundamento iterativo

Roda a profundidade limitada com l = 0, depois l = 1, l = 2 e assim por diante, até achar a solução.

**Completude.** É completa se b for finito, igual à largura. Como o limite vai subindo de um em um, em algum momento ele chega em d.

**Otimalidade.** É ótima se cada passo custar 1, ou de forma mais geral se o custo do caminho não diminuir com a profundidade. É a mesma condição da largura, porque ela também acha primeiro a solução mais rasa.

**Tempo e memória.** O tempo é O(b^d) e a memória é O(b·d). Ela refaz os níveis de cima a cada rodada, mas isso pesa pouco, porque numa árvore que cresce exponencialmente o último nível sozinho já tem quase todos os nós. No exemplo do slide, com b = 10 e d = 5, o retrabalho é de só 11%. Por isso ela é a escolha indicada quando o espaço de busca é grande e não se sabe a profundidade da solução.

## Existem condições para serem ótimas ou completas?

Sim:

- **Completude da largura e do aprofundamento iterativo:** b finito e a solução numa profundidade finita.
- **Otimalidade da largura e do aprofundamento iterativo:** custo do caminho que não diminui com a profundidade, na prática todas as ações custando o mesmo.
- **Completude da profundidade limitada:** limite maior ou igual à profundidade da solução (l ≥ d).
- **Profundidade:** não tem condição que garanta otimalidade. A completude só aparece num espaço de estados finito e com controle de estados repetidos.

## Resumo de como cheguei na solução

Montei primeiro a tabela juntando o que estava nos slides de cada algoritmo, e só depois fui escrever cada um. Enquanto escrevia, percebi que a pergunta do final é o ponto principal da questão: quase todo "sim" da tabela tem um "se" junto, então resolvi deixar a condição escrita na própria tabela em vez de colocar só sim ou não.

Para explicar de onde vem cada complexidade tentei relacionar com o comportamento da fronteira que vi na questão 5. A memória da largura é exponencial porque a fila guarda o nível inteiro, e a da profundidade é linear porque a pilha só guarda um ramo. O +1 da largura eu entendi pela explicação do professor na aula, de que ela expande antes de testar.

Para as condições de otimalidade usei o resultado da questão 5 como exemplo, porque foi ali que vi na prática a largura devolvendo uma rota que não era a mais curta. Também usei o resultado da questão 9 para a profundidade limitada, onde o limite 2 falhou mesmo existindo solução.
