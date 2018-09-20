import pygame

class Score():
   def __init__(self):
       self.left_score = 0
       self.right_score = 0
       self.score_font = pygame.font.SysFont("monospace", 96)
       self.left_score_label = self.score_font.render(str(self.left_score), True, (255,255,255))
       self.right_score_label = self.score_font.render(str(self.right_score), True, (255, 255, 255))
       