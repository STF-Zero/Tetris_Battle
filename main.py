import pygame
from settings import *
from game_mode import *

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("屠龙")
clock = pygame.time.Clock()
game_mode = GameMode()

running = True
while running:
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_LEFT:
                game_mode.tetris.move_piece(-1, 0)
            elif event.key == pygame.K_RIGHT:
                game_mode.tetris.move_piece(1, 0)
            elif event.key == pygame.K_SPACE:
                game_mode.tetris.rotate_piece()
            
    pygame.display.flip()
    screen.fill((0, 0, 0))
    
    # print(clock)
    game_mode.update()
    game_mode.draw(screen)
    
pygame.quit()
quit()