import pygame
from settings import BLOCK_SIZE

class Piece:
    def __init__(self, shape, color, x, y):
        self.shape = shape
        self.color = color
        self.x = x
        self.y = 0
        print("x=%d, y=%d" % (self.x, self.y))
        
    def get_rotated(self):
        return [list(row) for row in zip(*reversed(self.shape))]
    
    def draw(self, screen):
        for y, row in enumerate(self.shape):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(screen, self.color, (self.x * BLOCK_SIZE + x * BLOCK_SIZE, self.y * BLOCK_SIZE + y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))