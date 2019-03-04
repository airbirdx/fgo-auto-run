import os
import cv2

from util.default import screenshot_path
from util.default import fail_path
from util.scene import curr_png_lst
from util.cvs import position
from util.cvs import analyze
from util.ats import tap
from util.ats import random_tap


def withdrawn():
    sh = cv2.imread(screenshot_path, 0)
    lst = curr_png_lst(fail_path)
    for file in lst:
        tmp = cv2.imread(file, 0)
        thd = 0.85
        if analyze(sh, tmp, thd):
            ps = position(sh, tmp, thd)
            tap(ps[0][0], ps[0][1])
