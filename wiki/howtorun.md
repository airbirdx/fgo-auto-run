📙 [如何运行](https://github.com/airbirdx/fgo-auto-run/blob/master/wiki/howtorun.md) → :house: **[返回主页面](https://github.com/airbirdx/fgo-auto-run)**

📙 [如何运行](https://github.com/airbirdx/fgo-auto-run/blob/master/wiki/howtorun.md) → 2️⃣ [参数详解](https://github.com/airbirdx/fgo-auto-run/blob/master/wiki/parameter.md) → :three: [刷图示例](https://github.com/airbirdx/fgo-auto-run/blob/master/wiki/example.md) → :four: [配置环境](https://github.com/airbirdx/fgo-auto-run/blob/master/wiki/environment.md) → :five: [文件架构](https://github.com/airbirdx/fgo-auto-run/blob/master/wiki/architecture.md) → 1️⃣ [如何运行](https://github.com/airbirdx/fgo-auto-run/blob/master/wiki/howtorun.md)

---

# 执行前准备

:sunny: 确保手机分辨率为 `1920x1080`，或使用模拟器并将分辨率设为 `1920x1080`。

* 构筑所用的队伍。由于当前版本不支持获取敌方信息，建议选择稳定的速刷队或者过图。
* 在设置中 **关闭**「灵基再临第四阶段展示」选项，可以减少一部分助战识别的工作量。
* 手动进行一场对战 ( 非必需，用于选中队伍以及调整相关设置 )。
* 在战斗菜单中 **关闭**「技能使用确认」和「宝具匀速」，**打开**「缩短敌人消失时间」（不关闭可能会因为技能释放间隔不够而引发错误）。
* 在选择指令卡界面调整游戏速度为 2 倍速。
* 将游戏置于进入任务前的界面。

# 参数设定

* 修改 `config.py` 文件，将参数设定为自己需要的参数。
* 准备好以下图片作为程序正常运行的前提。

| 编号 | 文件               | 说明                                                         |
| ---- | ------------------ | ------------------------------------------------------------ |
| 1    | task.png           | 必需                                                         |
| 2    | material.png       | 非必需，如果有相关设定则为必需 (设定刷取多少个某种材料)      |
| 3.1  | support0/1/2/x.png | 非必需，如果有相关设定则为必需 (设定了指定助战)(0/1/2.. 表示某一从者可能有多种头像立绘) |
| 3.2  | skill.png          | 非必需，如果有相关设定则为必需 (设定了指定助战以及其技能)    |
| 3.3  | craft.png          | 非必需，如果有相关设定则为必需 (设定了指定礼装)              |
| 4.x  | servant0/1/2/x.png | 非必需，如果有相关设定则为必需 (手动设定从者优先级)          |

# 运行程序

在程序目录下，打开命令行，运行程序即可。

```python
python3 main.py
```

windows 系统下如果只安装了 python3，可能执行上面的会提示错误，那么请尝试
```python
python main.py
```

# 截图功能

本程序还提供一种 `快速截图` 模式，只需要你在运行程序的时候多输入一个参数，不论是数字还是字符串，程序将只返回当前屏幕截图。

任意数字

```python
python main.py 123
```

或者，任意字符串

```python
python main.py hello
```

