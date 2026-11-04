# funcao de avaliacao (fitness) da grade
#
# igual ao artigo da UFPB (Santos, 2016): cada restricao violada gera uma penalidade
#   restricao hard = 100   (grade invalida)
#   restricao soft = 10    (grade valida, mas pior)
#   fitness = 100 / (100 + soma das penalidades)  -> vai de 0 a 1, 1 = nenhuma violacao
#
# a grade e um dicionario: codigo da disciplina -> lista de slots das aulas dela

from dados import divide_em_blocos

HARD = 100
SOFT = 10

# o que cada restricao significa (aparece no relatorio e no terminal)
RESTRICOES = {
    "professor": ("hard", "professor com duas aulas no mesmo horario"),
    "indisponivel": ("hard", "professor dando aula em horario que ja tem aula em outro periodo/curso"),
    "periodo": ("hard", "duas aulas do mesmo periodo no mesmo horario"),
    "pre_requisito": ("hard", "pre-requisito e sua dependente no mesmo horario"),
    "mesmo_dia": ("soft", "aulas da mesma disciplina juntas em poucos dias"),
    "janela": ("soft", "horario vago entre duas aulas do mesmo turno (janela)"),
    "dia_vazio": ("soft", "dia da semana sem nenhuma aula no periodo"),
    "dias_professor": ("soft", "dia a mais que o professor precisa ir pra universidade"),
    "pre_junto": ("soft", "dependente fora do horario da pre-requisito (leitura dos artigos)"),
}


# modo do pre-requisito:
#   "enunciado" -> pre-requisito e dependente NAO podem ter aula no mesmo horario (hard)
#   "artigos"   -> a dependente deve ficar no horario da pre-requisito (soft), como fazem
#                  os artigos da UFPB e da UFT: quem reprova refaz a pre-requisito no horario
#                  da dependente, que ele nao pode cursar, e nao perde as outras do periodo
def avalia(grade, disciplinas, indisponivel, modo="enunciado"):
    conta = {nome: 0 for nome in RESTRICOES}
    por_codigo = {d.codigo: d for d in disciplinas}
    por_id = {d.id_ppc: d for d in disciplinas}

    # quantas aulas cada professor e cada periodo tem em cada slot
    uso_prof = {}
    uso_periodo = {}
    # aulas de horario fixo (Projeto Integrador I) ja ocupam o periodo
    for periodo in range(1, 5):
        for s in indisponivel.get("periodo %d" % periodo, set()):
            uso_periodo[(periodo, s)] = 1
    for d in disciplinas:
        for s in grade[d.codigo]:
            for p in d.professores:
                uso_prof[(p, s)] = uso_prof.get((p, s), 0) + 1
                if s in indisponivel.get(p, set()):
                    conta["indisponivel"] += 1
            uso_periodo[(d.periodo, s)] = uso_periodo.get((d.periodo, s), 0) + 1

    for n in uso_prof.values():
        if n > 1:
            conta["professor"] += n - 1
    for n in uso_periodo.values():
        if n > 1:
            conta["periodo"] += n - 1

    # pre-requisitos
    for d in disciplinas:
        for id_pre in d.pre:
            if id_pre not in por_id:
                continue
            pre = por_id[id_pre]
            juntos = len(set(grade[d.codigo]) & set(grade[pre.codigo]))
            if modo == "enunciado":
                conta["pre_requisito"] += juntos
            else:
                maximo = min(len(grade[d.codigo]), len(grade[pre.codigo]))
                conta["pre_junto"] += maximo - juntos

    # soft: a disciplina deve ter aula em pelo menos tantos dias quanto blocos
    for d in disciplinas:
        dias = set(s // 10 for s in grade[d.codigo])
        blocos = len(divide_em_blocos(d.aulas_semana))
        if len(dias) < blocos:
            conta["mesmo_dia"] += blocos - len(dias)

    # soft: janelas de cada periodo, em cada dia e turno
    for periodo in range(1, 5):
        for dia in range(5):
            for turno in range(2):
                ocupadas = []
                for aula in range(turno * 5, turno * 5 + 5):
                    if uso_periodo.get((periodo, dia * 10 + aula), 0) > 0:
                        ocupadas.append(aula)
                if ocupadas:
                    conta["janela"] += (ocupadas[-1] - ocupadas[0] + 1) - len(ocupadas)

    # soft (UFPB): minimizar dias sem aula em cada periodo
    for periodo in range(1, 5):
        for dia in range(5):
            vazio = True
            for aula in range(10):
                if uso_periodo.get((periodo, dia * 10 + aula), 0) > 0:
                    vazio = False
            if vazio:
                conta["dia_vazio"] += 1

    # soft (UFPB): maximizar disciplinas por dia pro professor = ele ir menos dias
    # conta os dias com aula (contando as aulas dele em outros cursos) menos o minimo possivel
    for p in set(uso for d in disciplinas for uso in d.professores):
        dias = set(s // 10 for s in indisponivel.get(p, set()))
        total = len(indisponivel.get(p, set()))
        for d in disciplinas:
            if p in d.professores:
                dias.update(s // 10 for s in grade[d.codigo])
                total += d.aulas_semana
        minimo = (total + 9) // 10
        conta["dias_professor"] += len(dias) - minimo

    penalidade = 0
    for nome, n in conta.items():
        if RESTRICOES[nome][0] == "hard":
            penalidade += n * HARD
        else:
            penalidade += n * SOFT
    return 100 / (100 + penalidade), conta


def violacoes_hard(conta):
    total = 0
    for nome, n in conta.items():
        if RESTRICOES[nome][0] == "hard":
            total += n
    return total
