import pygame
import config
conf = config


class Score:
    def __init__(self):
        pygame.init()
        self.font = pygame.font.Font("dependencies/EightBit Atari-Thick.ttf", 34)
        self.font_Atari = "dependencies/EightBit Atari-Thick.ttf"

    def display_score(self, score_value, size, color):
        font = pygame.font.Font(self.font_Atari, size)
        score = f'{score_value}'
        score_format = font.render(score, True, color)
        return score_format
