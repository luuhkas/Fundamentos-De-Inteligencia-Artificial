# Trabalho 2 - Algoritmo Genetico
# monta a grade do 1o ao 4o periodo de Ciencia da Computacao (UTFPR Santa Helena)
# rodar de dentro da pasta codigo: python3 main.py

import os
import matplotlib.pyplot as plt
from dados import carrega, grade_oficial
from avaliacao import avalia, RESTRICOES, violacoes_hard
from genetico import Problema, executa, SELECOES, CRUZAMENTOS
from visual import desenha_grade, desenha_convergencia, imprime_grade
from comparativo import le, tabela, grafico, memetico, OTIMO

PASTA = os.path.dirname(os.path.abspath(__file__))
PASTA_IMAGENS = os.path.join(PASTA, "..", "imagens")


def escolhe(titulo, opcoes):
    nomes = list(opcoes)
    for i, nome in enumerate(nomes):
        print("  %d - %s" % (i + 1, nome))
    return nomes[int(input(titulo)) - 1]


def mostra_conta(conta):
    for nome, n in conta.items():
        tipo, descricao = RESTRICOES[nome]
        if n > 0:
            print("  %-5s %3d x %s" % (tipo, n, descricao))
    print("  violacoes hard: %d" % violacoes_hard(conta))


disciplinas, fixas, indisponivel, oficial = carrega()
modo = "enunciado"

while True:
    print("\n==== Trabalho 2 - grade horaria com algoritmo genetico ====")
    print("pre-requisito: leitura do %s" % modo)
    print("1 - rodar o algoritmo genetico")
    print("2 - avaliar a grade oficial de 2026/2")
    print("3 - comparativo das 9 configuracoes (30 sementes)")
    print("4 - comparativo AG x AG com busca local (memetico)")
    print("5 - trocar a leitura do pre-requisito (enunciado / artigos)")
    print("6 - comparativo das taxas de mutacao (1%, 2% e 5%)")
    print("0 - sair")
    opcao = input("opcao: ").strip()

    if opcao == "1":
        selecao = escolhe("selecao: ", SELECOES)
        cruzamento = escolhe("cruzamento: ", CRUZAMENTOS)
        com_busca = input("usar busca local (memetico)? s/n: ").strip() == "s"
        geracoes = int(input("geracoes (minimo 500, enter = 800): ") or 800)
        geracoes = max(geracoes, 500)
        semente = input("semente (enter = aleatoria, a figura do relatorio e a 13): ").strip()
        semente = int(semente) if semente else None
        problema = Problema(disciplinas, indisponivel, modo)
        melhor, nota, geracao, historico = executa(problema, selecao, cruzamento, geracoes=geracoes,
                                                   busca_local=memetico if com_busca else None,
                                                   semente=semente, mostra=True)
        grade = problema.decodifica(melhor)
        fitness, conta = avalia(grade, disciplinas, indisponivel, modo)
        print("\nmelhor fitness: %.4f   penalidade: %d   (achado na geracao %d)" % (fitness, round(100 / fitness - 100), geracao))
        mostra_conta(conta)
        imprime_grade(grade, disciplinas)
        nome = "%s + %s%s" % (selecao, cruzamento.replace("_", " "), " + busca local" if com_busca else "")
        desenha_grade(grade, disciplinas, indisponivel, "Grade gerada pelo AG (%s)" % nome,
                      "Figura: melhor grade encontrada%s. Fitness %.4f, penalidade %d, %d violações hard."
                      % (" (semente %d)" % semente if semente is not None else "", fitness,
                         round(100 / fitness - 100), violacoes_hard(conta)), modo,
                      os.path.join(PASTA_IMAGENS, "grade-ag.png"))
        desenha_convergencia(historico, "Convergência do AG (%s)" % nome,
                             100 / (100 + OTIMO) if modo == "enunciado" else None,
                             os.path.join(PASTA_IMAGENS, "convergencia.png"))
        plt.show()

    elif opcao == "2":
        grade = grade_oficial(disciplinas, oficial)
        fitness, conta = avalia(grade, disciplinas, indisponivel, modo)
        print("\ngrade oficial 2026/2: fitness %.4f   penalidade %d" % (fitness, round(100 / fitness - 100)))
        mostra_conta(conta)
        desenha_grade(grade, disciplinas, indisponivel, "Grade oficial 2026/2 (UTFPR-SH)",
                      "Figura: grade oficial avaliada com a mesma função do AG. Fitness %.4f, penalidade %d. "
                      "Contorno vermelho = conflito hard." % (fitness, round(100 / fitness - 100)), modo,
                      os.path.join(PASTA_IMAGENS, "grade-oficial.png"))
        plt.show()

    elif opcao == "6":
        linhas = le("mutacao.csv")
        if linhas is None:
            print("ainda nao tem resultado salvo. rode antes: python3 comparativo.py mutacao truncamento um_ponto")
            continue
        grafico(tabela(linhas, True), "Taxa de mutação (truncamento + um ponto)",
                os.path.join(PASTA_IMAGENS, "mutacao.png"))
        plt.show()

    elif opcao in ("3", "4"):
        arquivo = "ag_9_configuracoes.csv" if opcao == "3" else "memetico.csv"
        linhas = le(arquivo)
        if linhas is None:
            print("ainda nao tem resultado salvo. rode antes: python3 comparativo.py")
            continue
        if opcao == "4":
            melhor_ag = le("ag_9_configuracoes.csv") or []
            sel, cru = linhas[0]["selecao"], linhas[0]["cruzamento"]
            linhas = [l for l in melhor_ag if l["selecao"] == sel and l["cruzamento"] == cru] + linhas
        resumo = tabela(linhas)
        titulo = "9 configurações do AG (800 gerações)" if opcao == "3" else "AG puro x AG com busca local"
        grafico(resumo, titulo, os.path.join(PASTA_IMAGENS, "comparativo.png" if opcao == "3" else "memetico.png"))
        plt.show()

    elif opcao == "5":
        modo = "artigos" if modo == "enunciado" else "enunciado"
        print("agora o pre-requisito segue a leitura do", modo)

    elif opcao == "0":
        break
