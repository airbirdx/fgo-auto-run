# 示例目录

☀️ 每个例子均有 B 站视频链接

* XXXX / XXXX / 刷图1次(无技能，无宝具)
* 冬木 / 未确认坐标X-G / 刷图5次(或刷取5个凶骨)
* 每日任务 / 40AP QP 本 / 刷图 3 次

# XXX / XXX / 刷图1次

:sunny: 不使用宝具，不使用技能

* 设定task.png图片

![example 1 task]()

* 队伍礼装配好。不挑选特定助战
* 队伍简单介绍如下
  * 小莫 | 清姬 | 大英雄 | 梅林 | 助战 | 式姐
* 全程序选卡，打开`chain`选卡功能，无技能，无宝具

* 对应`config.py`文件如下

```python
# CONFIG PARAMETER
run_times = 1
# run_materials = 5
# run_apples = ['Cu', 1]
# default_support = 1
# default_servant_priority = [0, 1, 3, 2] 
default_color_priority = 'RBG'
# default_skill = '(1)q(2)o(3)y31abc'
# default_final = '(1)cxx(2)bxx(3)axx'
# default_final_unit = 'round'
# speed_ratio = 1   # normal(=1), faster(>1), slower(<1)
default_chain = 1

# for debug use
dbg_shoot = 0
dbg_train = 0
# rotation if needed
default_rotation = 0   # range : 0/1/2/3, 1 for meizu phone
```

* 如果设定**刷取5个凶骨**，将`run_materials`设定为5，注释其他两个选项

* `./cfg`路径下文件

![example 1 files in cfg path]()

* 效果视频:rocket:[XXX / XXXXXXXX]()

# 冬木 / 未确认坐标X-G / 刷图5次(或刷取5个凶骨)

* 设定task.png图片

![example 1 task]()

* (如果刷取5个凶骨的话，需要material.png，推荐设定方式为在成功刷取的战利品界面截图，然后截屏后将其截取出来)
* 队伍礼装配好。在此我们设定三回合刷图，不挑选特定助战
* 队伍简单介绍如下
  * 小莫 | 清姬 | 大英雄 | 梅林 | 助战 | 式姐
* 技能释放文字说明如下，
  * 第一回合大英雄三技能自充，然后没良心赏烟花
  * 第二回合梅林一技能群充，然后清姬烧烤
  * 第三回合礼装二技能给小莫充能，小莫自充，小莫宝具收尾

| 从者1     | servant 2 | 从者3     | 御主礼装  | 换人 |
| --------- | --------- | --------- | --------- | ---- |
| a / b / c | i / j / k | x / y / z | x / y / z | s    |

* 对应`config.py`文件如下

```python
# CONFIG PARAMETER
run_times = 8
# run_materials = 5
# run_apples = ['Cu', 1]
# default_support = 1
# default_servant_priority = [0, 1, 3, 2] 
default_color_priority = 'RBG'
default_skill = '(1)q(2)o(3)y31abc'
default_final = '(1)cxx(2)bxx(3)axx'
default_final_unit = 'round'
# speed_ratio = 1   # normal(=1), faster(>1), slower(<1)
# default_chain = 1

# for debug use
dbg_shoot = 0
dbg_train = 0
# rotation if needed
default_rotation = 0   # range : 0/1/2/3, 1 for meizu phone
```

* 如果设定**刷取5个凶骨**，将`run_materials`设定为5，注释其他两个选项

* `./cfg`路径下文件

![example 1 files in cfg path]()

* 效果视频:rocket:[冬木 / 未确认坐标X-G]()​ (只连续运行两次作为示例)

# 每日任务 / 40AP QP 本 / 刷图 3 次

* 设定task.png图片

![example 2 task]()

* 队伍礼装配好。在此我们设定三回合刷图，助战挑选"蒙娜丽莎"礼装
* 队伍简单介绍如下
  * 小莫 | 清姬 | 大英雄 | 梅林 | 助战 | 式姐
* 技能释放文字说明如下，
  * 第一回合大英雄三技能自充，R姐自充，然后没良心赏烟花
  * 第二回合直接宝具，R姐骑马打门
  * 第三回合梅林一技能，R呆毛宝具收尾

| 从者1     | servant 2 | 从者3     | 御主礼装  | 换人 |
| --------- | --------- | --------- | --------- | ---- |
| a / b / c | i / j / k | x / y / z | x / y / z | s    |

* 对应`config.py`文件如下

```python
# CONFIG PARAMETER
run_times = 3
# run_materials = 5
# run_apples = ['Cu', 1]
# default_support = 1
# default_servant_priority = [0, 1, 3, 2] 
default_color_priority = 'RBG'
default_skill = '(1)qa(3)o'
default_final = '(1)cxx(2)axx(3)bxx'
default_final_unit = 'round'
# speed_ratio = 1   # normal(=1), faster(>1), slower(<1)
# default_chain = 1

# for debug use
dbg_shoot = 0
dbg_train = 0
# rotation if needed
default_rotation = 0   # range : 0/1/2/3, 1 for meizu phone
```

* `./cfg`路径下文件

![example 2 files in cfg path]()

* 效果视频:rocket:[每日任务 / 40AP QP 本]()​ (只连续运行两次作为示例)





