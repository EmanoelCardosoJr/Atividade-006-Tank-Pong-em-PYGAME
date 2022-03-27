import pygame


pygame.init()
# screen
screen_width = 700
screen_height = 800
# time
time_text = "5".rjust(3)
time_counter = 5
time_text2 = "5".rjust(3)
time_counter2 = 5
# score
score_p_1 = 0
score_p_2 = 0
font = pygame.font.Font("dependencies/EightBit Atari-Thick.ttf", 34)
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
LIGHT_GREEN = (2, 250, 0)
VIOLET = (2, 9, 250)
# ball
ball_mx = 0
ball_my = 0
ball2_mx = 0
ball2_my = 0
shoot = False
shoot2 = False
hit = False
hit2 = False
timer_on = False
timer_on2 = False
wiggle_cont = 0
wiggle_cont2 = 0
# sounds
BALL_COLLISION_WALLS = "sound/ball_collision.mp3"
TANK_HIT = "sound/cannon_hit.mp3"
TANK_ROTATE = "sound/rotate.mp3"
TANK_SHOOT = "sound/shoot.mp3"
TANK_WALK = "sound/walk.mp3"
cant_go = False
cant_go2 = False
unlock_cont = 0
unlock_cont2 = 0
tank1_index = 0
tank2_index = 0
tank1_x = 30
tank1_y = 350
tank2_x = 740
tank2_y = 350
tank_size = 32