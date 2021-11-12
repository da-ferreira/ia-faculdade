
import os
import math
from time import sleep

from no import No
from estado import Estado
from minimax import mini_max_poda_alfa_beta

jogo = No(Estado())

turno = 0
game_over = [False, '']
cachorros_comidos = 0
auxilio_tabuleiro = {"A": "1", "B": "2", "C": "3", "D": "4", "E": "5", "F": "6", "G": "7"}

os.system("cls")

print(" ~> JOGO DA ONÇA <~ ")
print("\n~ A onça (IA) começa jogando. Ela não come em sequência, apenas 1 cachorro por vez. ~ ")
print("~ A onça é representada pela letra maiúscula 'C' e os cachorros por cifrão '$'. ~ ")
input("\nAperte Enter para começar.")

os.system("cls")

jogo.printTabuleiro()
print("\nNúmero de cachorros comidos pela onça: 0")

while not game_over[0]:
    if turno == 1:
        peca = input("\nInforme a linha [A-G] e a coluna [1-5] do cachorro escolhido: ")
        peca = auxilio_tabuleiro[peca[0]] + peca[1]

        jogada = input("Informe a linha [A-G] e a coluna [1-5] para colocar o cachorro: ")
        jogada = auxilio_tabuleiro[jogada[0]] + jogada[1]

        jogo.estado.tabuleiro[peca][0] = 'o'
        jogo.estado.tabuleiro[jogada][0] = '$'

        if jogo.estado.cachorrosVenceram():
            game_over = [True, 'Cachorros']

    else:  # A onça (que é a IA) começa jogando. Ela sempre quer minimizar seu jogo.
        print("\nOnça jogando...")        

        novo_jogo, minimax_score = mini_max_poda_alfa_beta(jogo, 6, -math.inf, math.inf, onca_ou_cachorros=1)
        jogo = novo_jogo

        if jogo.estado.oncaVenceu():
            game_over = [True, 'Onça']

    os.system("cls")
    jogo.printTabuleiro()
    print(f"\nNúmero de cachorros comidos pela onça: {14 - len(jogo.estado.pegaPosicoesCachorros())}")
    turno = 1 - turno

if game_over[1] == 'Onça':
    print("\n -=- Onça venceu -=- \n")
    sleep(5)
else:
    print("\n -=- Cachorros venceram -=- \n")
    sleep(5)
