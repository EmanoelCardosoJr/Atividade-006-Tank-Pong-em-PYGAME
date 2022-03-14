import pygame
from pygame.locals import *
from sys import exit
screen_width, screen_height = 700, 800
tank_size = 32

pos_x = 30
pos_y = 350

# Tela
screen = pygame.display.set_mode((screen_height, screen_width))
pygame.display.set_caption('Combat')

player = pygame.image.load('img/player1_00.png').convert_alpha()


pygame.init()
index = 0

def add_images(index, pos_x, pos_y):
    sprites = []
    sprites.append(pygame.image.load('img/player1_00.png'))
    sprites.append(pygame.image.load('img/player1_01.png'))
    sprites.append(pygame.image.load('img/player1_02.png'))
    sprites.append(pygame.image.load('img/player1_03.png'))
    sprites.append(pygame.image.load('img/player1_04.png'))
    sprites.append(pygame.image.load('img/player1_05.png'))
    sprites.append(pygame.image.load('img/player1_06.png'))
    sprites.append(pygame.image.load('img/player1_07.png'))
    sprites.append(pygame.image.load('img/player1_08.png'))
    sprites.append(pygame.image.load('img/player1_09.png'))
    sprites.append(pygame.image.load('img/player1_10.png'))
    sprites.append(pygame.image.load('img/player1_11.png'))
    sprites.append(pygame.image.load('img/player1_12.png'))
    sprites.append(pygame.image.load('img/player1_13.png'))
    sprites.append(pygame.image.load('img/player1_14.png'))
    sprites.append(pygame.image.load('img/player1_15.png'))
    screen.blit(sprites[int(index)], (pos_x, pos_y))
    return sprites[index]

while True:
    screen.fill((0, 0, 0))


    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                index -= 1
                if index < 0:
                    index = 15
            if event.key == K_RIGHT:
                index += 1
                if index > 15:
                    index = 0



    add_images(int(index), pos_x, pos_y)

    pygame.display.update()
