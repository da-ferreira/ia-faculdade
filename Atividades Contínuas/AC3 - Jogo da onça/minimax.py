
from no import No
import random
import math

def mini_max_poda_alfa_beta(no, profundidade, alfa, beta, onca_ou_cachorros=0):  # Onca == 0, Cachorros == 1
    eh_no_terminal = no.estado.funcaoObjetivo()

    if profundidade == 0 or eh_no_terminal:
        if eh_no_terminal:
            if no.estado.oncaVenceu():
                return (None, -math.inf)
            
            if no.estado.cachorrosVenceram():
                return (None, math.inf)
        else:
            return (None, no.heuristica(onca_ou_cachorros))

    if onca_ou_cachorros == 0:
        pass
    else:
        pass            
