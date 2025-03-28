import pygame
from settings import WIDTH, HEIGHT

WHITE = (255, 255, 255)
pygame.font.init()
FONT = pygame.font.SysFont("SimHei", 16)

class Warrior:
    def __init__(self, x, y, radius, color, speed, damage, health, initial_attack_range, max_attack_range, attack_cd):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.speed = speed
        self.damage = damage
        self.health = health
        self.initial_attack_range = initial_attack_range
        self.max_attack_range = max_attack_range
        self.attack_cd = attack_cd
        self.last_attack_time = pygame.time.get_ticks()
        self.is_attacking = False
        self.attack_range = self.initial_attack_range
        self.attack_speed = 5  # 扩散速度
        self.hit_enemies = set() # 记录当前攻击波次已经打过的敌人
        
    def move(self, dx, dy):
        new_x = dx * self.speed + self.x
        new_y = dy * self.speed + self.y
        left = new_x - self.radius
        right = new_x + self.radius
        top = new_y - self.radius
        bottom = new_y + self.radius
        if left < 0 or right > WIDTH or top < 0 or bottom > HEIGHT:
            return
        self.x = new_x
        self.y = new_y
        # print("Warrior moved to ({}, {})", self.x, self.y)
        
    def attack(self, enemies):
        # 开始攻击，重置攻击范围，进入攻击状态
        current_time = pygame.time.get_ticks()
        if current_time - self.last_attack_time >= self.attack_cd:       
            self.is_attacking = True
            self.attack_range = self.initial_attack_range
            self.last_attack_time = current_time
            # self.hit_enemies.clear()
        
        beat_num = 0 
        for enemy in enemies:
            if self.is_in_attack_range(enemy):
                if enemy.reduce_hp(self.damage):
                    beat_num += 1
                    enemies.remove(enemy)
        return beat_num
    
    def update_attack_range(self, enemies, last_attack_time):
        beat_num = 0
        beated = 0 # 代表是否发出攻击，0为发出攻击，1为未发出攻击
        self.attack_range += self.attack_speed
        if self.attack_range >= self.max_attack_range:
            self.attack_range = self.max_attack_range
            self.is_attacking = False
            
        current_time = pygame.time.get_ticks()
        if current_time - last_attack_time >= self.attack_cd:
            beated = 1
            for enemy in enemies:
                if self.is_in_attack_range(enemy):
                    if enemy.reduce_hp(self.damage):
                        beat_num += 1
                        enemies.remove(enemy)
            self.attack_range = self.initial_attack_range
        return beat_num, beated
    
    def is_in_enemy_range(self, target):
        # 计算目标与自己的距离
        distance = ((self.x - target.x)**2 + (self.y - target.y)**2) ** 0.5
        if distance <= self.radius:
            return True
        return False
    
    def is_in_attack_range(self, target):
        # 计算目标与自己的距离
        distance = ((self.x - target.x)**2 + (self.y - target.y)**2) ** 0.5 - target.radius - self.attack_range
        print("distance is ", distance)
        print("attack range is ", self.attack_range)
        if distance <= self.attack_range:
            print("attack range is ", self.attack_range)
            print("target in range")
            return True
        return False
    
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
        text_surface = FONT.render(f"{self.health}", True, WHITE)  # 白色字体
        text_rect = text_surface.get_rect(center=(self.x, self.y - self.radius - 5))  # 居中显示
        screen.blit(text_surface, text_rect)  # 绘制文本
        
        pygame.draw.circle(screen, (255, 255, 0), (self.x, self.y), self.attack_range, 2)  # 绘制攻击范围