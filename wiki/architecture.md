:orange_book: [文件架构](https://github.com/airbirdx/fgo-auto-run/blob/master/wiki/architecture.md) → 🏠 **[返回主页面](https://github.com/airbirdx/fgo-auto-run)**

1️⃣ [如何运行](https://github.com/airbirdx/fgo-auto-run/blob/master/wiki/howtorun.md) → 2️⃣ [参数详解](https://github.com/airbirdx/fgo-auto-run/blob/master/wiki/parameter.md) → 3️⃣ [刷图示例](https://github.com/airbirdx/fgo-auto-run/blob/master/wiki/example.md) → 4️⃣ [配置环境](https://github.com/airbirdx/fgo-auto-run/blob/master/wiki/environment.md) → :orange_book: [文件架构](https://github.com/airbirdx/fgo-auto-run/blob/master/wiki/architecture.md) → 1️⃣ [如何运行](https://github.com/airbirdx/fgo-auto-run/blob/master/wiki/howtorun.md)

# 文档架构

| 文件 (夹)  | 作用简介                                                     |
| --------- | ------------------------------------------------------------ |
| cfg/      | 放置 `task`，`support` 以及 `servant` 和 `material` 文件 `( 如果有的话 )`         |
| db/       | 图片的数据库，比如常用 `task`，`support` 以及 `material` 可以先在里面找找看有没有            |
| func/     | 脚本运行中一些功能函数                              |
| lib/      | 脚本运行所进行图片比对的数据库，涵盖各种不同的界面           |
| psn/      | 一些图标的像素位置点信息，功能函数，以及 `Class` 自动生成脚本。每次更改完对应的 `excel` 表格，都需要重新使用脚本生成对应类 |
| tmp/      | 脚本运行中的临时文件存放地                                   |
| util/     | 脚本运行所需的基本函数                                 |
| wiki/ | 脚本说明文档 |
| sh.png    | 游戏界面截图                                                 |
| config.py | 配置文件                                                     |
| main.py   | 主程序                                                     |
