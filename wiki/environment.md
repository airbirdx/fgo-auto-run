:house: **[返回主页面](https://github.com/airbirdx/fgo-auto-run)**

** 本脚本仅支持 python3，不支持 python2。**

# Mac

使用 Homebrew 工具安装 python 和 adb.

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

* 安装 ImageMagick 来对 png 图片进行标准化，减少程序运行的 warning (非必需)

```
brew install imagemagick
```

#  Windows

大致与 Mac 下相同。

* 安装 python3 并添加 PATH 变量，[Python](https://www.python.org/)
* 下载 adb 的服务并添加 PATH 变量，[adb shell](http://adbshell.com/downloads)，[配置 adb 环境变量](https://www.cnblogs.com/cnwutianhao/p/6557571.html)

* 使用 pip 安装脚本运行所需要的库 (同上)
