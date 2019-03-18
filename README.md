fgo-auto-run

***基于 python3 + adb 的国服 FGO 半自动过图/刷材料脚本 (仅支持 1920x1080 分辨率 Android 手机)***

## 基本讲解

所有的运行参数调整，请修改`config.py`文件。

运行程序命令为，`python main.py`，在下文中简化为`RUN SCRIPT`。

`./cfg`路径下的文件，请在每一个类别的脚本运行前检查一下。

`./cfg`路径下需要有以下文件。

| 文件 | 简介 |
| ------ | ------ |
| task.png | 自动过图的任务，必须有，这是所有的起点 |
| material.png | 所需要刷取的素材（如果设定为刷多少个素材模式的话） |


### 注释某些不使用的参数

**！需要注意的是，当有些选项你不需要使用的时候，请在其前面加`#`符号进行注释。**

### 运行次数的参数

有关于运行次数，本脚本提供三种选择方式,**同时只能够使用一种模式**，其他两种需要手动注释掉。。
```python
run_times = 1                            # How many times do you want to run
# run_materials = 5                        # How many materials do you want to get
# run_apples = ['Ag', 1]                   # How many apple do you want to eat, only support 'Au' and 'Ag' apple
```

1. 运行 N 次某个任务，参数为`run_times`，只需要将其修改为你所需要的个数就好了。如果一管体力刷完了后还没有到你所设定的次数，它将会自动吃苹果，
    使用顺序如下`铜苹果`，`银苹果`和`金苹果`，苹果刷完后将不再运行，退出脚本。
   * 例如无限池的时候，你需要刷 20 个某副本，修改为`run_times = 20`即可。

2. 刷取 N 次材料，参数为`run_materials`，同样修改为你所需要的数值。需要说明的是，这里需要你在`./cfg`文件夹下防止你所需要刷取的素材小图标，并
    将其命名为`material.png`，而且本脚本只会记录你这次刷图，有没有目标素材掉落，如果掉落了2个或者更多，也只会按照1个来进行计算。所以如果脚本正常执
    行完，你所获取的材料数是`>= N`的。刷取过程中依然会自动吃苹果，顺序同上。
   * 例如你需要刷 20 个凶骨，设定`run_materials = 20`，并将`material.png`放到`./cfg`路径下即可。

3. 使用多少个什么样子的苹果，参数为`run_apples`，这里只有金银两种选择，因为铜苹果是不按照个数来选择的。那么当其刷够了所设定的数值后，就会自动停
    止运行。
   * 例如无限池想要刷取某个副本，一共刷取 20 个银苹果的体力，设定`run_apples = ['Ag', 20]`即可。

   * 金苹果代号为`Au`，两种均为元素缩写。


### 助战选择

本脚本支持选定助战，比如什么从者，什么礼装，还有什么技能。但是需要将你所设定的助战相关的图片放置在`./lib/support`文件夹下。

```python
default_support = [   # example # default support information # servant # skill # craft
    'meilin',         # servant
    '310',            # skill
    'craft'           # craft
]
```

**[图片]**

### 战斗选项

`default_servant_priority`为从者优先级，范围`0~5`，从者编号在`./cfg`里对应查找。

`default_color_priority`为色卡优先级，`R`表示`Blaster`，`G`表示`Quick`，`B`表示`Arts`，优先级越高的话放在最前面。

`default_skill`为技能释放相关参数，场上 3 个从者，一共 9 个技能，`abc`为第一位从者技能，`ijk`为第二位从者技能，`opq`为第三位从者技能，`xyz`为御主礼装技能。例如从者 1 的第一个技能为`a`。`(x)`为战斗中`turn`或`round`数，需要严格保证一个数字被括号括起来的形式。如果涉及指向性技能，例如孔明的1技能，写成以下形式`a31`，其中第一个字母为技能，后两个数字表示指向性，`31`表示选择三个从者中的第一个从者。如果场上有两个从者，应该为`a21`，一位从者类推。需要特别说明的关于换人礼装有一个特定的字母`s`，`s34`表示3号从者和4号从者换人操作。

`default_final`为宝具释放相关参数，`abc`分别表示第`123`位从者的宝具。

* `axx`表示一个战斗回合中三张指令卡，第一张为第一位从者的宝具卡，第二三张程序自动选卡。`
* `xab`表示一个战斗回合中三张指令卡，第一张程序自选，第二张为第一位从者宝具，第三张为第二位从者宝具。

`default_final_unit`表示释放技能或者释放宝具的单位，是以`turn`为单位还是`round`为单位，默认为`round`。

```python
default_servant_priority = [0, 1, 3, 2]  # servant priority # high(left) -> low(right)
default_color_priority = 'RBG'           # R -> Blaster, G -> Quick, B -> Arts # high(left) -> low(right)
default_skill = '(1)q(2)o(3)ac'   # skill _seq & final # (n) means for turn n # abc / ijk / opq / xyz / s
default_final = '(1)cxx(2)bxx(3)axx'     # a/b/c for final card... BaoJu(Pinyin)
default_final_unit = 'round'             # round(default) / turn
```

[图片]

### 其他选项

`dbg_shoot`截图选项，如果打开后`RUN SCRIPT`的话，只会截取当前手机屏幕图片到电脑，然后结束程序运行。

`dbg_train`基本不适用，也不多写了，可以无视掉。

`default_rotation`是旋转参数，为了调整截图到手机上的图片是不是`1920x1080`大小，排布如下图所示这种，如果不是，可以调整这个参数，范围为`0~3`。

[图片]

**注意**：这三个参数在不使用的时候请设定为0，不要注释掉，不然会引起程序异常退出。

```python
# for debug use
dbg_shoot = 1
dbg_train = 0

# rotation if needed
default_rotation = 0   # range : 0/1/2/3, 1 for meizu phone
```



## 环境搭建

本脚本仅支持python3，不支持python2。

### Mac

使用Homebrew工具安装python和adb.

* 安装 homebrew
  

[homebrew](https://brew.sh/)

* 安装 python3

```
brew install python3
```

* 安装 adb
  
```
brew cask install android-platform-tools
```

* 检查安卓设备

```
adb devices
```

* 安装 tesseract
  
```
brew install tesseract
```

* 使用 pip 安装脚本运行所需要的库

```
pip install pillow
pip install openpyxl
pip install opencv-python
pip install numpy
pip install pytesseract
```

* 安装 ImageMagick 来对png图片进行标准化，减少程序运行的warning (非必需)

```
brew install imagemagick
```

###  Windows

大致与Mac下相同。

* 安装python3并添加PATH变量，[Python](https://www.python.org/)
* 下载adb的服务并添加PATH变量，[adb shell](http://adbshell.com/downloads)，[配置adb环境变量](https://www.cnblogs.com/cnwutianhao/p/6557571.html)

* 使用 pip 安装脚本运行所需要的库 (同上)

## 小技能点

### 设定优先级

* 建议组好队伍后，先注释掉优先级
* 打开`冬木-X-G`副本，保持当前队伍，默认刷取第一次，获得前三个从者的LOGO肖像
* 之后更换队伍前3位与后3位从者，再刷取一次，获得后三位从者的LOGO肖像
* **注意**：第一次刷取完成后，要在`./cfg`中将`servant_x.png`先备份出来，不然下一次脚本开始，会先将其删除。(最好在`./cfg`下新建一个文件夹用于存放)

### 组队确认

* 脚本开始执行前，确认一下当前默认队伍与礼装是不是所想设定队伍，避免浪费不必要的AP。



## 几个例子

### 冬木 / 未确认坐标X-G / 刷图5次(或刷取5个凶骨)

* 设定task.png图片
* (如果刷取5个凶骨的话，需要material.png，推荐设定方式为在成功刷取的战利品界面截图，然后截屏后将其截取出来)
* 队伍礼装配好。在此我们设定三回合刷图，不挑选特定助战。
* 队伍简单介绍如下
  * abc  | opq  | xyz       | xyz / s (礼装技能)
  * 小莫 | 清姬 | 大英雄 | 梅林 | 助战 | 式姐
* 技能释放文字说明如下，
  * 第一回合大英雄三技能自充，然后没良心赏烟花
  * 第二回合梅林一技能群充，然后清姬烧烤
  * 第三回合礼装二技能给小莫充能，小莫自充，小莫宝具收尾

* 对应`config.py`文件如下

```python
run_times = 5
# run_materials = 5
# run_apples = ['Cu', 1]
# default_servant_priority = [0, 1, 3, 2] 
default_color_priority = 'RBG'
default_skill = '(1)q(2)o(3)y31abc'
default_final = '(1)cxx(2)bxx(3)axx'
default_final_unit = 'round'
# default_chain = 1
# default_support = [   # example 
#     '',         # meilin
#     '',      # skill_310
#     'event'      # bao shi weng
# ]

# for debug use
dbg_shoot = 0
dbg_train = 0
# rotation if needed
default_rotation = 0   # range : 0/1/2/3, 1 for meizu phone
```

* 如果设定**刷取5个凶骨**，将`run_materials`设定为5，注释其他两个选项



### 每日任务 / QP 本 / 刷图3次









## 设计框架

| 文件(夹)  | 作用简介                                                     |
| --------- | ------------------------------------------------------------ |
| cfg/      | 放置task，servant 以及 material 文件(如果有的话)             |
| db/       | 图片的数据库，比如常用task，support 以及 material            |
| func/     | 脚本运行中一些功能函数集散地                                 |
| lib/      | 脚本运行所进行图片比对的数据库，涵盖各种不同的界面           |
| psn/      | 一些图标的像素位置点信息，功能函数，以及 Class 自动生成脚本。每次更改完 excel 表格，都需要重新生成类 |
| tmp/      | 脚本运行中的临时文件存放地                                   |
| util/     | 脚本运行所需的基本函数集散地                                 |
| sh.png    | 手机截图                                                     |
| config.py | 配置文件                                                     |
| main.py   | 主程序                                                     |
| convert.py | png 转换工具                                                     |
