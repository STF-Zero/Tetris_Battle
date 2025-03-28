# 用于判断游戏类型是俄罗斯方块还是战斗系统。
# 若game_mode为True，则游戏类型为俄罗斯方块，否则为战斗系统。

from tetris.tetris import Tetris

class GameMode:
    def __init__(self):
        self.game_mode = True
        self.tetris = Tetris()
        
    def pause(self):
        if self.game_mode:
            self.tetris.pause()
        else:
            # TODO: 暂停战斗系统
            pass
        
    def shop(self):
        if self.game_mode:
            self.tetris.shop()
        else:
            # TODO: 打开战斗系统商店
            pass
        
    def update(self, hud):
        if self.game_mode:
            self.tetris.update(hud)
        else:
            # TODO: 更新战斗系统
            pass
        
    def draw(self, screen, hud):
        if self.game_mode:
            self.tetris.draw(screen)
        else:
            # TODO: 绘制战斗系统
            pass
        hud.draw(screen)