# solver exato (programacao por restricoes, CP-SAT do Google OR-Tools) pra saber qual e
# a MENOR penalidade possivel. Serve pra conferir o AG, igual a forca bruta do trabalho 1.
#
# modela exatamente as mesmas restricoes da avaliacao.py:
#   as hard viram restricoes obrigatorias e as soft viram o que o solver minimiza
#
# rodar (precisa do ortools, que nao instala no python 3.14 ainda):
#   uv run --python 3.12 --with ortools python3 exato.py [enunciado|artigos]

import sys
from ortools.sat.python import cp_model
from dados import carrega, divide_em_blocos, inicios_possiveis
from avaliacao import avalia, SOFT


def resolve(modo="enunciado", tempo=120):
    disciplinas, fixas, indisponivel, oficial = carrega()
    m = cp_model.CpModel()

    # x[(i, inicio)] = 1 se o bloco i comeca no slot inicio
    blocos = []
    for d in disciplinas:
        for tamanho in divide_em_blocos(d.aulas_semana):
            blocos.append((d, tamanho))
    x = {}
    for i, (d, tamanho) in enumerate(blocos):
        opcoes = []
        for inicio in inicios_possiveis(tamanho):
            x[(i, inicio)] = m.NewBoolVar("")
            opcoes.append(x[(i, inicio)])
        m.AddExactlyOne(opcoes)

    # aula[(codigo, s)] = 1 se a disciplina tem aula no slot s
    aula = {}
    for d in disciplinas:
        for s in range(50):
            cobre = []
            for i, (db, tamanho) in enumerate(blocos):
                if db is d:
                    for inicio in inicios_possiveis(tamanho):
                        if inicio <= s < inicio + tamanho:
                            cobre.append(x[(i, inicio)])
            aula[(d.codigo, s)] = m.NewBoolVar("")
            m.Add(aula[(d.codigo, s)] == sum(cobre))

    profs = sorted(set(p for d in disciplinas for p in d.professores))
    por_id = {d.id_ppc: d for d in disciplinas}
    custo = []

    for s in range(50):
        # hard: professor, indisponivel, periodo
        for p in profs:
            dele = [aula[(d.codigo, s)] for d in disciplinas if p in d.professores]
            if s in indisponivel.get(p, set()):
                m.Add(sum(dele) == 0)
            else:
                m.Add(sum(dele) <= 1)
        for periodo in range(1, 5):
            fixa = 1 if s in indisponivel.get("periodo %d" % periodo, set()) else 0
            m.Add(sum(aula[(d.codigo, s)] for d in disciplinas if d.periodo == periodo) + fixa <= 1)

    # pre-requisito
    for d in disciplinas:
        for id_pre in d.pre:
            if id_pre not in por_id:
                continue
            pre = por_id[id_pre]
            if modo == "enunciado":
                for s in range(50):
                    m.Add(aula[(d.codigo, s)] + aula[(pre.codigo, s)] <= 1)
            else:
                juntos = []
                for s in range(50):
                    j = m.NewBoolVar("")
                    m.AddMultiplicationEquality(j, [aula[(d.codigo, s)], aula[(pre.codigo, s)]])
                    juntos.append(j)
                maximo = min(d.aulas_semana, pre.aulas_semana)
                custo.append(maximo - sum(juntos))

    # soft: dias de aula da disciplina >= numero de blocos
    for d in disciplinas:
        dias = []
        for dia in range(5):
            tem = m.NewBoolVar("")
            m.AddMaxEquality(tem, [aula[(d.codigo, dia * 10 + a)] for a in range(10)])
            dias.append(tem)
        falta = m.NewIntVar(0, 5, "")
        m.Add(falta >= len(divide_em_blocos(d.aulas_semana)) - sum(dias))
        custo.append(falta)

    # ocupacao de cada periodo
    ocupa = {}
    for periodo in range(1, 5):
        for s in range(50):
            fixa = 1 if s in indisponivel.get("periodo %d" % periodo, set()) else 0
            ocupa[(periodo, s)] = sum(aula[(d.codigo, s)] for d in disciplinas if d.periodo == periodo) + fixa

    for periodo in range(1, 5):
        for dia in range(5):
            # soft: dia sem aula
            tem = m.NewBoolVar("")
            m.Add(sum(ocupa[(periodo, dia * 10 + a)] for a in range(10)) >= 1).OnlyEnforceIf(tem)
            m.Add(sum(ocupa[(periodo, dia * 10 + a)] for a in range(10)) == 0).OnlyEnforceIf(tem.Not())
            custo.append(1 - tem)
            # soft: janelas (slot vazio com aula antes e depois no mesmo turno)
            for turno in range(2):
                slots = [dia * 10 + turno * 5 + a for a in range(5)]
                for k in range(1, 4):
                    antes = m.NewBoolVar("")
                    depois = m.NewBoolVar("")
                    m.AddMaxEquality(antes, [ocupa[(periodo, t)] for t in slots[:k]])
                    m.AddMaxEquality(depois, [ocupa[(periodo, t)] for t in slots[k + 1:]])
                    buraco = m.NewBoolVar("")
                    m.Add(buraco >= antes + depois - 1 - ocupa[(periodo, slots[k])])
                    custo.append(buraco)

    # soft: dias que cada professor vai pra universidade, menos o minimo
    for p in profs:
        outros = indisponivel.get(p, set())
        total = len(outros) + sum(d.aulas_semana for d in disciplinas if p in d.professores)
        dias = []
        for dia in range(5):
            if any(s // 10 == dia for s in outros):
                dias.append(1)
                continue
            vai = m.NewBoolVar("")
            m.AddMaxEquality(vai, [aula[(d.codigo, dia * 10 + a)] for d in disciplinas
                                   if p in d.professores for a in range(10)])
            dias.append(vai)
        custo.append(sum(dias) - (total + 9) // 10)

    m.Minimize(sum(custo))
    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = tempo
    solver.parameters.num_workers = 8
    status = solver.Solve(m)

    # monta a grade e confere com a mesma avaliacao do AG
    grade = {d.codigo: [] for d in disciplinas}
    for (i, inicio), var in x.items():
        if solver.Value(var):
            d, tamanho = blocos[i]
            grade[d.codigo] += list(range(inicio, inicio + tamanho))
    fitness, conta = avalia(grade, disciplinas, indisponivel, modo)
    otimo = status == cp_model.OPTIMAL
    return grade, fitness, conta, otimo, solver.ObjectiveValue() * SOFT


if __name__ == "__main__":
    modo = sys.argv[1] if len(sys.argv) > 1 else "enunciado"
    grade, fitness, conta, otimo, penalidade = resolve(modo)
    print("modo:", modo)
    print("prova de otimo:", "sim" if otimo else "nao (parou no limite de tempo)")
    print("%s: %d   fitness: %.4f" % ("menor penalidade possivel" if otimo else "melhor penalidade achada", penalidade, fitness))
    print(conta)
