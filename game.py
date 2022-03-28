import pygame
import config
from ball import Ball
from obstacles import Obstacles
from score import Score
from tank import Tank
from timer import Timer

Score = Score()
conf = config
Tank = Tank()
Ball = Ball()
Timer = Timer()
Obstacles = Obstacles()
pygame.init()


class Game:
    def __init__(self):
        self.ball1 = Ball.create_ball(Tank.tank1_x, Tank.tank1_y)
        self.ball2 = Ball.create_ball(Tank.tank2_x, Tank.tank2_y)
        self.tank1 = Tank.create_tank(Tank.tank1_x, Tank.tank1_y)
        self.tank2 = Tank.create_tank(Tank.tank2_x, Tank.tank2_y)
        self.screen = pygame.display.set_mode(
            (conf.screen_height, conf.screen_width)
        )
        pygame.time.set_timer(pygame.USEREVENT, 1000)
        pygame.display.set_caption("Combat")
        self.clock = pygame.time.Clock()

    def main_loop(self):
        while True:
            self.screen.fill(conf.RED)
            self.timer()
            self.ball_definition()
            self.tank_definition()
            self.collisions_and_obstacles()
            self.hud()
            self.screen_update()

    def screen_update(self):
        pygame.display.flip()
        pygame.display.update()
        self.clock.tick(60)

    def hud(self):
        score_1 = Score.display_score(conf.score_p_1, 40, (141, 197, 80))
        score_2 = Score.display_score(conf.score_p_2, 40, (78, 89, 221))
        self.screen.blit(score_1, (180, 0.5))
        self.screen.blit(score_2, (580, 0.5))

    def collisions_and_obstacles(self):
        # ball collision with tank rect
        Ball.ball_collision_with_tank(
            self.tank2, self.ball1, Ball, self.tank1, self.ball2
        )
        # ball collision with wall
        Ball.ball_mx, Ball.ball_my = Ball.limit_wall_collision(
            self.ball1,
            Ball.ball_mx,
            Ball.ball_my,
            conf.screen_width,
            conf.screen_height,
        )
        Ball.ball2_mx, Ball.ball2_my = Ball.limit_wall_collision(
            self.ball2,
            Ball.ball2_mx,
            Ball.ball2_my,
            conf.screen_width,
            conf.screen_height,
        )
        # obstacle collision
        obstacles_list = Obstacles.draw_obstacles()
        Obstacles.obstacle_collision(self.tank1, self.tank2, obstacles_list)
        Ball.ball_collision_with_obstacles(
            obstacles_list, self.ball1, self.ball2
        )
        Tank.tank_collision_with_outer_wall()
        Tank.tank_collision_with_outer_wall_2()

    def ball_definition(self):
        # ball movement and event handling
        # draw ball
        tank_sprite, tank_sprite2 = self.tank_sprites()
        Ball.ball_timer(self.screen, self.ball1, self.ball2)
        Ball.ball_shoot_and_hit(
            self.ball1,
            self.ball2,
            tank_sprite,
            Tank.tank1_x,
            Tank.tank1_y,
            tank_sprite2,
            Tank.tank2_x,
            Tank.tank2_y,
        )
        # ball speed correction
        Ball.speed_correct()

    def tank_definition(self):
        # tank rect position refresh
        self.tank_sprites()
        Tank.tank_rect_follow(self.tank1, Tank.tank1_x, Tank.tank1_y)
        Tank.tank_rect_follow(self.tank2, Tank.tank2_x, Tank.tank2_y)
        # keyboard inputs/tank movement
        Tank.tank_input()

    def tank_sprites(self):
        tank_sprite = Tank.add_tank1(
            self.screen, Tank.tank1_index, Tank.tank1_x, Tank.tank1_y
        )
        tank2_sprite = Tank.add_tank2(
            self.screen, Tank.tank2_index, Tank.tank2_x, Tank.tank2_y
        )
        return tank_sprite, tank2_sprite


    def timer(self):
        # Timer
        Timer.timer(self.ball1, self.ball2)
