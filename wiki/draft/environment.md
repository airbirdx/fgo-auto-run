:house: **[返回主页面](https://github.com/airbirdx/fgo-auto-run)**

**本脚本仅支持python3，不支持python2。**

# Mac

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

#  Windows

大致与Mac下相同。

* 安装python3并添加PATH变量，[Python](https://www.python.org/)
* 下载adb的服务并添加PATH变量，[adb shell](http://adbshell.com/downloads)，[配置adb环境变量](https://www.cnblogs.com/cnwutianhao/p/6557571.html)

* 使用 pip 安装脚本运行所需要的库 (同上)