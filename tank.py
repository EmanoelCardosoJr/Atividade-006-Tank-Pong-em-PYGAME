import pygame
from pygame.locals import *
GREEN = (0, 50, 0)
RED = (130, 0, 0)
BLUE = (0, 0, 100)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (250, 150, 0)

# Contantes
screen_width, screen_height = 700, 800

# Tela
screen = pygame.display.set_mode((screen_height, screen_width))
pygame.display.set_caption('Combat')

def Create_walls_mode3():
    pygame.draw.line(screen, YELLOW, (0, 60), (0, 670), 20)  # Parede esquerda
    pygame.draw.line(screen, YELLOW, (800, 60), (800, 670), 25)  # Parede direita
    pygame.draw.line(screen, YELLOW, (0, 700), (800, 700), 80)  # Chão
    pygame.draw.line(screen, YELLOW, (0, 60), (800, 60), 20)  # Teto
    pygame.draw.rect(screen, YELLOW, (385, 621, 35, 40))  # Bloco do meio baixo
    pygame.draw.rect(screen, YELLOW, (385, 71, 35, 40))  # Bloco do meio cima
    pygame.draw.rect(screen, YELLOW, (125, 160, 70, 25))  # Bloco superior esquerda
    pygame.draw.rect(screen, YELLOW, (595, 160, 70, 25))  # Bloco superior direito
    pygame.draw.rect(screen, YELLOW, (125, 525, 70, 25))  # Bloco inferior esquerdo
    pygame.draw.rect(screen, YELLOW, (595, 525, 70, 25))  # Bloco inferior esquerdo
    pygame.draw.rect(screen, YELLOW, (555, 335, 40, 40))  # Bloco direito
    pygame.draw.rect(screen, YELLOW, (200, 335, 40, 40))  # Bloco esquerdo
    pygame.draw.rect(screen, YELLOW, (110, 255, 25, 200))  # Poste da tabala esquerda
    pygame.draw.rect(screen, YELLOW, (80, 255, 30, 25))
    pygame.draw.rect(screen, YELLOW, (80, 430, 30, 25))
    pygame.draw.rect(screen, YELLOW, (270, 215, 70, 25))  # Bloco meio superior esquerdo
    pygame.draw.rect(screen, YELLOW, (270, 235, 25, 25))
    pygame.draw.rect(screen, YELLOW, (270, 455, 70, 25))  # Bloco meio inferior esquerdo
    pygame.draw.rect(screen, YELLOW, (270, 435, 25, 25))
    pygame.draw.rect(screen, YELLOW, (655, 255, 30, 200))  # Poste da tabela direita
    pygame.draw.rect(screen, YELLOW, (685, 255, 30, 25))
    pygame.draw.rect(screen, YELLOW, (685, 430, 30, 25))
    pygame.draw.rect(screen, YELLOW, (460, 215, 70, 25))  # Bloco meio superior direito
    pygame.draw.rect(screen, YELLOW, (505, 235, 25, 25))
    pygame.draw.rect(screen, YELLOW, (460, 455, 70, 25))  # Bloco meio inferior direito
    pygame.draw.rect(screen, YELLOW, (505, 435, 25, 25))

class Tank1(pygame.sprite.Sprite()):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('img/player1_00.png'))
        self.sprites.append(pygame.image.load('img/player1_01.png'))
        self.sprites.append(pygame.image.load('img/player1_02.png'))
        self.sprites.append(pygame.image.load('img/player1_03.png'))
        self.sprites.append(pygame.image.load('img/player1_04.png'))
        self.sprites.append(pygame.image.load('img/player1_05.png'))
        self.sprites.append(pygame.image.load('img/player1_06.png'))
        self.sprites.append(pygame.image.load('img/player1_07.png'))
        self.sprites.append(pygame.image.load('img/player1_08.png'))
        self.sprites.append(pygame.image.load('img/player1_09.png'))
        self.sprites.append(pygame.image.load('img/player1_10.png'))
        self.sprites.append(pygame.image.load('img/player1_11.png'))
        self.sprites.append(pygame.image.load('img/player1_12.png'))
        self.sprites.append(pygame.image.load('img/player1_13.png'))
        self.sprites.append(pygame.image.load('img/player1_14.png'))
        self.sprites.append(pygame.image.load('img/player1_15.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (32, 32))
        self.rect = self.image.get_rect()
        self.topleft = 100, 100

    def update(self):
        if self.index_list > 15:
            self.index_list = 0
        self.index_list += 0.25
        self.image = self.image_tank1[int(self.index_list)]

all_sprites = pygame.sprite.Group()
player1 = Tank1()
all_sprites.add(player1)

pygame.init()
while True:
    screen.fill(RED)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    # Desenho das paredes e cenário
    Create_walls_mode3()

    # Desenho do tanque
    all_sprites.draw(screen)
    all_sprites.update()

    pygame.display.flip()
