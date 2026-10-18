# Trabalho 1 - Busca: interface com painel de botoes
# o mesmo programa do main.py, mas tudo e escolhido clicando (painel no estilo do PathFinding.js)
# textos e figuras seguem as convencoes do artigo do RMA*: legenda "Figura 1:" embaixo,
# que descreve a figura e traz o resultado; rotulos em frase normal, sem caixa alta
# clicar numa celula do mapa escolhe o destino; as tabelas continuam saindo no terminal
# rodar de dentro da pasta codigo: python3 painel.py

import os
import textwrap
import matplotlib.pyplot as plt
from matplotlib.widgets import Button, RadioButtons
from mapa import Mapa, usa_heuristica, VALOR_RECOMPENSA
from gerador import gera_mapa
from visual import desenha_mapa, legenda, anima, FUNDO, TEXTO, CINZA, ROTA
from comparativo import ALGORITMOS, tabela, grafico, compara_heuristicas, compara_aleatorios

PASTA = os.path.dirname(os.path.abspath(__file__))
PASTA_MAPAS = os.path.join(PASTA, "..", "mapas")
PASTA_IMAGENS = os.path.join(PASTA, "..", "imagens")
MAPAS = sorted(os.listdir(PASTA_MAPAS)) + ["aleatorio"]
NOMES = [nome for nome, _ in ALGORITMOS]

estado = {"indice_mapa": 0, "ocupado": False}

fig = plt.figure(figsize=(15, 8.4), facecolor=FUNDO)
fig.canvas.manager.set_window_title("Trabalho 1 - Busca")
titulo = fig.text(0.03, 0.945, "", fontsize=16, color=TEXTO)
info = fig.text(0.03, 0.905, "", fontsize=12, color=TEXTO)
ax = fig.add_axes([0.03, 0.17, 0.68, 0.67])
# legenda de figura embaixo do mapa, como no artigo: descreve a figura e traz o resultado
rodape = fig.text(0.03, 0.012, "", fontsize=10, color=TEXTO, va="bottom", linespacing=1.4)


def legenda_figura(texto):
    # quebra na largura do mapa, pra nao passar por baixo do painel
    estado["legenda"] = texto
    rodape.set_text(textwrap.fill(texto, 130))


def mostra(texto_titulo, texto_info, cor=TEXTO):
    ax.clear()
    estado["moedas"] = desenha_mapa(ax, estado["mapa"], estado["destino"])
    legenda(ax, embaixo=True)
    mapa = estado["mapa"]
    legenda_figura("Figura 1: mapa %s, com %d vértices e %d recompensas. Os pontos azuis são os nós "
                    "expandidos (mais escuros quando expandidos várias vezes) e a linha é a rota do agente."
                    % (estado["nome"], len(mapa.grafo), len(mapa.recompensas)))
    titulo.set_text(texto_titulo)
    info.set_text(texto_info)
    info.set_color(cor)
    fig.canvas.draw_idle()


def carrega_mapa():
    nome = MAPAS[estado["indice_mapa"]]
    if nome == "aleatorio":
        estado["mapa"] = Mapa(linhas=gera_mapa())
    else:
        estado["mapa"] = Mapa(os.path.join(PASTA_MAPAS, nome))
    estado["nome"] = nome.replace(".txt", "")
    estado["destino"] = estado["mapa"].premio
    mostra("Mapa %s" % estado["nome"], "Clique numa célula para mudar o destino e depois em Buscar.")


def heuristica_atual():
    return escolha_heuristica.value_selected.lower()


# ---- o que cada botao faz

def buscar(_):
    if estado["ocupado"]:
        return
    estado["ocupado"] = True
    nome, busca = ALGORITMOS[NOMES.index(escolha_algoritmo.value_selected)]
    rota, ordem, gerados = busca(estado["mapa"], estado["destino"])
    texto = nome
    if nome in ("Gulosa", "A*", "RMA*"):
        texto += " com heurística %s" % heuristica_atual().capitalize()
    mostra(texto, "")
    plt.figure(fig.number)   # a animacao desenha na janela ativa
    anima(estado["mapa"], rota, ordem, estado["destino"], nome, tela=(fig, ax, estado["moedas"], info))
    # completa a legenda da figura com o resultado, como as legendas do artigo
    mapa = estado["mapa"]
    if rota is None:
        resultado = "Não existe caminho até o destino; a busca esgotou a região alcançável com %d nós expandidos." % len(ordem)
    else:
        pegas = len(mapa.coletadas(rota))
        resultado = "Resultado: lucro %+d (custo %d e %d recompensas) com %d nós expandidos." % (
            VALOR_RECOMPENSA * pegas - mapa.custo(rota), mapa.custo(rota), pegas, len(ordem))
    legenda_figura(estado["legenda"] + " " + resultado)
    fig.canvas.draw_idle()
    estado["ocupado"] = False


def troca_heuristica(rotulo):
    usa_heuristica(rotulo.lower())
    info.set_text("Heurística: %s." % rotulo)
    fig.canvas.draw_idle()


def troca_mapa(_):
    if estado["ocupado"]:
        return
    estado["indice_mapa"] = (estado["indice_mapa"] + 1) % len(MAPAS)
    carrega_mapa()


def comparativo(_):
    print("\nmapa %s   heuristica %s" % (estado["nome"], heuristica_atual()))
    resultados = tabela(estado["mapa"], estado["destino"])
    grafico(resultados, os.path.join(PASTA_IMAGENS, "comparativo-%s-%s.png" % (estado["nome"], heuristica_atual())),
            trava=False)


def heuristicas(_):
    print("\nmapa %s" % estado["nome"])
    compara_heuristicas(estado["mapa"], estado["destino"], heuristica_atual(),
                        os.path.join(PASTA_IMAGENS, "heuristicas-%s.png" % estado["nome"]), trava=False)


def aleatorios(_):
    info.set_text("Rodando os 5 algoritmos em 30 mapas aleatórios...")
    fig.canvas.draw()
    fig.canvas.flush_events()
    print()
    medias = compara_aleatorios(30)
    grafico(medias, os.path.join(PASTA_IMAGENS, "comparativo-aleatorios-%s.png" % heuristica_atual()),
            "média dos 5 algoritmos em 30 mapas aleatórios (só os mapas com caminho)", trava=False)
    info.set_text("Resultado no terminal e na janela do gráfico.")
    fig.canvas.draw_idle()


def clique(evento):
    # clicar numa celula do mapa muda o destino
    if estado["ocupado"] or evento.inaxes is not ax or evento.xdata is None:
        return
    no = (int(round(evento.ydata)), int(round(evento.xdata)))
    if no not in estado["mapa"].terreno:
        info.set_text("A célula %s é parede; escolha outra." % (no,))
        info.set_color(ROTA)
        fig.canvas.draw_idle()
        return
    estado["destino"] = no
    mostra("Mapa %s" % estado["nome"], "Destino %s. Clique em Buscar." % (no,))


# ---- painel da direita

def secao(y, texto):
    fig.text(0.755, y, texto, fontsize=12, fontweight="bold", color=TEXTO)


def sem_borda(eixo):
    for borda in eixo.spines.values():
        borda.set_visible(False)


# todos os botoes no visual classico do matplotlib (cinza claro com contorno);
# o de buscar so se diferencia pelo texto em negrito
def botao(y, texto, funcao, destaque=False):
    eixo = fig.add_axes([0.755, y, 0.2, 0.056])
    b = Button(eixo, texto, color="#F2F2F2", hovercolor="#E0E0E0")
    b.label.set_color(TEXTO)
    b.label.set_fontsize(12)
    if destaque:
        b.label.set_fontweight("bold")
    for borda in eixo.spines.values():
        borda.set_color("#999999")
        borda.set_linewidth(0.8)
    b.on_clicked(funcao)
    return b   # precisa guardar o botao numa variavel, senao ele para de responder


secao(0.865, "Algoritmo")
eixo = fig.add_axes([0.75, 0.63, 0.2, 0.23], facecolor=FUNDO)
escolha_algoritmo = RadioButtons(eixo, NOMES, active=len(NOMES) - 1, activecolor=TEXTO,
                                 label_props={"fontsize": [12] * len(NOMES), "color": [TEXTO] * len(NOMES)},
                                 radio_props={"s": [110] * len(NOMES)})
sem_borda(eixo)

secao(0.595, "Heurística")
eixo = fig.add_axes([0.75, 0.48, 0.2, 0.11], facecolor=FUNDO)
escolha_heuristica = RadioButtons(eixo, ["Manhattan", "Euclidiana"], activecolor=TEXTO,
                                  label_props={"fontsize": [12, 12], "color": [TEXTO, TEXTO]},
                                  radio_props={"s": [110, 110]})
escolha_heuristica.on_clicked(troca_heuristica)
sem_borda(eixo)

botoes = [
    botao(0.395, "Buscar", buscar, destaque=True),
    botao(0.325, "Trocar mapa", troca_mapa),
    botao(0.255, "Comparativo", comparativo),
    botao(0.185, "Euclidiana × Manhattan", heuristicas),
    botao(0.115, "30 mapas aleatórios", aleatorios),
]
fig.text(0.755, 0.02, "Clique numa célula do mapa para\ndefinir o destino. As tabelas são\nimpressas no terminal.",
         fontsize=9, color=CINZA, linespacing=1.5, va="bottom")
fig.canvas.mpl_connect("button_press_event", clique)

carrega_mapa()
plt.show()
