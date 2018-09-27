import sys
import pygame

def check_events(screen, paddle1, paddleT, paddleB):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                paddle1.paddle_moving_up = True
            if event.key == pygame.K_DOWN:
                paddle1.paddle_moving_down = True
            if event.key == pygame.K_LEFT:
                paddleT.paddle_moving_left = True
                paddleB.paddle_moving_left = True
            if event.key == pygame.K_RIGHT:
                paddleT.paddle_moving_right = True
                paddleB.paddle_moving_right = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                paddle1.paddle_moving_up = False
            if event.key == pygame.K_DOWN:
                paddle1.paddle_moving_down = False
            if event.key == pygame.K_LEFT:
                paddleT.paddle_moving_left = False
                paddleB.paddle_moving_left = False
            if event.key == pygame.K_RIGHT:
                paddleT.paddle_moving_right = False
                paddleB.paddle_moving_right = False

def check_menu_events(screen, button, menu_screen):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if pos[0] > button.rect.left and pos[0] < button.rect.right and pos[1] < button.rect.bottom and pos[1] > button.rect.top:
                return False
    return True
            
def update_screen(game_settings, screen, score, paddle1, paddle2, ball, paddleT, paddleB, paddleT2, paddleB2):
    screen.fill(game_settings.bg_color)
    
    y = 0
    while y < game_settings.screen_height:
        pygame.draw.rect(screen, (255,255,255), (game_settings.screen_width/2, y + 10, 0, 20), 0)
        y += 50
    
    paddle1.draw(screen)
    paddle2.draw(screen)
    paddleT.draw(screen)
    paddleB.draw(screen)
    paddleT2.draw(screen)
    paddleB2.draw(screen)
    ball.draw(screen)

    screen.blit(score.left_score_label, (game_settings.screen_width/2 - 140, 40))
    screen.blit(score.right_score_label, (game_settings.screen_width/2 + 80, 40))
    
    pygame.display.flip()

def update_menu_screen(game_settings, screen, button, title):
    screen.fill(game_settings.bg_color)
    screen.blit(title.title_label, (game_settings.screen_width / 5, 40))

    button.draw(screen)
    screen.blit(button.button_label, (button.rect.left, button.rect.top))

    pygame.display.flip()
    