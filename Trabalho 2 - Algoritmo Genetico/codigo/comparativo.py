# comparativo das estrategias, no protocolo do artigo da UFPB (Santos, 2016):
# 3 selecoes x 3 cruzamentos = 9 configuracoes. A UFPB rodou uma vez cada; aqui cada
# configuracao roda com 30 sementes diferentes (igual aos 30 mapas do trabalho 1),
# porque o AG e aleatorio e uma execucao so nao diz qual estrategia e melhor.
#
# rodar: python3 comparativo.py                                  (AG puro, 9 configuracoes)
#        python3 comparativo.py memetico truncamento um_ponto    (com busca local)
#        python3 comparativo.py mutacao truncamento um_ponto     (taxas de mutacao 1%, 2% e 5%)
# os resultados ficam salvos em ../resultados/*.csv

import csv
import os
import sys
import time
from multiprocessing import Pool
from dados import carrega
from genetico import Problema, executa, SELECOES, CRUZAMENTOS
from busca_local import subida_de_encosta
import random

PASTA = os.path.dirname(os.path.abspath(__file__))
PASTA_RESULTADOS = os.path.join(PASTA, "..", "resultados")
SEMENTES = 30
GERACOES = 800
OTIMO = 60   # menor penalidade possivel, provada pelo solver exato (exato.py)


# busca local em 10% dos filhos, em 4 genes sorteados
def memetico(problema, filho):
    if random.random() < 0.1:
        subida_de_encosta(problema, filho, 4)


def uma_execucao(tarefa):
    selecao, cruzamento, usa_busca_local, semente, taxa_mutacao = tarefa
    disciplinas, fixas, indisponivel, oficial = carrega()
    problema = Problema(disciplinas, indisponivel)
    inicio = time.time()
    melhor, nota, geracao, historico = executa(problema, selecao, cruzamento, geracoes=GERACOES,
                                               busca_local=memetico if usa_busca_local else None,
                                               taxa_mutacao=taxa_mutacao, semente=semente)
    penalidade = round(100 / nota - 100)
    return [selecao, cruzamento, usa_busca_local, taxa_mutacao, semente, penalidade, geracao,
            round(time.time() - inicio, 1)]


def roda(tarefas, arquivo):
    os.makedirs(PASTA_RESULTADOS, exist_ok=True)
    caminho = os.path.join(PASTA_RESULTADOS, arquivo)
    with Pool() as pool:
        linhas = pool.map(uma_execucao, tarefas)
    with open(caminho, "w") as f:
        w = csv.writer(f)
        w.writerow(["selecao", "cruzamento", "busca_local", "taxa_mutacao", "semente", "penalidade",
                    "geracao_do_melhor", "segundos"])
        w.writerows(linhas)
    return caminho


def le(arquivo):
    caminho = os.path.join(PASTA_RESULTADOS, arquivo)
    if not os.path.exists(caminho):
        return None
    with open(caminho) as f:
        return list(csv.DictReader(f))


# tabela no terminal: media, melhor, pior penalidade e quantas vezes chegou no otimo
def tabela(linhas, por_taxa=False):
    grupos = {}
    for l in linhas:
        nome = "%s + %s%s" % (l["selecao"], l["cruzamento"].replace("_", " "), " + busca local" if l["busca_local"] == "True" else "")
        if por_taxa:
            nome = "mutação %s%%" % round(float(l["taxa_mutacao"]) * 100)
        grupos.setdefault(nome, []).append(l)
    print("\n%-38s %7s %6s %6s %8s %9s %7s" % ("configuracao", "media", "melhor", "pior", "otimo", "geracao", "tempo"))
    resumo = []
    for nome, g in grupos.items():
        pen = [int(l["penalidade"]) for l in g]
        ger = [int(l["geracao_do_melhor"]) for l in g]
        seg = [float(l["segundos"]) for l in g]
        otimos = sum(1 for p in pen if p == OTIMO)
        media = sum(pen) / len(pen)
        print("%-38s %7.1f %6d %6d %5d/%-2d %9.0f %6.0fs" % (nome, media, min(pen), max(pen), otimos, len(pen),
                                                             sum(ger) / len(ger), sum(seg) / len(seg)))
        resumo.append((nome, pen))
    return resumo


def grafico(resumo, titulo, arquivo):
    import matplotlib.pyplot as plt
    plt.rcParams["font.family"] = ["DejaVu Sans"]
    resumo = sorted(resumo, key=lambda r: sum(r[1]) / len(r[1]))
    fig, ax = plt.subplots(figsize=(9, 0.45 * len(resumo) + 1.6))
    ax.boxplot([r[1] for r in resumo], vert=False, widths=0.55,
               medianprops={"color": "#D55E00", "linewidth": 2})
    ax.set_yticks(range(1, len(resumo) + 1))
    ax.set_yticklabels([r[0] for r in resumo])
    ax.axvline(OTIMO, color="#0072B2", linestyle="--", linewidth=1.2, label="ótimo (solver exato) = %d" % OTIMO)
    ax.set_xlabel("penalidade do melhor indivíduo (menor = melhor), %d sementes" % SEMENTES)
    ax.grid(axis="x", color="#DDDDDD", linewidth=0.6)
    ax.legend(loc="lower right", frameon=True, edgecolor="black")
    ax.set_title(titulo, fontsize=11)
    fig.tight_layout()
    fig.savefig(arquivo, dpi=150)
    return fig


if __name__ == "__main__":
    modo = sys.argv[1] if len(sys.argv) > 1 else "ag"
    if modo == "ag":
        tarefas = [(s, c, False, semente, 0.02) for s in SELECOES for c in CRUZAMENTOS for semente in range(SEMENTES)]
        print(roda(tarefas, "ag_9_configuracoes.csv"))
    elif modo == "mutacao":
        selecao, cruzamento = sys.argv[2], sys.argv[3]
        tarefas = [(selecao, cruzamento, False, semente, taxa) for taxa in (0.01, 0.02, 0.05) for semente in range(SEMENTES)]
        print(roda(tarefas, "mutacao.csv"))
    else:
        selecao, cruzamento = sys.argv[2], sys.argv[3]
        tarefas = [(selecao, cruzamento, True, semente, 0.02) for semente in range(SEMENTES)]
        print(roda(tarefas, "memetico.csv"))
