
from No import *
from Estado import *
from MiniMax import *

import numpy as np

#inicia tabuleiro
tab = Estado()
jogo = No(tab)

jogo.printTabuleiro()
game_over = False

turno = 0

while not game_over:
    #jogada jogador 1
    if turno == 0:
        coluna = int(input("Jogador 1, faca sua jogada (0-6): "))
        #coloca a peca do jogador 1 no tabuleiro
        if jogo.ehUmaPosicaoValida(coluna):
            jogo.liberaPeca(jogo.estado.tabuleiro, coluna, jogo.estado.pecaHumano)
            if jogo.estado.jogadorVenceu(jogo.estado.tabuleiro, jogo.estado.pecaHumano):
                print(">>> Voce VENCEU!! <<<")
                game_over = True

    #jogada jogador 2
    else:
        novoJogo, minimax_score = minimax(jogo, 4, True)

        jogo = novoJogo

        if jogo.estado.jogadorVenceu(jogo.estado.tabuleiro, jogo.estado.pecaIA):
            print(">>> Eu (IA) Venci!!!!! <<<")
            game_over = True

    print()
    jogo.printTabuleiro()
    turno += 1
    turno = turno % 2
