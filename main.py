import pygame
from settings import *
from game_mode import *
from ui.hud import HUD
from ui.inventory import Inventory

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("BIT-勇士屠龙记")
pygame.display.set_icon(pygame.image.load("assets/captain.png"))
clock = pygame.time.Clock()
game_mode = GameMode()
# game_over = False
game_pause = False
last_move_time = 0
# 移动延迟，每warrior_move_delay个ticks可以移动一次，防止移动过快
warrior_move_delay = 15
hud = HUD()
inventory = Inventory()

def update():
    screen.fill((0, 0, 0))
    game_mode.update(hud, inventory)
    game_mode.draw(screen, hud, inventory)

def handle_warrior_move():
    global last_move_time
    current_time = pygame.time.get_ticks()
    # 获取当前按下的键
    keys = pygame.key.get_pressed()
    if not game_pause:
        if current_time - last_move_time > warrior_move_delay:
            if keys[pygame.K_s]:
                game_mode.battle.move_warrior(0, 1)
            elif keys[pygame.K_w]:
                game_mode.battle.move_warrior(0, -1)
            elif keys[pygame.K_a]:
                game_mode.battle.move_warrior(-1, 0)
            elif keys[pygame.K_d]:
                game_mode.battle.move_warrior(1, 0)
            last_move_time = current_time
        
def handle_piece_move(event):
    global game_over
    if not game_pause:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # 调用tetris的rotate_piece方法
                game_mode.tetris.rotate_piece()
            elif event.key == pygame.K_a:
                game_mode.tetris.move_piece(-1, 0)
            elif event.key == pygame.K_d:
                game_mode.tetris.move_piece(1, 0)
            elif event.key == pygame.K_s:
                game_mode.tetris.move_piece(0, 1)
        
def handle_inventory(event):
    if not game_pause:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                print("使用治疗！")
                inventory.use_item(0, game_mode.battle)
            elif event.key == pygame.K_2:
                print("使用护盾！")
                inventory.use_item(1, game_mode.battle)
            elif event.key == pygame.K_3:
                print("使用伤害！")
                inventory.use_item(2, game_mode.battle)
            elif event.key == pygame.K_4:
                print("使用移速！")
                inventory.use_item(3, game_mode.battle)
            elif event.key == pygame.K_5:
                print("使用攻速！")
                inventory.use_item(4, game_mode.battle)
            elif event.key == pygame.K_6:
                print("使用攻击范围！")
                inventory.use_item(5, game_mode.battle)
        
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if game_mode.game_mode:
            handle_piece_move(event)
        elif not game_mode.game_mode:
            handle_inventory(event)
            
        if hud.pause_button.is_clicked(event):
            game_mode.pause()
            game_pause = not game_pause
            
        # if hud.shop_button.is_clicked(event):
        #     game_mode.pause()
        #     game_pause = not game_pause
        #     game_mode.shop()
            
        if hud.battle_button.is_clicked(event):
            if game_pause:
                game_mode.pause()
                game_pause = not game_pause
            game_mode.switch_mode()
            
    if not game_mode.game_mode:     
        handle_warrior_move()
    update()
    
    pygame.display.flip()
    clock.tick(FPS)
    
pygame.quit()
quit()