# desenha o mapa com matplotlib e anima em duas fases:
#   1. os nos que a busca expandiu, na ordem (quanto mais escuro, mais vezes foi expandido)
#   2. o agente andando na rota e pegando as recompensas

import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap, to_rgb
from matplotlib.lines import Line2D
from matplotlib.patches import Patch
from mapa import CUSTO, VALOR_RECOMPENSA

# visual das figuras do artigo do RMA* (SoCS 2024): padrao do matplotlib (fonte DejaVu Sans,
# fundo branco, eixos nomeados, legenda em caixa) e cores da paleta Okabe-Ito, a mesma do artigo
# terreno com a cor suave do material, indo do claro ao escuro conforme o custo
# (luminosidade L*: plano 98, arenoso 90, rochoso 81, pantano 73)
plt.rcParams["font.family"] = ["DejaVu Sans"]
plt.rcParams["toolbar"] = "None"

FUNDO = "#FFFFFF"
TEXTO = "#1A1A1A"
CINZA = "#555555"
# indice na matriz do mapa: 0 parede, 1 plano, 2 arenoso, 3 rochoso, 4 pantano
SIMBOLOS = ["#", ".", ":", "^", "~"]
CORES = ["#5F5F5F", "#FBFAF7", "#EFE3C4", "#CDC8BF", "#A9B89A"]
NOMES = {".": "plano", ":": "arenoso", "^": "rochoso", "~": "pântano"}
EXPANDIDO = "#0072B2"   # azul Okabe-Ito (no artigo, a cor do metodo dos autores)
ROTA = "#D55E00"        # vermelhao Okabe-Ito
AGENTE = "#1A1A1A"
OURO = "#F0E442"        # amarelo Okabe-Ito (recompensas)

# velocidade da animacao (segundos de espera, fora o tempo de desenhar a tela)
QUADROS_BUSCA = 40      # a busca inteira aparece em uns 40 quadros (~4 s)
ESPERA_PASSO = 0.05     # entre um passo e outro do agente
ESPERA_FASE = 1.0       # entre o fim da busca e o agente comecar a andar
ESPERA_MOEDA = 0.4      # quando o agente pega uma recompensa


def matriz(mapa):
    largura = max(len(linha) for linha in mapa.linhas)
    m = []
    for l in range(len(mapa.linhas)):
        m.append([SIMBOLOS.index(mapa.terreno.get((l, c), "#")) for c in range(largura)])
    return m


# desenha o mapa num eixo: terrenos, grade, coordenadas, recompensas e destino
# (usado pelo modo terminal e pelo painel)
def desenha_mapa(ax, mapa, destino):
    m = matriz(mapa)
    altura, largura = len(m), len(m[0])
    ax.imshow(m, cmap=ListedColormap(CORES), vmin=0, vmax=4)

    # linhas finas entre as celulas pra parecer ladrilho
    ax.set_xticks([x - 0.5 for x in range(largura + 1)], minor=True)
    ax.set_yticks([y - 0.5 for y in range(altura + 1)], minor=True)
    ax.grid(which="minor", color=FUNDO, linewidth=1.5)
    # coordenadas nas bordas pra o usuario digitar o destino
    ax.set_xticks(range(largura))
    ax.set_yticks(range(altura))
    ax.xaxis.tick_top()
    ax.xaxis.set_label_position("top")
    ax.set_xlabel("coluna", fontsize=9, color=TEXTO)
    ax.set_ylabel("linha", fontsize=9, color=TEXTO)
    ax.tick_params(which="both", length=0, labelsize=8, labelcolor=TEXTO)
    for borda in ax.spines.values():
        borda.set_color(TEXTO)
        borda.set_linewidth(0.8)

    # recompensas e destino
    moedas = {}
    for (l, c) in mapa.recompensas:
        # losango, como os marcadores de figura cientifica; fica vazado quando e pego
        moedas[(l, c)] = ax.scatter(c, l, marker="D", s=110, color=OURO, edgecolor="#8C7A2E",
                                    linewidth=1.2, zorder=4)
    # destino marcado com X, como no PythonRobotics e no Red Blob Games
    ax.scatter(destino[1], destino[0], marker="X", s=230, color=AGENTE, edgecolor="white",
               linewidth=1, zorder=4)
    return moedas


# barra de escala do custo do terreno, como a barra de cores de uma figura cientifica:
# mostra que o cinza e uma medida (claro = barato, escuro = caro)
def escala_de_custo(ax, posicao, separador=" "):
    barra = ax.inset_axes(posicao)
    barra.imshow([[1, 2, 3, 4]], cmap=ListedColormap(CORES), vmin=0, vmax=4, aspect="auto")
    barra.set_xticks(range(4))
    barra.set_xticklabels(["%s%s%d" % (NOMES[t], separador, CUSTO[t]) for t in CUSTO], fontsize=8, color=TEXTO)
    barra.set_yticks([])
    barra.tick_params(length=0)
    for borda in barra.spines.values():
        borda.set_color(TEXTO)
        borda.set_linewidth(0.6)
    barra.set_title("custo do terreno", fontsize=8, color=TEXTO, loc="left", pad=3)


# legenda ao lado do mapa (no painel ela fica embaixo, porque o lado e dos botoes)
def legenda(ax, embaixo=False):
    itens = [Patch(color=CORES[0], label="parede")]
    itens.append(Line2D([], [], marker="o", linestyle="", markersize=11, color=AGENTE, label="agente"))
    itens.append(Line2D([], [], marker="D", linestyle="", markersize=8, color=OURO,
                        markeredgecolor="#8C7A2E", label="recompensa (%d)" % VALOR_RECOMPENSA))
    itens.append(Line2D([], [], marker="D", linestyle="", markersize=8, markerfacecolor="none",
                        markeredgecolor="#8C7A2E", label="recompensa pega"))
    itens.append(Line2D([], [], marker="X", linestyle="", markersize=11, color=AGENTE, label="destino"))
    itens.append(Line2D([], [], marker="o", linestyle="", markersize=7, color=EXPANDIDO, label="nó expandido"))
    itens.append(Line2D([], [], color=ROTA, linewidth=3, label="rota"))
    if embaixo:
        escala_de_custo(ax, [0, -0.11, 0.34, 0.045])
        ax.legend(handles=itens, loc="upper left", bbox_to_anchor=(0.36, -0.03), ncol=4,
                  frameon=True, edgecolor="#CCCCCC", labelcolor=TEXTO, fontsize=9,
                  handlelength=1.3, columnspacing=1.4)
    else:
        escala_de_custo(ax, [1.03, 0.87, 0.26, 0.06], separador="\n")
        ax.legend(handles=itens, loc="upper left", bbox_to_anchor=(1.03, 0.72), frameon=True,
                  edgecolor="#CCCCCC", labelcolor=TEXTO, fontsize=10, handlelength=1.4, labelspacing=0.9)


# janela propria do modo terminal: mapa + legenda + titulo + linha de informacao
def desenha_base(mapa, destino, titulo):
    plt.close("all")
    m = matriz(mapa)
    altura, largura = len(m), len(m[0])
    fig, ax = plt.subplots(figsize=(largura * 0.5 + 3.2, max(altura * 0.5 + 1.6, 6)), facecolor=FUNDO)
    fig.subplots_adjust(left=0.04, right=0.76, top=0.84, bottom=0.04)
    moedas = desenha_mapa(ax, mapa, destino)
    legenda(ax)

    fig.text(0.04, 0.94, titulo, fontsize=16, color=TEXTO)
    info = fig.text(0.04, 0.895, "", fontsize=12, color=TEXTO)
    return fig, ax, moedas, info


def tamanho_do_ponto(fig, ax, largura):
    # ponto da busca com 40% do lado da celula, pra nao esconder a cor do terreno
    fig.canvas.draw()
    pixels = ax.get_window_extent().width / largura * 0.4
    return (pixels * 72 / fig.dpi) ** 2


def mostra_mapa(mapa, destino):
    fig, ax, moedas, info = desenha_base(mapa, destino, "Mapa")
    info.set_text("Digite no terminal a coordenada de destino (linha coluna).")
    plt.show(block=False)
    plt.pause(0.1)


# tela = (fig, ax, moedas, info) de uma janela ja aberta (painel); sem tela abre uma nova
def anima(mapa, rota, ordem, destino, nome, tela=None):
    if tela is None:
        fig, ax, moedas, info = desenha_base(mapa, destino, nome)
    else:
        fig, ax, moedas, info = tela
    largura = len(matriz(mapa)[0])
    tamanho = tamanho_do_ponto(fig, ax, largura)
    l0, c0 = mapa.inicio
    halo = ax.scatter(c0, l0, s=900, color=AGENTE, alpha=0.18, linewidths=0, zorder=6)
    agente = ax.scatter(c0, l0, s=380, color=AGENTE, edgecolor="white", linewidth=2, zorder=6)

    # fase 1: busca (pula de varios em varios nos pra caber em QUADROS_BUSCA quadros)
    # cada no vira um ponto, mais forte quanto mais vezes foi expandido (com limite)
    busca = ax.scatter([], [], marker="o", s=tamanho, color=EXPANDIDO, linewidths=0, zorder=2)
    r, g, b = to_rgb(EXPANDIDO)
    vezes = {}
    passo = max(1, len(ordem) // QUADROS_BUSCA)
    for i in range(0, len(ordem), passo):
        for no in ordem[i:i + passo]:
            vezes[no] = vezes.get(no, 0) + 1
        busca.set_offsets([(c, l) for l, c in vezes])
        busca.set_alpha(None)
        busca.set_facecolor([(r, g, b, min(0.45 + 0.1 * v, 0.95)) for v in vezes.values()])
        info.set_text("Buscando... nós expandidos: %d" % min(i + passo, len(ordem)))
        plt.pause(0.03)

    if rota is None:
        info.set_text("Não existe caminho até o destino   ·   nós expandidos: %d." % len(ordem))
        info.set_color(ROTA)
        if tela is None:
            plt.show()
        return

    plt.pause(ESPERA_FASE)

    # fase 2: agente andando (a busca fica mais clara pra rota aparecer)
    busca.set_facecolor([(r, g, b, min(0.12 + 0.03 * v, 0.3)) for v in vezes.values()])
    # rota inteira mais clara e os ultimos passos fortes, pra ver pra onde o agente vai
    linha, = ax.plot([], [], color=ROTA, linewidth=3, alpha=0.4, solid_capstyle="round",
                     solid_joinstyle="round", zorder=3)
    rastro, = ax.plot([], [], color=ROTA, linewidth=4, solid_capstyle="round",
                      solid_joinstyle="round", zorder=3)
    custo = 0
    pegas = []
    for i, no in enumerate(rota):
        if i > 0:
            custo += mapa.grafo[rota[i - 1]][no]
        espera = ESPERA_PASSO
        if no in moedas and no not in pegas:
            pegas.append(no)
            moedas[no].set_facecolor("none")   # recompensa pega fica vazada
            espera = ESPERA_MOEDA
        linha.set_data([c for l, c in rota[:i + 1]], [l for l, c in rota[:i + 1]])
        recente = rota[max(0, i - 6):i + 1]
        rastro.set_data([c for l, c in recente], [l for l, c in recente])
        agente.set_offsets([(no[1], no[0])])
        halo.set_offsets([(no[1], no[0])])
        info.set_text("Passo %d/%d   ·   custo %d   ·   recompensas %d   ·   lucro %+d   ·   nós expandidos %d"
                      % (i, len(rota) - 1, custo, len(pegas), VALOR_RECOMPENSA * len(pegas) - custo, len(ordem)))
        plt.pause(espera)
    # no fim a rota inteira fica forte, porque e a tela que fica parada na explicacao
    linha.set_alpha(1)
    linha.set_linewidth(4)
    rastro.set_data([], [])
    info.set_text(info.get_text() + "   ·   chegou ao destino.")
    if tela is None:
        plt.show()
