import pygame
from pygame.locals import *
from sys import exit

pygame.init()

tela = pygame.display.set_mode((600, 600), 0, 32)
pygame.display.set_caption('Jogo da velha')

ESTADO = 'JOGANDO'
VEZ = 'JOGADOR1'
ESCOLHA = 'X'

marca_tabu = [
    0, 1, 2,
    3, 4, 5,
    6, 7, 8
]

def desenhar_tabur():
    pygame.draw.line(tela, (255, 255,255), (200, 0), (200, 600), 10)
    pygame.draw.line(tela, (255, 255,255), (400, 0), (400, 600), 10)
    pygame.draw.line(tela, (255, 255,255), (0, 200), (600, 200), 10)
    pygame.draw.line(tela, (255, 255,255), (0, 400), (600, 400), 10)

while True:
    for e in pygame.event.get():
        if e.type == QUIT:
            pygame.quit
            exit()
    desenhar_tabur()
    pygame.display.flip()