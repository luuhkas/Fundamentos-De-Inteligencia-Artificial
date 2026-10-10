# Questão 11

A busca gulosa se parece com a busca em profundidade porque **as duas tendem a seguir um único caminho até o fim, sem voltar**. A profundidade faz isso por regra: sempre desce no filho mais à esquerda. A gulosa faz isso por consequência da heurística: quando ela entra num ramo, os filhos desse nó costumam estar mais perto da meta e ter h menor que os nós deixados para trás, então ela continua descendo por ali.

Essa semelhança aparece em quatro pontos:

| | Profundidade | Gulosa |
|:--|:--|:--|
| Comportamento | mergulha por um ramo | mergulha pelo ramo que parece mais perto da meta |
| Completa? | não, pode descer para sempre ou ficar em ciclo | não, pode ficar em ciclo (Iasi e Neamt) |
| Ótima? | não, devolve a primeira solução do ramo | não, devolve a primeira solução que parece perto |
| Tempo no pior caso | O(b^m) | O(b^m) |

Dá para ver isso na questão 6 desta lista. A profundidade examinou A, B, D, E, H, I e a gulosa examinou A, B, E, I. As duas entraram pelo lado de B, ficaram nele até achar I, e nunca chegaram a olhar o lado de C, onde estava a meta mais barata.

A diferença é que a profundidade escolhe o ramo às cegas, pela posição, e a gulosa escolhe pelo h(n), então costuma acertar o rumo bem mais vezes. E a profundidade gasta memória linear, O(b·m), enquanto a gulosa guarda toda a fronteira, O(b^m).

## Resumo de como cheguei na solução

O slide da gulosa diz que ela, "assim como busca em profundidade, tenta seguir ao longo de um único caminho até a meta, podendo nunca retornar". Parti dessa frase e montei a tabela comparando os critérios, onde a semelhança ficou clara: as duas não são completas, não são ótimas e têm o mesmo tempo no pior caso. Para mostrar na prática, voltei na questão 6, onde as duas buscas tomaram exatamente o mesmo rumo pela esquerda e perderam a meta de custo 15. Também deixei registrada a diferença na memória, que eu tinha confundido no começo achando que eram iguais em tudo.
