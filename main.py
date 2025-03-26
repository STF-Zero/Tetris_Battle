import pygame
from settings import *
from game_mode import *
import utils.keyboard as keyboard

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("屠龙")
clock = pygame.time.Clock()
game_mode = GameMode()
# origin_speed = game_mode.tetris.drop_speed
# target_speed = origin_speed * 1.5

running = True
while running:
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        keyboard.handle_input(event, game_mode)
    pygame.display.flip()
    screen.fill((0, 0, 0))
    
    # print(clock)
    game_mode.update()
    game_mode.draw(screen)
    
pygame.quit()
quit()