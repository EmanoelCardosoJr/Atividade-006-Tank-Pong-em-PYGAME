import pygame
from pygame.locals import *
from sys import exit
from config_oop import Config

conf = Config()


class Game_Functions:

    def __init__(self):
        # Tela
        pygame.init()
        self.screen = pygame.display.set_mode((conf.screen_height, conf.screen_width))
        pygame.display.set_caption('Combat')
        pygame.time.set_timer(pygame.USEREVENT, 1000)


    def timer(self):
        for event in pygame.event.get():
            if event.type == pygame.USEREVENT:
                conf.time_counter -= 1
                conf.time_text = (
                str(conf.time_counter).rjust(3)
                if conf.time_counter > 0
                else "X"
            )
            if conf.time_text == "X":
                    pygame.display.flip()
                    pygame.time.wait(2000)
                    pygame.quit()
            if event.type == QUIT:
                pygame.quit()
                exit()

    def draw(self):

        self.screen.fill(conf.RED)
        # Desenho do tanque

        pygame.draw.rect(self.screen, conf.WHITE, (conf.tank1_speed_x, conf.tank1_speed_y, 15, 15))

        # Desenho das paredes e cenário

        pygame.draw.line(self.screen, conf.YELLOW, (0, 60), (0, 670), 20)  # Parede esquerda

        pygame.draw.line(self.screen, conf.YELLOW, (800, 60), (800, 670), 25)  # Parede direita

        pygame.draw.line(self.screen, conf.YELLOW, (0, 700), (800, 700), 80)  # Chão

        pygame.draw.line(self.screen, conf.YELLOW, (0, 60), (800, 60), 20)  # Teto

        pygame.draw.rect(self.screen, conf.YELLOW, (385, 621, 35, 40))  # Bloco do meio baixo

        pygame.draw.rect(self.screen, conf.YELLOW, (385, 71, 35, 40))  # Bloco do meio cima

        pygame.draw.rect(self.screen, conf.YELLOW, (125, 160, 70, 25))  # Bloco superior esquerda

        pygame.draw.rect(self.screen, conf.YELLOW, (595, 160, 70, 25))  # Bloco superior direito

        pygame.draw.rect(self.screen, conf.YELLOW, (125, 525, 70, 25))  # Bloco inferior esquerdo

        pygame.draw.rect(self.screen, conf.YELLOW, (595, 525, 70, 25))  # Bloco inferior esquerdo

        pygame.draw.rect(self.screen, conf.YELLOW, (555, 335, 40, 40))  # Bloco direito

        pygame.draw.rect(self.screen, conf.YELLOW, (200, 335, 40, 40))  # Bloco esquerdo

        pygame.draw.rect(self.screen, conf.YELLOW, (110, 255, 25, 200))  # Poste da tabala esquerda
        pygame.draw.rect(self.screen, conf.YELLOW, (80, 255, 30, 25))
        pygame.draw.rect(self.screen, conf.YELLOW, (80, 430, 30, 25))

        pygame.draw.rect(self.screen, conf.YELLOW, (270, 215, 70, 25))  # Bloco meio superior esquerdo
        pygame.draw.rect(self.screen, conf.YELLOW, (270, 235, 25, 25))

        pygame.draw.rect(self.screen, conf.YELLOW, (270, 455, 70, 25))  # Bloco meio inferior esquerdo
        pygame.draw.rect(self.screen, conf.YELLOW, (270, 435, 25, 25))

        pygame.draw.rect(self.screen, conf.YELLOW, (655, 255, 30, 200))  # Poste da tabela direita
        pygame.draw.rect(self.screen, conf.YELLOW, (685, 255, 30, 25))
        pygame.draw.rect(self.screen, conf.YELLOW, (685, 430, 30, 25))

        pygame.draw.rect(self.screen, conf.YELLOW, (460, 215, 70, 25))  # Bloco meio superior direito
        pygame.draw.rect(self.screen, conf.YELLOW, (505, 235, 25, 25))

        pygame.draw.rect(self.screen, conf.YELLOW, (460, 455, 70, 25))  # Bloco meio inferior direito
        pygame.draw.rect(self.screen, conf.YELLOW, (505, 435, 25, 25))

        if pygame.key.get_pressed()[K_w]:
                conf.tank1_speed_y -= 1
        if pygame.key.get_pressed()[K_s]:
                conf.tank1_speed_y += 1
        if pygame.key.get_pressed()[K_a]:
                conf.tank1_speed_x -= 1
        if pygame.key.get_pressed()[K_d]:
                conf.tank1_speed_x += 1

        # Colisão das paredes

        pygame.display.update()

#def slide_show(self):
