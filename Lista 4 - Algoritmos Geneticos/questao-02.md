# Questão 2

O algoritmo genético imita a evolução das espécies: os indivíduos mais adaptados têm mais chance de sobreviver e passar suas características para a próxima geração. Cada indivíduo é uma solução possível do problema. As quatro partes pedidas funcionam assim dentro do ciclo:

```
população inicial → avaliar (fitness) → selecionar os melhores
        ↑                                        ↓
   nova geração  ←  mutação  ←  cruzamento (crossover)
```

## a) Cromossomos

**O que é.** É a estrutura de dados que representa uma solução do problema, ou seja, um indivíduo da população. Também é chamado de genótipo. Cada posição do cromossomo é um **gene**, e o valor dela é o **alelo**.

**Como funciona.** O cromossomo codifica os parâmetros da solução. Pode ser:

| Representação | Exemplo | Quando usar |
|:--|:--|:--|
| cadeia de bits | `111011011` | números inteiros ou escolhas sim/não |
| vetor de reais | `(2.345, 4.3454, 5.1)` | parâmetros contínuos, como os pesos do Dino Run da aula |
| vetor de inteiros | `(1, 4, 2, 5, 3)` | ordens e permutações, como a rota do caixeiro viajante |

Escolher a representação é o primeiro passo e um dos mais importantes. Um cromossomo mal pensado pode gerar soluções inválidas ou deixar o cruzamento sem sentido. A população inicial é formada por vários cromossomos gerados aleatoriamente.

## b) Fitness

**O que é.** É a função de avaliação, ou aptidão. Ela dá uma **nota para cada cromossomo**, dizendo o quanto aquela solução é boa para o problema.

**Como funciona.** Para cada indivíduo, o fitness decodifica o cromossomo e calcula a nota, normalmente usando a função objetivo do problema. Na questão 4, o cromossomo `111000` vira x = 56 e o fitness é f(56) = 56² = 3136. Quanto maior a nota, mais chance o indivíduo tem de ser escolhido como pai.

Ele é usado na **seleção**. Na roleta, cada indivíduo ocupa uma fatia proporcional ao seu fitness, pᵢ = fᵢ / Σf, e a roleta é girada. No torneio, alguns indivíduos são sorteados e o de maior fitness vence. Um detalhe que o professor destacou: a roleta não funciona com fitness negativo, porque não existe fatia negativa. Nesse caso, ou se transforma a função para ficar positiva, ou se usa o torneio.

Em problemas de minimização, como achar a rota mais curta, o fitness precisa ser invertido, por exemplo fitness = 1 / custo, para que a rota mais curta tenha a maior nota. Fiz isso na questão 6.

## c) Cruzamento (crossover)

**O que é.** É o operador que combina dois pais para gerar filhos, que **herdam características dos dois**. É ele que junta as partes boas de soluções diferentes.

**Como funciona.** Depende da representação:

- **Um ponto** (binário): sorteia uma posição de corte e troca as partes. Com corte depois do bit 2, por exemplo, `10|1011` e `01|0101` geram `10|0101` e `01|1011`.
- **Dois pontos**: dois cortes, e a parte do meio é trocada.
- **Uniforme**: uma máscara aleatória de bits decide de qual pai vem cada gene.
- **Reais**: operações aritméticas, como a média dos pais ou o BLX-α, que sorteia o filho num intervalo em volta dos pais.
- **Permutações**: cruzamento baseado em ordem ou em posição, para não repetir cidade.

Ele é aplicado com uma **taxa alta**, normalmente entre 60% e 90%. Para cada par, sorteia-se um número r entre 0 e 1: se r for menor que a taxa, os pais cruzam; senão, os filhos saem iguais aos pais. Isso ajuda a preservar algumas soluções boas.

## d) Mutação

**O que é.** É uma pequena alteração aleatória em um filho, depois do cruzamento. Ela **coloca características novas** na população, que nenhum pai tinha.

**Como funciona.** No binário, cada bit passa por um teste com uma probabilidade pequena e, se passar, é invertido (0 vira 1 e 1 vira 0). Por exemplo, `111000` com mutação no bit 4 vira `111100`, que aconteceu na questão 4. Em reais, troca-se o gene por um valor aleatório, ou soma-se um valor pequeno (mutação creep). Em permutações, trocam-se duas cidades de lugar.

A **taxa é baixa**, normalmente menos de 5%. Se for alta demais, o algoritmo vira uma busca aleatória e perde o que aprendeu. Mas ela é essencial: sem mutação, a população pode convergir cedo demais para soluções parecidas e ficar presa num ótimo local, o que a aula chama de **convergência prematura**. A mutação é o que manda alguns indivíduos para outras regiões do espaço de busca.

## Como as quatro se juntam

O **cromossomo** define o que é uma solução, o **fitness** diz quais são as boas, o **cruzamento** combina as boas para aproveitar o que já funciona, e a **mutação** garante variedade para continuar explorando. O ciclo se repete até um critério de parada: número máximo de gerações, fitness bom o suficiente, ou a população parar de melhorar.

## Resumo de como cheguei na solução

Organizei cada item respondendo as duas perguntas do enunciado separadamente, o que é e como funciona, porque no começo eu misturava a definição com o funcionamento. Usei os slides da aula como base para os tipos de representação, de cruzamento e de mutação, e para as taxas de cada operador.

Para não ficar só na teoria, coloquei exemplos que eu mesmo calculei nas questões 4 e 6: o fitness de `111000` e a mutação que transformou ele em `111100`. Também reparei que o slide sobre o operador de cruzamento fala em "taxa de mutação é normalmente alta (entre 60% e 90%)", mas pelo contexto do slide e pelo slide seguinte, que diz que a mutação deve ser menor que 5%, quem tem taxa alta é o cruzamento. Escrevi assim na resposta.
