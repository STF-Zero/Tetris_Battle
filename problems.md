### 问题1
关于键盘↓键的使用，当方块与边界或已有方块即将碰撞时，再按下↓键，会将game_over判定为true，导致游戏结束，如何解决？

### 问题2
在即将碰到已有方块时，再按下空格旋转方块，会导致方块插入方块中，如何解决？

<hr> 
以上两个问题均由rotate_piece、check_collision_with_shape函数解决（由AI生成）
<hr>

### 问题3
消除方块如何对hud中的分数进行更新？是否需要将hud作为参数传给tetris实例？
