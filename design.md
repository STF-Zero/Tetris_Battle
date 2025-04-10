# 游戏设计
## 游戏玩法
每一轮俄罗斯方块设置固定的时长，玩家通过控制俄罗斯方块，消除特殊增益方块后，勇士能力获得提升，时间结束后，可以选择继续进行俄罗斯方块获得增益，或者控制勇士进行战斗，挑战北理工恶龙。
每次打败恶龙，都会获得三个不同的大幅增益，玩家只能选择其中一个，然后选择进行俄罗斯方块或者继续下一轮恶龙挑战。
增加积分系统和商店系统，玩家可以利用消除方块积累的积分在商店购买增益或道具。

## 游戏规则
1. 俄罗斯方块消除规则：与传统俄罗斯方块一致。
2. 积分获取规则：每消除一行方块，获得x的积分。玩家选择的游戏难度hard_level（取值为1，2，3，分别代表easy，normal，hard）越大，每一行方块获得的积分越低（例如，x=120/hard_level）。同时，玩家可以在游戏过程中，自主提高方块下落的速度speed（取值为[1,2]），方块速度越快，x越大（例如，x=x*speed）。
3. 勇士战斗规则：在有限的方形窗口空间内，勇士和BOSS拥有各自的血量条。勇士每隔一段时间会自动对周围的圆形区域进行攻击，圆形区域内的BOSS会受到伤害。BOSS也会每隔一段时间对周围的圆形区域进行攻击，且BOSS会朝着勇士靠近。当BOSS血量降至0时，勇士获得胜利。当勇士血量降至0时，勇士失败。
4. 勇士战斗结束事件：若挑战成功，勇士获得三个不同的永久增益，玩家只能选择其中一个，同时，玩家也获得了一定量的积分，然后选择进行俄罗斯方块或者继续下一轮恶龙挑战。若挑战失败，玩家会根据对BOSS造成的伤害，获取一定数量的积分，然后选择进行俄罗斯方块或者继续下一轮恶龙挑战。
5. 商店规则：商店图标永远存在于游戏界面的正上方中间，玩家可以随时进入商店进行购买增益或道具。
6. 道具规则：道具指的是只能持续一段时间或者只能使用一次的道具，一段时间后或者使用过后就会消失。道具栏永远存在于游戏界面的右侧，呈竖直排列，玩家可以随时使用道具。道具分为两种，一种是增益道具，一种是战斗道具。
增益道具包括：移动加速道具、瞬间血量回复道具、攻击加速道具、攻击力增加道具、防御力增加道具、攻击范围提升道具。
战斗道具包括：炸弹道具（即瞬间伤害道具）、冰冻道具（即限制BOSS移动的道具）、毒药道具（即一段时间内降低BOSS防御力的道具）、火焰道具（即持续伤害道具）。
两种道具均为主动道具，用户在道具栏中点击相应道具即可使用。
7. 增益规则：增益指的是对勇士自身能力的提升。增益信息永远存在于游戏界面的左上方。增益分为两种，一种是永久增益，一种是临时增益。永久增益包括：攻击力增益、防御力增益、移动速度增益、攻击速度增益。临时增益包括：攻击力临时增益、防御力临时增益、移动速度临时增益、攻击速度临时增益。
8. 武器升级规则：武器分为三种，分别是普通武器、高级武器、顶级武器。普通武器可以升级为高级武器，高级武器可以升级为顶级武器。武器升级只能通过商店购买，升级后，武器攻击力、攻击速度、攻击范围都会增加。

## 游戏界面
### 俄罗斯方块界面
界面的最上方的中间，从左往右依次排列有暂停按钮、商店按钮和积分显示。
界面的右侧竖直排列有道具栏，道具栏中从上往下依次排列有增益道具和战斗道具，并显示各道具的数量。
界面的左上方显示有勇士的增益信息，包括永久增益和临时增益。
其余的部分为俄罗斯方块游戏界面，俄罗斯方块与其余的游戏界面元素相互独立，互不影响，它们占用的区域不会相交。
### 勇士战斗界面
界面的最上方的中间，从左往右依次排列有暂停按钮、商店按钮和积分显示。
界面的右侧竖直排列有道具栏，道具栏中从上往下依次排列有增益道具和战斗道具，并显示各道具的数量。
界面的左上方显示有勇士的增益信息，包括永久增益和临时增益。
其余的部分为勇士战斗游戏界面，勇士与其余的游戏界面元素可以相交，但战斗界面是最底层图层。

## 游戏道具
### 道具获取
玩家在俄罗斯方块游戏中，通过消除特殊增益方块，获得道具。道具分为两种，一种是增益道具，一种是战斗道具。这些特殊增益方块，是以一定的概率在方块生成时自动产生的。
可自动生成的增益/道具方块包括：移动加速方块、瞬间血量回复方块、攻击加速方块、攻击力增加方块、防御力增加方块、炸弹方块、冰冻方块、毒药方块、火焰方块。消除掉每块这样的方块后，道具栏中会增加一个相应的道具。
### 道具效果
#### 增益道具
1. 移动加速道具：使用后，勇士的移动速度提升，持续一段时间。
2. 瞬间血量回复道具：使用后，勇士的血量瞬间回复固定值。
3. 攻击加速道具：使用后，勇士的攻击速度提升，持续一段时间。
4. 攻击力增加道具：使用后，勇士的攻击力提升，持续一段时间。
5. 防御力增加道具：使用后，勇士的防御力提升，持续一段时间。
6. 攻击范围提升道具：使用后，勇士的攻击范围提升，持续一段时间。
#### 战斗道具
1. 炸弹道具：使用后，勇士对BOSS造成瞬间伤害。
2. 冰冻道具：使用后，BOSS的移动速度降低，持续一段时间。
3. 毒药道具：使用后，BOSS的防御力降低，持续一段时间。
4. 火焰道具：使用后，BOSS每隔一段时间受到持续伤害。