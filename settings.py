class Settings():
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)
        self.game_speed = .5
        self.ai_speed = .35

    def game_speed_reset(self):
        self.game_speed = .5