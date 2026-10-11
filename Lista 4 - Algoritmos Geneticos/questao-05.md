# Questão 5

O problema da partição: dado um conjunto S com N inteiros cuja soma é M, existe um subconjunto de S cuja soma é M/2? Isso é o mesmo que dividir S em dois grupos com a mesma soma.

Para os exemplos usei S = {3, 1, 4, 2, 2}, com N = 5 e M = 12, então o objetivo é achar um subconjunto que some **6**.

## a) Codificação

**Um bit para cada número de S.** O cromossomo tem N bits, e o bit i diz em qual grupo o i-ésimo número fica:

- **1** = o número está no subconjunto
- **0** = o número fica de fora, no outro grupo

```
S          =  3  1  4  2  2
cromossomo = [1  0  0  1  0]   →  subconjunto {3, 2}, soma 5
cromossomo = [0  0  1  1  0]   →  subconjunto {4, 2}, soma 6  ✓
```

Essa codificação tem três vantagens. **Todo cromossomo é uma solução válida**, porque qualquer sequência de bits representa algum subconjunto, então o cruzamento e a mutação nunca geram algo sem sentido. O tamanho é fixo, igual a N. E os operadores binários da aula funcionam direto: o cruzamento de um ponto troca pedaços dos subconjuntos, e a mutação inverte um bit, que é passar um número de um grupo para o outro.

## b) Função de custo

O que interessa é o quanto a soma do subconjunto está longe de M/2:

```
custo(c) = | Σ sᵢ·cᵢ  −  M/2 |
```

em que sᵢ é o i-ésimo número de S e cᵢ é o bit dele. O custo é **0 exatamente quando o subconjunto soma M/2**, ou seja, quando o problema está resolvido. Como o algoritmo genético maximiza o fitness e a roleta precisa de valores positivos, transformei o custo num fitness:

```
fitness(c) = 1 / (1 + custo(c))
```

Ele vale 1 na solução e diminui conforme a soma se afasta de M/2. O "+1" evita a divisão por zero.

Exemplos com S = {3, 1, 4, 2, 2} e M/2 = 6:

| Cromossomo | Subconjunto | Soma | Custo | Fitness |
|:--:|:--|:--:|:--:|:--:|
| 10010 | {3, 2} | 5 | 1 | 0,50 |
| 11111 | todos | 12 | 6 | 0,14 |
| 00000 | vazio | 0 | 6 | 0,14 |
| 00110 | {4, 2} | 6 | **0** | **1,00** |
| 11001 | {3, 1, 2} | 6 | **0** | **1,00** |

**Critério de parada:** se algum indivíduo chegar no custo 0, a resposta é **sim** e o cromossomo dele é o subconjunto. Se o algoritmo parar pelo número máximo de gerações sem chegar no 0, ele só consegue dizer que não encontrou. Isso **não prova** que não existe, porque o algoritmo genético não testa todas as possibilidades.

## c) Uma abordagem sem algoritmos genéticos

**Programação dinâmica**, perguntando quais somas dá para formar.

A ideia é montar um vetor `possivel[0..M/2]`, em que `possivel[s]` diz se existe um subconjunto que soma s. Começa com `possivel[0] = verdadeiro`, porque o conjunto vazio soma 0, e todo o resto falso. Depois, para cada número x de S, percorre-se as somas **de trás para frente**, de M/2 até x:

```
se possivel[s − x] é verdadeiro, então possivel[s] = verdadeiro
```

No fim, a resposta é `possivel[M/2]`.

Com S = {3, 1, 4, 2, 2} e M/2 = 6:

| Depois de usar | Somas possíveis (até 6) |
|:--|:--|
| começo | 0 |
| 3 | 0, 3 |
| 1 | 0, 1, 3, 4 |
| 4 | 0, 1, 3, 4, 5 |
| 2 | 0, 1, 2, 3, 4, 5, 6 |
| 2 | 0, 1, 2, 3, 4, 5, 6 |

O 6 apareceu, então **a resposta é sim**.

Comparando com o algoritmo genético:

| | Algoritmo genético | Programação dinâmica |
|:--|:--|:--|
| Resposta | encontra uma solução se tiver sorte | **sempre** dá a resposta certa |
| Se a resposta é "não" | não consegue provar | prova que não existe |
| Custo | depende de quantas gerações rodar | O(N · M/2) operações |

A programação dinâmica é exata, mas o custo cresce com M. Se os números forem muito grandes, M/2 fica enorme e o vetor não cabe na memória. É nesse caso que o algoritmo genético vale a pena: ele não depende do tamanho dos números, só da quantidade N.

Outra alternativa, mais simples, é a **força bruta**: testar os 2ᴺ subconjuntos. Com N = 5 são só 32, mas com N = 50 já passam de 10¹⁵. É o mesmo problema de explosão combinatória que vimos nas buscas cegas.

## Resumo de como cheguei na solução

Para a codificação, pensei no que uma solução precisa dizer: para cada número, se ele está ou não no subconjunto. Isso é uma escolha de sim ou não, então um bit por número foi o mais natural. Conferi que qualquer sequência de bits é um subconjunto válido, o que deixa o cruzamento e a mutação seguros.

Para a função de custo, a ideia veio do próprio enunciado: o objetivo é a soma dar M/2, então o custo é a distância até M/2. Depois lembrei, pela aula, que a roleta não aceita valores negativos e que o algoritmo maximiza, e por isso transformei o custo em fitness com 1 / (1 + custo). Testei com um exemplo pequeno, para ver os valores fazendo sentido.

Para a abordagem sem algoritmo genético, escolhi a programação dinâmica porque ela dá a resposta certa sempre, que é justamente o que falta no algoritmo genético. Fiz a tabela à mão com o mesmo exemplo, e também comparei as duas abordagens para mostrar quando cada uma é melhor.
