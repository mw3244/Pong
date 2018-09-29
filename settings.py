class Settings():
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)
        self.game_speed = .5
        self.ai_speed = .25
        self.max_score = 15

    def game_speed_reset(self):
        self.game_speed = .5