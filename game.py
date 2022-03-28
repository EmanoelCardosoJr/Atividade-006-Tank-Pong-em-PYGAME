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
        self.ball1 = Ball.create_ball(conf.tank1_x, conf.tank1_y)
        self.ball2 = Ball.create_ball(conf.tank2_x, conf.tank2_y)
        self.tank1 = Tank.create_tank(
            conf.tank1_x, conf.tank1_y, conf.tank_size
        )
        self.tank2 = Tank.create_tank(
            conf.tank2_x, conf.tank2_y, conf.tank_size
        )
        self.screen = pygame.display.set_mode(
            (conf.screen_height, conf.screen_width)
        )
        pygame.time.set_timer(pygame.USEREVENT, 1000)
        pygame.display.set_caption("Combat")
        self.clock = pygame.time.Clock()

    def main_loop(self):
        while True:
            # screen
            self.screen.fill(conf.RED)
            # tank rect position refresh
            Tank.tank_rect_follow(self.tank1, conf.tank1_x, conf.tank1_y)
            Tank.tank_rect_follow(self.tank2, conf.tank2_x, conf.tank2_y)
            # tank sprites
            tank_sprite = Tank.add_tank1(
                self.screen, conf.tank1_index, conf.tank1_x, conf.tank1_y
            )
            tank2_sprite = Tank.add_tank2(
                self.screen, conf.tank2_index, conf.tank2_x, conf.tank2_y
            )
            # draw ball
            Ball.ball_draw(self.screen, self.ball1, self.ball2)
            # Timer
            Timer.timer(self.ball1, self.ball2)
            # wall and obstacles drawing
            obstacles_list = Obstacles.draw_obstacles(self.screen)
            # ball speed correction
            Ball.speed_correct()
            # obstacle collision with tank
            Obstacles.obstacle_collision(
                self.tank1, self.tank2, self.ball1, self.ball2, obstacles_list
            )
            Obstacles.tank_collision_with_outer_wall()
            Obstacles.tank_collision_with_outer_wall_2()
            # ball movement and collision
            Ball.ball_shoot_and_hit(
                self.ball1,
                self.ball2,
                tank_sprite,
                conf.tank1_x,
                conf.tank1_y,
                tank2_sprite,
                conf.tank2_x,
                conf.tank2_y,
            )
            # ball collision with wall
            conf.ball_mx, conf.ball_my = Ball.limit_wall_collision(
                self.ball1,
                conf.ball_mx,
                conf.ball_my,
                conf.screen_width,
                conf.screen_height,
            )
            conf.ball2_mx, conf.ball2_my = Ball.limit_wall_collision(
                self.ball2,
                conf.ball2_mx,
                conf.ball2_my,
                conf.screen_width,
                conf.screen_height,
            )
            # ball collision with tank rect
            Ball.ball_collision_with_tank(
                self.tank2, self.ball1, Ball, self.tank1, self.ball2
            )
            # keyboard inputs/tank movement
            Tank.tank_input()
            # score
            score_1 = Score.display_score(conf.score_p_1, 40, (141, 197, 80))
            score_2 = Score.display_score(conf.score_p_2, 40, (78, 89, 221))
            # score blit
            self.screen.blit(score_1, (180, 0.5))
            self.screen.blit(score_2, (580, 0.5))
            # display and fps
            pygame.display.flip()
            pygame.display.update()
            self.clock.tick(60)

