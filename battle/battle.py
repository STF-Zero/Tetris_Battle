import pygame
import random
from settings import *
from battle.warrior import Warrior
from battle.enemy import Enemy

BLUE = (0, 0, 255)
SHALLOW_BULE = (0, 0, 150)

class Battle:
    def __init__(self):
        # def __init__(self, x, y, radius, color, speed, damage, health, initial_attack_range, max_attack_range, attack_cd):
        self.warrior = Warrior(WIDTH//2, HEIGHT//2, 20, SHALLOW_BULE, 10, 20, 100, 20, 20*6, 800)
        # 每0.5秒攻击一次
        self.enemies = []
        self.last_spawn_time = pygame.time.get_ticks()
        self.spawn_cd = 2000    # 生成敌人的间隔时间，单位为毫秒
        self.start_time = pygame.time.get_ticks()
        self.duration = 30000    # 战斗时长设置为30秒
        self.last_attack_time = pygame.time.get_ticks()
        self.game_over = False
        
    def move_warrior(self, dx, dy):
        if not self.game_over:
            self.warrior.move(dx, dy)
        # self.warrior.update()
        
    def pause(self):
        self.game_over = not self.game_over
        
    def update(self, hud):
        if not self.game_over:
            # 生成敌人
            current_time = pygame.time.get_ticks()
            if current_time - self.last_spawn_time >= self.spawn_cd:
                self.last_spawn_time = current_time
                self.enemies.append(Enemy())
            
            # 移动敌人
            for enemy in self.enemies:
                enemy.move_to(self.warrior)

            # if current_time - self.last_attack_time >= self.warrior.attack_cd:
            # 角色自动攻击
            # dmoney = self.warrior.attack(self.enemies)
            # hud.update_money(hud.money + dmoney)
            # self.last_attack_time = current_time
            
            # print(self.last_attack_time)
            x = self.warrior.update_attack_range(self.enemies, self.last_attack_time)
            # print(x)
            if x[1]:
                # print("hit")
                dmoney = x[0]
                hud.update_money(hud.money + dmoney)
                self.last_attack_time = pygame.time.get_ticks()
                
            # 检测碰撞
            for enemy in self.enemies:
                if self.warrior.is_in_enemy_range(enemy):
                    self.warrior.health -= 10  # 被撞击扣血
                    self.enemies.remove(enemy)
                    
            # 检查游戏胜负
            if self.warrior.health <= 0:
                self.game_over = True
                print("You lose!")
                # return True
            if current_time - self.start_time >= self.duration:
                self.game_over = True
                print("You win!")
                # return False
        
    def draw(self, screen):
        self.warrior.draw(screen)
        # self.warrior.draw_health_bar(screen)
        for enemy in self.enemies:
            enemy.draw(screen)
