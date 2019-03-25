📙 [参数详解](https://github.com/airbirdx/fgo-auto-run/blob/master/wiki/parameter.md) → :house: **[返回主页面](https://github.com/airbirdx/fgo-auto-run)**

:one: [如何运行](https://github.com/airbirdx/fgo-auto-run/blob/master/wiki/howtorun.md) → 📙 [参数详解](https://github.com/airbirdx/fgo-auto-run/blob/master/wiki/parameter.md) → :three: [刷图示例](https://github.com/airbirdx/fgo-auto-run/blob/master/wiki/example.md) → :four: [配置环境](https://github.com/airbirdx/fgo-auto-run/blob/master/wiki/environment.md) → :five: [文件架构](https://github.com/airbirdx/fgo-auto-run/blob/master/wiki/architecture.md) → 1️⃣ [如何运行](https://github.com/airbirdx/fgo-auto-run/blob/master/wiki/howtorun.md)

---

本章节中所提到的 `默认值` 为参数未定义或注释掉情况下的数值。

# 运行次数

:sunny: 本脚本提供三种选择方式，但 **同一次运行只能够使用一种模式**，其他两种需要手动注释掉。

:abcd: `run_times` 运行 `n` 次某个任务，默认值设定为 `-1` 。

* 如果一管体力刷完了后还没有到你所设定的次数，它将会自动吃苹果来增加 AP。

* 使用苹果优先级为 `铜苹果`，`银苹果` 和 `金苹果`。

* 当一种苹果消耗完以后，自动选择下一种苹果，所有苹果刷完后将不再运行，退出脚本。

---

:abcd: `run_materials` 刷取 `n` 次材料，默认值设定为 `-1` 。

* 这里需要在 `./cfg` 文件夹下放置你所需要刷取的素材图标。
* 素材图标为需要将其命名为 `material.png`。
* 本脚本只会记录你这次刷图，有无目标素材掉落，如果掉落了 2 个或者更多，也只会按照 1 个来进行计算。
* 所以如果脚本正常执行完，你所获取的材料数是 `>= n` 的。刷取过程中依然会自动吃苹果，顺序同上。

---

:abcd: `run_apples` 使用多少苹果刷取某一个副本。默认值为 `-1` 。

* 只有金银两种苹果选择。金苹果代号为 `Au` ，银苹果代号为 `Ag` 
* 当脚本刷够了所设定的数值后，就会自动停止运行。
  * 例如无限池想要刷取某个副本，一共刷取 5 个银苹果的体力
  * 设定 `run_apples = ['Ag', 20]` 即可

```python
run_times = 1             # How many times do you want to run
# run_materials = 2       # How many materials do you want to get
# run_apples = ['Ag', 5]  # How many apple do you want to eat, support 'Au' / 'Ag' apple
```


# 助战选择

☀️ 需要将你所设定的助战相关的图片放置在 `./lib/cfg` 文件夹下。可以为从者头像、技能或礼装。助战相关图片明明规则如下表所示。

| 类别 | 命名                                                         |
| ----- | ------------------------------------------------------------ |
| 从者 | support0/1/2/x.png `( 0/1/2.. 表示某一从者可能有多种头像立绘 )` |
| 技能 | skill.png                                                    |
| 礼装 | craft.png `( 如果几种不同的礼装选择，可以在设为 craft0/1/2.png )` |

:abcd: `default_support_mode` 设定助战选择模式，默认值设定为 `0`。

* 助战模式有以下几种可供选择。
  * `= 0` 表示不选择助战
  * `> 0` 表示选择特定助战
* 如果另外还指定了助战礼装，在 `mode > 0` 模式下还有几种细分模式，对应说明可参见下表。
  * 只有当 `./cfg` 路径下存在 `craft.png` 礼装文件的时候才会进行对应 `mode = 1/2/3` 的选择

| 模式  | 简介 | 简介 (`满破 == 满破礼装 / 未满破 == 未满破礼装`) |
| :---: | :---: | ------------------------------------------------------------ |
| `= 0` | 0    | 选择列表中第一个从者作为助战从者，此时自动忽略 `./cfg` 文件夹下的助战相关设定 |
| `> 0` | 1    | 礼装筛选过程中 **只选择满破** |
|       | 2   | 礼装筛选过程中 **优先选择满破**，如果没有，再选取出现过的 **未满破**|
|       | 3 | 礼装筛选过程中 **优先选择满破**，如果没有，再选取出现过的 **未满破** |
| |  | 如果仍然没有，筛选助战时略过礼装，选择最后一次刷新中第一个助战从者 |

---

:abcd: `default_support_rank` 为助战职阶，默认值设定为 `0` 。

* 详细参数设定见下表，

| 代码 |  0   |  1   |  2   |  3   |  4   |  5   |  6   |  7   |  8   |  9   |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 职阶 | 默认 |  剑  |  弓  |  枪  |  骑  |  术  |  杀  |  狂  |  全  | 特殊 |

* 其中，
  * `rank = 0` 为默认设定，即保持玩家游戏中当前的助战页面职阶，不进行切换改动
  * `rank = 8` 为全部职阶，对应助战界面 **第一个** 职阶位助战栏
  * `rank = 9` 为特殊职介，对应助战界面 **最后一个** 职阶位助战栏

* 可以通过此参数设定为你想要选择的助战职阶。
* 可以设定为一个职阶，也可以设定为部分职阶。
* 可以设定为数字或字符串，设定值见下表。例如，

```python
default_support_rank = 123     # 或 = '123'  # 表示从上三骑中选择符合条件的助战
default_support_rank = 4567    # 或 = '4567' # 表示从下四骑中选择符合条件的助战
default_support_rank = 89      # 或 = '89'   # 表示从 ' 全' 和 ' 特' 中选择符合条件的助战
default_support_rank = 20      # 或 = '20'   # 表示从弓阶选择合适的助战，'0' 将会被忽略
default_support_rank = 666     # 或 = '666'  # 表示从杀阶选择合适的助战，重复设定无效
```

---

:abcd: `default_support_refresh` 为助战列表刷新次数 `n`，默认值设定为 `1` 。

* 如果所设定职阶当前的助战列表中都没有刷取到符合设定的助战，那么将进行一次刷新，再次尝试匹配。
* 刷新 `n` 次后依然没有筛选到合适的助战，脚本将会给出提示，然后结束执行。

```python
# default_support_mode = 0       # range: 0/1/2/3
# default_support_rank = 0       # range: 0/1/2/3/4/5/6/7/8/9
# default_support_refresh = 1    # range: 0/1/2/3/...
```

# 战斗选项

:abcd: `default_servant_priority` 为从者优先级，默认值设定为 `[]` 。

* 从者编号 `0~5`，从者编号需要在 `./cfg` 里对应查找。
* `[1, 0, 3, 2]` 表示设定从者优先级 `servant1 > 0 > 3 > 2` 。

---

:abcd: `default_color_priority` 为色卡优先级，默认值设定为 `RBG` 。

* `R` 表示 `Blaster`，`G` 表示 `Quick`，`B` 表示 `Arts` 。
* `RBG`表示优先级 `Blaster > Arts > Quick` 。

---

:abcd: `default_skill` 为技能释放相关参数，默认值设定为 `NULL` 。

* 共 `abc / ijk / opq / xyz / s / v` 十四个技能代码。
* 参数中间可以自由添加空格增加可读性。

| 从者 1     | 从者 2    | 从者 3     | 御主礼装  | 换人 | 切换敌人 |
| :----: | :----: | :----: | :----: | :----: | :------: |
| a / b / c | i / j / k | o / p / q | x / y / z | s    |    v     |

* 说明 1，指向性技能，`a31` 将 `a` 技能释放给 3 个在场从者的第一位从者。
* 说明 2，换人技能，`s34` 使用换人礼装将队列中从者 3 与从者 4 交换。
* 说明 3，对敌人指向性技能，`a01` 将 `a` 技能对敌方 `1` 怪物或从者释放。
  * 第一个数字 `0` 表示向敌方释放技能，需要紧跟技能字母之后
  * 第二个数字表示敌方怪物或从者的编号
* 说明 4，切换敌人，`v1` 表示攻击目标切换为敌人 1，敌方与己方满配情况下的编号可参考下表，

| 敌方       |        |        | 中线 |        |        |   己方 |
| ---------- | :----: | :----: | :--: | :----: | :----: | -----: |
| ↖          |   ——   |   ——   |  +   |   ——   |   ——   |      ↗ |
| 敌人 3     | 敌人 2 | 敌人 1 |  \|  | 从者 1 | 从者 2 | 从者 3 |
| ↙ |   ——   |   ——   |  +   |   ——   |   ——   |      ↘ |

---

:abcd: `default_final` 为宝具释放相关参数，默认值设定为 `NULL` 。

* 如果本回合需要释放宝具，那么需要此参数。`a/b/c` 分别表示第 `1/2/3` 位从者的宝具。`x` 表示普通指令卡。

* `axx` 表示一个战斗回合三张指令卡中，第一张为 `从者 1 宝具卡`，第二三张为 `普通指令卡`。
* `xab` 表示一个战斗回合三张指令中卡，第一张为 `普通指令卡`，第二张为 `从者 1 宝具卡`，第三张为 `从者 2 宝具卡`。

---

:abcd: `default_final_unit` 为释放技能或者释放宝具的单位，默认值设定为 `round` 。

* 有两种单位可供选择， `turn` 和 `round` 。

---

:abcd: `speed_ratio` 为技能释放速度，默认值设定为 `1` 。

* 其主要调节的是技能之间的等待时间间隔的长短。
* 脚本内默认的非指向性技能间隔时间为 `3 s`，指向性技能为 `5 s`。
  * 此数据在小米 6 手机上通过测试
  * 如果你的手机性能较好，可以适当调快速度，降低等待时间
  * 但如果手机性能较差运行较慢，需要调慢速度，增加等待时间

* `speed_ratio = 2`，技能释放后等待时间将会缩短一倍。
* `speed_ratio = 0.5`，技能释放后等待时间将会延长一倍。

---

:abcd: `default_chain_mode` 为战斗中指令卡选择模式，默认值设定为 `0`。

* 一共提供四种模式选择，详细简介见下表，

| 模式  | 简介 | 简介 |
| ----- | ---- | ------------------------------------------------------------ |
| `= 0` | 0    | 不使用 `chian` 功能，默认按照 `从者优先级` 以及 `色卡优先级` 来进行选择 |
| `> 0` | 1    | 启用 `extra chain` **和** `color chain`，其中 `extra chain` 优先级较高 |
|       | 2   | 只启用 `extra chain` 判断选择 |
|       | 3 | 只启用 `color chain` 判断选择 |

```python
default_servant_priority = [0, 1, 3, 2]  # servant priority # high(left) -> low(right)
default_color_priority = 'RBG'           # R -> Blaster, G -> Quick, B -> Arts 
default_skill = '(1)q(2)o(3)ac'          # abc / ijk / opq / xyz / s / v
default_final = '(1)cxx(2)bxx(3)axx'     # a/b/c for final card... BaoJu(Pinyin)
default_final_unit = 'round'             # round(default) / turn
# speed_ratio = 1                        # normal(=1), faster(>1), slower(<1)
# default_chain = 0                      # range : 0/1/2/3 -> no / extra / color / auto
```

# 其它参数

:abcd: `default_rotation` 是旋转参数，默认值设定为 `0`。

* 为了调整截图到手机上的图片是不是 `1920x1080` 大小，`w = 1920, h = 1080` 。
* 如果不是，可以调整这个参数来旋转图像，范围为 `0~3`。

:sunny: 这个参数注意不要注释掉，不然会引起程序异常退出。

```python
default_rotation = 0        # range : 0/1/2/3, 1 for meizu phone
```

