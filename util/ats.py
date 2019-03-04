import os
import random
import time
import datetime
import cv2
import numpy as np
from util.default import screenshot_path
from util.cvs import position
from util.cvs import analyze
from config import *

def click(x, y):
    cmd_tap = 'adb shell input tap {x0} {y0}'.format(
        x0=x,
        y0=y
    )
    print(cmd_tap)
    os.system(cmd_tap)


def swipe(x0, y0, x1, y1, delay0):
    cmd_swipe = 'adb shell input swipe {x2} {y2} {x3} {y3} {delay1}'.format(
        x2=x0,
        y2=y0,
        x3=x1,
        y3=y1,
        delay1=delay0
    )
    print(cmd_swipe)
    os.system(cmd_swipe)


# def long_tap(x, y):  # random length tap
#     delay = random.randrange(5, 100)
#     x0 = x + random.randrange(-10, 10)
#     y0 = y + random.randrange(-10, 10)
#     swipe(x, y, x0, y0, delay)


# tap on random location of the button
def tap(x, y, error=10):
    ct = datetime.datetime.now()            # current time
    cts = int(time.mktime(ct.timetuple()))  # current time timestamp
    random.seed(cts)
    x0 = x + random.randint(-error, error)
    y0 = y + random.randint(-error, error)
    click(x0, y0)


def screenshot():
    os.system('adb shell screencap -p /sdcard/tst.png')
    os.system('adb pull /sdcard/tst.png ' + screenshot_path)
    # inv-clockwise dir
    if default_rotation:
        img = cv2.imread(screenshot_path, 1)  # 1 is color, 0 is gray
        for i in range(default_rotation):
            img = np.rot90(img)
        cv2.imwrite(screenshot_path, img)


def random_tap():
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
    if thd is None:
        thd = 0.85
    sh = cv2.imread(screenshot_path, 0)
    tmp = cv2.imread(pic, 0)

    if analyze(sh, tmp, thd):
        ps = position(sh, tmp, thd)
        tap(ps[0][0], ps[0][1])
        return True
    else:
        return False

