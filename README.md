# **fgo-auto-run**

***基于 python3 + adb 的国服 FGO 「半自动」过图 / 刷材料 脚本 (仅支持 1920x1080 分辨率)***

# 特点

* 「半自动」是因为需要手动配置队伍以及助战，副本等参数
* 完全模拟用户操作运行，非劫持网络包
* 可支持手机，也可以支持模拟器，仅支持`1920x1080`分辨率
* 可自动过图 / 刷材料 （并不适用于所有副本，仅适用用重复性比较大的副本）
* 支持三种设定模式
  * 刷取某副本 `N` 次
  * 刷取某副本直到刷到 `N` 个某材料
  * 刷取某副本直到使用了 `N` 个设定的苹果(暂不支持圣晶石，因为本人福袋党)
* 战斗中可以自动识别 `extra chain` 和 `color chain`
* 支持掉线重连
* 可以自定义「助战从者」 / 「礼装」
* 如果攻略失败（脸黑），脚本将会自行撤退，再次进入副本尝试攻略
  * 编队时，请尽量确保队伍可以较为简单的获取胜利

# 详细文档

建议阅读完以下文档后再尝试运行

:one: [如何运行](https://github.com/airbirdx/fgo-auto-run/blob/master/wiki/howtorun.md) → :two: [参数详解](https://github.com/airbirdx/fgo-auto-run/blob/master/wiki/parameter.md) → :three: [刷图示例](https://github.com/airbirdx/fgo-auto-run/blob/master/wiki/example.md) → :four: [配置环境](https://github.com/airbirdx/fgo-auto-run/blob/master/wiki/environment.md) → :five: [文件架构](https://github.com/airbirdx/fgo-auto-run/blob/master/wiki/architecture.md) → :one: ​[如何运行](https://github.com/airbirdx/fgo-auto-run/blob/master/wiki/howtorun.md) 

# 使用场景

以下为作者曾经使用过的场景，在此记录一下。

脚本适用范围包括但不仅限于这些。

* 周常
  * 刷狗粮 / 刷 QP / 刷技能石
* 刷素材
  * 凶骨 / 羽毛 / ...
* 复刻：达芬奇与七位赝作英灵 轻量版
  * 图书馆刷心脏
* 复刻版：空之境界/the Garden of Order -Revival-
  * 停车场刷 QP

# 参考

本文在设计上参考了 [Meowcolm024/FGO-One](https://github.com/Meowcolm024/FGO-One) 

感谢各位曾经造的轮子

