import pygame
import config
from random import randint
from score import Score

conf = config
Score = Score()


class Ball:
    def __init__(self):
        pygame.init()
        self.ball_mx = 0
        self.ball_my = 0
        self.ball2_mx = 0
        self.ball2_my = 0
        self.wiggle_cont = 0
        self.wiggle_cont2 = 0

    def shoot(self, ball, tank_sprite, ball_x, ball_y, ball_mx, ball_my):
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
        if ball_mx == 0 == ball_my:
            return 5, 5
        else:
            return ball_mx, ball_my

    def shoot2(self, ball, tank_sprite, ball_x, ball_y, ball_mx, ball_my):
        ball.x = ball_x
        ball.y = ball_y
        if tank_sprite == "img/player2_08.png":
            ball_mx = 5
            ball_my = 0.1
        if tank_sprite == "img/player2_09.png":
            ball_mx = 5
            ball_my = -1.5
        if tank_sprite == "img/player2_10.png":
            ball_mx = 5
            ball_my = -4
        if tank_sprite == "img/player2_11.png":
            ball_mx = 3
            ball_my = -8
        if tank_sprite == "img/player2_12.png":
            ball_mx = 0
            ball_my = -5
        if tank_sprite == "img/player2_13.png":
            ball_mx = -3
            ball_my = -8
        if tank_sprite == "img/player2_14.png":
            ball_mx = -5
            ball_my = -4
        if tank_sprite == "img/player2_15.png":
            ball_mx = -5
            ball_my = -1.5
        if tank_sprite == "img/player2_00.png":
            ball_mx = -5
            ball_my = 0.1
        if tank_sprite == "img/player2_01.png":
            ball_mx = -5
            ball_my = 1.5
        if tank_sprite == "img/player2_02.png":
            ball_mx = -5
            ball_my = 4
        if tank_sprite == "img/player2_03.png":
            ball_mx = -3
            ball_my = 8
        if tank_sprite == "img/player2_04.png":
            ball_mx = 0
            ball_my = 5
        if tank_sprite == "img/player2_05.png":
            ball_mx = 3
            ball_my = 8
        if tank_sprite == "img/player2_06.png":
            ball_mx = 5
            ball_my = 4
        if tank_sprite == "img/player2_07.png":
            ball_mx = 5
            ball_my = 1.5
        return ball_mx, ball_my

    def end_ball(self, ball):
        ball.x = conf.screen_width + 100
        ball.y = conf.screen_height + 100
        ball_mx = 0
        ball_my = 0
        return ball_mx, ball_my

    def create_ball(self, tank_pos_x, tank_pos_y):
        return pygame.Rect(tank_pos_x, tank_pos_y, 5, 5)

    def draw_ball(self, display, color, ball):
        pygame.draw.ellipse(display, color, ball)

    def move_ball(self, ball, ball_dx, ball_dy):
        ball.x += ball_dx
        ball.y += ball_dy

    def speed_correct(self):
        # ball speed correction
        if self.ball2_my == 0:
            self.ball2_my = 5 if randint(1, 3) == 1 else 5
        if self.ball2_mx == 0:
            self.ball2_mx = 5 if randint(1, 3) == 1 else 5
        if self.ball_my == 0:
            self.ball1_my = 5 if randint(1, 3) == 1 else 5
        if self.ball_mx == 0:
            self.ball1_mx = 5 if randint(1, 3) == 1 else 5

    def limit_wall_collision(self, ball, ball_mx, ball_my, height, width):

        # collision with the upper wall

        if ball.y < 0 + 80:

            # when the ball is in idle mode outside the screen
            if (
                ball.x == conf.screen_width + 100
                or ball.x > conf.screen_width + 100
            ) and (
                ball.y == conf.screen_height + 100
                or ball.y > conf.screen_height + 100
            ):
                return ball_mx, ball_my
            else:
                ball.y = 0 + 80
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
        # collision with the lower wall

        elif ball.y > height - 50:

            # when the ball is in idle mode outside the screen
            if (
                ball.x == conf.screen_width + 100
                or ball.x > conf.screen_width + 100
            ) and (
                ball.y == conf.screen_height + 100
                or ball.y > conf.screen_height + 100
            ):
                return ball_mx, ball_my
            else:
                ball.y = height - 50
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

            if (
                ball.x == conf.screen_width + 100
                or ball.x > conf.screen_width + 100
            ) and (
                ball.y == conf.screen_height + 100
                or ball.y > conf.screen_height + 100
            ):
                return ball_mx, ball_my
            else:
                ball.x = 0 + 15
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

            if (
                ball.x == conf.screen_width + 100
                or ball.x > conf.screen_width + 100
            ) and (
                ball.y == conf.screen_height + 100
                or ball.y > conf.screen_height + 100
            ):
                return ball_mx, ball_my
            else:
                ball.x = width - 30
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

    def ball_shoot_and_hit(
        self,
        ball1,
        ball2,
        tank_sprite,
        tank1_x,
        tank1_y,
        tank2_sprite,
        tank2_x,
        tank2_y,
    ):
        if conf.timer_on:
            self.move_ball(ball1, self.ball_mx, self.ball_my)
        elif not conf.timer_on:
            conf.ball_mx, conf.ball_my = self.end_ball(ball1)
        if conf.timer_on2:
            self.move_ball(ball2, self.ball2_mx, self.ball2_my)
        elif not conf.timer_on2:
            conf.ball2_mx, conf.ball2_my = self.end_ball(ball2)
        if conf.shoot:
            self.ball_mx, self.ball_my = self.shoot(
                ball1,
                tank_sprite,
                tank1_x + 25 / 2,
                tank1_y + 28 / 2,
                self.ball_mx,
                self.ball_my,
            )
            conf.timer_on = True
            conf.shoot = False
        if conf.hit:
            self.ball_mx, self.ball_my = self.end_ball(ball1)
            conf.timer_on = False
            conf.hit = False
        if conf.shoot2:
            self.ball2_mx, self.ball2_my = self.shoot2(
                ball2,
                tank2_sprite,
                tank2_x + 25 / 2,
                tank2_y + 28 / 2,
                self.ball2_mx,
                self.ball2_my,
            )
            conf.timer_on2 = True
            conf.shoot2 = False
        if conf.hit2:
            self.ball2_mx, self.ball2_my = self.end_ball(ball2)
            conf.timer_on2 = False
            conf.hit2 = False

    def ball_collision_with_tank(
        self, tank2_rect, ball1, ball, tank1_rect, ball2
    ):
        if tank2_rect.colliderect(ball1):
            # use whatever tank collision functions with the ball you have here
            self.ball_mx, self.ball_my = ball.end_ball(ball1)

            hit = pygame.mixer.Sound(conf.TANK_HIT)
            pygame.mixer.Sound.play(hit)
            hit.set_volume(0.1)
            conf.score_p_1 += 1
        if tank1_rect.colliderect(ball2):
            # use whatever tank collision functions with the ball you have here
            hit = pygame.mixer.Sound(conf.TANK_HIT)
            pygame.mixer.Sound.play(hit)
            self.ball2_mx, self.ball2_my = ball.end_ball(ball2)
            conf.score_p_2 += 1

    def ball_timer(self, screen, ball1, ball2):
        if conf.timer_on:
            self.draw_ball(screen, conf.LIGHT_GREEN, ball1)
        if conf.timer_on2:
            self.draw_ball(screen, conf.VIOLET, ball2)

    def ball_collision_with_obstacles(self, obstacle_list, ball1, ball2):
        for obs in obstacle_list:
            if obs.colliderect(ball1):
                if self.ball_my == 0:
                    self.ball_my = 5 if randint(1, 3) == 1 else 5
                if self.ball_mx == 0:
                    self.ball_mx = 5 if randint(1, 3) == 1 else 5
                self.ball_mx *= -1
                self.wiggle_cont += 1
                if self.wiggle_cont > 5:
                    self.ball_my *= -1
                    self.ball_mx *= -1 if randint(1, 3) == 1 else 1
                    conf.wiggle_cont = 0
            if obs.colliderect(ball2):
                if self.ball2_my == 0:
                    self.ball2_my = 5 if randint(1, 3) == 1 else 5
                if self.ball2_mx == 0:
                    self.ball2_mx = 5 if randint(1, 3) == 1 else 5
                self.ball2_mx *= -1
                self.wiggle_cont2 += 1
                if self.wiggle_cont2 > 5:
                    self.ball2_my *= -1
                    self.wiggle_cont2 = 0
