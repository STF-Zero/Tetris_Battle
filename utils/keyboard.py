import pygame

def handle_input(event, game_mode):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_DOWN:
            game_mode.tetris.move_piece(0, 1)
        # elif event.key == pygame.K_UP:
        #     game_mode.tetris.move_piece(0, -1)
        elif event.key == pygame.K_LEFT:
            game_mode.tetris.move_piece(-1, 0)
        elif event.key == pygame.K_RIGHT:
            game_mode.tetris.move_piece(1, 0)
        elif event.key == pygame.K_SPACE:
            game_mode.tetris.rotate_piece()
            