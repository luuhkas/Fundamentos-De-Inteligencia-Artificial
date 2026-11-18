# Questão 4

São os mesmos três argumentos da questão 3, mas agora por refutação. Em vez de sair das premissas e chegar na conclusão, eu nego a conclusão (hipótese) e mostro que isso bate de frente com a base. Na aula o professor falou assim: "vou provar que o contrário é um absurdo". Se o contrário não pode existir, a conclusão é verdadeira.

Como o enunciado pede sem FNC, fiz igual o slide do time de futebol (o do "técnico não é culpado"): as premissas ficam com as implicações do jeito que estão e eu uso MT e MP normais até aparecer a contradição.

**a) {p → q, ¬q, ¬p → r} ⊢ r**

```
(1) p → q      Δ
(2) ¬q         Δ
(3) ¬p → r     Δ
---------------------
(4) ¬r         hipótese
(5) ¬¬p        MT(3,4)
(6) p          negação em (5), ¬(¬α) ≡ α
(7) q          MP(1,6)
(8) contradição! confrontando (7) e (2)
```

Supus que r é falso. Com ¬r e (3) o modus tollens devolve a negação de ¬p, que é p. Com p e (1) sai q. Só que a base diz ¬q na linha (2). q e ¬q juntos não dá, então a hipótese ¬r é impossível e r vale.

**b) {¬p → ¬q, q, p → ¬r} ⊢ ¬r**

```
(1) ¬p → ¬q    Δ
(2) q          Δ
(3) p → ¬r     Δ
---------------------
(4) ¬¬r        hipótese
(5) ¬p         MT(3,4)
(6) ¬q         MP(1,5)
(7) contradição! confrontando (6) e (2)
```

A conclusão já é uma negação (¬r), então a hipótese é a negação dela, ¬¬r, que é o mesmo que supor r. Deixei como ¬¬r porque assim ela é exatamente a negação do consequente de (3), e o MT entra direto dando ¬p. Com ¬p e (1) sai ¬q, que contradiz o q da linha (2).

**c) {p → q, q → r, ¬r, ¬p → s} ⊢ s**

```
(1) p → q      Δ
(2) q → r      Δ
(3) ¬r         Δ
(4) ¬p → s     Δ
---------------------
(5) ¬s         hipótese
(6) ¬¬p        MT(4,5)
(7) p          negação em (6), ¬(¬α) ≡ α
(8) q          MP(1,7)
(9) r          MP(2,8)
(10) contradição! confrontando (9) e (3)
```

Esse é o próprio exemplo do slide com outras letras: nega a conclusão, MT pra descobrir p, e depois vai descendo a cadeia p → q → r com MP até bater no ¬r da base.

Duas observações. No slide o passo (b) vai direto de "o técnico não é culpado" pra "o time joga bem", sem a linha do ¬¬p. Eu mantive as duas linhas pra ficar igual ao que fiz na questão 3, onde o MT devolve a negação do antecedente ao pé da letra. E o slide termina com "logo o argumento é inválido!", mas acho que é erro de digitação: a hipótese contradizer as premissas é justamente o que mostra que o argumento é VÁLIDO, e é o que o professor fala na aula ("logo a outra parte é verdadeira, o técnico é de fato culpado").

## Resumo de como cheguei na solução

Nos três fiz os mesmos passos: copiei as premissas como Δ, coloquei a negação da conclusão como hipótese e fui aplicando MT e MP sempre usando a última linha que descobri com uma premissa. O caminho é o contrário da questão 3. Lá eu partia das premissas e ia atrás da conclusão, aqui eu parto da conclusão negada e vou andando até trombar com uma premissa que diz o oposto. Na a a contradição foi com ¬q, na b com q e na c com ¬r. Achei mais fácil que a prova direta porque não precisei escolher por onde começar, a hipótese já diz qual premissa usar primeiro (a que tem a conclusão no consequente).
