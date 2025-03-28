import pygame
# import main

def handle_input(event, game_mode):
    
    # 获取当前按下的键
    keys = pygame.key.get_pressed()
    
    # 如果游戏模式为tetris
    if game_mode.game_mode:
        # 如果游戏模式为tetris
        if game_mode.game_mode:
            
            # 如果按下空格键
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # 调用tetris的rotate_piece方法
                    game_mode.tetris.rotate_piece()
                    return
            
            if keys[pygame.K_s]:
                game_mode.tetris.move_piece(0, 1)
            elif keys[pygame.K_a]:
                game_mode.tetris.move_piece(-1, 0)
            elif keys[pygame.K_d]:
                game_mode.tetris.move_piece(1, 0)
            # main.update()
            print("piece is moving")
    else:
        if keys[pygame.K_s]:
            game_mode.battle.move_warrior(0, 1)
        elif keys[pygame.K_w]:
            game_mode.battle.move_warrior(0, -1)
        elif keys[pygame.K_a]:
            game_mode.battle.move_warrior(-1, 0)
        elif keys[pygame.K_d]:
            game_mode.battle.move_warrior(1, 0)
        print("warrior is moving")
            