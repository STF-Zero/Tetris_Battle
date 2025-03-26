# 用于判断游戏类型是俄罗斯方块还是战斗系统。
# 若game_mode为True，则游戏类型为俄罗斯方块，否则为战斗系统。

from tetris.tetris import Tetris

class GameMode:
    def __init__(self):
        self.game_mode = True
        self.tetris = Tetris()
        
    def update(self):
        if self.game_mode:
            self.tetris.update()
        else:
            # TODO: 更新战斗系统
            pass
        
    def draw(self, screen):
        if self.game_mode:
            self.tetris.draw(screen)
        else:
            # TODO: 绘制战斗系统
            pass