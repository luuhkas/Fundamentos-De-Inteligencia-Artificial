# Questão 1

Até agora na disciplina a gente resolvia tudo com busca: gera estado, testa se é a meta, gera mais. Nessa aula a ideia muda. Em vez de gerar estados, o sistema guarda o que se sabe sobre o mundo e tira conclusões novas disso. Pra isso ele precisa de duas coisas, que são as que a questão pede: conhecimento e raciocínio.

**Conhecimento**

A definição do slide (Russell e Norvig) é que conhecimento é um conjunto integrado de fatos e relações que, quando bem interpretado, produz um desempenho eficiente. Ou seja, um fato solto tipo "Cuba é uma nação" não resolve nada. Vira conhecimento quando os fatos estão LIGADOS por relações e alguém interpreta isso pra tomar uma decisão.

O slide também separa o fato da representação do fato. O fato é a verdade no mundo ("todo míssil é uma arma"). A representação é esse fato escrito num formalismo que a máquina consegue manipular, tipo `∀x Míssil(x) ⇒ Arma(x)`. A máquina nunca mexe no fato em si, só na representação dele.

O que torna difícil representar conhecimento, pelas características do slide:

- é volumoso: tudo que um cardiologista sabe encheria vários cadernos, como o professor falou na aula
- é difícil de caracterizar: nem o especialista sabe explicar direito como aprendeu o que sabe
- muda o tempo todo: sai tratamento novo, regra nova
- é individual: cada pessoa interpreta do seu jeito

Por isso uma boa representação tem que ser generalizável, dar pra atualizar, ser robusta (funcionar mesmo incompleta) e ser compreensível pra uma pessoa.

Esse conhecimento fica na base de conhecimento. Na aula o professor dividiu ele em conhecimento prévio, que já está na base (a lei americana no caso do West), e conhecimento do problema, que chega na hora (West é americano, Cuba tem mísseis).

**Raciocínio**

Raciocínio é gerar conhecimento NOVO a partir do que já se sabe. Quem faz isso é a máquina de inferência: ela pega o que está na base, junta com o fato novo que chegou e tira uma conclusão que não estava escrita em lugar nenhum. No caso do West nenhuma frase diz "West é criminoso", mas juntando a lei com os fatos novos dá pra concluir isso. O gif da lenha e do fósforo da aula é a mesma ideia: tendo os dois, o sistema tem que "pensar" pra chegar no fogo.

Tem várias formas de raciocinar (dedução, indução, abdução e analogia, que são as questões 3 e 5), mas o professor falou que só a dedução gera fato novo com certeza, as outras podem errar.

**Como os dois se ligam**

Nos sistemas baseados em conhecimento os dois ficam separados: a base é específica do assunto (o que o médico sabe) e a máquina de inferência é genérica (o mesmo modus ponens serve pra medicina ou pro West). Elas conversam pelo Tell (coloca fato na base), Ask (pergunta se algo é verdade) e Retract (tira fato da base). Então se eu quiser mudar de assunto, troco só a base e não preciso mexer no algoritmo.

## Resumo de como cheguei na solução

Comecei pela definição do slide e pela diferença entre fato e representação do fato, que pra mim foi o que fez a ideia fazer sentido. Depois usei as características que o slide lista e coloquei o exemplo do cardiologista que o professor deu na aula. Pro raciocínio usei a arquitetura do slide (base, máquina de inferência, Tell, Ask e Retract) e o caso do West, porque ele mostra uma conclusão nova saindo de fatos que não falavam isso direto.
