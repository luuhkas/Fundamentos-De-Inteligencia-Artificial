# Questão 1

Pra formalizar segui o jeito do slide do time de futebol: primeiro dou uma letra pra cada proposição simples, depois monto a fórmula com os conectivos. O cuidado foi separar direito o que é proposição simples: cada frase que pode ser verdadeira ou falsa sozinha ganha uma letra, mesmo quando o português junta elas numa só ("alta e magra" são duas).

**a) Se Ana é alta e magra, então ela é elegante.**

```
p : Ana é alta
q : Ana é magra
r : Ana é elegante

(p ∧ q) → r
```

"Alta e magra" vai pro antecedente como p ∧ q. Pela prioridade o ∧ já vem antes do →, mas deixei o parêntese pra separar o "se" do "então".

**b) Se Beto é rico, então ele não precisa de empréstimos.**

```
p : Beto é rico
q : Beto precisa de empréstimos

p → ¬q
```

O "não" não entra na proposição, fica como negação na fórmula. Foi o que o professor fez na aula com o time: "o time não joga bem" não ganhou letra nova, ele falou que é a mesma proposição só que negada. Se eu fizesse q : "Beto não precisa de empréstimos" dava p → q, que também representa a frase, mas esconde a negação e isso atrapalha depois nas regras de inferência.

**c) Se Caio ama a natureza, então ele ama as plantas e os animais.**

```
p : Caio ama a natureza
q : Caio ama as plantas
r : Caio ama os animais

p → (q ∧ r)
```

Igual a a, só que a conjunção está do outro lado da implicação.

**d) Se Denis jogar na loteria, então ele ficará rico ou desiludido.**

```
p : Denis joga na loteria
q : Denis fica rico
r : Denis fica desiludido

p → (q ∨ r)
```

Fiquei na dúvida nesse "ou", porque no português "rico ou desiludido" soa como um ou outro. Mas entre os cinco conectivos da aula só tem o ∨ inclusivo (vale um, outro ou os dois), e a frase não diz que não pode ser os dois, então mantive.

**e) Se faz frio ou chove, então Eva fica em casa e vê tevê.**

```
p : faz frio
q : chove
r : Eva fica em casa
s : Eva vê tevê

(p ∨ q) → (r ∧ s)
```

Essa junta as duas anteriores: disjunção no antecedente e conjunção no consequente.

## Resumo de como cheguei na solução

Usei o mesmo passo a passo do slide "Formalizando Argumentos": separar as proposições simples, dar uma letra minúscula pra cada uma (o slide fala que proposição atômica é letra minúscula) e depois trocar os "se...então", "e", "ou" e "não" pelos conectivos →, ∧, ∨ e ¬. Deixei a negação fora da letra, igual o professor fez com o time. Nas frases com "e" ou "ou" dentro do se/então usei parênteses pra marcar antecedente e consequente, mesmo onde a prioridade já resolveria, porque prefiro não depender da ordem padrão.
