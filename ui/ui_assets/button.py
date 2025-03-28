import pygame

pygame.font.init()
FONT = pygame.font.SysFont("SimHei", 20)

class Button:
    def __init__(self, x, y, width, height, text, color, text_color):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.text_color = text_color
    
    def draw(self, region):
        pygame.draw.rect(region, self.color, self.rect)
        text_surface = FONT.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        region.blit(text_surface, text_rect)
        
    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                return True
        return False
        
