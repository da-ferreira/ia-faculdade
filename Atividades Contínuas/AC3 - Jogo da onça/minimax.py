
from no import No
from estado import Estado
import random
import math

def mini_max_poda_alfa_beta(no, profundidade, alfa, beta, onca_ou_cachorros):  # Cachorros == 0, Onça == 1
    eh_no_terminal = no.estado.funcaoObjetivo()

    if profundidade == 0 or eh_no_terminal:
        if eh_no_terminal:
            if no.estado.oncaVenceu():
                return (None, -math.inf)
            
            if no.estado.cachorrosVenceram():
                return (None, math.inf)
        else:
            return (None, no.heuristica(onca_ou_cachorros))

    if onca_ou_cachorros == 0:  # Maximizador
        jogadas_validas = no.estado.funcaoSucessora(onca_ou_cachorros)
        valor = -math.inf
        melhor_jogada = No(random.choice(jogadas_validas))

        for jogada in jogadas_validas:
            novo_no = No(Estado(jogada))
            _, nova_pontuacao = mini_max_poda_alfa_beta(novo_no, profundidade - 1, alfa, beta, onca_ou_cachorros=1)

            if nova_pontuacao > valor:
                valor = nova_pontuacao
                melhor_jogada = novo_no

            alfa = max(alfa, valor)

            if alfa >= beta:
                break

        return melhor_jogada, valor

    else:  # Minimizador
        jogadas_validas = no.estado.funcaoSucessora(onca_ou_cachorros)
        valor = math.inf
        melhor_jogada = No(random.choice(jogadas_validas))

        for jogada in jogadas_validas:
            novo_no = No(Estado(jogada))
            _, nova_pontuacao = mini_max_poda_alfa_beta(novo_no, profundidade - 1, alfa, beta, onca_ou_cachorros=0)

            if nova_pontuacao < valor:
                valor = nova_pontuacao
                melhor_jogada = novo_no

            beta = min(beta, valor)

            if alfa >= beta:
                break

        return melhor_jogada, valor            


if __name__ == "__main__":
    jogo = No(Estado())
    novoJogo, minimax_score = mini_max_poda_alfa_beta(jogo, 5, -math.inf, math.inf, 0)
    jogo = novoJogo

    jogo.printTabuleiro()