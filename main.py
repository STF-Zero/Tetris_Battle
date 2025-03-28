import pygame
from settings import *
from game_mode import *
import utils.keyboard as keyboard
from ui.hud import HUD

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("屠龙")
clock = pygame.time.Clock()
game_mode = GameMode()
# origin_speed = game_mode.tetris.drop_speed
# target_speed = origin_speed * 1.5

running = True
while running:
    
    hud = HUD()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        keyboard.handle_input(event, game_mode)
        
        if hud.pause_button.is_clicked(event):
            game_mode.pause()
        if hud.shop_button.is_clicked(event):
            game_mode.shop()
     
    screen.fill((0, 0, 0))
    
    game_mode.update(hud)
    game_mode.draw(screen, hud)
    
    # hud.update_money(10)
    # hud.draw(screen)
    
    pygame.display.flip()
    clock.tick(FPS)
    
pygame.quit()
quit()