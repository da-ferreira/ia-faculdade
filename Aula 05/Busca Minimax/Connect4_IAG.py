
import numpy as np
import random
import pygame
import sys
import math

from No import *
from Estado import *
#from MiniMax import *
from MiniMaxAlphaBeta import *

BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)

ROW_COUNT = 6
COLUMN_COUNT = 7

PLAYER = 0
AI = 1

tab = Estado()
jogo = No(tab)

jogo.printTabuleiro()
game_over = False

pygame.init()

SQUARESIZE = 100

width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT+1) * SQUARESIZE

size = (width, height)

RADIUS = int(SQUARESIZE/2 - 5)

def draw_board(jogo):
	for c in range(COLUMN_COUNT):
		for r in range(ROW_COUNT):
			pygame.draw.rect(screen, BLUE, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
			pygame.draw.circle(screen, BLACK, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)
	
	for c in range(COLUMN_COUNT):
		for r in range(ROW_COUNT):		
			if jogo.estado.tabuleiro[r][c] == jogo.estado.pecaHumano:
				pygame.draw.circle(screen, RED, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
			elif jogo.estado.tabuleiro[r][c] == jogo.estado.pecaIA: 
				pygame.draw.circle(screen, YELLOW, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
	pygame.display.update()

screen = pygame.display.set_mode(size)
draw_board(jogo)
pygame.display.update()

myfont = pygame.font.SysFont("monospace", 75)

turn = random.randint(PLAYER, AI)

while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
            posx = event.pos[0]
            if turn == PLAYER:
                pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE/2)), RADIUS)

        pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
            if turn == PLAYER:
                posx = event.pos[0]
                col = int(math.floor(posx/SQUARESIZE))

                if jogo.ehUmaPosicaoValida(col):
                    jogo.liberaPeca(jogo.estado.tabuleiro, col, jogo.estado.pecaHumano)

                    if jogo.estado.jogadorVenceu(jogo.estado.tabuleiro, jogo.estado.pecaHumano):
                        label = myfont.render("Voce Venceu!!", 1, RED)
                        screen.blit(label, (40,10))
                        game_over = True

                    turn += 1
                    turn = turn % 2

                    jogo.printTabuleiro()
                    draw_board(jogo)



    if turn == AI and not game_over:
        novoJogo, minimax_score = minimax(jogo, 6, -math.inf, math.inf,True)   # Minimax alphabeta
        #novoJogo, minimax_score = minimax(jogo, 4, True)

        jogo = novoJogo
        
        if jogo.estado.jogadorVenceu(jogo.estado.tabuleiro, jogo.estado.pecaIA):
            label = myfont.render("Eu Venci!!", 1, YELLOW)
            screen.blit(label, (40,10))
            game_over = True

        jogo.printTabuleiro()
        draw_board(jogo)

        turn += 1
        turn = turn % 2

    if game_over:
        pygame.time.wait(3000)