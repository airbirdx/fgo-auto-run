import os
import random
import time
import datetime
import cv2
import subprocess
import platform
import numpy as np
from util.default import screenshot_path
from util.cvs import position
from util.cvs import analyze
from config import *


def click(x, y):
    '''
    点击屏幕坐标 x,y
    :param x:
    :param y:
    :return:
    '''
    cmd_click = 'adb shell input tap {x0} {y0}'.format(
        x0=x,
        y0=y
    )
    os.system(cmd_click)


def swipe(x0, y0, x1, y1, delay0):
    '''
    从 x0,y0 滑动到 x1,y1
    :param x0:
    :param y0:
    :param x1:
    :param y1:
    :param delay0:
    :return:
    '''
    cmd_swipe = 'adb shell input swipe {x2} {y2} {x3} {y3} {delay1}'.format(
        x2=x0,
        y2=y0,
        x3=x1,
        y3=y1,
        delay1=delay0
    )
    os.system(cmd_swipe)
    time.sleep(1)


# def long_tap(x, y):  # random length tap
#     delay = random.randrange(200, 1000)
#     x0 = x + random.randrange(-5, 5)
#     y0 = y + random.randrange(-5, 5)
#     swipe(x, y, x0, y0, delay)


# tap on random location of the button
def tap(x, y, error=10):
    '''
    点击坐标 x,y 引入一定范围随机性
    :param x:
    :param y:
    :param error:
    :return:
    '''
    ct = datetime.datetime.now()            # current time
    cts = int(time.mktime(ct.timetuple()))  # current time timestamp
    random.seed(cts)
    x0 = x + random.randint(-error, error)
    y0 = y + random.randint(-error, error)
    click(x0, y0)
    time.sleep(0.3)


def screenshot():
    '''
    获取手机截图
    :return:
    '''
    tmp_png = 'ts1t.png'

    filter_str = ''
    if platform.system() == 'Darwin':
        filter_str = '| grep FGO'

    subprocess.call(f'adb shell screencap -p /sdcard/{tmp_png}', shell=True, stdout=None)
    subprocess.call(f'adb pull /sdcard/{tmp_png} {screenshot_path} {filter_str}', shell=True, stdout=None)
    # os.system(f'adb shell screencap -p /sdcard/{tmp_png}')
    # os.system(f'adb pull /sdcard/{tmp_png} {screenshot_path}')
    # inv-clockwise dir
    if default_rotation:
        img = cv2.imread(screenshot_path, 1)  # 1 is color, 0 is gray
        for i in range(default_rotation):
            img = np.rot90(img)
        cv2.imwrite(screenshot_path, img)
    # time.sleep(1)


def random_tap():
    '''
    在屏幕上随机点触
    :return:
    '''
    sh = cv2.imread(screenshot_path, 0)
    set = 5
    w, h = sh.shape[::-1]
    ct = datetime.datetime.now()  # current time
    cts = int(time.mktime(ct.timetuple()))  # current time timestamp
    random.seed(cts)
    x = random.randint(w // set, w // set * (set - 1))
    y = random.randint(h // set, h // set * (set - 1))
    tap(x, y)
    


def picture_tap(pic, thd=None):
    '''
    点击截图中图片部分
    :param pic:
    :param thd:
    :return:
    '''
    if thd is None:
        thd = 0.85
    sh = cv2.imread(screenshot_path, 0)
    tmp = cv2.imread(pic, 0)

    if analyze(sh, tmp, thd):
        ps = position(sh, tmp, thd)
        w, h = tmp.shape[::-1]
        px = ps[0][0]
        py = ps[0][1]
        tap(px, py, int(0.3 * min(w, h)))  # +/- -> 0.6
        return True
    else:
        return False
    