import pygame

class Paddle1():
    def __init__(self, game_settings, screen):
        super(Paddle1, self).__init__()
        self.x = game_settings.screen_width - 10
        self.y = game_settings.screen_height / 2
        self.width = 10
        self.height = 80

        self.paddle1_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        
        self.paddle_moving_up = False
        self.paddle_moving_down = False
        
    def update(self, game_settings, paddleT, paddleB):
        if self.paddle_moving_up and self.paddle1_rect.top > 0:
            self.y -= game_settings.game_speed
        if self.paddle_moving_down and self.paddle1_rect.top < (game_settings.screen_height - self.height):
            self.y += game_settings.game_speed

        if pygame.Rect.colliderect(self.paddle1_rect, paddleT.paddleT_rect):
            self.paddle_moving_up = False

        if pygame.Rect.colliderect(self.paddle1_rect, paddleB.paddleB_rect):
            self.paddle_moving_down = False

        self.paddle1_rect.center = (self.x, self.y)
            
    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), (self.paddle1_rect), 0)
 
        
class Paddle2():
    def __init__(self, game_settings):
        self.x = 10
        self.y = (game_settings.screen_height / 2)
        self.width = 10
        self.height = 80

        self.paddle_moving_up = False
        self.paddle_moving_down = False

        self.paddle2_rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def update(self, game_settings, ball, paddleT2, paddleB2):
        if ball.ball_rect.top < self.y:
            self.paddle_moving_up = True
            self.paddle_moving_down = False

        if ball.ball_rect.top > self.y:
            self.paddle_moving_up = False
            self.paddle_moving_down = True

        if self.paddle_moving_up and self.paddle2_rect.top > 0:
            self.y -= game_settings.ai_speed
        if self.paddle_moving_down and self.paddle2_rect.top < (game_settings.screen_height - self.height):
            self.y += game_settings.ai_speed

        if pygame.Rect.colliderect(self.paddle2_rect, paddleT2.paddleT2_rect):
            self.paddle_moving_up = False

        if pygame.Rect.colliderect(self.paddle2_rect, paddleB2.paddleB2_rect):
            self.paddle_moving_down = False

        self.paddle2_rect.center = (self.x, self.y)

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), (self.paddle2_rect), 0)

class PaddleT():
    def __init__(self, game_settings, screen):
        self.x = (game_settings.screen_width * .75)
        self.y = 10
        self.width = 80
        self.height = 10

        self.paddleT_rect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.paddle_moving_left = False
        self.paddle_moving_right = False

    def update(self, game_settings, paddle1):
        if self.paddle_moving_left and self.paddleT_rect.left > (game_settings.screen_width / 2):
            self.x -= game_settings.game_speed
        if self.paddle_moving_right and self.paddleT_rect.left < (game_settings.screen_width - self.paddleT_rect.width):
            self.x += game_settings.game_speed

        if pygame.Rect.colliderect(self.paddleT_rect, paddle1.paddle1_rect):
            self.paddle_moving_right = False

        self.paddleT_rect.center = (self.x, self.y)

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), (self.paddleT_rect), 0)


class PaddleB():
    def __init__(self, game_settings, screen):
        self.x = (game_settings.screen_width * .75)
        self.y = game_settings.screen_height - 20
        self.width = 80
        self.height = 10

        self.paddleB_rect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.paddle_moving_left = False
        self.paddle_moving_right = False

    def update(self, game_settings, paddle1):
        if self.paddle_moving_left and self.paddleB_rect.left > (game_settings.screen_width / 2):
            self.x -= game_settings.game_speed
        if self.paddle_moving_right and self.paddleB_rect.left < (game_settings.screen_width - self.paddleB_rect.width):
            self.x += game_settings.game_speed

        if pygame.Rect.colliderect(self.paddleB_rect, paddle1.paddle1_rect):
            self.paddle_moving_right = False

        self.paddleB_rect.center = (self.x, self.y)

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), (self.paddleB_rect), 0)

class PaddleT2():
    def __init__(self, game_settings):
        self.x = (game_settings.screen_width * .25)
        self.y = 10
        self.width = 80
        self.height = 10

        self.paddleT2_rect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.paddle_moving_left = False
        self.paddle_moving_right = False

    def update(self, game_settings, paddle2, ball):
        if ball.ball_rect.left < self.x:
            self.paddle_moving_left = True
            self.paddle_moving_right = False

        if ball.ball_rect.left > self.x:
            self.paddle_moving_left = False
            self.paddle_moving_right = True

        if self.paddle_moving_left and self.paddleT2_rect.left > 0:
            self.x -= game_settings.ai_speed
        if self.paddle_moving_right and self.paddleT2_rect.left < ((game_settings.screen_width / 2) - self.paddleT2_rect.width):
            self.x += game_settings.ai_speed

        if pygame.Rect.colliderect(self.paddleT2_rect, paddle2.paddle2_rect):
            self.x -= game_settings.ai_speed

        self.paddleT2_rect.center = (self.x, self.y)

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), (self.paddleT2_rect), 0)


class PaddleB2():
    def __init__(self, game_settings):
        self.x = (game_settings.screen_width * .25)
        self.y = game_settings.screen_height - 20
        self.width = 80
        self.height = 10

        self.paddleB2_rect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.paddle_moving_left = False
        self.paddle_moving_right = False

    def update(self, game_settings, paddle2, ball):
        if ball.ball_rect.left < self.x:
            self.paddle_moving_left = True
            self.paddle_moving_right = False

        if ball.ball_rect.left > self.x:
            self.paddle_moving_left = False
            self.paddle_moving_right = True

        if self.paddle_moving_left and self.paddleB2_rect.left > 0:
            self.x -= game_settings.ai_speed
        if self.paddle_moving_right and self.paddleB2_rect.left < ((game_settings.screen_width / 2) - self.paddleB2_rect.width):
            self.x += game_settings.ai_speed

        if pygame.Rect.colliderect(self.paddleB2_rect, paddle2.paddle2_rect):
            self.x -= game_settings.ai_speed

        self.paddleB2_rect.center = (self.x, self.y)

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), (self.paddleB2_rect), 0)