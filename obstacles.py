from pygame import K_a, K_d, K_LEFT, K_RIGHT

import tank
import config
import pygame

conf = config
Tank = tank.Tank()


class Obstacles:
    def __init__(self):
        self.screen_dimensions = pygame.display.set_mode(
            (conf.screen_height, conf.screen_width)
        )
        self.unlock_cont = 0
        self.unlock_cont2 = 0

    def draw_obstacles(self):

        pygame.draw.line(
            self.screen_dimensions, conf.YELLOW, (0, 60), (0, 670), 20
        )  # Left wall

        pygame.draw.line(
            self.screen_dimensions, conf.YELLOW, (800, 60), (800, 670), 25
        )  # Right wall

        pygame.draw.line(
            self.screen_dimensions, conf.YELLOW, (0, 700), (800, 700), 80
        )  # Floor

        pygame.draw.line(
            self.screen_dimensions, conf.YELLOW, (0, 60), (800, 60), 20
        )  # Ceiling
        #
        obs1 = pygame.draw.rect(
            self.screen_dimensions, conf.YELLOW, (385, 621, 35, 40)
        )  # Down middle block

        obs2 = pygame.draw.rect(
            self.screen_dimensions, conf.YELLOW, (385, 71, 35, 40)
        )  # Up middle block

        obs3 = pygame.draw.rect(
            self.screen_dimensions, conf.YELLOW, (125, 160, 70, 25)
        )  # Up left block

        obs4 = pygame.draw.rect(
            self.screen_dimensions, conf.YELLOW, (595, 160, 70, 25)
        )  # Up right block

        obs5 = pygame.draw.rect(
            self.screen_dimensions, conf.YELLOW, (125, 525, 70, 25)
        )  # Down right block

        obs6 = pygame.draw.rect(
            self.screen_dimensions, conf.YELLOW, (595, 525, 70, 25)
        )  # Down left block

        obs7 = pygame.draw.rect(
            self.screen_dimensions, conf.YELLOW, (555, 335, 40, 40)
        )  # Right block

        obs8 = pygame.draw.rect(
            self.screen_dimensions, conf.YELLOW, (200, 335, 40, 40)
        )  # Left block

        obs9 = pygame.draw.rect(
            self.screen_dimensions, conf.YELLOW, (110, 255, 25, 200)
        )
        obs10 = pygame.draw.rect(
            self.screen_dimensions, conf.YELLOW, (80, 255, 30, 25)
        )
        obs11 = pygame.draw.rect(
            self.screen_dimensions, conf.YELLOW, (80, 430, 30, 25)
        )

        obs12 = pygame.draw.rect(
            self.screen_dimensions, conf.YELLOW, (270, 215, 70, 25)
        )  # mid upper left block
        obs13 = pygame.draw.rect(
            self.screen_dimensions, conf.YELLOW, (270, 235, 25, 25)
        )

        obs14 = pygame.draw.rect(
            self.screen_dimensions, conf.YELLOW, (270, 455, 70, 25)
        )  # mid lower left block
        obs15 = pygame.draw.rect(
            self.screen_dimensions, conf.YELLOW, (270, 435, 25, 25)
        )

        obs16 = pygame.draw.rect(
            self.screen_dimensions, conf.YELLOW, (655, 255, 30, 200)
        )
        obs17 = pygame.draw.rect(
            self.screen_dimensions, conf.YELLOW, (685, 255, 30, 25)
        )
        obs18 = pygame.draw.rect(
            self.screen_dimensions, conf.YELLOW, (685, 430, 30, 25)
        )

        obs19 = pygame.draw.rect(
            self.screen_dimensions, conf.YELLOW, (460, 215, 70, 25)
        )  # mid upper right block
        obs20 = pygame.draw.rect(
            self.screen_dimensions, conf.YELLOW, (505, 235, 25, 25)
        )

        obs21 = pygame.draw.rect(
            self.screen_dimensions, conf.YELLOW, (460, 455, 70, 25)
        )  # mid upper right block
        obs22 = pygame.draw.rect(
            self.screen_dimensions, conf.YELLOW, (505, 435, 25, 25)
        )

        obstacles_list = [
            obs1,
            obs2,
            obs3,
            obs4,
            obs5,
            obs6,
            obs7,
            obs8,
            obs9,
            obs10,
            obs11,
            obs12,
            obs13,
            obs14,
            obs15,
            obs16,
            obs17,
            obs18,
            obs19,
            obs20,
            obs21,
            obs22,
        ]
        return obstacles_list

    def cant_go(self):
        if conf.cant_go:
            if pygame.key.get_pressed()[K_a] or pygame.key.get_pressed()[K_d]:
                self.unlock_cont += 1
            if self.unlock_cont > 4:
                conf.cant_go = False
                self.unlock_cont = 0

    def cant_go2(self):
        if conf.cant_go2:
            if (
                pygame.key.get_pressed()[K_LEFT]
                or pygame.key.get_pressed()[K_RIGHT]
            ):
                self.unlock_cont2 += 1
            if self.unlock_cont2 > 4:
                conf.cant_go2 = False
                self.unlock_cont2 = 0

    def obstacle_collision(self, tank1_rect, tank2_rect, obstacles_list):
        for obs in obstacles_list:
            self.cant_go()
            self.cant_go2()
            if obs.colliderect(tank1_rect):
                conf.cant_go = True
            if obs.colliderect(tank2_rect):
                conf.cant_go2 = True
