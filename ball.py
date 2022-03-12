import pygame
import config

conf = config


def shoot(ball, ball_x, ball_y, ball_mx, ball_my, shoot=bool):
    ball.x = ball_x
    ball.y = ball_y
    ball_mx = 5
    ball_my = 5
    return ball_mx, ball_my


def end_ball(ball, ball_mx, ball_my):
    ball.x = conf.screen_height + 100
    ball.y = conf.screen_width + 100
    ball_mx = 0
    ball_my = 0
    return ball_mx, ball_my


def create_ball(tank_pos_x, tank_pos_y):
    return pygame.Rect(tank_pos_x, tank_pos_y, 5, 5)


def draw_ball(display, color, ball):
    pygame.draw.ellipse(display, color, ball)


def shooting_accel(tank_x, tank_y):
    ball_mx, ball_my = tank_x, tank_y
    return ball_mx, ball_my


def move_ball(ball, ball_dx, ball_dy):
    ball.x += ball_dx
    ball.y += ball_dy


# left wall collision


def limit_wall_collision(ball, ball_mx, ball_my, height, width):
    # collision with the upper wall
    if ball.y < 0 + 80:
        ball_my *= -1
        return ball_mx, ball_my


    # collision with the lower wall

    elif ball.y > height - 50:
        ball_my *= -1
        return ball_mx, ball_my



    # collision with left wall

    elif ball.x < 0 + 15:
        ball_mx *= -1
        return ball_mx, ball_my



    # collision with right wall

    elif ball.x > width - 30:
        ball_mx *= -1
        return ball_mx, ball_my


    else:
        return ball_mx, ball_my
