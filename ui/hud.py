import pygame
from settings import WIDTH
from ui.ui_assets import button as btn

#定义三原色和白色的RGB值
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.font.init()
FONT = pygame.font.SysFont("SimHei", 20)

class HUD:
    def __init__(self):
        self.pause_button = btn.Button(WIDTH*0.35, 2, 50, 20, '暂停', BLACK, WHITE)
        self.shop_button = btn.Button(WIDTH*0.5, 2, 50, 20, '商店', BLACK, WHITE)
        self.battle_button = btn.Button(WIDTH*0.65, 2, 50, 20, '战斗', BLACK, WHITE)
        self.money = 0
        
    def update_money(self, new_money):
        self.money = new_money
        
    def draw(self, screen):
        # 绘制按钮
        self.pause_button.draw(screen)
        self.shop_button.draw(screen)
        self.battle_button.draw(screen)
        # 绘制金钱
        money_text = "Money: {}".format(self.money)
        money_surface = FONT.render(money_text, True, WHITE)
        money_rect = money_surface.get_rect(center=(WIDTH // 2, 50))  # 居中显示积分
        screen.blit(money_surface,money_rect)