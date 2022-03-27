import pygame
from config import Config
conf = Config()


def display_score(score_value, size, color):
    font = pygame.font.Font(conf.font_Atari, size)
    score = f'{score_value}'
    score_format = font.render(score, True, color)
    return score_format
