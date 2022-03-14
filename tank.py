import pygame
from pygame.locals import *
from sys import exit
screen_width, screen_height = 700, 800
tank_size = 32



# Tela
screen = pygame.display.set_mode((screen_height, screen_width))
pygame.display.set_caption('Combat')



pygame.init()

# lista dos tanques
tank1_index = 0
tank2_index = 0

# Posição dos tanques:
tank1_x = 30
tank1_y = 350
tank2_x = 740
tank2_y = 350
def add_tank1 (tank1_index, tank1_x, tank1_y):
    p1_img0 = pygame.image.load('img/player1_00.png')
    p1_img1 = pygame.image.load('img/player1_01.png')
    p1_img2 = pygame.image.load('img/player1_02.png')
    p1_img3 = pygame.image.load('img/player1_03.png')
    p1_img4 = pygame.image.load('img/player1_04.png')
    p1_img5 = pygame.image.load('img/player1_05.png')
    p1_img6 = pygame.image.load('img/player1_06.png')
    p1_img7 = pygame.image.load('img/player1_07.png')
    p1_img8 = pygame.image.load('img/player1_08.png')
    p1_img9 = pygame.image.load('img/player1_09.png')
    p1_img10 = pygame.image.load('img/player1_10.png')
    p1_img11 = pygame.image.load('img/player1_11.png')
    p1_img12 = pygame.image.load('img/player1_12.png')
    p1_img13 = pygame.image.load('img/player1_13.png')
    p1_img14 = pygame.image.load('img/player1_14.png')
    p1_img15 = pygame.image.load('img/player1_15.png')
    player1 = [p1_img0, p1_img1, p1_img2, p1_img3, p1_img4, p1_img5, p1_img6, p1_img7,
               p1_img8, p1_img9, p1_img10, p1_img11, p1_img12, p1_img13, p1_img14, p1_img15]
    player1_img = ['img/player1_00.png', 'img/player1_01.png', 'img/player1_02.png', 'img/player1_03.png', 'img/player1_04.png',
                  'img/player1_05.png', 'img/player1_06.png', 'img/player1_07.png', 'img/player1_08.png', 'img/player1_09.png',
                  'img/player1_10.png', 'img/player1_11.png', 'img/player1_12.png', 'img/player1_13.png', 'img/player1_14.png',
                  'img/player1_15.png']
    screen.blit(player1[int(tank1_index)], (tank1_x, tank1_y))
    return player1_img[tank1_index]

def add_tank2 (tank2_index, tank2_x, tank2_y):

    p2_img0 = pygame.image.load('img/player2_00.png')
    p2_img1 = pygame.image.load('img/player2_01.png')
    p2_img2 = pygame.image.load('img/player2_02.png')
    p2_img3 = pygame.image.load('img/player2_03.png')
    p2_img4 = pygame.image.load('img/player2_04.png')
    p2_img5 = pygame.image.load('img/player2_05.png')
    p2_img6 = pygame.image.load('img/player2_06.png')
    p2_img7 = pygame.image.load('img/player2_07.png')
    p2_img8 = pygame.image.load('img/player2_08.png')
    p2_img9 = pygame.image.load('img/player2_09.png')
    p2_img10 = pygame.image.load('img/player2_10.png')
    p2_img11 = pygame.image.load('img/player2_11.png')
    p2_img12 = pygame.image.load('img/player2_12.png')
    p2_img13 = pygame.image.load('img/player2_13.png')
    p2_img14 = pygame.image.load('img/player2_14.png')
    p2_img15 = pygame.image.load('img/player2_15.png')
    player2 = [p2_img0, p2_img1, p2_img2, p2_img3, p2_img4, p2_img5, p2_img6, p2_img7,
               p2_img8, p2_img9, p2_img10, p2_img11, p2_img12, p2_img13, p2_img14, p2_img15]
    player2_img = ['img/player2_00.png', 'img/player2_01.png', 'img/player2_02.png', 'img/player2_03.png', 'img/player2_04.png',
                  'img/player2_05.png', 'img/player2_06.png', 'img/player2_07.png', 'img/player2_08.png', 'img/player2_09.png',
                  'img/player2_10.png', 'img/player2_11.png', 'img/player2_12.png', 'img/player2_13.png', 'img/player2_14.png',
                  'img/player2_15.png']
    screen.blit(player2[int(tank2_index)], (tank2_x, tank2_y))
    return player2_img[tank2_index]

    # Movimentação tanque 1
    if pygame.key.get_pressed()[K_w]:
        # Esquerda
        if tank1_index == 0:
            tank1_x += 0.27
        # Esquerda baixo
        if tank1_index == 1:
            tank1_x += 0.27
            tank1_y -= 0.2
        if tank1_index == 2:
            tank1_x += 0.27
            tank1_y -= 0.27
        if tank1_index == 3:
            tank1_x += 0.2
            tank1_y -= 0.27
        # Baixo
        if tank1_index == 4:
            tank1_y -= 0.27
        # Baixo direita
        if tank1_index == 5:
            tank1_y -= 0.27
            tank1_x -= 0.2
        if tank1_index == 6:
            tank1_y -= 0.27
            tank1_x -= 0.27
        if tank1_index == 7:
            tank1_y -= 0.2
            tank1_x -= 0.27
        # Direita
        if tank1_index == 8:
            tank1_x -= 0.27
        # Direita cima
        if tank1_index == 9:
            tank1_y += 0.2
            tank1_x -= 0.27
        if tank1_index == 10:
            tank1_y += 0.2
            tank1_x -= 0.27
        if tank1_index == 11:
            tank1_y += 0.27
            tank1_x -= 0.2
        # Encima
        if tank1_index == 12:
            tank1_y += 0.27
        # Esquerda cima
        if tank1_index == 13:
            tank1_x += 0.2
            tank1_y += 0.27
        if tank1_index == 14:
            tank1_x += 0.27
            tank1_y += 0.27
        if tank1_index == 15:
            tank1_x += 0.27
            tank1_y += 0.2

            # Movimentação tanque 2
    if pygame.key.get_pressed()[K_UP]:
        # Esquerda
        if tank2_index == 0:
            tank2_x -= 0.27
        # Esquerda baixo
        if tank2_index == 1:
            tank2_x -= 0.27
            tank2_y += 0.2
        if tank2_index == 2:
            tank2_x -= 0.27
            tank2_y += 0.27
        if tank2_index == 3:
            tank2_x -= 0.2
            tank2_y += 0.27
        # Baixo
        if tank2_index == 4:
            tank2_y += 0.27
        # Baixo direita
        if tank2_index == 5:
            tank2_y += 0.27
            tank2_x += 0.2
        if tank2_index == 6:
            tank2_y += 0.27
            tank2_x += 0.27
        if tank2_index == 7:
            tank2_y += 0.2
            tank2_x += 0.27
        # Direita
        if tank2_index == 8:
            tank2_x += 0.27
        # Direita cima
        if tank2_index == 9:
            tank2_y -= 0.2
            tank2_x += 0.27
        if tank2_index == 10:
            tank2_y -= 0.2
            tank2_x += 0.27
        if tank2_index == 11:
            tank2_y -= 0.27
            tank2_x += 0.2
        # Encima
        if tank2_index == 12:
            tank2_y -= 0.27
        # Esquerda cima
        if tank2_index == 13:
            tank2_x -= 0.2
            tank2_y -= 0.27
        if tank2_index == 14:
            tank2_x -= 0.27
            tank2_y -= 0.27
        if tank2_index == 15:
            tank2_x -= 0.27
            tank2_y -= 0.2



