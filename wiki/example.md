📙 [刷图示例](https://github.com/airbirdx/fgo-auto-run/blob/master/wiki/example.md) → :house: **[返回主页](https://github.com/airbirdx/fgo-auto-run)**

1️⃣ [如何运行](https://github.com/airbirdx/fgo-auto-run/blob/master/wiki/howtorun.md) → 2️⃣ [参数详解](https://github.com/airbirdx/fgo-auto-run/blob/master/wiki/parameter.md) → 📙 [刷图示例](https://github.com/airbirdx/fgo-auto-run/blob/master/wiki/example.md) → :four: [配置环境](https://github.com/airbirdx/fgo-auto-run/blob/master/wiki/environment.md) → :five: [文件架构](https://github.com/airbirdx/fgo-auto-run/blob/master/wiki/architecture.md) → 1️⃣ [如何运行](https://github.com/airbirdx/fgo-auto-run/blob/master/wiki/howtorun.md)

---

# 示例总览

| 编号 | 简介                                                | 视频链接 | 备注            |
| ---- | --------------------------------------------------- | -------- | --------------- |
| 1    | 奥尔良 / 波尔多 / 刷图 1 次                         | ~~暂无~~ | 无技能，无宝具  |
| 2    | 冬木 / 未确认坐标 X-G / 刷图 5 次 (或刷取 5 个凶骨) | ~~暂无~~      | 有技能，有宝具  |
| 3    | 每日任务 / 40AP QP 本 / 刷图 3 次                   | ~~暂无~~      | 挑选特定助战    |
|      |                                                     |          | 有技能，有宝具 |

# 模式设定参考

助战模式代码

| 模式  | 简介 | 简介 (`满破 == 满破礼装 / 未满破 == 未满破礼装`)             |
| :---: | :---: | ------------------------------------------------------------ |
| `= 0` | 0    | 选择列表中第一个从者作为助战从者，此时自动忽略 `./cfg` 文件夹下的助战相关设定 |
| `> 0` | 1    | 礼装筛选过程中 **只选择满破**                                |
|       | 2    | 礼装筛选过程中 **优先选择满破**，如果没有，再选取出现过的 **未满破** |
|       | 3    | 礼装筛选过程中 **优先选择满破**，如果没有，再选取出现过的 **未满破** |
|       |      | 如果仍然没有，筛选助战时略过礼装，选择最后一次刷新中第一个助战从者 |

助战职阶代码

| 代码 | 0    | 1    | 2    | 3    | 4    | 5    | 6    | 7    | 8    | 9    |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 职阶 | 默认 | 剑   | 弓   | 枪   | 骑   | 术   | 杀   | 狂   | 全   | 特殊 |

技能代码

| 从者 1     | 从者 2    | 从者 3     | 御主礼装  | 换人 | 切换敌人 |
| :----: | :----: | :----: | :----: | :----: | :------: |
| a / b / c | i / j / k | o / p / q | x / y / z | s    |    v     |

config.py 文件

```python
# # # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - # # #
# # # - - - - - - - - - - - - - - - CONFIG  PARAMETER - - - - - - - - - - - - - - - # # #
# # # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - # # #
run_times = 1               # How many times do you want to run
# run_materials = 2         # How many materials do you want to get
# run_apples = ['Ag', 5]    # How many apple do you want to eat, support 'Au' / 'Ag' apple
# # # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - # # #
default_support_mode = 0       # range: 0/1/2/3
default_support_rank = 0       # range: 0/1/2/3/4/5/6/7/8/9
default_support_refresh = 1    # range: 0/1/2/3/...
# # # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - # # #
default_servant_priority = [0, 1, 3, 2]  # servant priority # high(left) -> low(right)
default_color_priority = 'RBG'           # R -> Blaster, G -> Quick, B -> Arts 
default_skill = '(1)q(2)o(3)ac'          # abc / ijk / opq / xyz / s / v
default_final = '(1)cxx(2)bxx(3)axx'     # a/b/c for final card... BaoJu(Pinyin)
default_final_unit = 'round'             # round(default) / turn
speed_ratio = 1                          # normal(=1), faster(>1), slower(<1)
default_chain = 0                        # range : 0/1/2/3 -> no / extra / color / auto
# # # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - # # #
default_rotation = 0        # range : 0/1/2/3, 1 for meizu phone
```

# 奥尔良 / 波尔多 / 刷图 1 次

:sunny: 不使用宝具，不使用技能

* 设定 `task.png` 图片，界面切换到副本界面
* 队伍以及礼装配好，不挑选特定助战
* 示例队伍设定如下

![example-1-team](https://github.com/airbirdx/fgo-auto-run/blob/master/wiki/media/ex1_team.png)

* 全程序自动选卡，色卡优先级保持默认，打开 `chain` 自动选卡功能，无技能，无宝具
* 对应 `config.py` 文件如下`( 为了篇幅控制，不使用变量已删除 )`

```python
run_times = 1               # How many times do you want to run
# run_materials = 2         # How many materials do you want to get
# run_apples = ['Ag', 5]    # How many apple do you want to eat, support 'Au' / 'Ag' apple
# # # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - # # #
default_color_priority = 'RBG'           # R -> Blaster, G -> Quick, B -> Arts 
default_chain = 1                        # range : 0/1/2/3 -> no / extra / color / auto
# # # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - # # #
default_rotation = 0        # range : 0/1/2/3, 1 for meizu phone
```

* `./cfg` 路径下文件

| 文件名   | 内容                |
| -------- | ------------------- |
| task.png | ![example-1-task](https://github.com/airbirdx/fgo-auto-run/blob/master/wiki/media/ex1_task.png) |

# 冬木 / 未确认坐标 X-G / 刷图 5 次 (或刷取 5 个凶骨)

* 设定 `task.png` 图片，界面切换到副本界面
* 如果刷取 5 个凶骨的话，另外 `./cfg` 下还需要 `material.png`
* 设定图片获取方式为在成功刷取的战利品界面截屏，将其截取出来
* 队伍以及礼装配好，在此我们设定三回合刷图，挑选「梅林」作为助战
* 示例队伍设定如下

![example-2-team](https://github.com/airbirdx/fgo-auto-run/blob/master/wiki/media/ex2_team.png)

* 技能释放文字说明如下，
	* 第一回合大英雄三技能自充，然后没良心赏烟花，触发自动换人，好友梅林加班
	* 第二回合梅林一技能群充，然后清姬烧烤
	* 第三回合玉藻喵宝具收尾，结束战斗

* 对应 `config.py` 文件如下`( 为了篇幅控制，不使用变量已删除 )`

```python
run_times = 5               # How many times do you want to run
# run_materials = 2         # How many materials do you want to get
# run_apples = ['Ag', 5]    # How many apple do you want to eat, support 'Au' / 'Ag' apple
# # # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - # # #
default_color_priority = 'RBG'           # R -> Blaster, G -> Quick, B -> Arts 
default_skill = '(1)q(2)o'               # abc / ijk / opq / xyz / s / v
default_final = '(1)cxx(2)bxx(3)axx'     # a/b/c for final card... BaoJu(Pinyin)
default_final_unit = 'round'             # round(default) / turn
# # # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - # # #
default_rotation = 0        # range : 0/1/2/3, 1 for meizu phone
```

* 如果设定 **刷取 5 个凶骨**，将 `run_materials` 设定为 5，注释或删除其他两个选项

* `./cfg` 路径下文件如下表所示

| 文件名       | 内容                                                         |
| ------------ | ------------------------------------------------------------ |
| task.png     | ![example-2-task](https://github.com/airbirdx/fgo-auto-run/blob/master/wiki/media/ex2_task.png) |
| material.png | ![example-2-material](https://github.com/airbirdx/fgo-auto-run/blob/master/wiki/media/ex2_material.png) |
| servant1.png | ![example-2-servant1](https://github.com/airbirdx/fgo-auto-run/blob/master/wiki/media/ex2_servant1.png) |
| servant2.png | ![example-2-servant2](https://github.com/airbirdx/fgo-auto-run/blob/master/wiki/media/ex2_servant2.png) |
| servant3.png | ![example-2-servant3](https://github.com/airbirdx/fgo-auto-run/blob/master/wiki/media/ex2_servant3.png) |

表格中有三个 `servant` 图片是因为助战栏中梅林可能有三种不同的立绘。

# 每日任务 / 40AP QP 本 / 刷图 3 次

* 设定 `task.png` 图片，界面切换到副本界面
* 队伍以及礼装配好。在此我们设定三回合刷图，助战**只**挑选搭配「蒙娜丽莎」礼装的「骑阶」从者
* 设定职阶刷新次数上限为 `1`
* 示例队伍设定如下

![example 3 team](https://github.com/airbirdx/fgo-auto-run/blob/master/wiki/media/ex3_team.png)

* 技能释放文字说明如下，
  * 第一回合大英雄三技能自充，R 姐自充，然后没良心赏烟花，触发自动换人，梅林加班
  * 第二回合直接宝具，R 姐骑马打门
  * 第三回合梅林一技能，R 呆毛宝具收尾

* 对应 `config.py` 文件如下`( 为了篇幅控制，不使用变量已删除 )`

```python
# # # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - # # #
# # # - - - - - - - - - - - - - - - CONFIG  PARAMETER - - - - - - - - - - - - - - - # # #
# # # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - # # #
run_times = 3               # How many times do you want to run
# run_materials = 2         # How many materials do you want to get
# run_apples = ['Ag', 5]    # How many apple do you want to eat, support 'Au' / 'Ag' apple
# # # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - # # #
default_support_mode = 1       # range: 0/1/2/3
default_support_rank = 4       # range: 0/1/2/3/4/5/6/7/8/9
default_support_refresh = 2    # range: 0/1/2/3/...
# # # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - # # #
default_color_priority = 'RBG'           # R -> Blaster, G -> Quick, B -> Arts 
default_skill = '(1)qc(3)o'              # abc / ijk / opq / xyz / s / v
default_final = '(1)cxx(2)axx(3)bxx'     # a/b/c for final card... BaoJu(Pinyin)
default_final_unit = 'round'             # round(default) / turn
# # # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - # # #
default_rotation = 0        # range : 0/1/2/3, 1 for meizu phone
```

* `./cfg` 路径下文件

| 文件名    | 内容                                                         |
| --------- | ------------------------------------------------------------ |
| task.png  | ![example-3-task](https://github.com/airbirdx/fgo-auto-run/blob/master/wiki/media/ex3_task.png) |
| craft.png | ![example-3-craft](https://github.com/airbirdx/fgo-auto-run/blob/master/wiki/media/ex3_craft.png) |






