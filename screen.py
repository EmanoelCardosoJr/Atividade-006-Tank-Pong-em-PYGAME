import pygame
from pygame.locals import *
import config
from sys import exit
import ball
conf = config
pygame.init()

screen = pygame.display.set_mode((conf.screen_height, conf.screen_width))
ball1 = ball.create_ball(conf.screen_height+100, conf.screen_width+100)
pygame.time.set_timer(pygame.USEREVENT, 1000)
tank_sprite = "img/player1_05.png"
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
    # Desenho do tanque
    tank = pygame.draw.rect(screen, conf.WHITE, (conf.tank1_speed_x, conf.tank1_speed_y, 15, 15))
    # Desenho das paredes e cenário

    pygame.draw.line(screen, conf.YELLOW, (0, 60), (0, 670), 20)  # Parede esquerda

    pygame.draw.line(screen, conf.YELLOW, (800, 60), (800, 670), 25)  # Parede direita

    pygame.draw.line(screen, conf.YELLOW, (0, 700), (800, 700), 80)  # Chão

    pygame.draw.line(screen, conf.YELLOW, (0, 60), (800, 60), 20)  # Teto

    pygame.draw.rect(screen, conf.YELLOW, (385, 621, 35, 40))  # Bloco do meio baixo

    pygame.draw.rect(screen, conf.YELLOW, (385, 71, 35, 40))  # Bloco do meio cima

    pygame.draw.rect(screen, conf.YELLOW, (125, 160, 70, 25))  # Bloco superior esquerda

    pygame.draw.rect(screen, conf.YELLOW, (595, 160, 70, 25))  # Bloco superior direito

    pygame.draw.rect(screen, conf.YELLOW, (125, 525, 70, 25))  # Bloco inferior esquerdo

    pygame.draw.rect(screen, conf.YELLOW, (595, 525, 70, 25))  # Bloco inferior esquerdo

    pygame.draw.rect(screen, conf.YELLOW, (555, 335, 40, 40))  # Bloco direito

    pygame.draw.rect(screen, conf.YELLOW, (200, 335, 40, 40))  # Bloco esquerdo

    pygame.draw.rect(screen, conf.YELLOW, (110, 255, 25, 200))  # Poste da tabala esquerda
    pygame.draw.rect(screen, conf.YELLOW, (80, 255, 30, 25))
    pygame.draw.rect(screen, conf.YELLOW, (80, 430, 30, 25))

    pygame.draw.rect(screen, conf.YELLOW, (270, 215, 70, 25))  # Bloco meio superior esquerdo
    pygame.draw.rect(screen, conf.YELLOW, (270, 235, 25, 25))

    pygame.draw.rect(screen, conf.YELLOW, (270, 455, 70, 25))  # Bloco meio inferior esquerdo
    pygame.draw.rect(screen, conf.YELLOW, (270, 435, 25, 25))

    pygame.draw.rect(screen, conf.YELLOW, (655, 255, 30, 200))  # Poste da tabela direita
    pygame.draw.rect(screen, conf.YELLOW, (685, 255, 30, 25))
    pygame.draw.rect(screen, conf.YELLOW, (685, 430, 30, 25))

    pygame.draw.rect(screen, conf.YELLOW, (460, 215, 70, 25))  # Bloco meio superior direito
    pygame.draw.rect(screen, conf.YELLOW, (505, 235, 25, 25))

    pygame.draw.rect(screen, conf.YELLOW, (460, 455, 70, 25))  # Bloco meio inferior direito
    pygame.draw.rect(screen, conf.YELLOW, (505, 435, 25, 25))

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

    conf.ball_mx, conf.ball_my = ball.limit_wall_collision(ball1, conf.ball_mx, conf.ball_my, conf.screen_width, conf.screen_height)

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

