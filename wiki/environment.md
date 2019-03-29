📙 [配置环境](https://github.com/airbirdx/fgo-auto-run/blob/master/wiki/environment.md) → :house: **[返回主页](https://github.com/airbirdx/fgo-auto-run)**

1️⃣ [如何运行](https://github.com/airbirdx/fgo-auto-run/blob/master/wiki/howtorun.md) → 2️⃣ [参数详解](https://github.com/airbirdx/fgo-auto-run/blob/master/wiki/parameter.md) → 3️⃣ [刷图示例](https://github.com/airbirdx/fgo-auto-run/blob/master/wiki/example.md) → 📙 [配置环境](https://github.com/airbirdx/fgo-auto-run/blob/master/wiki/environment.md) → :five: [文件架构](https://github.com/airbirdx/fgo-auto-run/blob/master/wiki/architecture.md) → 1️⃣ [如何运行](https://github.com/airbirdx/fgo-auto-run/blob/master/wiki/howtorun.md)

---

:exclamation:`本脚本仅支持 python3，不支持 python2`

# MacOS

使用 Homebrew 工具安装 python 和 adb

* 安装 homebrew

[homebrew 官网](https://brew.sh/)

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

* 安装脚本运行所需要的其他库

```
python setup.py install
```
上述办法在网络不好时可能会失败，此时请使用使用 `pip` 手动安装脚本运行所需要的库

```
pip install pillow
pip install openpyxl
pip install opencv-python
pip install numpy
pip install pangu
pip install win10toast        # 只 windows 用户需要
```

* 安装 ImageMagick 来对 png 图片进行标准化，减少程序运行的警告` ( 非必需 )`

```
brew install imagemagick
```

#  Windows

大致与 Mac 下相同。

* 安装 python3 并添加 PATH 变量，[Python 官网](https://www.python.org/)
* 下载 adb 的服务并添加 PATH 变量，[adb shell](http://adbshell.com/downloads)，[配置 adb 环境变量](https://www.cnblogs.com/cnwutianhao/p/6557571.html)

* 安装脚本运行所需要的库 ( 同上 )

# ADB

* 连接手机
  * 手机打开「开发者模式」
  * 使用 USB 线材连接电脑与手机
  * 手机同意调试
* 连接虚拟机 `( 如果使用 )`
  * 虚拟机打开「开发者模式」
  * 输入以下命令进行连接

```
                               # 以网易 MuMu 为例
adb connect 127.0.0.1:7555     # win
adb connect 127.0.0.1          # mac
```
