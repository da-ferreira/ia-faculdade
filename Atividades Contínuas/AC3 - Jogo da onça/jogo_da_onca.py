
import math

from no import No
from estado import Estado
from minimax import mini_max_poda_alfa_beta

jogo = No(Estado())
jogo.printTabuleiro()

turno = 0

while True:
    if turno == 0:
        jogada = input("Escolha linha e coluna: ")
        
        posicao_onca = jogo.estado.pegaPosicaoOnca()
        jogo.estado.tabuleiro[posicao_onca][0] = 'o'
        jogo.estado.tabuleiro[jogada][0] = 'C'
    else:
        novo_jogo, minimax_score = mini_max_poda_alfa_beta(jogo, 4, -math.inf, math.inf, 1)
        jogo = novo_jogo

    jogo.printTabuleiro()
    turno = 1 - turno
    
