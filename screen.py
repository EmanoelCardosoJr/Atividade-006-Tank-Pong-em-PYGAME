import pygame
from pygame.locals import *
from sys import exit

screen = pygame.display.set_mode((weight , width))  # Não esquecer de importar as variaveis do config
pygame.display.set_caption('Combat')

pygame.init()
while True:
    screen.fill()  # Ainda temos que decidir se vamos importar uma imagem ou pintá-la
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.display.update()
