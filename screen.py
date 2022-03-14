import pygame
from pygame.locals import *
import config
from sys import exit
import ball
import obstacles
from random import randint
conf = config
pygame.init()

screen = pygame.display.set_mode((conf.screen_height, conf.screen_width))
ball1 = ball.create_ball(conf.screen_height+100, conf.screen_width+100)
pygame.time.set_timer(pygame.USEREVENT, 1000)
tank_sprite = "img/player1_06.png"
tank_test = pygame.image.load(tank_sprite)
pygame.display.set_caption('Combat')
clock = pygame.time.Clock()


while True:
    screen.fill(conf.RED)
    screen.blit(tank_test, (conf.tank_idle_pos_x, conf.tank_idle_pos_y))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if conf.timer_on:
                if event.type == pygame.USEREVENT:
                    conf.time_counter -= 0
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


    # Desenho do tanque


    tank = pygame.draw.rect(screen, conf.WHITE, (conf.tank1_speed_x, conf.tank1_speed_y, 15, 15))


    # Desenho das paredes e cenário

    pygame.draw.line(screen, conf.YELLOW, (0, 60), (0, 670), 20)  # Parede esquerda

    pygame.draw.line(screen, conf.YELLOW, (800, 60), (800, 670), 25)  # Parede direita

    pygame.draw.line(screen, conf.YELLOW, (0, 700), (800, 700), 80)  # Chão

    pygame.draw.line(screen, conf.YELLOW, (0, 60), (800, 60), 20)  # Teto
    #
    obstacles.draw_obstacles()

    for obs in obstacles.obstacles_list:
        if obs.colliderect(ball1):
                conf.ball_mx *= -1 if randint(-3, 3) > 0 else 1
                conf.ball_my *= -1 if randint(-3, 3) > 0 else 1


    # colisão e movimento da bola

    ball.move_ball(ball1, conf.ball_mx, conf.ball_my)
    if conf.shoot:
        conf.ball_mx, conf.ball_my = ball.shoot(ball1, tank_sprite, conf.tank_idle_pos_x+25/2, conf.tank_idle_pos_y+28/2, conf.ball_mx, conf.ball_my)
        conf.timer_on = True
        conf.shoot = False
    if conf.hit:
        conf.ball_mx, conf.ball_my = ball.end_ball(ball1, conf.ball_mx, conf.ball_my)
        conf.timer_on = False
        conf.hit = False
    # ball collision with wall
    conf.ball_mx, conf.ball_my = ball.limit_wall_collision(ball1, conf.ball_mx, conf.ball_my, conf.screen_width, conf.screen_height)
    # ball collision with tank rect
    if tank.colliderect(ball1):
        # use whatever tank collision functions with the ball you have here
        conf.hit = True
    # keyboard inputs
    if pygame.key.get_pressed()[K_w]:

        conf.tank1_speed_y -= 1
        conf.hit = True
    if pygame.key.get_pressed()[K_s]:
        conf.tank1_speed_y += 1

    if pygame.key.get_pressed()[K_c]:
        if conf.timer_on:
            conf.shoot = conf.shoot
        else:
            conf.shoot = True

    if pygame.key.get_pressed()[K_a]:
        conf.tank1_speed_x -= 1
    if pygame.key.get_pressed()[K_d]:
        conf.tank1_speed_x += 1


    ball.draw_ball(screen, conf.WHITE, ball1)
    pygame.display.flip()
    pygame.display.update()
    clock.tick(60)

