tetris_battle_game/
│── main.py                   # 游戏主入口
│── settings.py                # 游戏设置（窗口大小、颜色、速度等）
│── game_mode.py              # 维护游戏状态（勇士、BOSS、俄罗斯方块、道具等）
│── tetris/                    # 俄罗斯方块模块
│   ├── __init__.py
│   ├── tetris.py              # 俄罗斯方块逻辑
│   ├── piece.py               # 俄罗斯方块的方块定义
│── battle/                    # 勇士战斗模块
│   ├── __init__.py
│   ├── warrior.py             # 勇士角色控制
│   ├── boss.py                # BOSS逻辑
│   ├── combat.py              # 战斗系统（攻击、技能）
│── ui/                        # UI相关
│   ├── __init__.py
│   ├── hud.py                 # 头部 UI（积分、暂停、商店按钮）
│   ├── inventory.py           # 道具栏
│   ├── shop.py                # 商店界面
│── assets/                    # 存放图片、音效、字体等资源
│── utils/                     # 工具函数
│   ├── __init__.py
│   ├── helpers.py             # 计算碰撞、范围检测等工具函数
