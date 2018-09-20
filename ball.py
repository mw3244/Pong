import pygame

class Ball():
    def __init__(self, game_settings):
        self.x = (game_settings.screen_width / 2) - 10
        self.y = (game_settings.screen_height / 2) + 10
        self.width = 20
        self.height = 20