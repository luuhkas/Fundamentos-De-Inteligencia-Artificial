# Questão 7

Essa junta tudo da lista: formalizar o argumento, passar pra FNC, negar a conclusão e resolver.

**Formalização**

```
p : o programa possui erros de sintaxe
q : a compilação produz mensagem de erro
r : a compilação produz um executável
s : executamos o programa para obter um resultado

(1) p → q      se o programa possui erros de sintaxe, sua compilação produz mensagem de erro
(2) ¬p → r     se o programa não possui erros de sintaxe, sua compilação produz um executável
(3) r → s      se tivermos um programa executável, podemos executá-lo para obter um resultado
(4) ¬s         não temos como executar o programa para obter um resultado
(5) q          logo, a compilação do programa produz uma mensagem de erro

{p → q, ¬p → r, r → s, ¬s} ⊢ q
```

O cuidado foi o mesmo da lista passada, não criar letra nova pra frase que já tem letra. "Se tivermos um programa executável" na (3) é o mesmo fato de "a compilação produz um executável" da (2), então é o r. Se eu desse outra letra, a (2) e a (3) não se ligavam e não tinha como provar nada. E "não temos como executar" é a negação do s.

**FNC**

As três implicações só precisam do passo 1 (α → β ≡ ¬α ∨ β). Na segunda aparece dupla negação:

```
p → q    ≡ ¬p ∨ q
¬p → r   ≡ ¬¬p ∨ r ≡ p ∨ r
r → s    ≡ ¬r ∨ s
¬s       já é cláusula
```

**Refutação com resolução**

```
(1) ¬p ∨ q     Δ
(2) p ∨ r      Δ
(3) ¬r ∨ s     Δ
(4) ¬s         Δ
---------------------
(5) ¬q         hipótese
(6) ¬p         RES(5,1)
(7) r          RES(6,2)
(8) s          RES(7,3)
(9) □          RES(8,4)
```

Supus que a compilação NÃO produz mensagem de erro (¬q). Com a (1) isso obriga o programa a não ter erro de sintaxe (¬p). Sem erro de sintaxe, a (2) diz que sai um executável (r). Com executável, a (3) diz que dá pra executar e obter resultado (s). Mas a (4) diz que não temos como executar. s e ¬s dão a cláusula vazia, então a hipótese é um absurdo e a conclusão vale: a compilação produz mensagem de erro.

Depois de formalizado vi que é o argumento do time de futebol do slide com outra história: {p → q, ¬p → r, q → s, ¬s} ⊢ r. A diferença é que aqui a cadeia que leva até a contradição sai do lado do ¬p (¬p → r → s) e a conclusão é o q, e lá é o contrário. A prova ficou com o mesmo tamanho do exemplo do slide, quatro resoluções.

## Resumo de como cheguei na solução

Fiz na ordem dos passos do slide de refutação. Antes de tudo formalizei, casando as frases que falam do mesmo fato com palavras diferentes (o executável da segunda e da terceira frase). Depois converti cada premissa pra FNC, que aqui foi só trocar a implicação por ¬α ∨ β. Coloquei ¬q como hipótese e resolvi sempre o último resultado com uma cláusula de Δ, como o slide recomenda, e deu certo direto: cada resolução deixou uma letra só, até o s bater com o ¬s.
