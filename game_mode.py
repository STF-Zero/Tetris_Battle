# 用于判断游戏类型是俄罗斯方块还是战斗系统。
# 若game_mode为True，则游戏类型为俄罗斯方块，否则为战斗系统。

from tetris.tetris import Tetris
from battle.battle import Battle

class GameMode:
    def __init__(self):
        self.game_mode = True
        self.tetris = Tetris()
        self.battle = Battle()
        
    def pause(self):
        if self.game_mode:
            self.tetris.pause()
        else:
            self.battle.pause()
        
    def shop(self):
        if self.game_mode:
            self.tetris.shop()
        else:
            # TODO: 打开战斗系统商店
            pass
        
    def switch_mode(self):
        if self.game_mode:
            # self.pause()
            self.game_mode = False
        else:
            self.game_mode = True
            # self.pause()
        
    def update(self, hud, inventory):
        if self.game_mode:
            self.tetris.update(hud, inventory)
        else:
            self.battle.update(hud, inventory)
            # pass
        
    def draw(self, screen, hud, inventory):
        if self.game_mode:
            self.tetris.draw(screen)
        else:
            self.battle.draw(screen)
            # pass
        hud.draw(screen)
        inventory.draw(screen)