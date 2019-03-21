📙 [刷图示例](https://github.com/airbirdx/fgo-auto-run/blob/master/wiki/example.md) → :house: **[返回主页面](https://github.com/airbirdx/fgo-auto-run)**

1️⃣ [如何运行](https://github.com/airbirdx/fgo-auto-run/blob/master/wiki/howtorun.md) → 2️⃣ [参数详解](https://github.com/airbirdx/fgo-auto-run/blob/master/wiki/parameter.md) → 📙 [刷图示例](https://github.com/airbirdx/fgo-auto-run/blob/master/wiki/example.md) → :four: [配置环境](https://github.com/airbirdx/fgo-auto-run/blob/master/wiki/environment.md) → :five: [文件架构](https://github.com/airbirdx/fgo-auto-run/blob/master/wiki/architecture.md) → 1️⃣ [如何运行](https://github.com/airbirdx/fgo-auto-run/blob/master/wiki/howtorun.md)

# 示例总览

* 奥尔良 / 波尔多 / 刷图 1 次 (无技能，无宝具)

* 冬木 / 未确认坐标 X-G / 刷图 5 次 (或刷取 5 个凶骨)

* 每日任务 / 40AP QP 本 / 刷图 3 次

~~☀️ 每个例子均有 B 站视频链接→TODO🌌~~

# 奥尔良 / 波尔多 / 刷图 1 次

:sunny: 不使用宝具，不使用技能

* 设定 task.png 图片，界面切换到副本界面
* 队伍礼装配好。不挑选特定助战
* 示例队伍设定如下

![example-1-team](https://github.com/airbirdx/fgo-auto-run/blob/master/wiki/media/ex1_team.png)

* 全程序自动选卡，打开 `chain` 选卡功能，无技能，无宝具
* 对应 `config.py` 文件如下

```python
# CONFIG PARAMETER
run_times = 1
# run_materials = 5
# run_apples = ['Ag', 1]

# default_support = 0
# default_craft_manpo = 2

# default_servant_priority = [0, 1, 3, 2]
default_color_priority = 'RBG'
# default_skill = '(1)q(2)o(3)y31abc'
# default_final = '(1)cxx(2)bxx(3)axx'
# default_final_unit = 'round'
# speed_ratio = 1   # normal(=1), faster(>1), slower(<1)
default_chain = 1

# rotation if needed
default_rotation = 0   # range : 0/1/2/3, 1 for meizu phone
```

* `./cfg` 路径下文件

| 文件名   | 内容                |
| -------- | ------------------- |
| task.png | ![example-1-task](https://github.com/airbirdx/fgo-auto-run/blob/master/wiki/media/ex1_task.png) |

# 冬木 / 未确认坐标 X-G / 刷图 5 次 (或刷取 5 个凶骨)

* 设定 task.png 图片，界面切换到副本界面
* 如果刷取 5 个凶骨的话，需要 material.png
* 设定图片获取方式为在成功刷取的战利品界面截屏，将其截取出来
* 队伍礼装配好。在此我们设定三回合刷图，挑选 "梅林" 作为助战
* 示例队伍设定如下

![example-2-team](https://github.com/airbirdx/fgo-auto-run/blob/master/wiki/media/ex2_team.png)

* 技能释放文字说明如下，
* 第一回合大英雄三技能自充，然后没良心赏烟花，触发自动换人，好友梅林加班
* 第二回合梅林一技能群充，然后清姬烧烤
* 第三回合玉藻喵宝具收尾，结束战斗

| 从者 1     | 从者 2    | 从者 3     | 御主礼装  | 换人 |
| --------- | --------- | --------- | --------- | ---- |
| a / b / c | i / j / k | o / p / q | x / y / z | s    |

* 对应 `config.py` 文件如下

```python
# CONFIG PARAMETER
run_times = 5
# run_materials = 5
# run_apples = ['Ag', 1]

# default_support = 0
# default_craft_manpo = 2

# default_servant_priority = [0, 1, 3, 2]
default_color_priority = 'RBG'
default_skill = '(1)q(2)o'
default_final = '(1)cxx(2)bxx(3)axx'
default_final_unit = 'round'
# speed_ratio = 1   # normal(=1), faster(>1), slower(<1)
# default_chain = 1

# rotation if needed
default_rotation = 0   # range : 0/1/2/3, 1 for meizu phone
```

* 如果设定 ** 刷取 5 个凶骨 **，将 `run_materials` 设定为 5，注释其他两个选项

* `./cfg` 路径下文件

| 文件名       | 内容                                                         |
| ------------ | ------------------------------------------------------------ |
| task.png     | ![example-2-task](https://github.com/airbirdx/fgo-auto-run/blob/master/wiki/media/ex2_task.png) |
| material.png | ![example-2-material](https://github.com/airbirdx/fgo-auto-run/blob/master/wiki/media/ex2_material.png) |
| servant1.png | ![example-2-servant1](https://github.com/airbirdx/fgo-auto-run/blob/master/wiki/media/ex2_servant1.png) |
| servant2.png | ![example-2-servant2](https://github.com/airbirdx/fgo-auto-run/blob/master/wiki/media/ex2_servant2.png) |
| servant3.png | ![example-2-servant3](https://github.com/airbirdx/fgo-auto-run/blob/master/wiki/media/ex2_servant3.png) |

表格中有三个 `servant` 是因为助战栏中梅林可能有三种不同的立绘。

# 每日任务 / 40AP QP 本 / 刷图 3 次

* 设定 task.png 图片，界面切换到副本界面
* 队伍礼装配好。在此我们设定三回合刷图，助战挑选 "蒙娜丽莎" 礼装
* 示例队伍设定如下

![example 3 team](https://github.com/airbirdx/fgo-auto-run/blob/master/wiki/media/ex3_team.png)

* 技能释放文字说明如下，
* 第一回合大英雄三技能自充，R 姐自充，然后没良心赏烟花，触发自动换人，梅林加班
* 第二回合直接宝具，R 姐骑马打门
* 第三回合梅林一技能，R 呆毛宝具收尾

| 从者 1     | 从者 2    | 从者 3     | 御主礼装  | 换人 |
| --------- | --------- | --------- | --------- | ---- |
| a / b / c | i / j / k | o / p / q | x / y / z | s    |

* 对应 `config.py` 文件如下

```python
# CONFIG PARAMETER
run_times = 3
# run_materials = 5
# run_apples = ['Ag', 1]

default_support = 0
default_craft_manpo = 1

# default_servant_priority = [0, 1, 3, 2]
default_color_priority = 'RBG'
default_skill = '(1)qc(3)o'
default_final = '(1)cxx(2)axx(3)bxx'
default_final_unit = 'round'
# speed_ratio = 1   # normal(=1), faster(>1), slower(<1)
# default_chain = 1

# rotation if needed
default_rotation = 0   # range : 0/1/2/3, 1 for meizu phone
```

* `./cfg` 路径下文件

| 文件名    | 内容                                                         |
| --------- | ------------------------------------------------------------ |
| task.png  | ![example-3-task](https://github.com/airbirdx/fgo-auto-run/blob/master/wiki/media/ex3_task.png) |
| craft.png | ![example-3-craft](https://github.com/airbirdx/fgo-auto-run/blob/master/wiki/media/ex3_craft.png) |






