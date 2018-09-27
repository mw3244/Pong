import pygame

class Button():
    def __init__(self, game_settings):
        self.button_text = "Play"
        self.button_font = pygame.font.SysFont("monospace", 64)
        self.button_label = self.button_font.render(self.button_text, True, (0,0,0))
        self.width = 160
        self.height = 80
        self.x = 0
        self.y = 0

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.rect.center = (game_settings.screen_width / 2, game_settings.screen_height / 2)

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), (self.rect), 0)

class Title():
    def __init__(self, game_settings):
        self.title_text = "EXTREME PONG"
        self.title_font = pygame.font.SysFont("monospace", 96)
        self.title_label = self.title_font.render(self.title_text, True, (255,255,255))