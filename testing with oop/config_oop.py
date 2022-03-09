import pygame
pygame.init()

class Config:

    def __init__(self):
        # screen
        self.screen_width = 700
        self.screen_height = 800
        #time
        self.time_text = "2".rjust(3)
        self.time_counter = 2
        #score
        self.score_p_1 = 0
        self.score_p_2 = 0
        #font
        self.font = pygame.font.Font("dependencies/EightBit Atari-Thick.ttf", 34)
        #tank constants
        self.tank1_speed_x = 45
        self.tank1_speed_y = 350
        self.GREEN = (0, 50, 0)
        self.RED = (130, 0, 0)
        self.BLUE = (0, 0, 100)
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.YELLOW = (250, 150, 0)
