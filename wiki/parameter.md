:house: **[返回主页面](https://github.com/airbirdx/fgo-auto-run)**

:sunny: ** 不需要使用的参数，请在其前面加 `#` 符号进行注释。**

# 运行次数

:sunny: 本脚本提供三种选择方式，但 ** 同一次运行只能够使用一种模式 **，其他两种需要手动注释掉。

`run_times` 运行 `N` 次某个任务。如果一管体力刷完了后还没有到你所设定的次数，它将会自动吃苹果来增加 AP， 使用苹果优先级为 `铜苹果`，`银苹果` 和 `金苹果`，一种苹果没有了之后，自动选择下一种苹果，所有苹果刷完后将不再运行，退出脚本。

`run_materials` 刷取 `N` 次材料。需要说明的是，这里需要你在 `./cfg` 文件夹下防止你所需要刷取的素材小图标，并将其命名为 `material.png`，而且本脚本只会记录你这次刷图，有没有目标素材掉落，如果掉落了 2 个或者更多，也只会按照 1 个来进行计算。所以如果脚本正常执行完，你所获取的材料数是 `>= N` 的。刷取过程中依然会自动吃苹果，顺序同上。

`run_apples` 使用多少苹果刷取某一个副本。这里只有金银两种苹果选择，因为这两种易于统计。那么当其刷够了所设定的数值后，就会自动停止运行。例如无限池想要刷取某个副本，一共刷取 20 个银苹果的体力，设定 `run_apples = ['Ag', 20]` 即可。另外，金苹果代号为 `Au`。

```python
run_times = 1             # How many times do you want to run
# run_materials = 5       # How many materials do you want to get
# run_apples = ['Ag', 1]  # How many apple do you want to eat, only support 'Au' and 'Ag' apple
```


# 助战选择

`default_support` 选择特定助战，为一个 list 参数，共三个元素，依次为从者、技能和礼装。

:sunny: 助战选择时，如果第一次列表中没有符合条件的助战，那么将会进行一次列表更新。如果第二次列表中仍然没有符合条件的助战，那么退出程序。

:sunny: 需要将你所设定的助战相关的图片放置在 `./lib/cfg` 文件夹下。​

助战相关图片明明规则如下表所示。

| 类别 | 命名                                                       |
| ---- | ---------------------------------------------------------- |
| 从者 | support0/1/2/3.png (0/1/2.. 表示某一从者可能有多种头像立绘) |
| 技能 | skill.png                                                  |
| 礼装 | craft.png                                                  |

`default_craft_manpo` 在设定助战的时候礼装满破的模式选择，一共有三种模式，如下表所示。

| 模式 | 简介                                                         |
| ---- | ------------------------------------------------------------ |
| 0    | 默认模式，不区分满破与未满破，从上到下依次筛选到礼装就进入下一环节 |
| 1    | 只选择满破礼装模式                                           |
| 2    | 优先选择满破礼装模式，当前列表中如果没有满破礼装，筛选是否有未满破礼装，如果有，选择未满破礼装 |

该参数在 `./cfg` 路径下没有设定 `craft.png` 的情况下都将保持默认模式，不论你在 `config.py` 中将其设定为了任何模式。


```python
# default_support = 1
# default_craft_manpo = 2
```

# 战斗选项

`default_servant_priority` 为从者优先级，范围 `0~5`，从者编号需要在 `./cfg` 里对应查找。

`default_color_priority` 为色卡优先级，`R` 表示 `Blaster`，`G` 表示 `Quick`，`B` 表示 `Arts`，优先级越高的话放在最前面。

`default_skill` 为技能释放相关参数，一共 `abc/ijk/opq/xyz/s` 共十三个技能代码。

| 从者 1     | 从者 2    | 从者 3     | 御主礼装  | 换人 |
| --------- | --------- | --------- | --------- | ---- |
| a / b / c | i / j / k | o / p / q | x / y / z | s    |

* 特例 1，指向性技能，`a31` 将 `a` 技能释放给 3 个在场从者的第一位从者
* 特例 2，换人技能，`s34` 使用换人礼装将队列中从者 3 与从者 4 交换

`default_final` 为宝具释放相关参数，如果本回合需要释放宝具，那么需要此参数。`abc` 分别表示第 `123` 位从者的宝具。

* `axx` 表示一个战斗回合中三张指令卡，第一张为第一位从者的宝具卡，第二三张程序自动选卡。
* `xab` 表示一个战斗回合中三张指令卡，第一张程序自选，第二张为第一位从者宝具，第三张为第二位从者宝具。

`default_final_unit` 为释放技能或者释放宝具的单位，是以 `turn` 为单位还是 `round` 为单位，默认为 `round`。

`speed_ratio` 为技能释放速度，其实调节的是技能之间的间隔时间，默认为 `1`，同时默认的非指向性技能间隔时间为 `3s`，指向性技能为 `5s`。此数据在小米 6 手机上通过测试。如果你的手机性能较好，可以适当调大，但如果手机性能较差运行较慢，需要调慢速度。

* `speed_ratio = 2`，技能释放后等待时间将会缩短一倍
* `speed_ratio = 0.5`，技能释放后等待时间将会延长一倍

`default_chain` 为战斗中指令卡是否优先选择 `chain`，`1` 表示使能此功能，`0` 表示不使能，默认为关闭。程序内部同一从者的 `chain` 优先级高于同一颜色的 `chain`。

```python
default_servant_priority = [0, 1, 3, 2]  # servant priority # high(left) -> low(right)
default_color_priority = 'RBG'  # R -> Blaster, G -> Quick, B -> Arts # high(left) -> low(right)
default_skill = '(1)q(2)o(3)ac'  # skill _seq & final # (n) means for turn n # abc / ijk / opq / xyz / s
default_final = '(1)cxx(2)bxx(3)axx'  # a/b/c for final card... BaoJu(Pinyin)
default_final_unit = 'round'  # round(default) / turn
# speed_ratio = 1   # normal(=1), faster(>1), slower(<1)
# default_chain = 1
```

# 其它参数

`default_rotation` 是旋转参数，为了调整截图到手机上的图片是不是 `1920x1080` 大小，排布如下图所示这种，如果不是，可以调整这个参数，范围为 `0~3`。

:sunny: 这个参数注意不要注释掉，不然会引起程序异常退出。

```python
# rotation if needed
default_rotation = 0   # range : 0/1/2/3, 1 for meizu phone
```

