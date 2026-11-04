# carrega as disciplinas do 1o ao 4o periodo, os horarios e a grade oficial de 2026/2
#
# horario de cada aula = um numero de 0 a 49 (slot):
#   slot = dia * 10 + aula
#   dia:  0 = segunda ... 4 = sexta
#   aula: 0..4 = M1..M5 (manha), 5..9 = T1..T5 (tarde)
# ex.: slot 25 = quarta (dia 2), T1 (aula 5)

import csv
import os

PASTA = os.path.dirname(os.path.abspath(__file__))
PASTA_DADOS = os.path.join(PASTA, "..", "dados")

DIAS = ["Seg", "Ter", "Qua", "Qui", "Sex"]
AULAS = ["M1", "M2", "M3", "M4", "M5", "T1", "T2", "T3", "T4", "T5"]
N_SLOTS = 50


def nome_slot(s):
    return DIAS[s // 10] + " " + AULAS[s % 10]


# converte o codigo da UTFPR ("2M1" = segunda, primeira aula da manha) pro numero do slot
# devolve None se estiver fora da grade que o AG usa (sabado, M6, T6)
def slot_utfpr(codigo):
    dia = int(codigo[0]) - 2
    aula = codigo[1:]
    if dia < 0 or dia > 4 or aula not in AULAS:
        return None
    return dia * 10 + AULAS.index(aula)


# como a UTFPR divide as aulas da semana em blocos seguidos (visto na grade oficial)
#   3 aulas -> um bloco de 3
#   4 aulas -> dois blocos de 2
#   6 aulas -> dois blocos de 3
def divide_em_blocos(aulas_semana):
    if aulas_semana == 3:
        return [3]
    if aulas_semana == 4:
        return [2, 2]
    if aulas_semana == 6:
        return [3, 3]
    return None


# lugares onde um bloco pode comecar sem passar do fim do turno
def inicios_possiveis(tamanho):
    inicios = []
    for dia in range(5):
        for aula in range(10):
            turno = aula // 5
            if (aula + tamanho - 1) // 5 == turno and aula + tamanho - 1 < 10:
                inicios.append(dia * 10 + aula)
    return inicios


class Disciplina:
    def __init__(self, linha):
        self.periodo = int(linha["periodo"])
        self.id_ppc = linha["id_ppc"]
        self.codigo = linha["codigo"]
        self.nome = linha["disciplina"]
        self.aulas_semana = int(linha["aulas_semana"])
        self.pre = [p for p in linha["pre_requisitos"].split(";") if p]
        self.professores = linha["professores"].split(";")


def carrega():
    disciplinas = []
    with open(os.path.join(PASTA_DADOS, "disciplinas.csv")) as f:
        for linha in csv.DictReader(f):
            disciplinas.append(Disciplina(linha))

    # o Projeto Integrador I fica com horario fixo (o da grade oficial), igual as disciplinas
    # de horario fixo do artigo da UFPB. Quase tudo dele e sabado remoto ou T6, fora da
    # grade do AG, mas uma aula cai na Sex T5: esse horario fica ocupado pro 3o periodo
    fixas = [d for d in disciplinas if d.codigo == "CC3PI1"]
    disciplinas = [d for d in disciplinas if d.codigo != "CC3PI1"]

    oficial = carrega_oficial()

    # professor indisponivel = horario em que ele da aula em outro periodo ou curso
    indisponivel = {}
    codigos = [d.codigo for d in disciplinas]
    for prof, codigo, turma, slots in oficial:
        if codigo in codigos:
            continue
        for s in slots:
            if s is not None:
                indisponivel.setdefault(prof, set()).add(s)
                if codigo == "CC3PI1":
                    indisponivel.setdefault("periodo 3", set()).add(s)

    return disciplinas, fixas, indisponivel, oficial


def carrega_oficial():
    oficial = []
    with open(os.path.join(PASTA_DADOS, "grade_oficial_2026_2.csv")) as f:
        linhas = [l for l in f if not l.startswith("#")]
    for linha in csv.DictReader(linhas):
        slots = [slot_utfpr(c) for c in linha["slots"].split()]
        oficial.append((linha["professor"], linha["codigo"], linha["turma"], slots))
    return oficial


# a grade oficial do 1o ao 4o no mesmo formato que o AG gera: codigo -> lista de slots
def grade_oficial(disciplinas, oficial):
    grade = {}
    codigos = [d.codigo for d in disciplinas]
    for prof, codigo, turma, slots in oficial:
        if codigo in codigos:
            grade[codigo] = [s for s in slots if s is not None]
    return grade
