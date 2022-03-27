import pygame
import config
import ball
import obstacles
from score import display_score
import tank
import Timer

conf = config
pygame.init()
Tank = tank

ball1 = ball.create_ball(conf.tank1_x, conf.tank1_y)
ball2 = ball.create_ball(conf.tank2_x, conf.tank2_y)
tank1 = Tank.create_tank(conf.tank1_x, conf.tank1_y, conf.tank_size)
tank2 = Tank.create_tank(conf.tank2_x, conf.tank2_y, conf.tank_size)
screen = pygame.display.set_mode((conf.screen_height, conf.screen_width))
pygame.time.set_timer(pygame.USEREVENT, 1000)
pygame.display.set_caption("Combat")
clock = pygame.time.Clock()

while True:
    # screen
    screen.fill(conf.RED)
    # tank rect position refresh
    Tank.tank_rect_follow(tank1, conf.tank1_x, conf.tank1_y)
    Tank.tank_rect_follow(tank2, conf.tank2_x, conf.tank2_y)
    # tank sprites
    tank_sprite = Tank.add_tank1(screen, conf.tank1_index, conf.tank1_x, conf.tank1_y)
    tank2_sprite = Tank.add_tank2(screen, conf.tank2_index, conf.tank2_x, conf.tank2_y)
    # draw ball
    ball.ball_draw(screen, ball1, ball2)
    # Timer
    Timer.timer(ball1, ball2)
    # wall and obstacles drawing
    obstacles_list = obstacles.draw_obstacles(screen)
    # ball speed correction
    ball.speed_correct()
    # obstacle collision with tank
    obstacles.obstacle_collision(tank1, tank2, ball1, ball2, obstacles_list)
    # ball movement and collision
    ball.ball_shoot_and_hit(ball1, ball2, tank_sprite, conf.tank1_x, conf.tank1_y, tank2_sprite,
                            conf.tank2_x, conf.tank2_y)
    # ball collision with wall
    conf.ball_mx, conf.ball_my = ball.limit_wall_collision(
        ball1,
        conf.ball_mx,
        conf.ball_my,
        conf.screen_width,
        conf.screen_height,
    )
    conf.ball2_mx, conf.ball2_my = ball.limit_wall_collision(
        ball2,
        conf.ball2_mx,
        conf.ball2_my,
        conf.screen_width,
        conf.screen_height,
    )
    # ball collision with tank rect
    ball.ball_collision_with_tank(conf.score_p_1, tank2, ball1, ball, conf.score_p_2, tank1, ball2)
    # keyboard inputs/tank movement
    tank.tank_input()
    # score
    score_1 = display_score(conf.score_p_1, 40, (141, 197, 80))
    score_2 = display_score(conf.score_p_2, 40, (78, 89, 221))
    # score blit
    screen.blit(score_1, (180, 0.5))
    screen.blit(score_2, (580, 0.5))
    # display and fps
    pygame.display.flip()
    pygame.display.update()
    clock.tick(60)
