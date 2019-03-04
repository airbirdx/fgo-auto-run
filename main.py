import cv2
import os
import numpy as np
import random
from PIL import Image
import operator
import time

from util.ats import screenshot
from util.initmp import init_tmp
from func.operation import scene_operation
from func.battle import training

from config import *




init_tmp()

if dbg_shoot:
    screenshot()
    exit()

if dbg_train:
    training()
    exit()


while True:
    screenshot()
    scene_operation()
    time.sleep(1)

print('//-------------------------------------------------//')
print('//-------   D  O  N  E    -------------------------//')
print('//-------------------------------------------------//')
print('//-------------------------------------------------//')
#
# from psn.psfunc import *
# from func.attack import *
# training()
# print(os.getcwd())


# def sh_for_training(rotation=0):
#     from util.default import tmp_path
#     # from util.
#     i = 0
#     while True:
#         file = tmp_path + f'/sh_{i}.png'
#         os.system('adb shell screencap -p /sdcard/tst.png')
#         os.system('adb pull /sdcard/tst.png ' + file)
#         # inv-clockwise dir
#         if rotation:
#             img = cv2.imread(file, 1)  # 1 is color, 0 is gray
#             for i in range(rotation):
#                 img = np.rot90(img)
#             cv2.imwrite(file, img)
#         time.sleep(0.2)
#         i += 1
#         print('[ - ] You can press Ctrl + C to exit the screenshoot for training ...')




