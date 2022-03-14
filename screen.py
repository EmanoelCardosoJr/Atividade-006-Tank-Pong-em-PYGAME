import pygame
from pygame.locals import *
import config
from sys import exit
import ball
import obstacles
from score import display_score
from random import randint
from config import score_p_1, score_p_2
import tank
conf = config
pygame.init()
Tank = tank

screen = pygame.display.set_mode((conf.screen_height, conf.screen_width))
ball1 = ball.create_ball(Tank.tank1_x, Tank.tank1_y)
ball2 = ball.create_ball(Tank.tank2_x, Tank.tank2_y)
tank1_rect = Tank.create_tank(Tank.tank1_x, Tank.tank1_y, Tank.tank_size)
tank2_rect = pygame.Rect(Tank.tank2_x, Tank.tank2_y, Tank.tank_size, Tank.tank_size)
pygame.time.set_timer(pygame.USEREVENT, 1000)
#tank_sprite = "img/player1_04.png"
cant_go = False
cant_go2 = False
#tank_test = pygame.image.load(tank_sprite)
pygame.display.set_caption('Combat')
clock = pygame.time.Clock()


while True:
    tank1_rect = Tank.create_tank(Tank.tank1_x, Tank.tank1_y, Tank.tank_size)
    tank2_rect = pygame.Rect(Tank.tank2_x, Tank.tank2_y, Tank.tank_size, Tank.tank_size)
    screen.fill(conf.RED)
    #screen.blit(tank_test, (conf.tank_idle_pos_x, conf.tank_idle_pos_y))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if conf.timer_on:
            if event.type == pygame.USEREVENT:
                conf.time_counter -= 1
                conf.time_text = (
                    str(conf.time_counter).rjust(3)
                    if conf.time_counter > 0
                    else "X"
                )
            if conf.time_text == "X":
                conf.ball_mx, conf.ball_my = ball.end_ball(ball1, conf.ball_mx, conf.ball_my)
                conf.shoot = False
                conf.timer_on = False
        else:
            conf.time_text = "5".rjust(3)
            conf.time_counter = 5
        if conf.timer_on2:
            if event.type == pygame.USEREVENT:
                conf.time_counter2 -= 1
                conf.time_text2 = (
                    str(conf.time_counter2).rjust(3)
                    if conf.time_counter2 > 0
                    else "X"
                )
            if conf.time_text2 == "X":
                conf.ball2_mx, conf.ball2_my = ball.end_ball(ball2, conf.ball2_mx, conf.ball2_my)
                conf.shoot2 = False
                conf.timer_on2 = False
        else:
            conf.time_text2 = "5".rjust(3)
            conf.time_counter2 = 5


    # Desenho do tanque


   # tank = pygame.draw.rect(screen, conf.WHITE, (conf.tank1_speed_x, conf.tank1_speed_y, 15, 15))


    # Desenho das paredes e cenário

    pygame.draw.line(screen, conf.YELLOW, (0, 60), (0, 670), 20)  # Parede esquerda

    pygame.draw.line(screen, conf.YELLOW, (800, 60), (800, 670), 25)  # Parede direita

    pygame.draw.line(screen, conf.YELLOW, (0, 700), (800, 700), 80)  # Chão

    pygame.draw.line(screen, conf.YELLOW, (0, 60), (800, 60), 20)  # Teto
    #
    obstacles.draw_obstacles()
    tank_sprite = Tank.add_tank1( Tank.tank1_index,  Tank.tank1_x,  Tank.tank1_y)
    tank2_sprite = Tank.add_tank2( Tank.tank2_index,  Tank.tank2_x,  Tank.tank2_y)
    if conf.ball2_my == 0:
        conf.ball2_my = 5 if randint(1, 3) == 1 else 5
    if conf.ball2_mx == 0:
        conf.ball2_mx = 5 if randint(1, 3) == 1 else 5

    for obs in obstacles.obstacles_list:
        if cant_go:
            if pygame.key.get_pressed()[K_a] or pygame.key.get_pressed()[K_d]:
                conf.unlock_cont += 1
            if conf.unlock_cont > 4:
                cant_go = False
                conf.unlock_cont = 0

        if obs.colliderect(tank1_rect):
            cant_go = True
        if cant_go2:
            if pygame.key.get_pressed()[K_LEFT] or pygame.key.get_pressed()[K_RIGHT]:
                conf.unlock_cont2 += 1
            if conf.unlock_cont2 > 4:
                cant_go2 = False
                conf.unlock_cont2 = 0

        if obs.colliderect(tank2_rect):
            cant_go2 = True

        if obs.colliderect(ball1):
            if conf.ball_my == 0:
                conf.ball_my = 5 if randint(1,3) == 1 else 5
            if conf.ball_mx == 0:
                conf.ball_mx = 5 if randint(1,3) == 1 else 5
            conf.ball_mx *= -1
            conf.wiggle_cont += 1
            if conf.wiggle_cont >5:
                conf.ball_my *= -1
                conf.ball_mx *= -1  if randint(1,3) == 1 else 1
                conf.wiggle_cont = 0


        if obs.colliderect(ball2):
            if conf.ball2_my == 0:
                conf.ball2_my = 5 if randint(1,3) == 1 else 5
            if conf.ball2_mx == 0:
                conf.ball2_mx = 5 if randint(1,3) == 1 else 5
            conf.ball2_mx *= -1
            conf.wiggle_cont2 += 1
            if conf.wiggle_cont2 > 5:
                conf.ball2_my *= -1
                conf.wiggle_cont2 = 0

    # colisão e movimento da bola

    if conf.timer_on:
        ball.move_ball(ball1, conf.ball_mx, conf.ball_my)
    if conf.timer_on2:
        ball.move_ball(ball2, conf.ball2_mx, conf.ball2_my)
    if conf.shoot:
        conf.ball_mx, conf.ball_my = ball.shoot(ball1, tank_sprite, Tank.tank1_x+25/2, Tank.tank1_y+28/2, conf.ball_mx, conf.ball_my)
        conf.timer_on = True
        conf.shoot = False
    if conf.hit:
        conf.ball_mx, conf.ball_my = ball.end_ball(ball1, conf.ball_mx, conf.ball_my)
        conf.timer_on = False
        conf.hit = False
    if conf.shoot2:
        conf.ball2_mx, conf.ball2_my = ball.shoot(ball2, tank2_sprite, Tank.tank2_x+25/2, Tank.tank2_y+28/2, conf.ball2_mx, conf.ball2_my)
        conf.timer_on2 = True
        conf.shoot2 = False
    if conf.hit2:
        conf.ball2_mx, conf.ball2_my = ball.end_ball(ball2, conf.ball2_mx, conf.ball2_my)
        conf.timer_on2 = False
        conf.hit2 = False
    # ball collision with wall
    conf.ball_mx, conf.ball_my = ball.limit_wall_collision(ball1, conf.ball_mx, conf.ball_my, conf.screen_width, conf.screen_height)
    conf.ball2_mx, conf.ball2_my = ball.limit_wall_collision(ball2, conf.ball2_mx, conf.ball2_my,
                                                           conf.screen_width, conf.screen_height)
    # ball collision with tank rect
    if tank2_rect.colliderect(ball1):
        # use whatever tank collision functions with the ball you have here
        conf.ball_mx, conf.ball_my = ball.end_ball(ball1, conf.ball_mx, conf.ball_my)

        score_p_1 += 1
        hit = pygame.mixer.Sound(conf.TANK_HIT)
        pygame.mixer.Sound.play(hit)
        hit.set_volume(0.1)
    if tank1_rect.colliderect(ball2):
        # use whatever tank collision functions with the ball you have here
        # change tank
        hit = pygame.mixer.Sound(conf.TANK_HIT)
        pygame.mixer.Sound.play(hit)
        conf.ball2_mx, conf.ball2_my = ball.end_ball(ball2, conf.ball2_mx, conf.ball2_my)
        score_p_2 += 1


    # keyboard inputs
    if pygame.key.get_pressed()[K_r]:
        conf.hit = True
    if pygame.key.get_pressed()[K_t]:
        conf.hit2 = True
    if pygame.key.get_pressed()[K_c]:
        shoot = pygame.mixer.Sound(conf.TANK_SHOOT)
        pygame.mixer.Sound.play(shoot)
        shoot.set_volume(0.05)
        if conf.timer_on:
            conf.shoot = conf.shoot
        else:
            conf.shoot = True
    if pygame.key.get_pressed()[K_v]:
        shoot = pygame.mixer.Sound(conf.TANK_SHOOT)
        pygame.mixer.Sound.play(shoot)
        shoot.set_volume(0.05)
        if conf.timer_on2:
            conf.shoot2 = conf.shoot2
        else:
            conf.shoot2 = True

    if pygame.key.get_pressed()[K_a]:
        rotate = pygame.mixer.Sound(conf.TANK_ROTATE)
        pygame.mixer.Sound.play(rotate)
        rotate.set_volume(0.1)
        Tank.tank1_index -= 1
        if Tank.tank1_index < 0:
            Tank.tank1_index = 15
    if pygame.key.get_pressed()[K_d]:
        rotate = pygame.mixer.Sound(conf.TANK_ROTATE)
        pygame.mixer.Sound.play(rotate)
        rotate.set_volume(0.1)
        Tank.tank1_index += 1
        if Tank.tank1_index > 15:
            Tank.tank1_index = 0
    if pygame.key.get_pressed()[K_LEFT]:
        rotate = pygame.mixer.Sound(conf.TANK_ROTATE)
        pygame.mixer.Sound.play(rotate)
        rotate.set_volume(0.1)
        Tank.tank2_index -= 1
        if Tank.tank2_index < 0:
            Tank.tank2_index = 15
    if pygame.key.get_pressed()[K_RIGHT]:
        rotate = pygame.mixer.Sound(conf.TANK_ROTATE)
        pygame.mixer.Sound.play(rotate)
        rotate.set_volume(0.1)
        Tank.tank2_index += 1
        if Tank.tank2_index > 15:
            Tank.tank2_index = 0
        # Movimentação tanque 1
    if cant_go:
        conf.shoot = conf.shoot
    else:
        if pygame.key.get_pressed()[K_w]:
            walk = pygame.mixer.Sound(conf.TANK_WALK)
            pygame.mixer.Sound.play(walk)
            walk.set_volume(0.1)
            # Esquerda
            if Tank.tank1_index == 0:
                Tank.tank1_x += 0.27
            # Esquerda baixo
            if Tank.tank1_index == 1:
                Tank.tank1_x += 0.27
                Tank.tank1_y -= 0.2
            if Tank.tank1_index == 2:
                Tank.tank1_x += 0.27
                Tank.tank1_y -= 0.27
            if Tank.tank1_index == 3:
                Tank.tank1_x += 0.2
                Tank.tank1_y -= 0.27
            # Baixo
            if Tank.tank1_index == 4:
                Tank.tank1_y -= 0.27
            # Baixo direita
            if Tank.tank1_index == 5:
                Tank.tank1_y -= 0.27
                Tank.tank1_x -= 0.2
            if Tank.tank1_index == 6:
                Tank.tank1_y -= 0.27
                Tank.tank1_x -= 0.27
            if Tank.tank1_index == 7:
                Tank.tank1_y -= 0.2
                Tank.tank1_x -= 0.27
            # Direita
            if Tank.tank1_index == 8:
                Tank.tank1_x -= 0.27
            # Direita cima
            if Tank.tank1_index == 9:
                Tank.tank1_y += 0.2
                Tank.tank1_x -= 0.27
            if Tank.tank1_index == 10:
                Tank.tank1_y += 0.2
                Tank.tank1_x -= 0.27
            if Tank.tank1_index == 11:
                Tank.tank1_y += 0.27
                Tank.tank1_x -= 0.2
            # Encima
            if Tank.tank1_index == 12:
                Tank.tank1_y += 0.27
            # Esquerda cima
            if Tank.tank1_index == 13:
                Tank.tank1_x += 0.2
                Tank.tank1_y += 0.27
            if Tank.tank1_index == 14:
                Tank.tank1_x += 0.27
                Tank.tank1_y += 0.27
            if Tank.tank1_index == 15:
                Tank.tank1_x += 0.27
                Tank.tank1_y += 0.2

            # Movimentação tanque 2
    if cant_go2:
        conf.shoot = conf.shoot
    else:
        if pygame.key.get_pressed()[K_UP]:
            walk = pygame.mixer.Sound(conf.TANK_WALK)
            pygame.mixer.Sound.play(walk)
            walk.set_volume(0.1)
            # Esquerda
            if Tank.tank2_index == 0:
                Tank.tank2_x -= 0.27
            # Esquerda baixo
            if Tank.tank2_index == 1:
                Tank.tank2_x -= 0.27
                Tank.tank2_y += 0.2
            if Tank.tank2_index == 2:
                Tank.tank2_x -= 0.27
                Tank.tank2_y += 0.27
            if Tank.tank2_index == 3:
                Tank.tank2_x -= 0.2
                Tank.tank2_y += 0.27
            # Baixo
            if Tank.tank2_index == 4:
                Tank.tank2_y += 0.27
            # Baixo direita
            if Tank.tank2_index == 5:
                Tank.tank2_y += 0.27
                Tank.tank2_x += 0.2
            if Tank.tank2_index == 6:
                Tank.tank2_y += 0.27
                Tank.tank2_x += 0.27
            if Tank.tank2_index == 7:
                Tank.tank2_y += 0.2
                Tank.tank2_x += 0.27
            # Direita
            if Tank.tank2_index == 8:
                Tank.tank2_x += 0.27
            # Direita cima
            if Tank.tank2_index == 9:
                Tank.tank2_y -= 0.2
                Tank.tank2_x += 0.27
            if Tank.tank2_index == 10:
                Tank.tank2_y -= 0.2
                Tank.tank2_x += 0.27
            if Tank.tank2_index == 11:
                Tank.tank2_y -= 0.27
                Tank.tank2_x += 0.2
            # Encima
            if Tank.tank2_index == 12:
                Tank.tank2_y -= 0.27
            # Esquerda cima
            if Tank.tank2_index == 13:
                Tank.tank2_x -= 0.2
                Tank.tank2_y -= 0.27
            if Tank.tank2_index == 14:
                Tank.tank2_x -= 0.27
                Tank.tank2_y -= 0.27
            if Tank.tank2_index == 15:
                Tank.tank2_x -= 0.27
                Tank.tank2_y -= 0.2

    # score
    score_1 = display_score(score_p_1, 40, (141, 197, 80))
    score_2 = display_score(score_p_2, 40, (78, 89, 221))

    screen.blit(score_1, (180, 0.5))
    screen.blit(score_2, (580, 0.5))

    if conf.timer_on:
        ball.draw_ball(screen, conf.LIGHT_GREEN, ball1)
    if conf.timer_on2:
        ball.draw_ball(screen, conf.VIOLET, ball2)

    pygame.display.flip()
    pygame.display.update()
    clock.tick(60)

