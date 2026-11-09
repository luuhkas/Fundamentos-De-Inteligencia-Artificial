# Questão 2

Formalizar um argumento é o mesmo que a questão 1, só que agora são várias frases e uma delas é a conclusão. Segui o slide do time de futebol: dou as letras, escrevo cada frase como fórmula, separo premissas de conclusão e monto a notação {premissas} |= conclusão, que na aula o professor descreveu como vários fatos implicando num fato específico. O trabalho a mais aqui foi entender o que cada frase está dizendo de verdade, porque o enunciado troca as palavras entre a premissa e a conclusão.

**a) Filme bom e cinema lotado**

```
p : o filme é bom
q : o cinema fica lotado

(1) p → q      quando o filme é bom, o cinema fica lotado
(2) p          a crítica diz que esse filme é muito bom
(3) q          não encontraremos lugares livres

{p → q, p} |= q
```

Tive que interpretar duas frases. "A crítica diz que o filme é muito bom" tratei como p mesmo, o "muito" não muda o valor-verdade. E "não encontraremos lugares livres" é só outro jeito de dizer que o cinema está lotado, então é o próprio q, não é proposição nova nem negação. Se eu criasse uma letra pra "lugares livres" a conclusão ficava sem ligação nenhuma com as premissas.

No fim ficou com a cara do modus ponens da tabela: α, α → β |= β.

**b) Chuva e trânsito na marginal**

```
p : chove à tarde
q : à noite o trânsito na marginal fica congestionado

(1) p → q      sempre que chove à tarde, à noite o trânsito fica congestionado
(2) ¬q         agora à noite o trânsito está fluindo bem
(3) ¬p         não choveu à tarde

{p → q, ¬q} |= ¬p
```

"Fluindo bem" é o contrário de congestionado, então é ¬q, mesma ideia do "time não joga bem" da aula que vira ¬p em vez de ganhar letra nova. Nega o consequente e conclui a negação do antecedente, modus tollens: α → β, ¬β |= ¬α.

**c) ETs**

```
p : existem ETs
q : os ETs nos enviaram algum sinal
r : fizemos contato com os ETs

(1) p → q      se existissem ETs, já teriam enviado sinal
(2) q → r      se tivessem enviado sinal, teríamos feito contato
(3) p → r      se existissem ETs, já teríamos feito contato

{p → q, q → r} |= p → r
```

Aqui a conclusão não é uma proposição simples, é uma implicação inteira. É a regra da cadeia (silogismo hipotético) da tabela: α → β, β → γ |= α → γ. O "se existissem" eu li como "se existem", a lógica proposicional não tem tempo verbal, a frase só é V ou F.

## Resumo de como cheguei na solução

Fiz igual ao slide: letras pras proposições, uma fórmula por frase e no final a notação com |=. A parte que deu mais trabalho foi casar as palavras, porque a conclusão nunca repete a premissa do mesmo jeito ("lotado" vira "sem lugares livres", "congestionado" vira "fluindo bem"). A regra que usei foi: antes de criar letra nova, perguntar se a frase não é a mesma coisa, ou a negação, de uma que já tem letra. Depois de formalizados os três ficaram com a cara de uma regra da tabela (MP, MT e regra da cadeia), aí fiquei mais tranquilo que estava certo.
