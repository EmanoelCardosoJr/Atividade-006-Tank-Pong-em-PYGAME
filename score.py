import pygame
from config import font_Atari


def display_score(score_value, size, color):
    font = pygame.font.Font(font_Atari, size)
    score = f'{score_value}'
    score_format = font.render(score, True, color)
    return score_format
