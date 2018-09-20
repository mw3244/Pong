import pygame
import game_functions as gf
from settings import Settings
from score import Score
from paddle import Paddle1
from paddle import Paddle2
from ball import Ball

def run_game():
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    score = Score()
    paddle1 = Paddle1(game_settings, screen)
    paddle2 = Paddle2(game_settings)
    ball = Ball(game_settings)
    pygame.display.set_caption("Pong")

    while True:
        gf.check_events(screen, paddle1)
        paddle1.update(game_settings)
        gf.update_screen(game_settings, screen, score, paddle1, paddle2, ball)
run_game()