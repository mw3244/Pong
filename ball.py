import pygame
import random
import time



class Ball():
    def __init__(self, game_settings):
        self.x = (game_settings.screen_width / 2) - 10
        self.y = (game_settings.screen_height / 2) + 10
        self.width = 20
        self.height = 20

        self.ball_rect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.ball_moving = True
        self.x_direction = random.choice([-1, 1]) * random.random()
        self.y_direction = random.choice([-1, 1]) * random.random()

    def update(self, game_settings, paddle1, paddleT, paddleB, paddle2, paddleT2, paddleB2, score, bounce):
        if pygame.Rect.colliderect(self.ball_rect, paddle1.paddle1_rect):
            self.x_direction *= -1
            bounce.play()
            game_settings.game_speed += .1

        if pygame.Rect.colliderect(self.ball_rect, paddleT.paddleT_rect):
            self.y_direction *= -1
            bounce.play()
            game_settings.game_speed += .1

        if pygame.Rect.colliderect(self.ball_rect, paddleB.paddleB_rect):
            self.y_direction *= -1
            bounce.play()
            game_settings.game_speed += .1

        if pygame.Rect.colliderect(self.ball_rect, paddle2.paddle2_rect):
            self.x_direction *= -1
            bounce.play()
            game_settings.game_speed += .1

        if pygame.Rect.colliderect(self.ball_rect, paddleT2.paddleT2_rect):
            self.y_direction *= -1
            bounce.play()
            game_settings.game_speed += .1

        if pygame.Rect.colliderect(self.ball_rect, paddleB2.paddleB2_rect):
            self.y_direction *= -1
            bounce.play()
            game_settings.game_speed += .1

        if self.ball_moving:
            self.x += (self.x_direction * game_settings.game_speed)
            self.y += (self.y_direction * game_settings.game_speed)

        if self.ball_rect.right < 0 or self.ball_rect.left > game_settings.screen_width or self.ball_rect.top > game_settings.screen_height or self.ball_rect.bottom < 0:
            if self.x < game_settings.screen_width / 2:
                score.right_scored()
            else:
                score.left_scored()
            game_settings.game_speed_reset()

            self.x = (game_settings.screen_width / 2) - 10
            self.y = (game_settings.screen_height / 2) + 10
            self.x_direction = random.choice([-1, 1]) * random.random()
            self.y_direction = random.choice([-1, 1]) * random.random()


        self.ball_rect.center = (self.x, self.y)

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), (self.ball_rect.left, self.ball_rect.top, self.ball_rect.width, self.ball_rect.height), 0)