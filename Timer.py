from pygame import QUIT

import pygame
import ball
import config
conf = config


def timer(ball1, ball2):
    for event in pygame.event.get ():
        if event.type == QUIT:
            pygame.quit ()
            exit ()
        if conf.timer_on:
            if event.type == pygame.USEREVENT:
                conf.time_counter -= 1
                conf.time_text = (
                    str (conf.time_counter).rjust (3)
                    if conf.time_counter > 0
                    else "X"
                )
            if conf.time_text == "X":
                conf.ball_mx, conf.ball_my = ball.end_ball (
                    ball1, conf.ball_mx, conf.ball_my
                )
                conf.shoot = False
                conf.timer_on = False
        else:
            conf.time_text = "5".rjust (3)
            conf.time_counter = 5
        if conf.timer_on2:
            if event.type == pygame.USEREVENT:
                conf.time_counter2 -= 1
                conf.time_text2 = (
                    str (conf.time_counter2).rjust (3)
                    if conf.time_counter2 > 0
                    else "X"
                )
            if conf.time_text2 == "X":
                conf.ball2_mx, conf.ball2_my = ball.end_ball (
                    ball2, conf.ball2_mx, conf.ball2_my
                )
                conf.shoot2 = False
                conf.timer_on2 = False
        else:
            conf.time_text2 = "5".rjust (3)
            conf.time_counter2 = 5


    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if conf.timer_on:
            if event.type == pygame.USEREVENT:
                conf.time_counter -= 1
                conf.time_text = (
                    str(conf.time_counter).rjust(3)
                    if conf.time_counter > 0
                    else "X"
                )
            if conf.time_text == "X":
                conf.ball_mx, conf.ball_my = ball.end_ball(
                    ball1, conf.ball_mx, conf.ball_my
                )
                conf.shoot = False
                conf.timer_on = False
        else:
            conf.time_text = "5".rjust(3)
            conf.time_counter = 5
        if conf.timer_on2:
            if event.type == pygame.USEREVENT:
                conf.time_counter2 -= 1
                conf.time_text2 = (
                    str(conf.time_counter2).rjust(3)
                    if conf.time_counter2 > 0
                    else "X"
                )
            if conf.time_text2 == "X":
                conf.ball2_mx, conf.ball2_my = ball.end_ball(
                    ball2, conf.ball2_mx, conf.ball2_my
                )
                conf.shoot2 = False
                conf.timer_on2 = False
        else:
            conf.time_text2 = "5".rjust(3)
            conf.time_counter2 = 5
