# Lista 3 - Questao 1a
# conta quantas partidas diferentes existem no jogo da velha
# a partida acaba quando alguem fecha uma linha ou o tabuleiro enche

linhas = [(0, 1, 2), (3, 4, 5), (6, 7, 8),   # linhas
          (0, 3, 6), (1, 4, 7), (2, 5, 8),   # colunas
          (0, 4, 8), (2, 4, 6)]              # diagonais


def alguem_ganhou(tabuleiro):
    for a, b, c in linhas:
        if tabuleiro[a] != " " and tabuleiro[a] == tabuleiro[b] == tabuleiro[c]:
            return True
    return False


def conta_partidas(tabuleiro, vez):
    if alguem_ganhou(tabuleiro) or " " not in tabuleiro:
        return 1
    total = 0
    for casa in range(9):
        if tabuleiro[casa] == " ":
            tabuleiro[casa] = vez
            total += conta_partidas(tabuleiro, "O" if vez == "X" else "X")
            tabuleiro[casa] = " "   # desfaz a jogada
    return total


print("partidas possiveis:", conta_partidas([" "] * 9, "X"))
print("limite 9! =", 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1)
