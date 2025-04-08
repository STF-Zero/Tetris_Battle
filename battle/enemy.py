import pygame
import random

from settings import WIDTH, HEIGHT

RED = (255, 0, 0)
WHITE = (255, 255, 255)
pygame.font.init()
FONT = pygame.font.SysFont("SimHei", 16)

enemy1_icon = pygame.image.load("assets/enemy1.png")
enemy1_icon = pygame.transform.scale(enemy1_icon, (30, 30))

enemy2_icon = pygame.image.load("assets/enemy2.png")
enemy2_icon = pygame.transform.scale(enemy2_icon, (40, 40))

enemy3_icon = pygame.image.load("assets/enemy3.png")
enemy3_icon = pygame.transform.scale(enemy3_icon, (50, 50))

class Enemy:
    def __init__(self):
        self.health = random.choice([40, 60, 100])
        if self.health == 40:
            self.radius = 15
            self.speed = 2.5
            self.icon = enemy1_icon
            self.level = 1
        elif self.health == 60:
            self.radius = 20
            self.speed = 2
            self.icon = enemy2_icon
            self.level = 2
        else:
            self.radius = 25
            self.speed = 1
            self.icon = enemy3_icon
            self.level = 3
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
        # pygame.draw.circle(screen, RED, (int(self.x), int(self.y)), self.radius)
        screen.blit(self.icon, (int(self.x - self.radius), int(self.y - self.radius)))
        text_surface = FONT.render(f"{self.health}", True, WHITE)  # 白色字体
        text_rect = text_surface.get_rect(center=(self.x, self.y - self.radius - 5))  # 居中显示
        screen.blit(text_surface, text_rect)  # 绘制文本