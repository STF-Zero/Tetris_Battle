import pygame
from settings import *
from game_mode import *
# import utils.keyboard as keyboarda
from ui.hud import HUD

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("屠龙")
clock = pygame.time.Clock()
game_mode = GameMode()
# game_over = False
game_pause = False
last_move_time = 0
# 移动延迟，每warrior_move_delay个ticks可以移动一次，防止移动过快
warrior_move_delay = 15
hud = HUD()
# origin_speed = game_mode.tetris.drop_speed
# target_speed = origin_speed * 1.5

def update():
    screen.fill((0, 0, 0))
    game_mode.update(hud)
    game_mode.draw(screen, hud)

def handle_warrior_move():
    global last_move_time
    current_time = pygame.time.get_ticks()
    # 获取当前按下的键
    keys = pygame.key.get_pressed()
    # 如果game_mode不为空
    if game_mode:
        # 如果游戏模式为tetris
        if not game_mode.game_mode and not game_pause:
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
    if game_mode:
        if game_mode.game_mode and not game_pause:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # 调用tetris的rotate_piece方法
                    game_mode.tetris.rotate_piece()
                elif event.key == pygame.K_LEFT:
                    game_mode.tetris.move_piece(-1, 0)
                elif event.key == pygame.K_RIGHT:
                    game_mode.tetris.move_piece(1, 0)
                elif event.key == pygame.K_DOWN:
                    game_mode.tetris.move_piece(0, 1)
        
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        handle_piece_move(event)
            
        if hud.pause_button.is_clicked(event):
            game_mode.pause()
            game_pause = not game_pause
            #打印game_over的值和game_pause的值
            # print("game_over:", game_over)
            # print("game_pause:", game_pause)
            # print()
            
        if hud.shop_button.is_clicked(event):
            game_mode.pause()
            game_pause = not game_pause
            game_mode.shop()
            
        if hud.battle_button.is_clicked(event):
            game_pause = False
            game_mode.switch_to_battle()
            
    handle_warrior_move()
    update()
    
    pygame.display.flip()
    clock.tick(FPS)
    
pygame.quit()
quit()