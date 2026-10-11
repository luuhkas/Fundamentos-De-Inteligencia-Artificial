# Questão 4

O problema é maximizar f(x) = x², em que cada indivíduo de 6 bits é o valor de x em binário. Com 6 bits, x vai de 0 a 63, então o ótimo é `111111` = 63, com f = 3969.

Parâmetros que escolhi, seguindo a aula:

- **Seleção:** roleta, com probabilidade proporcional ao fitness
- **Cruzamento:** um ponto, com taxa de 80%
- **Mutação:** bit a bit, com taxa de 5%

Os sorteios saíram do programa [`codigo/questao-04.py`](codigo/questao-04.py), com semente fixa para dar sempre o mesmo resultado. A saída completa está em [`codigo/saida-questao-04.txt`](codigo/saida-questao-04.txt).

## 1. Avaliação da população inicial

| Indivíduo | Cromossomo | x | f(x) = x² | Probabilidade | Faixa na roleta |
|:--:|:--:|:--:|:--:|:--:|:--|
| 1 | 001100 | 12 | 144 | 2,0% | [0, 144) |
| 2 | 010101 | 21 | 441 | 6,1% | [144, 585) |
| 3 | 111000 | 56 | 3136 | 43,4% | [585, 3721) |
| 4 | 000111 | 7 | 49 | 0,7% | [3721, 3770) |
| 5 | 101011 | 43 | 1849 | 25,6% | [3770, 5619) |
| 6 | 101000 | 40 | 1600 | 22,2% | [5619, 7219) |
| | | | **Soma 7219** | | |

- **Média:** 7219 / 6 ≈ **1203,2**
- **Melhor:** **3136** (`111000`)

A probabilidade de cada um é o seu f dividido pela soma. Por exemplo, para o indivíduo 3: 3136 / 7219 ≈ 43,4%. A faixa na roleta é a soma acumulada.

## 2. Seleção pela roleta

Foram sorteados 6 números entre 0 e 7219. Cada número cai na faixa de um indivíduo:

| Sorteio | Número | Cai na faixa de |
|:--:|:--:|:--|
| 1 | 2337,7 | 111000 |
| 2 | 1089,0 | 111000 |
| 3 | 4699,1 | 101011 |
| 4 | 522,9 | 010101 |
| 5 | 3868,5 | 101011 |
| 6 | 2639,9 | 111000 |

O `111000`, que tem a maior fatia, foi escolhido 3 vezes, e o `101011` 2 vezes. Os dois piores, `001100` e `000111`, não foram escolhidos. Isso é a seleção natural acontecendo: quem é mais apto tem mais chance de ser pai.

## 3. Cruzamento de um ponto

Os selecionados foram cruzados em pares, na ordem do sorteio. Para cada par, sorteei r entre 0 e 1: se r < 0,8, cruza. Depois sorteei o ponto de corte.

| Par | Pai 1 | Pai 2 | r | Corte | Filho 1 | Filho 2 |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| 1 | 11100\|0 | 11100\|0 | 0,06 | depois do bit 5 | 111000 | 111000 |
| 2 | 1\|01011 | 0\|10101 | 0,21 | depois do bit 1 | **1**10101 | **0**01011 |
| 3 | 1\|01011 | 1\|11000 | 0,43 | depois do bit 1 | 1**11000** | 1**01011** |

- **Par 1:** os dois pais são iguais, então os filhos saem iguais a eles, não importa onde seja o corte.
- **Par 2:** o filho 1 pegou o primeiro bit do pai 1 e o resto do pai 2: `1` + `10101` = `110101` (x = 53).
- **Par 3:** os pais começam com o mesmo bit, então trocar depois do bit 1 só troca os dois de lugar.

## 4. Mutação

Cada um dos 36 bits passou por um teste com 5% de chance de ser invertido. Só um bit mudou:

| Filho | Antes | Bit mutado | Depois |
|:--:|:--:|:--:|:--:|
| 2 | 111000 | 4º | 111**1**00 |

O `111000` (x = 56) virou `111100` (x = 60). Essa mutação criou um indivíduo melhor que todos os da população inicial, e nenhum cruzamento teria gerado ele, porque nenhum pai tinha o padrão `1111` no começo.

## 5. Nova população

| Indivíduo | Cromossomo | x | f(x) = x² |
|:--:|:--:|:--:|:--:|
| 1 | 111000 | 56 | 3136 |
| 2 | 111100 | 60 | **3600** |
| 3 | 110101 | 53 | 2809 |
| 4 | 001011 | 11 | 121 |
| 5 | 111000 | 56 | 3136 |
| 6 | 101011 | 43 | 1849 |
| | | | **Soma 14651** |

## Comparando as duas gerações

| | Geração inicial | Depois de 1 geração |
|:--|:--:|:--:|
| Soma do fitness | 7219 | **14651** |
| Fitness médio | 1203,2 | **2441,8** |
| Melhor indivíduo | 3136 (x = 56) | **3600 (x = 60)** |

Em uma geração, **o fitness médio mais que dobrou** e o melhor indivíduo chegou mais perto do ótimo, x = 63. Quatro dos seis indivíduos agora começam com `11`, que é o padrão dos números grandes.

Também apareceu um indivíduo ruim, o `001011` (x = 11), que saiu do cruzamento do par 2. Isso é normal: o cruzamento não garante filhos melhores, e quem vai filtrar isso é a seleção da próxima geração. Outra coisa que dá para notar é que a população já tem duas cópias de `111000`. Se isso continuar por muitas gerações, a população pode ficar sem diversidade, que é a convergência prematura que a aula comenta.

## Resumo de como cheguei na solução

Primeiro converti os 6 cromossomos para decimal e calculei x² de cada um. Isso já mostrou quem era forte: o `111000` sozinho tem 43% da soma. Montei a roleta somando as aptidões acumuladas, do jeito que o slide explica, porque é isso que diz qual indivíduo corresponde a cada número sorteado.

Para os sorteios, em vez de inventar números, fiz um programa curto em Python com semente fixa. Assim qualquer pessoa pode rodar e conferir que os resultados são esses. Escolhi as taxas pelos valores da aula: cruzamento alto, entre 60% e 90%, e mutação baixa, menor que 5%.

O que eu achei mais interessante foi ver o papel de cada operador separado. A seleção fez os melhores se multiplicarem, o cruzamento gerou combinações novas (uma boa e uma ruim) e a mutação, mesmo mudando um bit só, criou o melhor indivíduo da geração. Comparei a soma, a média e o melhor antes e depois para mostrar que a população melhorou.
