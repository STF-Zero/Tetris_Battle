import pygame
import random
from settings import *
from tetris.piece import Piece

SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 0, 0], [1, 1, 1]],  #J
    [[0, 0, 1], [1, 1, 1]],  # L
    [[1, 1], [1, 1]],  # O
    [[0, 1, 1], [1, 1, 0]],  # S
    [[0, 1, 0], [1, 1, 1]],  # T
    [[1, 1, 0], [0, 1, 1]],  # Z
]

COLORS = [
    (0, 255, 255),  # I - 青色
    (0, 0, 255),  # J - 蓝色
    (255, 165, 0),  # L - 橙色
    (255, 255, 0),  # O - 黄色
    (0, 255, 0),  # S - 绿色
    (128, 0, 128),  # T - 紫色
    (255, 0, 0),  # Z - 红色
]

AWARDS = ["money", "heal", "sheld", "speed", "damage", "attack_speed", "attack_range"]

class Tetris:
    def __init__(self):
        self.game_over = False
        self.current_piece = self.new_piece()
        self.grid = [[0] * GRID_WIDTH for _ in range(GRID_HEIGHT)]
        self.gold_grid = []
        self.is_clearing = False
        self.money = 0
        # 设置游戏难度，游戏难度为1easy，2normal，3hard
        self.hard_level = 1
        # 玩家手动设置的下落速度倍数，同时也是消除方块得分的倍数
        self.speed = 1
        # 实际的方块下落速度，单位为帧，值越小，方块下落越快
        self.drop_speed = 30 // (self.hard_level * self.speed)
        # 计时器
        self.frame_count = 0
        self.inventory_nums = [1, 1, 1, 1, 1, 1]  # 分别是heal, sheld, speed, damage, attack_speed, attack_range
        
    def pause(self):
        if not self.game_over:
            self.game_over = True
            print("游戏暂停")
        else:
            self.game_over = False
            print("游戏继续")
            
    def shop(self):
        # self.pause()
        print("进入游戏商店")
         
    def set_drop_speed(self, speed):
        self.drop_speed = speed
        
    def new_piece(self):
        # 每种形状的俄罗斯方块都对应其固定的颜色
        shape = random.choice(SHAPES)
        color = COLORS[SHAPES.index(shape)]
        
        # 计算方块宽度，确保不会超出边界
        piece_width = len(shape[0])
        piece_height = len(shape)
        max_x = GRID_WIDTH - piece_width
        
        # 生成随机 x 位置
        random_x = random.randint(0, max_x)
        return Piece(shape, color, random_x, -piece_height)
    
    def move_piece(self, dx, dy):
        if not self.check_collision(self.current_piece, dx, dy):
            self.current_piece.x += dx
            self.current_piece.y += dy
        elif dy > 0:
            self.lock_piece()
            if not self.game_over:
                self.current_piece = self.new_piece()   # 固定一个方块，自动创建新方块
            if self.check_collision(self.current_piece, 0, 0):
                self.game_over = True
                print("游戏结束")
                    
    def rotate_piece(self):
        # 获取旋转后的方块形状
        rotated_piece = self.current_piece.get_rotated()
        # 获取当前方块的原始位置
        origin_x = self.current_piece.x
        origin_y = self.current_piece.y
        
        # 计算旋转后的方块宽度和高度，确保不会超出边界
        rotated_width = len(rotated_piece[0])
        rotated_height = len(rotated_piece)
        
        # 预调整，防止旋转后超出边界
        new_x = max(0, min(self.current_piece.x, GRID_WIDTH - rotated_width))
        new_y = max(0, min(self.current_piece.y, GRID_HEIGHT - rotated_height))
        
        # 先尝试直接旋转
        if not self.check_collision_with_shape(rotated_piece, new_x, new_y):
            self.current_piece.shape = rotated_piece
            self.current_piece.x, self.current_piece.y = new_x, new_y
            return

        # 墙踢逻辑：尝试微调位置（左右移动）
        for dx in [-1, 1, -2, 2]:  # 先小调整，再大调整
            if not self.check_collision_with_shape(rotated_piece, new_x + dx, new_y):
                self.current_piece.shape = rotated_piece
                self.current_piece.x = new_x + dx
                self.current_piece.y = new_y
                return

        # 如果所有尝试都失败，恢复原始状态
        self.current_piece.x = origin_x
        self.current_piece.y = origin_y
        
    def check_collision(self, piece, dx, dy):
        for y, row in enumerate(piece.shape):
            for x, cell in enumerate(row):
                if cell:
                    new_x = piece.x + x + dx
                    new_y = piece.y + y + dy
                    if new_x < 0 or new_x >= GRID_WIDTH or new_y >= GRID_HEIGHT or self.grid[new_y][new_x]:
                        return True
                    # elif 
        return False
    
    def check_collision_with_shape(self, shape, x, y):
        for row_idx, row in enumerate(shape):
            for col_idx, cell in enumerate(row):
                if cell:  # 仅检测非空方块
                    new_x = x + col_idx
                    new_y = y + row_idx

                    # 检查是否超出边界
                    if new_x < 0 or new_x >= GRID_WIDTH or new_y >= GRID_HEIGHT:
                        return True
                    # 检查是否与已有方块重叠
                    if self.grid[new_y][new_x]:
                        return True
        return False
    
    def lock_piece(self):
        # if not self.is_clearing:
        # 随机选择一个方块单元，有概率变为金色
        gold_x, gold_y = None, None
        for y, row in enumerate(self.current_piece.shape):
            for x, cell in enumerate(row):
                if cell:
                    if random.random() < 0.075 and gold_x is None and gold_y is None:
                        # 只有第一个非空方块有机会变为金色
                        gold_x, gold_y = x, y
                        self.gold_grid.append((self.current_piece.x + gold_x, self.current_piece.y + gold_y))
                    
        # 将方块锁定到网格中
        for y, row in enumerate(self.current_piece.shape):
            for x, cell in enumerate(row):
                if cell:
                    self.grid[self.current_piece.y + y][self.current_piece.x + x] = self.current_piece.color
    
    def clear_lines(self):
        new_grid = [row for row in self.grid if any(cell == 0 for cell in row)]
        lines_cleared = GRID_HEIGHT - len(new_grid)
        # if lines_cleared > 0:
            # self.is_clearing = True
            
        cleared_rows = []  # 记录被消除行的 y 值
        for y, row in enumerate(self.grid):
            if all(cell != 0 for cell in row):  # 如果一行是满的
                cleared_rows.append(y)  # 记录满行的索引
        
        # 检查并触发金色方块被消除时的特殊事件
        for gold_x, gold_y in self.gold_grid:
            if gold_y in cleared_rows:  # 判断金色方块是否在被清除的行中
                self.trigger_special_event(gold_x, gold_y)  # 触发特殊事件
        
        for _ in range(lines_cleared):
            new_grid.insert(0, [0] * GRID_WIDTH)
            
        self.grid = new_grid

        # 删除被消除的金色方块坐标
        self.gold_grid = [(gold_x, gold_y) for gold_x, gold_y in self.gold_grid if gold_y not in cleared_rows]
        
        self.money += lines_cleared * self.speed * 10
            
            # self.is_clearing = False
        
    def trigger_special_event(self, gold_x, gold_y):
        print(f"金色方块在 ({gold_x}, {gold_y}) 被消除，触发特殊事件！")
        # 每次消除一个金色方块，都会从AWARDS中随机选择一种奖励方式
        award = random.choice(AWARDS)
        if award == "money":
            self.money += 100
            print("获得100金币！")
        elif award == "heal":
            self.inventory_nums[0] += 1
            print("获得1个血瓶！")
        elif award == "sheld":
            self.inventory_nums[1] += 1
            print("获得1个盾牌！")
        elif award == "speed":
            self.inventory_nums[2] += 1
            print("获得1个加速药水！")
        elif award == "damage":
            self.inventory_nums[3] += 1
            print("获得1个攻击药水！")
        elif award == "attack_speed":
            self.inventory_nums[4] += 1
            print("获得1个攻击速度药水！")
        elif award == "attack_range":
            self.inventory_nums[5] += 1
            print("获得1个攻击范围药水！")
        else:
            print("奖励出错")
            return
    
    def update(self, hud, inventory):
        self.frame_count += 1
        if self.frame_count >= self.drop_speed and not self.game_over:
            self.move_piece(0, 1)
            self.frame_count = 0
            self.clear_lines()
        hud.update_money(self.money)
        inventory.update(self.inventory_nums)
        # return False
            
    def draw(self, screen):
        bkg = pygame.image.load("assets/bkg.png")
        # 修改比例为1：1
        bkg = pygame.transform.scale(bkg, (WIDTH, HEIGHT))
        screen.blit(bkg, (0, 0))
        
        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(screen, cell, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
        
        # 闪烁效果：周期性变化
        for gold_x, gold_y in self.gold_grid:
        # 每隔一定时间切换颜色
            if self.frame_count % 40 < 20:  # 每15帧切换一次
                gold_color = (255, 215, 0)  # 金色
            else:
                gold_color = (255, 255, 255)  # 白色
            
            pygame.draw.rect(screen, gold_color, 
                         (gold_x * BLOCK_SIZE, gold_y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
          
        self.current_piece.draw(screen)
    