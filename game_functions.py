import sys
import pygame

def check_events(screen, paddle1):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                paddle1.paddle_moving_up = True
            if event.key == pygame.K_DOWN:
                paddle1.paddle_moving_down = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                paddle1.paddle_moving_up = False
            if event.key == pygame.K_DOWN:
                paddle1.paddle_moving_down = False
            
            
def update_screen(game_settings, screen, score, paddle1, paddle2, ball):
    screen.fill(game_settings.bg_color)
    pygame.draw.rect(screen,(255, 255, 255),(0,0, game_settings.screen_width, 0), 30)
    pygame.draw.rect(screen, (255, 255, 255), (0, game_settings.screen_height, game_settings.screen_width, 0), 30)
    
    y = 0
    while y < game_settings.screen_height:
        pygame.draw.rect(screen, (255,255,255), (game_settings.screen_width/2, y, 0, 20), 0)
        y += 50

    screen.blit(score.left_score_label, (game_settings.screen_width/2 - 140, 40))
    screen.blit(score.right_score_label, (game_settings.screen_width/2 + 80, 40))
    
    paddle1.draw(screen)
    pygame.draw.rect(screen, (255, 255, 255), (paddle2.x, paddle2.y, paddle2.width, paddle2.height), 0)
    pygame.draw.rect(screen, (255, 255, 255), (ball.x, ball.y, ball.width, ball.height), 0)
    
    pygame.display.flip()
    