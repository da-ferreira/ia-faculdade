
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

        if jogo.estado.oncaVenceu():
            print("Onca venceu")
            break

    else:
        novo_jogo, minimax_score = mini_max_poda_alfa_beta(jogo, 5, -math.inf, math.inf, 0)
        jogo = novo_jogo

        if minimax_score == math.inf:
            print("Cachorros venceram")
            break

    print()
    jogo.printTabuleiro()
    turno = 1 - turno
    
jogo.printTabuleiro()
