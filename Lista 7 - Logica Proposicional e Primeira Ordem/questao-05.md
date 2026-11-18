# Questão 5

FNC (forma normal conjuntiva) é a fórmula escrita só com ¬, ∨ e ∧, onde por dentro só tem "ou" e esses blocos ficam ligados por "e". Segui os três passos do slide, um de cada vez como o professor pediu:

1. eliminar a implicação: α → β ≡ ¬α ∨ β
2. reduzir o escopo da negação: De Morgan e ¬¬α ≡ α
3. reduzir o escopo da disjunção: distributiva, α ∨ (β ∧ γ) ≡ (α ∨ β) ∧ (α ∨ γ)

Um cuidado que o professor avisou na aula: o α é TUDO que está antes do →, não só uma letra. Então quando o antecedente é um parêntese, o parêntese inteiro é negado.

**a) (A → B) → C**

```
(A → B) → C
≡ ¬(A → B) ∨ C           elimina a implicação de fora
≡ ¬(¬A ∨ B) ∨ C          elimina a implicação de dentro
≡ (¬¬A ∧ ¬B) ∨ C         De Morgan
≡ (A ∧ ¬B) ∨ C           dupla negação
≡ (A ∨ C) ∧ (¬B ∨ C)     distributiva

Fórmulas normais: {A ∨ C, ¬B ∨ C}
```

**b) A → (B → C)**

```
A → (B → C)
≡ ¬A ∨ (B → C)           elimina a implicação de fora
≡ ¬A ∨ (¬B ∨ C)          elimina a implicação de dentro
≡ ¬A ∨ ¬B ∨ C            tira o parêntese (associativa do ∨)

Fórmulas normais: {¬A ∨ ¬B ∨ C}
```

Aqui os passos 2 e 3 não tiveram o que fazer: nenhuma negação ficou em cima de parêntese e não apareceu nenhum ∧. Ficou uma cláusula só.

Comparando com a letra a dá pra ver que mudar o parêntese de lugar muda a fórmula. Na a o antecedente é uma implicação e ao negar ela vira um ∧, por isso saíram duas cláusulas.

**c) (A → B) ∨ (B → A)**

```
(A → B) ∨ (B → A)
≡ (¬A ∨ B) ∨ (¬B ∨ A)    elimina as duas implicações
≡ ¬A ∨ B ∨ ¬B ∨ A        tira os parênteses

Fórmulas normais: {¬A ∨ B ∨ ¬B ∨ A}
```

Também é uma cláusula só. E ela tem B ∨ ¬B dentro (e A ∨ ¬A também), então é sempre verdadeira, é uma tautologia, igual o p ∨ ¬p do slide de validade.

**d) (A → B) → (¬C → (D ∧ E))**

```
(A → B) → (¬C → (D ∧ E))
≡ ¬(A → B) ∨ (¬C → (D ∧ E))            elimina a implicação de fora
≡ ¬(¬A ∨ B) ∨ (¬¬C ∨ (D ∧ E))          elimina as duas de dentro
≡ (¬¬A ∧ ¬B) ∨ (¬¬C ∨ (D ∧ E))         De Morgan
≡ (A ∧ ¬B) ∨ C ∨ (D ∧ E)               dupla negação (em A e em C)
≡ ((A ∨ C) ∧ (¬B ∨ C)) ∨ (D ∧ E)       distributiva com o C
≡ ((A ∨ C) ∨ (D ∧ E)) ∧ ((¬B ∨ C) ∨ (D ∧ E))       distributiva de novo
≡ (A ∨ C ∨ D) ∧ (A ∨ C ∨ E) ∧ (¬B ∨ C ∨ D) ∧ (¬B ∨ C ∨ E)     e mais uma vez

Fórmulas normais: {A ∨ C ∨ D, A ∨ C ∨ E, ¬B ∨ C ∨ D, ¬B ∨ C ∨ E}
```

Essa foi a mais trabalhosa porque depois do passo 2 sobraram dois ∧ dentro de um ∨, e tive que distribuir três vezes até não ter mais nenhum ∧ por dentro. É a mesma situação do exemplo do slide (p ∨ q → r ∧ s), que também termina com quatro cláusulas e onde o slide avisa que o terceiro passo "ainda não foi concluído" depois da primeira distribuição.

## Resumo de como cheguei na solução

Fiz as quatro na ordem do slide, sem pular passo: primeiro tirei TODAS as implicações (de fora pra dentro), depois empurrei as negações pra dentro com De Morgan e cortei as duplas negações, e só no final distribuí o ∨ sobre o ∧. No fim de cada uma conferi se estava mesmo em FNC olhando duas coisas: negação só em cima de letra, e nenhum ∧ dentro de parêntese com ∨. A b e a c nem precisaram da distributiva. Pra ter certeza que não errei sinal no caminho, testei a fórmula original e a final com alguns valores (por exemplo na a, com A = F, B = F, C = F as duas dão F) e bateu.
