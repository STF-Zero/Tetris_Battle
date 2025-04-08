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
        self.inventory_duration = 8000    # 道具持续时间，单位为毫秒，即8秒
        
        self.is_shelding = False
        self.is_damaging = False
        self.is_speeding = False
        self.is_attacking_speed = False
        self.is_attacking_range = False
        
        self.is_using_inventory = False
        
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
    
    def use_item(self, item):
        if not self.game_over:
            self.is_using_inventory = True
            if item == 0:
                # 治疗道具
                self.warrior.health += 20
                if self.warrior.health > 100:
                    self.warrior.health = 100
                self.is_using_inventory = False
            elif item == 1:
                # 护盾道具
                self.sheld_time = pygame.time.get_ticks()
                self.is_shelding = True
            elif item == 2:
                # 伤害道具
                self.damage_time = pygame.time.get_ticks()
                self.warrior.damage *= 2
                self.is_damaging = True
            elif item == 3:
                # 加速道具
                self.speed_time = pygame.time.get_ticks()
                self.warrior.speed *= 2
                self.is_speeding = True
            elif item == 4:
                # 攻击速度道具
                self.attack_speed_time = pygame.time.get_ticks()
                self.warrior.attack_cd /= 2
                self.warrior.attack_speed += 2
                self.is_attacking_speed = True
            elif item == 5:
                # 攻击范围道具
                self.attack_range_time = pygame.time.get_ticks()
                self.warrior.max_attack_range *= 1.5
                self.is_attacking_range = True
                 
    def update(self, hud, inventory):
        if not self.game_over:
            # 生成敌人
            current_time = pygame.time.get_ticks()
            if current_time - self.last_spawn_time >= self.spawn_cd:
                self.last_spawn_time = current_time
                self.enemies.append(Enemy())          
            # 移动敌人
            for enemy in self.enemies:
                enemy.move_to(self.warrior)    
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
                    if not self.is_shelding:
                        self.warrior.health -= enemy.health // 5  # 被撞击扣血
                    self.enemies.remove(enemy)
            
            if self.is_using_inventory:
                if self.is_shelding and current_time - self.sheld_time >= 5000:
                    self.is_shelding = False
                if self.is_speeding and current_time - self.speed_time >= self.inventory_duration:
                    self.warrior.speed /= 2
                    self.is_speeding = False
                if self.is_damaging and current_time - self.damage_time >= self.inventory_duration:
                    self.warrior.damage = int(self.warrior.damage / 2)
                    # 不进行int类型强制转换的话，血量会变成float类型
                    self.is_damaging = False
                if self.is_attacking_speed and current_time - self.attack_speed_time >= self.inventory_duration:
                    self.warrior.attack_cd *= 2
                    self.warrior.attack_speed -= 2
                    self.is_attacking_speed = False
                if self.is_attacking_range and current_time - self.attack_range_time >= self.inventory_duration:
                    self.warrior.max_attack_range /= 1.5
                    self.is_attacking_range = False
            
                    
            # 检查游戏胜负
            if self.warrior.health <= 0:
                self.game_over = True
                print("You lose!")
                return True
            if current_time - self.start_time >= self.duration:
                self.game_over = True
                print("You win!")
                return False

    def draw(self, screen):
        # 绘制战场
        bkg = pygame.image.load("assets/bkg.png")
        # 修改比例为1：1
        bkg = pygame.transform.scale(bkg, (WIDTH, HEIGHT))
        screen.blit(bkg, (0, 0))
        # 绘制角色
        self.warrior.draw(screen)
        # self.warrior.draw_health_bar(screen)
        for enemy in self.enemies:
            enemy.draw(screen)
