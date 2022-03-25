from cmath import rect
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

rect1 = Rect((0,0), (200,200))
rect2 = Rect((200,0), (200,200))
rect3 = Rect((400,0), (200,200))
rect4 = Rect((0,200), (200,200))
rect5 = Rect((200,200), (200,200))
rect6 = Rect((400,400), (200,200))
rect7 = Rect((0,400), (200,200))
rect8 = Rect((200,400), (200,200))
rect9 = Rect((400,400), (200,200))

rec = [
    rect1, rect2, rect3, rect4,
    rect5, rect6, rect7, rect8, rect9
]

def desenhar_tabur():
    pygame.draw.line(tela, (255, 255,255), (200, 0), (200, 600), 10)
    pygame.draw.line(tela, (255, 255,255), (400, 0), (400, 600), 10)
    pygame.draw.line(tela, (255, 255,255), (0, 200), (600, 200), 10)
    pygame.draw.line(tela, (255, 255,255), (0, 400), (600, 400), 10)

def desenhar_peca(pos):
    global VEZ
    x, y = pos
    if VEZ == 'JOGADOR1':
        pygame.draw.circle(tela, (0,0,255), pos, 50)
    else:
        img = pygame.image.load('x.png').convert_alpha()
        imgR = pygame.transform.scale(img,(100,100))
        tela.blit(imgR, (x -50, y -50))

def teste_pos():
    for p in rec:
        if e.type == MOUSEBUTTONDOWN and p.collidepoint(mouse_pos):
            if p == rect1:
                desenhar_peca([100,100])

while True:
    mouse_pos = pygame.mouse.get_pos()
    for e in pygame.event.get():
        if e.type == QUIT:
            pygame.quit
            exit()
        if e.type == MOUSEBUTTONDOWN:
            teste_pos()
    desenhar_tabur()
    pygame.display.flip()