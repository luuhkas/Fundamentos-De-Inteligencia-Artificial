# Questão 8

Na lógica de predicados a frase não vira mais uma letra só. Eu separo os objetos das relações: cada propriedade ou relação vira um predicado, e os quantificadores ∀ (para todo) e ∃ (existe pelo menos um) dizem de quantos objetos estou falando. Escrevi os predicados com letra maiúscula e as variáveis minúsculas, como no slide de sintaxe, e usei → pra implicação como está no enunciado da lista.

O padrão que usei em quase todas veio de dois exemplos do slide:

```
∀x Rei(x) → Pessoa(x)                todo rei é pessoa         (∀ anda com →)
∃x Coroa(x) ∧ NaCabeça(x, João)      existe uma coroa que...   (∃ anda com ∧)
```

**a) Toda cobra é venenosa.**

```
∀x Cobra(x) → Venenosa(x)
```

Para todo x, se x é cobra então x é venenosa. É o exemplo do rei trocando os predicados.

**b) Nenhuma bruxa é bela.**

```
∀x Bruxa(x) → ¬Bela(x)
```

Para todo x, se x é bruxa então x não é bela. Dá pra escrever também como ¬∃x Bruxa(x) ∧ Bela(x), "não existe bruxa bela", que é equivalente pela regra de De Morgan dos quantificadores (∀x ¬P ≡ ¬∃x P).

**c) Algumas plantas são carnívoras.**

```
∃x Planta(x) ∧ Carnívora(x)
```

Existe pelo menos um x que é planta E é carnívora. Aqui é ∧ e não →, igual o exemplo da coroa: o x tem que ser as duas coisas ao mesmo tempo.

**d) Há aves que não voam.**

```
∃x Ave(x) ∧ ¬Voa(x)
```

**e) Tudo que sobe, desce.**

```
∀x Sobe(x) → Desce(x)
```

**f) Existem políticos que não são honestos.**

```
∃x Político(x) ∧ ¬Honesto(x)
```

Mesma forma da d.

**g) Não existe bêbado feliz.**

```
¬∃x Bêbado(x) ∧ Feliz(x)
```

Escrevi com ¬∃ porque a frase já começa com "não existe". Pela mesma equivalência da b, é o mesmo que ∀x Bêbado(x) → ¬Feliz(x), todo bêbado não é feliz. A g e a b são o mesmo tipo de frase, só muda o jeito de falar em português.

**h) Pedras preciosas são caras.**

```
∀x PedraPreciosa(x) → Cara(x)
```

A frase não tem "toda", mas está falando das pedras preciosas em geral, então é ∀. Igual o "irmãos são parentes" do slide, que também não tem a palavra "todo" e vira ∀x ∀y Irmão(x,y) → Parente(x,y). Tratei "pedra preciosa" como um predicado só. Separando ficaria ∀x Pedra(x) ∧ Preciosa(x) → Cara(x).

**i) Ninguém gosta de impostos.**

```
∀x ¬Gosta(x, Impostos)
```

Essa é o exemplo das cenouras do slide: "todo mundo detesta cenouras" ≡ "não existe alguém que goste de cenouras", ∀x ¬Gosta(x, Cenouras) ≡ ¬∃x Gosta(x, Cenouras). Gosta é um predicado binário (quem gosta, do quê) e Impostos entra como constante. A outra forma é ¬∃x Gosta(x, Impostos). A frase só tem uma negação, o "ninguém", então a fórmula também só tem uma.

**j) Vegetarianos não gostam de açougueiros.**

```
∀x ∀y Vegetariano(x) ∧ Açougueiro(y) → ¬Gosta(x, y)
```

Agora são dois objetos diferentes, o vegetariano e o açougueiro, então precisei de duas variáveis e quantificadores aninhados. Para todo x e todo y, se x é vegetariano e y é açougueiro, então x não gosta de y. Tem a mesma cara da frase 7 do exemplo de Roma (∀X ∀Y pessoa(X) ∧ tentarassassinar(X,Y) → ¬leal(X,Y)).

**k) Toda mãe ama seus filhos.**

```
∀m ∀c Mãe(c) = m → Ama(m, c)
```

Usei a função Mãe do exemplo de parentesco do slide (Mãe(c) = m quer dizer que a mãe de c é m). Para todo m e todo c, se m é a mãe de c, então m ama c. Como Mãe é função e não predicado, ela devolve um objeto, por isso aparece com o sinal de igual.

Se fosse com predicado binário em vez de função ficaria ∀x ∀y MãeDe(x, y) → Ama(x, y). Preferi a função porque é assim que o slide trata mãe e pai ("cada pessoa tem apenas um de cada").

## Resumo de como cheguei na solução

O que mais pesou foi decidir o quantificador. "Toda", "tudo", "nenhuma", "ninguém" e as frases gerais sem quantificador (h, j) viraram ∀. "Algumas", "há" e "existem" viraram ∃. Depois separei os predicados, o tipo do objeto (Cobra, Planta, Ave) e o que se afirma dele (Venenosa, Carnívora, Voa), e liguei com → quando era ∀ e com ∧ quando era ∃, que é o padrão dos dois exemplos do slide. Nas frases negativas (b, g, i) escolhi a forma mais parecida com o português e anotei a outra, usando a regra de De Morgan dos quantificadores. Só a j e a k precisaram de duas variáveis, porque falam de uma relação entre dois objetos. A k foi a que mais demorei, por causa do Mãe ser função no slide.
