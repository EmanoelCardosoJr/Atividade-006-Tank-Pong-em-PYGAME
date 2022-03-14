import pygame

pygame.init()
# screen
screen_width = 700
screen_height = 800
# time
time_text = "5".rjust(3)
time_counter = 5
# score
score_p_1 = 0
score_p_2 = 0
font_Atari = "dependencies/EightBit Atari-Thick.ttf"
# tank
tank1_speed_x = 45
tank1_speed_y = 350
tank_idle_pos_x = 400
tank_idle_pos_y = 400
GREEN = (0, 50, 0)
RED = (130, 0, 0)
BLUE = (0, 0, 100)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (250, 150, 0)
# ball
ball_y = 10
ball_x = 10
ball_mx = 0
ball_my = 0
shoot = False
hit = False
timer_on = False
