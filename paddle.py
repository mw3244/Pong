import pygame

class Paddle1():
    def __init__(self, game_settings, screen):
        super(Paddle1, self).__init__()
        self.x = game_settings.screen_width - 20
        self.y = game_settings.screen_height / 2
        self.width = 10
        self.height = 80
        
        self.paddle_moving_up = False
        self.paddle_moving_down = False
        
    def update(self, game_settings):
        if self.paddle_moving_up and self.y > 15:
            self.y -= game_settings.game_speed
        if self.paddle_moving_down and self.y < (game_settings.screen_height - 95):
            self.y += game_settings.game_speed
            
    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, self.width, self.height), 0)
 
        
class Paddle2():
    def __init__(self, game_settings):
        self.x = 10
        self.y = game_settings.screen_height / 2
        self.width = 10
        self.height = 80
        