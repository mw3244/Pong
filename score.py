import pygame
import time

class Score():
    def __init__(self, game_settings):
            self.left_score = 0
            self.right_score = 0
            self.score_font = pygame.font.SysFont("monospace", 96)
            self.left_score_label = self.score_font.render(str(self.left_score), True, (255,255,255))
            self.right_score_label = self.score_font.render(str(self.right_score), True, (255, 255, 255))
            self.max_score = game_settings.max_score
            self.max_score_label = self.score_font.render(str(self.max_score), True, (255, 255, 255))

    def left_scored(self):
            self.left_score += 1
            self.left_score_label = self.score_font.render(str(self.left_score), True, (255, 255, 255))

    def right_scored(self):
            self.right_score += 1
            self.right_score_label = self.score_font.render(str(self.right_score), True, (255, 255, 255))
