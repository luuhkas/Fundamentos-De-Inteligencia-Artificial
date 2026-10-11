# Questão 3

## Como os estados são representados

No algoritmo genético, **cada estado do problema é um indivíduo**, e cada indivíduo é guardado num **cromossomo**, que é uma sequência de genes. Diferente das buscas das Listas 1 e 2, aqui o estado não é um passo no meio do caminho, mas sim uma **solução completa**, que pode estar boa ou ruim. Na aula, o professor deu o exemplo do 8-puzzle: o indivíduo tem que ter todas as peças distribuídas no tabuleiro, mesmo que estejam fora do lugar.

## Codificação binária

A codificação binária transforma cada parâmetro da solução numa sequência de bits de **tamanho fixo**.

**Para um número inteiro**, basta escrever ele em binário. Com 6 bits dá para representar de 0 a 63. Por exemplo, `101011` = 32 + 8 + 2 + 1 = 43, que foi usado na questão 4.

**Para um número real num intervalo [mín, máx]**, escolhe-se a quantidade n de bits, que define a precisão, converte-se o binário para decimal (b) e mapeia-se para o intervalo:

```
x = mín + (máx − mín) · b / (2ⁿ − 1)
```

O exemplo do slide usa 22 bits para o intervalo [−1, 2]: `1000101110110101000111` vale 2.288.967 em decimal e representa x = −1 + 3 · 2.288.967 / 4.194.303 ≈ 0,637197.

**Para escolhas do tipo sim ou não**, cada bit diz se um elemento está ou não na solução.

**Vantagens da representação binária:**

- é a representação **tradicional** dos algoritmos genéticos, e quase toda a teoria foi feita em cima dela;
- é **fácil de manipular**: o cruzamento é só cortar e juntar pedaços, e a mutação é só inverter um bit;
- como **todos os cromossomos têm o mesmo tamanho**, o cruzamento sempre gera um filho no mesmo formato dos pais;
- é **leve e rápida**, porque o computador trabalha direto com bits;
- é **genérica**: qualquer coisa que dê para numerar dá para codificar em bits.

A desvantagem, que o slide também comenta, é que para números reais com muita precisão são necessários muitos bits, e aí a representação real costuma ser melhor.

## Exemplo 1: problema de rotas e caminhos

Usei o grafo da questão 6, com 5 cidades e 10 estradas. Dá para codificar uma rota em binário de dois jeitos.

**Jeito 1: um bit por estrada** (o que o professor sugeriu na aula). Numerando as 10 estradas, o cromossomo tem 10 bits, e cada bit diz se aquela estrada faz parte da rota:

| Estrada | 1-2 | 1-3 | 1-4 | 1-5 | 2-3 | 2-4 | 2-5 | 3-4 | 3-5 | 4-5 |
|:--|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| Rota 1-2-3-5-4-1 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 1 | 1 |

Cromossomo: `1010100011`. O fitness soma o custo das estradas com bit 1. O problema é que um cruzamento pode gerar algo que não é uma rota, por exemplo com uma cidade sem nenhuma estrada. Então o fitness precisa **penalizar** os cromossomos inválidos.

**Jeito 2: a ordem das cidades em binário.** Cada cidade vira um código de 3 bits (1 = `001`, 2 = `010`, ..., 5 = `101`), e o cromossomo é a sequência:

```
rota 1-2-3-5-4  →  001 010 011 101 100
```

Esse jeito tem o mesmo problema: um cruzamento pode repetir cidades. É por isso que, na prática e na questão 6, usei um vetor de inteiros com operadores próprios para permutação.

## Exemplo 2: distribuição de horários de um curso

Imaginei um caso pequeno: **4 disciplinas** (Fundamentos de IA, Estrutura de Dados, Redes e Banco de Dados) e **4 horários** na semana (segunda de manhã, segunda à tarde, terça de manhã e terça à tarde).

Cada disciplina recebe um horário, e 4 horários cabem em **2 bits**: `00` = segunda de manhã, `01` = segunda à tarde, `10` = terça de manhã, `11` = terça à tarde. O cromossomo tem 2 bits por disciplina, 8 no total:

```
          IA   ED   Redes  BD
         [00] [01]  [10]  [11]   →  cromossomo 00011011
```

Esse cromossomo quer dizer: IA na segunda de manhã, ED na segunda à tarde, Redes na terça de manhã e BD na terça à tarde.

O **fitness** conta os conflitos e dá uma nota maior para quem tem menos. Por exemplo, ele pode tirar pontos quando duas disciplinas do mesmo período caem no mesmo horário, ou quando um professor fica com duas aulas ao mesmo tempo. Num caso real, com dezenas de disciplinas, salas e professores, o cromossomo só fica maior: mais bits por disciplina e mais genes para a sala.

Uma alternativa, mais parecida com o jeito 1 das rotas, é uma matriz de bits com uma linha por disciplina e uma coluna por horário, em que 1 quer dizer que a disciplina está naquele horário.

## Resumo de como cheguei na solução

Comecei entendendo a codificação binária pelo exemplo do slide, refazendo a conta do x = 0,637197 para ter certeza de como funciona o mapeamento para o intervalo. Depois listei as vantagens, juntando o que o slide fala ("tradicional, fácil de manipular") com o que percebi fazendo a questão 4: com bits, o cruzamento de um ponto e a mutação ficaram muito simples.

Para os dois exemplos, tentei montar casos pequenos para dar para escrever o cromossomo inteiro. Nas rotas, usei o grafo da questão 6 e apliquei a ideia do professor de um bit por estrada. Fazendo isso, percebi que o cruzamento pode gerar rotas inválidas, e esse foi o motivo de eu ter usado vetor de inteiros na questão 6. Nos horários, escolhi 4 disciplinas e 4 horários para cada disciplina caber em exatamente 2 bits, e defini o fitness contando conflitos.
