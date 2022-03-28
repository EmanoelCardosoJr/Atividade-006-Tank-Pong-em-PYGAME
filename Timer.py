from pygame import QUIT
import pygame
from ball import Ball
import config

conf = config
Ball = Ball()


class Timer:
    def __init__(self):
        self.time_text = "5".rjust(3)
        self.time_counter = 5
        self.time_text2 = "5".rjust(3)
        self.time_counter2 = 5

    def timer(self, ball1, ball2):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if conf.timer_on:
                if event.type == pygame.USEREVENT:
                    self.time_counter -= 1
                    self.time_text = (
                        str(self.time_counter).rjust(3)
                        if self.time_counter > 0
                        else "X"
                    )
                if self.time_text == "X":
                    conf.ball_mx, conf.ball_my = Ball.end_ball(ball1)
                    conf.shoot = False
                    conf.timer_on = False
            else:
                self.time_text = "5".rjust(3)
                self.time_counter = 5
            if conf.timer_on2:
                if event.type == pygame.USEREVENT:
                    self.time_counter2 -= 1
                    self.time_text2 = (
                        str(self.time_counter2).rjust(3)
                        if self.time_counter2 > 0
                        else "X"
                    )
                if self.time_text2 == "X":
                    conf.ball2_mx, conf.ball2_my = Ball.end_ball(ball2)
                    conf.shoot2 = False
                    conf.timer_on2 = False
            else:
                self.time_text2 = "5".rjust(3)
                self.time_counter2 = 5
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if conf.timer_on:
                if event.type == pygame.USEREVENT:
                    self.time_counter -= 1
                    self.time_text = (
                        str(self.time_counter).rjust(3)
                        if self.time_counter > 0
                        else "X"
                    )
                if self.time_text == "X":
                    conf.ball_mx, conf.ball_my = Ball.end_ball(ball1)
                    conf.shoot = False
                    conf.timer_on = False
            else:
                self.time_text = "5".rjust(3)
                self.time_counter = 5
            if conf.timer_on2:
                if event.type == pygame.USEREVENT:
                    self.time_counter2 -= 1
                    self.time_text2 = (
                        str(self.time_counter2).rjust(3)
                        if self.time_counter2 > 0
                        else "X"
                    )
                if self.time_text2 == "X":
                    conf.ball2_mx, conf.ball2_my = Ball.end_ball(ball2)
                    conf.shoot2 = False
                    conf.timer_on2 = False
            else:
                self.time_text2 = "5".rjust(3)
                self.time_counter2 = 5
