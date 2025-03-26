import pygame
import random
from settings import *

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

class Tetris:
    def __init__(self):
        self.game_over = False
        self.current_piece = self.new_piece()
        self.grid = [[0] * GRID_WIDTH for _ in range(GRID_HEIGHT)]
        
        # 设置游戏难度，游戏难度为1easy，2normal，3hard
        self.hard_level = 1
        # 玩家手动设置的下落速度倍数，同时也是消除方块得分的倍数
        self.speed = 1
        # 实际的方块下落速度，单位为帧，值越小，方块下落越快
        self.drop_speed = 30 // (self.hard_level * self.speed)
        # 计时器
        self.frame_count = 0
        
        
    def new_piece(self):
        # 每种形状的俄罗斯方块都对应其固定的颜色
        shape = random.choice(SHAPES)
        color = COLORS[SHAPES.index(shape)]
        
        # 计算方块宽度，确保不会超出边界
        piece_width = len(shape[0])
        max_x = GRID_WIDTH - piece_width
        
        # 生成随机 x 位置
        random_x = random.randint(0, max_x)
        return Piece(shape, color, random_x)
    
    def move_piece(self, dx, dy):
        if not self.check_collision(self.current_piece, dx, dy):
            self.current_piece.x += dx
            self.current_piece.y += dy
        elif dy > 0:
            self.lock_piece()
            self.current_piece = self.new_piece()   # 固定一个方块，自动创建新方块
            if self.check_collision(self.current_piece, 0, 0):
                self.game_over = True
            # else:
            #     self.lock_piece()
            #     self.current_piece = self.new_piece()
        
    def rotate_piece(self):
        rotated_piece = self.current_piece.get_rotated()
        if not self.check_collision(self.current_piece, 0, 0):
            self.current_piece.shape = rotated_piece
        
    def check_collision(self, piece, dx, dy):
        for y, row in enumerate(piece.shape):
            for x, cell in enumerate(row):
                if cell:
                    new_x = piece.x + x + dx
                    new_y = piece.y + y + dy
                    if new_x < 0 or new_x >= GRID_WIDTH or new_y >= GRID_HEIGHT or self.grid[new_y][new_x]:
                        return True
        return False
    
    def lock_piece(self):
        for y, row in enumerate(self.current_piece.shape):
            for x, cell in enumerate(row):
                if cell:
                    self.grid[self.current_piece.y + y][self.current_piece.x + x] = self.current_piece.color
    
    def clear_lines(self):
        new_grid = [row for row in self.grid if any(cell == 0 for cell in row)]
        lines_cleared = GRID_HEIGHT - len(new_grid)
        for _ in range(lines_cleared):
            new_grid.insert(0, [0] * GRID_WIDTH)
        self.grid = new_grid
    
    def update(self):
        self.frame_count += 1
        
        if self.frame_count >= self.drop_speed and not self.game_over:
            self.move_piece(0, 1)
            self.frame_count = 0
        # if not self.game_over:
        #     self.move_piece(0, 1)
            
    def draw(self, screen):
        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(screen, cell, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
        self.current_piece.draw(screen)
    
class Piece:
    def __init__(self, shape, color, x):
        self.shape = shape
        self.color = color
        self.x = x
        self.y = 0
        
    def get_rotated(self):
        return [list(row) for row in zip(*reversed(self.shape))]
    
    def draw(self, screen):
        for y, row in enumerate(self.shape):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(screen, self.color, (self.x * BLOCK_SIZE + x * BLOCK_SIZE, self.y * BLOCK_SIZE + y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))