import pygame
import time
import game_functions as gf
from settings import Settings
from score import Score
from paddle import Paddle1
from paddle import Paddle2
from paddle import PaddleT
from paddle import PaddleB
from paddle import PaddleT2
from paddle import PaddleB2
from ball import Ball
from button import Button
from button import Title

def run_game():
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    score = Score()
    paddle1 = Paddle1(game_settings, screen)
    paddle2 = Paddle2(game_settings)
    paddleT = PaddleT(game_settings, screen)
    paddleB = PaddleB(game_settings, screen)
    paddleT2 = PaddleT2(game_settings)
    paddleB2 = PaddleB2(game_settings)
    ball = Ball(game_settings)
    pygame.display.set_caption("Extreme Pong")
    pygame.mixer.music.load('audio/OST.mp3')
    pygame.mixer.music.play(-1)
    bounce = pygame.mixer.Sound('audio/beep.wav')

    button = Button(game_settings)
    title = Title(game_settings)

    menu_screen = True

    while menu_screen:
        menu_screen = gf.check_menu_events(screen, button, menu_screen)
        gf.update_menu_screen(game_settings, screen, button, title)

    while True:
        gf.check_events(screen, paddle1, paddleT, paddleB)
        paddle1.update(game_settings, paddleT, paddleB)
        paddleT.update(game_settings, paddle1)
        paddleB.update(game_settings, paddle1)
        paddle2.update(game_settings, ball, paddleT2, paddleB2)
        paddleT2.update(game_settings, paddle2, ball)
        paddleB2.update(game_settings, paddle2, ball)
        ball.update(game_settings, paddle1, paddleT, paddleB, paddle2, paddleT2, paddleB2, score, bounce)
        gf.update_screen(game_settings, screen, score, paddle1, paddle2, ball, paddleT, paddleB, paddleT2, paddleB2)
run_game()