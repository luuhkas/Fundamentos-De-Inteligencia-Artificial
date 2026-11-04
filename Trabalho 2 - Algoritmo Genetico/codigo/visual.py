# figuras: a grade dos 4 periodos e a curva de convergencia do AG
# mesmas cores do trabalho 1

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from dados import DIAS, AULAS, nome_slot

plt.rcParams["font.family"] = ["DejaVu Sans"]
plt.rcParams["toolbar"] = "None"

# cores mais claras pra dar pra ler o texto em cima
CORES = ["#9BC9E8", "#F7C58A", "#9FD9C4", "#F5EE9A", "#C9A9DB", "#F2B59A"]
CONFLITO = "#D55E00"   # vermelho dos conflitos
TEXTO = "#1A1A1A"
CINZA = "#555555"


# celulas (codigo, slot) que estao em conflito com alguma restricao hard
def celulas_em_conflito(grade, disciplinas, indisponivel, modo):
    ruins = set()
    por_id = {d.id_ppc: d for d in disciplinas}
    for d in disciplinas:
        for s in grade[d.codigo]:
            for outra in disciplinas:
                if outra is d or s not in grade[outra.codigo]:
                    continue
                if outra.periodo == d.periodo or set(outra.professores) & set(d.professores):
                    ruins.add((d.codigo, s))
            for p in d.professores:
                if s in indisponivel.get(p, set()):
                    ruins.add((d.codigo, s))
            if s in indisponivel.get("periodo %d" % d.periodo, set()):
                ruins.add((d.codigo, s))
        if modo == "enunciado":
            for id_pre in d.pre:
                pre = por_id.get(id_pre)
                if pre is None:
                    continue
                for s in set(grade[d.codigo]) & set(grade[pre.codigo]):
                    ruins.add((d.codigo, s))
                    ruins.add((pre.codigo, s))
    return ruins


def desenha_grade(grade, disciplinas, indisponivel, titulo, legenda, modo="enunciado", arquivo=None):
    ruins = celulas_em_conflito(grade, disciplinas, indisponivel, modo)
    fig, eixos = plt.subplots(1, 4, figsize=(17, 6.2))
    fig.patch.set_facecolor("white")
    for periodo, ax in zip(range(1, 5), eixos):
        do_periodo = [d for d in disciplinas if d.periodo == periodo]
        # aula de horario fixo (Projeto Integrador I)
        for s in indisponivel.get("periodo %d" % periodo, set()):
            dia, aula = s // 10, s % 10
            linha = aula if aula < 5 else aula + 0.4
            ax.add_patch(Rectangle((dia, linha), 1, 1, facecolor="#EEEEEE", edgecolor="white",
                                   hatch="///", linewidth=1, zorder=0.5))
            ax.text(dia + 0.5, linha + 0.5, "PI-I (fixo)", ha="center", va="center", fontsize=7, color=CINZA)
        for i, d in enumerate(do_periodo):
            for s in grade[d.codigo]:
                dia, aula = s // 10, s % 10
                linha = aula if aula < 5 else aula + 0.4   # espaco do almoco entre M5 e T1
                borda = CONFLITO if (d.codigo, s) in ruins else "white"
                largura = 2.5 if (d.codigo, s) in ruins else 1
                ax.add_patch(Rectangle((dia, linha), 1, 1, facecolor=CORES[i % len(CORES)],
                                       edgecolor=borda, linewidth=largura, zorder=largura))
                ax.text(dia + 0.5, linha + 0.36, d.codigo, ha="center", va="center", fontsize=7.5, color=TEXTO)
                ax.text(dia + 0.5, linha + 0.70, d.professores[0].split()[0].capitalize(),
                        ha="center", va="center", fontsize=6.5, color=CINZA)
        ax.set_xlim(0, 5)
        ax.set_ylim(10.4, 0)
        ax.set_xticks([x + 0.5 for x in range(5)])
        ax.set_xticklabels(DIAS)
        ax.xaxis.tick_top()
        ax.set_yticks([a + 0.5 if a < 5 else a + 0.9 for a in range(10)])
        ax.set_yticklabels(AULAS)
        ax.tick_params(length=0)
        ax.set_title("%do período" % periodo, fontsize=11, pad=22)
        for lado in ax.spines.values():
            lado.set_color("#999999")
    fig.suptitle(titulo, fontsize=13, y=0.99)
    fig.text(0.5, 0.02, legenda, ha="center", fontsize=9.5, color=TEXTO, wrap=True)
    fig.subplots_adjust(left=0.03, right=0.99, top=0.86, bottom=0.10, wspace=0.18)
    if arquivo:
        fig.savefig(arquivo, dpi=150)
    return fig


def desenha_convergencia(historico, titulo, otimo=None, arquivo=None):
    fig, ax = plt.subplots(figsize=(8, 4.5))
    melhor = [h[0] for h in historico]
    media = [h[1] for h in historico]
    ax.plot(media, color="#56B4E9", linewidth=1, label="média da população")
    ax.plot(melhor, color="#0072B2", linewidth=2, label="melhor indivíduo")
    if otimo is not None:
        ax.axhline(otimo, color=CONFLITO, linestyle="--", linewidth=1.2, label="ótimo (solver exato)")
    ax.set_xlabel("geração")
    ax.set_ylabel("fitness = 100 / (100 + penalidades)")
    ax.set_ylim(0, 1.02)
    ax.grid(color="#DDDDDD", linewidth=0.6)
    ax.legend(loc="lower right", frameon=True, edgecolor="black")
    for lado in ax.spines.values():
        lado.set_color("black")
    ax.set_title(titulo, fontsize=11)
    fig.tight_layout()
    if arquivo:
        fig.savefig(arquivo, dpi=150)
    return fig


def imprime_grade(grade, disciplinas):
    for periodo in range(1, 5):
        print("\n%do periodo" % periodo)
        for d in disciplinas:
            if d.periodo == periodo:
                print("  %-8s %-16s %s" % (d.codigo, d.professores[0],
                                           ", ".join(nome_slot(s) for s in sorted(grade[d.codigo]))))
