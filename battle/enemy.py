import pygame
import random

from settings import WIDTH, HEIGHT

RED = (255, 0, 0)
WHITE = (255, 255, 255)
pygame.font.init()
FONT = pygame.font.SysFont("SimHei", 16)

class Enemy:
    def __init__(self):
        self.radius = 15
        self.health = 50
        self.speed = 2
        self.spawn(WIDTH, HEIGHT)
        
    def spawn(self, width, height):
        spawn_edge = random.choice(['top', 'bottom', 'left', 'right'])
        if spawn_edge == 'top':
            self.x = random.randint(self.radius, width - self.radius)
            self.y = self.radius
        elif spawn_edge == 'bottom':
            self.x = random.randint(self.radius, width - self.radius)
            self.y = height - self.radius
        elif spawn_edge == 'left':
            self.x = self.radius
            self.y = random.randint(self.radius, height - self.radius)
        else:
            self.x = width - self.radius
            self.y = random.randint(self.radius, height - self.radius)
            
    def move_to(self, warrior):
        dx = warrior.x - self.x
        dy = warrior.y - self.y
        distance = (dx ** 2 + dy ** 2) ** 0.5
        if distance > 0:
            dx, dy = dx / distance, dy / distance
            self.x += dx * self.speed
            self.y += dy * self.speed
            
    def reduce_hp(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            self.spawn(WIDTH, HEIGHT)
            return True
        return False
    
    def draw(self, screen):
        pygame.draw.circle(screen, RED, (int(self.x), int(self.y)), self.radius)
        text_surface = FONT.render(f"{self.health}", True, WHITE)  # 白色字体
        text_rect = text_surface.get_rect(center=(self.x, self.y - self.radius - 5))  # 居中显示
        screen.blit(text_surface, text_rect)  # 绘制文