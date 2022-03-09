import pygame

pygame.init()
#screen
screen_width = 700
screen_height = 800
#time
time_counter = "2".rjust(3)
time_text = 2
#score
score_p_1 = 0
score_p_2 = 0
font = pygame.font.Font("dependencies/EightBit Atari-Thick.ttf", 34)
#tank constants
tank1_speed_x = 45
tank1_speed_y = 350
GREEN = (0, 50, 0)
RED = (130, 0, 0)
BLUE = (0, 0, 100)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (250, 150, 0)