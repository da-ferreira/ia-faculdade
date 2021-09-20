
from No import *
import numpy as np
import random
import math

def minimax(noh, profundidade,ehJogadorMaximizador):
	ehNoTerminal = noh.estado.funcaoObjetivo()

	if profundidade == 0 or ehNoTerminal:
		if ehNoTerminal:
			if noh.estado.jogadorVenceu(noh.estado.tabuleiro,noh.estado.pecaIA):
				return (None, 100000000000000)
			elif noh.estado.jogadorVenceu(noh.estado.tabuleiro,noh.estado.pecaHumano):
				return (None, -10000000000000)
			else: #p jogo acabou
				return (None, 0)
		else: #profundidade eh zero
			return (None, noh.calculaHeuristica(noh.estado.tabuleiro,noh.estado.pecaIA))
	
	if ehJogadorMaximizador:
		jogadasValidas = noh.estado.funcaoSucessora(noh.estado.pecaIA)
		valor = -math.inf
		melhorJogada = No(random.choice(jogadasValidas))
		for jogada in jogadasValidas:	
			novoNo = No(Estado(jogada))		
			_,novaPontuacao = minimax(novoNo, profundidade-1, False)
			if novaPontuacao > valor:
				valor = novaPontuacao
				melhorJogada  = novoNo
		return melhorJogada , valor

	else: #jogador Minimizador
		jogadasValidas = noh.estado.funcaoSucessora(noh.estado.pecaHumano)
		valor= math.inf
		melhorJogada = No(random.choice(jogadasValidas))
		for jogada in jogadasValidas:
		    novoNo = No(Estado(jogada))	
		    _,novaPontuacao = minimax(novoNo, profundidade-1, True)
		    if novaPontuacao < valor:
		    	valor = novaPontuacao
		    	melhorJogada  = novoNo
		return melhorJogada , valor
		  