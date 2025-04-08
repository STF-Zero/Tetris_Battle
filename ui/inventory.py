import pygame
from settings import WIDTH, HEIGHT, BLACK, WHITE
from ui.ui_assets import button as btn

pygame.font.init()
FONT = pygame.font.SysFont("SimHei", 20)
sFONT = pygame.font.SysFont("SimHei", 15)

health_icon = pygame.image.load('assets/health.png')
health_icon = pygame.transform.scale(health_icon, (20, 20))

shield_icon = pygame.image.load('assets/shield.png')
shield_icon = pygame.transform.scale(shield_icon, (20, 20))

damage_icon = pygame.image.load('assets/damage.png')
damage_icon = pygame.transform.scale(damage_icon, (20, 20))

speed_icon = pygame.image.load('assets/speed.png')
speed_icon = pygame.transform.scale(speed_icon, (20, 20))

attack_speed_icon = pygame.image.load('assets/attack_speed.png')
attack_speed_icon = pygame.transform.scale(attack_speed_icon, (20, 20))

attack_range_icon = pygame.image.load('assets/attack_range.png')
attack_range_icon = pygame.transform.scale(attack_range_icon, (20, 20))


class Inventory:
    def __init__(self):
        self.heal_button = btn.Button(WIDTH-60, 50, 30, 20, '治疗', BLACK, WHITE, health_icon)
        self.sheld_button = btn.Button(WIDTH-60, 80, 30, 20, '护盾', BLACK, WHITE, shield_icon)
        self.damage_button = btn.Button(WIDTH-60, 110, 30, 20, '伤害', BLACK, WHITE, damage_icon)
        self.speed_button = btn.Button(WIDTH-60, 140, 30, 20, '移速', BLACK, WHITE, speed_icon)
        self.attack_speed_button = btn.Button(WIDTH-60, 170, 30, 20, '攻速', BLACK, WHITE, attack_speed_icon)
        self.attack_range_button = btn.Button(WIDTH-60, 200, 30, 20, '范围', BLACK, WHITE, attack_range_icon)
        self.buttons = [self.heal_button, self.sheld_button, self.damage_button, self.speed_button, self.attack_speed_button, self.attack_range_button]
        
        self.inventory_nums = [0, 0, 0, 0, 0, 0]  # 分别对应：治疗、护盾、伤害、移速、攻速、范围
        
    def use_item(self, item_index, battle):
        if self.inventory_nums[item_index] > 0:
            self.inventory_nums[item_index] -= 1
            battle.use_item(item_index)
        
    def update(self, inventory_nums):
        n = 0
        for num in inventory_nums:
            self.inventory_nums[n] = num
            n += 1
        
    def draw(self, screen):
        # 绘制按钮
        for button in self.buttons:
            button.draw(screen)
        #在每个按钮的后方以较小的字体显示当前拥有的数量
        screen.blit(sFONT.render("x{}".format(self.inventory_nums[0]), True, WHITE), (WIDTH-25, 55))
        screen.blit(sFONT.render("x{}".format(self.inventory_nums[1]), True, WHITE), (WIDTH-25, 85))
        screen.blit(sFONT.render("x{}".format(self.inventory_nums[2]), True, WHITE), (WIDTH-25, 115))
        screen.blit(sFONT.render("x{}".format(self.inventory_nums[3]), True, WHITE), (WIDTH-25, 145))
        screen.blit(sFONT.render("x{}".format(self.inventory_nums[4]), True, WHITE), (WIDTH-25, 175))
        screen.blit(sFONT.render("x{}".format(self.inventory_nums[5]), True, WHITE), (WIDTH-25, 205))
        