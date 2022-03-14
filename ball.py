import pygame
import config
from random import randint

conf = config


def shoot(ball, tank_sprite, ball_x, ball_y, ball_mx, ball_my):
    ball.x = ball_x
    ball.y = ball_y
    if tank_sprite == "img/player1_00.png":
        ball_mx = 5
        ball_my = 0
    if tank_sprite == "img/player1_01.png":
        ball_mx = 5
        ball_my = -1.5
    if tank_sprite == "img/player1_02.png":
        ball_mx = 5
        ball_my = -4
    if tank_sprite == "img/player1_03.png":
        ball_mx = 3
        ball_my = -8
    if tank_sprite == "img/player1_04.png":
        ball_mx = 0
        ball_my = -5
    if tank_sprite == "img/player1_05.png":
        ball_mx = -3
        ball_my = -8
    if tank_sprite == "img/player1_06.png":
        ball_mx = -5
        ball_my = -4
    if tank_sprite == "img/player1_07.png":
        ball_mx = -5
        ball_my = -1.5
    if tank_sprite == "img/player1_08.png":
        ball_mx = -5
        ball_my = 0
    if tank_sprite == "img/player1_09.png":
        ball_mx = -5
        ball_my = 1.5
    if tank_sprite == "img/player1_10.png":
        ball_mx = -5
        ball_my = 4
    if tank_sprite == "img/player1_11.png":
        ball_mx = -3
        ball_my = 8
    if tank_sprite == "img/player1_12.png":
        ball_mx = 0
        ball_my = 5
    if tank_sprite == "img/player1_13.png":
        ball_mx = 3
        ball_my = 8
    if tank_sprite == "img/player1_14.png":
        ball_mx = 5
        ball_my = 4
    if tank_sprite == "img/player1_15.png":
        ball_mx = 5
        ball_my = 1.5

    return ball_mx, ball_my


def end_ball(ball, ball_mx, ball_my):
    ball.x = conf.screen_width + 100
    ball.y = conf.screen_height + 100
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




def limit_wall_collision(ball, ball_mx, ball_my, height, width):

    # collision with the upper wall

    if ball.y < 0 + 80:
        # when the ball is in idle mode outside the screen
        if ball.x == conf.screen_width+100 and ball.y == conf.screen_height+100:
            return ball_mx, ball_my
        else:
            # the actual collision
            if(ball_my != 5) and (ball_my != -5):
                if ball_my > 0:
                    ball_my = 5
                else:
                    ball_my = -5
            else:
                ball_my = ball_my
            if ball_mx == 0:
                ball_mx = 5 if randint(-3, 3) > 0 else -5
            elif (ball_mx != 5) and (ball_mx != -5):
                if ball_mx > 0:
                    ball_mx = 5
                else:
                    ball_mx = -5
            else:
                ball_mx = ball_mx
            ball_my *= -1
            return ball_mx, ball_my


    # collision with the lower wall

    elif ball.y > height - 50:
        # when the ball is in idle mode outside the screen
        if ball.x == conf.screen_width + 100 and ball.y == conf.screen_height + 100:
            return ball_mx, ball_my
        else:
            # the actual collision

            if (ball_my != 5) and (ball_my != -5):
                if ball_my > 0:
                    ball_my = 5
                else:
                    ball_my = -5
            else:
                ball_my = ball_my
            if ball_mx == 0:
                ball_mx = 5 if randint(-3, 3) > 0 else -5
            elif (ball_mx != 5) and (ball_mx != -5):
                if ball_mx > 0:
                    ball_mx = 5
                else:
                    ball_mx = -5
            else:
                ball_mx = ball_mx
            ball_my *= -1
            return ball_mx, ball_my



    # collision with left wall

    elif ball.x < 0 + 15:
        # when the ball is in idle mode outside the screen

        if ball.x == conf.screen_width + 100 and ball.y == conf.screen_height + 100:
            return ball_mx, ball_my
        else:
            # the actual collision

            if ball_my == 0:
                ball_my = 5 if randint(-3, 3) > 0 else -5
            elif (ball_my != 5) and (ball_my != -5):
                if ball_my > 0:
                    ball_my = 5
                else:
                    ball_my = -5
            else:
                ball_my = ball_my
            if (ball_mx != 5) and (ball_mx != -5):
                if ball_mx > 0:
                    ball_mx = 5
                else:
                    ball_mx = -5
            else:
                ball_mx = ball_mx
            ball_mx *= -1
            return ball_mx, ball_my



    # collision with right wall

    elif ball.x > width - 30:
        # when the ball is in idle mode outside the screen
        if ball.x == conf.screen_width + 100 and ball.y == conf.screen_height + 100:
            return ball_mx, ball_my
        else:
            # the actual collision
            if ball_my == 0:
                ball_my = 5 if randint(-3, 3) > 0 else -5
            elif (ball_my != 5) and (ball_my != -5):
                if ball_my > 0:
                    ball_my = 5
                else:
                    ball_my = -5
            else:
                ball_my = ball_my
            if (ball_mx != 5) and (ball_mx != -5):
                if ball_mx > 0:
                    ball_mx = 5
                else:
                    ball_mx = -5
            else:
                ball_mx = ball_mx
            ball_mx *= -1

            return ball_mx, ball_my


    else:
        return ball_mx, ball_my

