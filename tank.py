import pygame
from pygame.locals import *
import config

conf = config

pygame.init()


def create_tank(tank_pos_x, tank_pos_y, tank_size):
    return pygame.Rect(tank_pos_x, tank_pos_y, tank_size, tank_size)


def add_tank1(screen, tank1_index, tank1_x, tank1_y):
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

def add_tank2 (screen, tank2_index, tank2_x, tank2_y):

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

def tank_rect_follow(tankrect, tank_x, tank_y):
    tankrect.x = tank_x
    tankrect.y = tank_y
def tank_input():
    if pygame.key.get_pressed ()[K_r]:
        conf.hit = True
    if pygame.key.get_pressed ()[K_t]:
        conf.hit2 = True
    if pygame.key.get_pressed ()[K_c]:
        #shoot = pygame.mixer.Sound (conf.TANK_SHOOT)
        #pygame.mixer.Sound.play (shoot)
        #shoot.set_volume (0.05)
        if conf.timer_on:
            conf.shoot = conf.shoot
        else:
            conf.shoot = True
    if pygame.key.get_pressed ()[K_v]:
        #shoot = pygame.mixer.Sound (conf.TANK_SHOOT)
        #pygame.mixer.Sound.play (shoot)
        #shoot.set_volume (0.05)
        if conf.timer_on2:
            conf.shoot2 = conf.shoot2
        else:
            conf.shoot2 = True
    if pygame.key.get_pressed ()[K_a]:
        #rotate = pygame.mixer.Sound (conf.TANK_ROTATE)
        #pygame.mixer.Sound.play (rotate)
        #rotate.set_volume (0.1)
        conf.tank1_index -= 1
        if conf.tank1_index < 0:
            conf.tank1_index = 15
    if pygame.key.get_pressed ()[K_d]:
        #rotate = pygame.mixer.Sound (conf.TANK_ROTATE)
        #pygame.mixer.Sound.play (rotate)
        #rotate.set_volume (0.1)
        conf.tank1_index += 1
        if conf.tank1_index > 15:
            conf.tank1_index = 0
    if pygame.key.get_pressed ()[K_LEFT]:
        #rotate = pygame.mixer.Sound (conf.TANK_ROTATE)
        #pygame.mixer.Sound.play (rotate)
        #rotate.set_volume (0.1)
        conf.tank2_index -= 1
        if conf.tank2_index < 0:
            conf.tank2_index = 15
    if pygame.key.get_pressed ()[K_RIGHT]:
        #rotate = pygame.mixer.Sound (conf.TANK_ROTATE)
        #pygame.mixer.Sound.play (rotate)
        #rotate.set_volume (0.1)
        conf.tank2_index += 1
        if conf.tank2_index > 15:
            conf.tank2_index = 0
        # Movimentação tanque 1
    if conf.cant_go:
        conf.shoot = conf.shoot
    else:
        if pygame.key.get_pressed ()[K_w]:
            #walk = pygame.mixer.Sound (conf.TANK_WALK)
            #pygame.mixer.Sound.play (walk)
            #walk.set_volume (0.1)
            # Esquerda
            if conf.tank1_index == 0:
                conf.tank1_x += 0.27
            # Esquerda baixo
            if conf.tank1_index == 1:
                conf.tank1_x += 0.27
                conf.tank1_y -= 0.2
            if conf.tank1_index == 2:
                conf.tank1_x += 0.27
                conf.tank1_y -= 0.27
            if conf.tank1_index == 3:
                conf.tank1_x += 0.2
                conf.tank1_y -= 0.27
            # Baixo
            if conf.tank1_index == 4:
                conf.tank1_y -= 0.27
            # Baixo direita
            if conf.tank1_index == 5:
                conf.tank1_y -= 0.27
                conf.tank1_x -= 0.2
            if conf.tank1_index == 6:
                conf.tank1_y -= 0.27
                conf.tank1_x -= 0.27
            if conf.tank1_index == 7:
                conf.tank1_y -= 0.2
                conf.tank1_x -= 0.27
            # Direita
            if conf.tank1_index == 8:
                conf.tank1_x -= 0.27
            # Direita cima
            if conf.tank1_index == 9:
                conf.tank1_y += 0.2
                conf.tank1_x -= 0.27
            if conf.tank1_index == 10:
                conf.tank1_y += 0.2
                conf.tank1_x -= 0.27
            if conf.tank1_index == 11:
                conf.tank1_y += 0.27
                conf.tank1_x -= 0.2
            # Encima
            if conf.tank1_index == 12:
                conf.tank1_y += 0.27
            # Esquerda cima
            if conf.tank1_index == 13:
                conf.tank1_x += 0.2
                conf.tank1_y += 0.27
            if conf.tank1_index == 14:
                conf.tank1_x += 0.27
                conf.tank1_y += 0.27
            if conf.tank1_index == 15:
                conf.tank1_x += 0.27
                conf.tank1_y += 0.2
            # Movimentação tanque 2
    if conf.cant_go2:
        conf.shoot = conf.shoot
    else:
        if pygame.key.get_pressed ()[K_UP]:
            #walk = pygame.mixer.Sound (conf.TANK_WALK)
            #pygame.mixer.Sound.play (walk)
            #walk.set_volume (0.1)
            # Esquerda
            if conf.tank2_index == 0:
                conf.tank2_x -= 0.27
            # Esquerda baixo
            if conf.tank2_index == 1:
                conf.tank2_x -= 0.27
                conf.tank2_y += 0.2
            if conf.tank2_index == 2:
                conf.tank2_x -= 0.27
                conf.tank2_y += 0.27
            if conf.tank2_index == 3:
                conf.tank2_x -= 0.2
                conf.tank2_y += 0.27
            # Baixo
            if conf.tank2_index == 4:
                conf.tank2_y += 0.27
            # Baixo direita
            if conf.tank2_index == 5:
                conf.tank2_y += 0.27
                conf.tank2_x += 0.2
            if conf.tank2_index == 6:
                conf.tank2_y += 0.27
                conf.tank2_x += 0.27
            if conf.tank2_index == 7:
                conf.tank2_y += 0.2
                conf.tank2_x += 0.27
            # Direita
            if conf.tank2_index == 8:
                conf.tank2_x += 0.27
            # Direita cima
            if conf.tank2_index == 9:
                conf.tank2_y -= 0.2
                conf.tank2_x += 0.27
            if conf.tank2_index == 10:
                conf.tank2_y -= 0.2
                conf.tank2_x += 0.27
            if conf.tank2_index == 11:
                conf.tank2_y -= 0.27
                conf.tank2_x += 0.2
            # Encima
            if conf.tank2_index == 12:
                conf.tank2_y -= 0.27
            # Esquerda cima
            if conf.tank2_index == 13:
                conf.tank2_x -= 0.2
                conf.tank2_y -= 0.27
            if conf.tank2_index == 14:
                conf.tank2_x -= 0.27
                conf.tank2_y -= 0.27
            if conf.tank2_index == 15:
                conf.tank2_x -= 0.27
                conf.tank2_y -= 0.2