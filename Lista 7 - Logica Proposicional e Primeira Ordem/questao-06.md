# Questão 6

Prova por resolução é a refutação da questão 4 só que com tudo em FNC. Em vez de MP, MT e SH eu uso a RES do slide, que faz o papel das três (o slide tem uma tabela mostrando a RES equivalente a cada uma):

```
RES(α ∨ β, ¬β ∨ γ) = α ∨ γ
RES(α, ¬α) = □
```

Ou seja, junto duas cláusulas que têm a mesma letra com sinais opostos, essa letra some e o resto fica. O objetivo é chegar na cláusula vazia □. Os passos são os do slide: converter pra FNC, colocar a negação da conclusão como hipótese e resolver até aparecer a contradição.

**a) {(A ∨ B ∨ ¬D), (A ∨ B ∨ C ∨ D), (¬B ∨ C), ¬A} ⊢ C**

As premissas já estão em FNC, cada uma é uma cláusula. Só entra a hipótese ¬C.

```
(1) A ∨ B ∨ ¬D       Δ
(2) A ∨ B ∨ C ∨ D    Δ
(3) ¬B ∨ C           Δ
(4) ¬A               Δ
---------------------
(5) ¬C               hipótese
(6) A ∨ B ∨ D        RES(5,2)
(7) B ∨ D            RES(6,4)
(8) A ∨ B            RES(7,1)
(9) B                RES(8,4)
(10) C               RES(9,3)
(11) □               RES(10,5)
```

A hipótese ¬C resolve com a (2) ou com a (3), que são as que têm C. Comecei pela (2), que é a maior e a única com D positivo, e daí fui limpando: o ¬A da (4) tira o A, a (1) tira o D por causa do ¬D. Na linha (8) a conta dá A ∨ B ∨ B, porque o B aparece nas duas cláusulas. B ∨ B é só B, então escrevi A ∨ B. Depois o ¬A tira o A de novo, e com B sozinho a (3) entrega C.

Na linha (10) apareceu C, que é o contrário da hipótese ¬C. Aí já tem a contradição, e resolvendo as duas dá a cláusula vazia. Logo Δ ∪ {¬C} é inconsistente e Δ ⊢ C é válido.

Nesse não deu pra seguir 100% a dica do slide de usar sempre o último resultado com uma cláusula de Δ. O último passo usa a hipótese (5) de novo, que não é de Δ, e usei o ¬A duas vezes. Não vi problema porque o 3º passo do slide diz que a resolução vai até "encontrar uma nova proposição que contradiz a hipótese" ou a cláusula vazia, e a linha (10) é isso, o C contradizendo o ¬C. Na aula o professor também falou que qualquer contradição vale, "seja o não T com o T que você queria ou uma outra qualquer".

**b) {A, (¬A ∨ (B ∧ (C ∨ ¬B))), (¬B ∨ D)} ⊢ (C ∧ D)**

Aqui a segunda premissa não está em FNC, tem ∧ dentro de ∨. Converti primeiro (só o passo 3, não tem implicação nem negação pra arrumar):

```
¬A ∨ (B ∧ (C ∨ ¬B))
≡ (¬A ∨ B) ∧ (¬A ∨ (C ∨ ¬B))     distributiva
≡ (¬A ∨ B) ∧ (¬A ∨ C ∨ ¬B)

Fórmulas normais: {¬A ∨ B, ¬A ∨ C ∨ ¬B}
```

A conclusão também não é uma letra só, então a negação dela precisa ir pra FNC, como o slide do 2º passo avisa:

```
¬(C ∧ D) ≡ ¬C ∨ ¬D      De Morgan
```

É UMA cláusula só (¬C ∨ ¬D), não duas. Negar "C e D" é dizer que pelo menos um dos dois é falso, não que os dois são.

```
(1) A                Δ
(2) ¬A ∨ B           Δ
(3) ¬A ∨ C ∨ ¬B      Δ
(4) ¬B ∨ D           Δ
---------------------
(5) ¬C ∨ ¬D          hipótese
(6) ¬B ∨ ¬C          RES(5,4)
(7) ¬A ∨ ¬B          RES(6,3)
(8) ¬B               RES(7,1)
(9) ¬A               RES(8,2)
(10) □               RES(9,1)
```

Na (7) de novo aparece letra repetida: resolvendo o C sobra ¬B ∨ ¬A ∨ ¬B, que é ¬A ∨ ¬B. Esse aqui seguiu certinho a dica do slide, cada linha usa o resultado anterior com uma cláusula de Δ. No final sobrou ¬A, e a base tem A, então cláusula vazia. Δ ⊢ (C ∧ D) é válido.

## Resumo de como cheguei na solução

Segui os três passos do slide. Na a as premissas já estavam em FNC, na b tive que distribuir a segunda, que virou duas cláusulas. Depois neguei a conclusão pra ter a hipótese, e na b precisei de De Morgan porque a conclusão é um ∧. Na resolução comecei sempre pela hipótese e a cada linha procurei em Δ uma cláusula com a letra de sinal oposto, cortando uma letra por vez. O que me confundiu no começo foi a letra repetida depois de resolver (B ∨ B), que tem que juntar numa só, senão a cláusula nunca diminui.
