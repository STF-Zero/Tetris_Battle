import pygame
from settings import WIDTH, BLACK, WHITE
from ui.ui_assets import button as btn

pygame.font.init()
FONT = pygame.font.SysFont("SimHei", 20)

class HUD:
    def __init__(self):
        pause_icon = pygame.image.load('assets/pause.png')
        pause_icon = pygame.transform.scale(pause_icon, (30, 30))
        
        shop_icon = pygame.image.load('assets/shop.png')
        shop_icon = pygame.transform.scale(shop_icon, (30, 30))
        
        battle_icon = pygame.image.load('assets/battle.png')
        battle_icon = pygame.transform.scale(battle_icon, (30, 30))
        
        self.pause_button = btn.Button(WIDTH*0.45, 2, 30, 30, '暂停', BLACK, WHITE, pause_icon)
        # self.shop_button = btn.Button(WIDTH*0.5, 2, 30, 30, '商店', BLACK, WHITE, shop_icon)
        self.battle_button = btn.Button(WIDTH*0.55, 2, 30, 30, '切换模式', BLACK, WHITE, battle_icon)
        self.money = 0
        
    def update_money(self, new_money):
        self.money = new_money
        
    def draw(self, screen):
        # 绘制按钮
        self.pause_button.draw(screen)
        # self.shop_button.draw(screen)
        self.battle_button.draw(screen)
        
        # 绘制金钱
        money_icon = pygame.image.load('assets/money.png')
        money_icon = pygame.transform.scale(money_icon, (20, 20))
        money_icon_rect = money_icon.get_rect(center=(WIDTH // 2, 50))
        screen.blit(money_icon, money_icon_rect)
        
        money_text = ": {}".format(self.money)
        money_surface = FONT.render(money_text, True, WHITE)
        money_rect = money_surface.get_rect(center=(WIDTH // 2 + 30, 50))  # 居中显示积分
        screen.blit(money_surface, money_rect)