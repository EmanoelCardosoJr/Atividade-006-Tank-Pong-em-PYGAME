import config
import pygame
import ball

conf = config
screen = pygame.display.set_mode((conf.screen_height, conf.screen_width))
ball1 = ball.create_ball(conf.screen_height + 100, conf.screen_width + 100)
pygame.time.set_timer(pygame.USEREVENT, 1000)
tank_sprite = "img/player1_05.png"
tank_test = pygame.image.load(tank_sprite)
pygame.display.set_caption('Combat')
clock = pygame.time.Clock()
b = ball



obs1 = pygame.draw.rect(screen, conf.YELLOW, (385, 621, 35, 40))  # Bloco do meio baixo

obs2 = pygame.draw.rect(screen, conf.YELLOW, (385, 71, 35, 40))  # Bloco do meio cima

obs3 = pygame.draw.rect(screen, conf.YELLOW, (125, 160, 70, 25))  # Bloco superior esquerda

obs4 = pygame.draw.rect(screen, conf.YELLOW, (595, 160, 70, 25))  # Bloco superior direito

obs5 = pygame.draw.rect(screen, conf.YELLOW, (125, 525, 70, 25))  # Bloco inferior esquerdo

obs6 = pygame.draw.rect(screen, conf.YELLOW, (595, 525, 70, 25))  # Bloco inferior esquerdo

obs7 = pygame.draw.rect(screen, conf.YELLOW, (555, 335, 40, 40))  # Bloco direito

obs8 = pygame.draw.rect(screen, conf.YELLOW, (200, 335, 40, 40))  # Bloco esquerdo

obs9 = pygame.draw.rect(screen, conf.YELLOW, (110, 255, 25, 200))  # Poste da tabala esquerda
obs10 = pygame.draw.rect(screen, conf.YELLOW, (80, 255, 30, 25))
obs11 = pygame.draw.rect(screen, conf.YELLOW, (80, 430, 30, 25))

obs12 = pygame.draw.rect(screen, conf.YELLOW,
                             (270, 215, 70, 25))  # Bloco meio superior esquerdo
obs13 = pygame.draw.rect(screen, conf.YELLOW, (270, 235, 25, 25))

obs14 = pygame.draw.rect(screen, conf.YELLOW,
                             (270, 455, 70, 25))  # Bloco meio inferior esquerdo
obs15 = pygame.draw.rect(screen, conf.YELLOW, (270, 435, 25, 25))

obs16 = pygame.draw.rect(screen, conf.YELLOW, (655, 255, 30, 200))  # Poste da tabela direita
obs17 = pygame.draw.rect(screen, conf.YELLOW, (685, 255, 30, 25))
obs18 = pygame.draw.rect(screen, conf.YELLOW, (685, 430, 30, 25))

obs19 = pygame.draw.rect(screen, conf.YELLOW, (460, 215, 70, 25))  # Bloco meio superior direito
obs20 = pygame.draw.rect(screen, conf.YELLOW, (505, 235, 25, 25))

obs21 = pygame.draw.rect(screen, conf.YELLOW, (460, 455, 70, 25))  # Bloco meio inferior direito
obs22 = pygame.draw.rect(screen, conf.YELLOW, (505, 435, 25, 25))

obstacles_list = [obs1, obs2, obs3, obs4, obs5, obs6, obs7, obs8, obs9, obs10, obs11, obs12,
                      obs13, obs14, obs15,
                      obs16, obs17, obs18, obs19, obs20, obs21, obs22]
def draw_obstacles():
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

    obs12 = pygame.draw.rect(screen, conf.YELLOW,
                             (270, 215, 70, 25))  # Bloco meio superior esquerdo
    obs13 = pygame.draw.rect(screen, conf.YELLOW, (270, 235, 25, 25))

    obs14 = pygame.draw.rect(screen, conf.YELLOW,
                             (270, 455, 70, 25))  # Bloco meio inferior esquerdo
    obs15 = pygame.draw.rect(screen, conf.YELLOW, (270, 435, 25, 25))

    obs16 = pygame.draw.rect(screen, conf.YELLOW, (655, 255, 30, 200))  # Poste da tabela direita
    obs17 = pygame.draw.rect(screen, conf.YELLOW, (685, 255, 30, 25))
    obs18 = pygame.draw.rect(screen, conf.YELLOW, (685, 430, 30, 25))

    obs19 = pygame.draw.rect(screen, conf.YELLOW, (460, 215, 70, 25))  # Bloco meio superior direito
    obs20 = pygame.draw.rect(screen, conf.YELLOW, (505, 235, 25, 25))

    obs21 = pygame.draw.rect(screen, conf.YELLOW, (460, 455, 70, 25))  # Bloco meio inferior direito
    obs22 = pygame.draw.rect(screen, conf.YELLOW, (505, 435, 25, 25))


