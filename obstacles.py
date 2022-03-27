from pygame import K_a, K_d, K_LEFT, K_RIGHT

import config
import pygame
from random import randint

conf = config
screen = pygame.display.set_mode((conf.screen_height, conf.screen_width))











def draw_obstacles(screen):
    pygame.draw.line (
        screen, conf.YELLOW, (0, 60), (0, 670), 20
    )  # Parede esquerda

    pygame.draw.line (
        screen, conf.YELLOW, (800, 60), (800, 670), 25
    )  # Parede direita

    pygame.draw.line (screen, conf.YELLOW, (0, 700), (800, 700), 80)  # Chão

    pygame.draw.line (screen, conf.YELLOW, (0, 60), (800, 60), 20)  # Teto
    #

    obs1 = pygame.draw.rect (screen, conf.YELLOW, (385, 621, 35, 40))  # Bloco do meio baixo

    obs2 = pygame.draw.rect (screen, conf.YELLOW, (385, 71, 35, 40))  # Bloco do meio cima

    obs3 = pygame.draw.rect (screen, conf.YELLOW, (125, 160, 70, 25))  # Bloco superior esquerda

    obs4 = pygame.draw.rect (screen, conf.YELLOW, (595, 160, 70, 25))  # Bloco superior direito

    obs5 = pygame.draw.rect (screen, conf.YELLOW, (125, 525, 70, 25))  # Bloco inferior esquerdo

    obs6 = pygame.draw.rect (screen, conf.YELLOW, (595, 525, 70, 25))  # Bloco inferior esquerdo

    obs7 = pygame.draw.rect (screen, conf.YELLOW, (555, 335, 40, 40))  # Bloco direito

    obs8 = pygame.draw.rect (screen, conf.YELLOW, (200, 335, 40, 40))  # Bloco esquerdo

    obs9 = pygame.draw.rect (screen, conf.YELLOW, (110, 255, 25, 200))  # Poste da tabala esquerda
    obs10 = pygame.draw.rect (screen, conf.YELLOW, (80, 255, 30, 25))
    obs11 = pygame.draw.rect (screen, conf.YELLOW, (80, 430, 30, 25))

    obs12 = pygame.draw.rect (screen, conf.YELLOW,
                              (270, 215, 70, 25))  # Bloco meio superior esquerdo
    obs13 = pygame.draw.rect (screen, conf.YELLOW, (270, 235, 25, 25))

    obs14 = pygame.draw.rect (screen, conf.YELLOW,
                              (270, 455, 70, 25))  # Bloco meio inferior esquerdo
    obs15 = pygame.draw.rect (screen, conf.YELLOW, (270, 435, 25, 25))

    obs16 = pygame.draw.rect (screen, conf.YELLOW, (655, 255, 30, 200))  # Poste da tabela direita
    obs17 = pygame.draw.rect (screen, conf.YELLOW, (685, 255, 30, 25))
    obs18 = pygame.draw.rect (screen, conf.YELLOW, (685, 430, 30, 25))

    obs19 = pygame.draw.rect (screen, conf.YELLOW,
                              (460, 215, 70, 25))  # Bloco meio superior direito
    obs20 = pygame.draw.rect (screen, conf.YELLOW, (505, 235, 25, 25))

    obs21 = pygame.draw.rect (screen, conf.YELLOW,
                              (460, 455, 70, 25))  # Bloco meio inferior direito
    obs22 = pygame.draw.rect (screen, conf.YELLOW, (505, 435, 25, 25))

    obstacles_list = [obs1, obs2, obs3, obs4, obs5, obs6, obs7, obs8, obs9, obs10, obs11, obs12,
                      obs13, obs14, obs15,
                      obs16, obs17, obs18, obs19, obs20, obs21, obs22]
    return obstacles_list


def obstacle_collision(tank1_rect, tank2_rect, ball1, ball2, obstacles_list):
    for obs in obstacles_list:
        if conf.cant_go:
            if pygame.key.get_pressed()[K_a] or pygame.key.get_pressed()[K_d]:
                conf.unlock_cont += 1
            if conf.unlock_cont > 4:
                conf.cant_go = False
                conf.unlock_cont = 0
        if obs.colliderect(tank1_rect):
            conf.cant_go = True
        if conf.cant_go2:
            if (
                pygame.key.get_pressed()[K_LEFT]
                or pygame.key.get_pressed()[K_RIGHT]
            ):
                conf.unlock_cont2 += 1
            if conf.unlock_cont2 > 4:
                conf.cant_go2 = False
                conf.unlock_cont2 = 0
        if obs.colliderect(tank2_rect):
            conf.cant_go2 = True
        if obs.colliderect(ball1):
            if conf.ball_my == 0:
                conf.ball_my = 5 if randint(1, 3) == 1 else 5
            if conf.ball_mx == 0:
                conf.ball_mx = 5 if randint(1, 3) == 1 else 5
            conf.ball_mx *= -1
            conf.wiggle_cont += 1
            if conf.wiggle_cont > 5:
                conf.ball_my *= -1
                conf.ball_mx *= -1 if randint(1, 3) == 1 else 1
                conf.wiggle_cont = 0
        if obs.colliderect(ball2):
            if conf.ball2_my == 0:
                conf.ball2_my = 5 if randint(1, 3) == 1 else 5
            if conf.ball2_mx == 0:
                conf.ball2_mx = 5 if randint(1, 3) == 1 else 5
            conf.ball2_mx *= -1
            conf.wiggle_cont2 += 1
            if conf.wiggle_cont2 > 5:
                conf.ball2_my *= -1
                conf.wiggle_cont2 = 0

