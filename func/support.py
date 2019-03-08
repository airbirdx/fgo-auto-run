import os
import operator
import cv2

from util.ats import tap
from util.ats import swipe
from util.cvs import analyze
from util.cvs import position
from util.ats import picture_tap
from util.global0 import *
from util.scene import png_lst
from util.default import *
from psn.PSN import *


def update_match(match, name, support, px, py):
    for i in range(len(support)):
        # 加if保证改变后面的时候，前面已经更改过的的不变
        if support[i] is not None and support[i] in name:
            match[i] = int(support[i] in name)
            if i == 0:
                match.append(px)
                match.append(py)
    return match


# size = x1, x2, y1, y2
# im = sh[250:590, 50:1820]  # support 1
# size = 50, 1820, 250, 590
def match_support(size, support):
    sh = cv2.imread(screenshot_path, 0)
    x1, x2, y1, y2 = size
    im = sh[y1:y2, x1:x2]
    match = [0] * len(support)
    lst = png_lst(support_path)
    for file in lst:
        name, extension = os.path.splitext(file)
        tmp = cv2.imread(support_path + '/' + file, 0)
        thd = 0.85
        if analyze(im, tmp, thd):
            ps = position(im, tmp, thd)
            px = ps[0][0] + x1
            py = ps[0][1] + y1
            match = update_match(match, name, support, px, py)
    return match


def select_support():
    support = eval(rd_global('set_default_support'))
    sh = cv2.imread(screenshot_path, 0)
    # confirm = cv2.imread(support_path + '/confirm.png', 0)
    end = cv2.imread(support_path + '/end.png', 0)
    refresh = False

    if support[0] + support[1] + support[2] == '':
        w, h = sh.shape[::-1]
        tap(w // 2, int(h * 0.4))  # choose the first one
        return True

    # thd = 0.85
    if picture_tap(support_path + '/confirm.png'):    # 如果有确认刷新按键，点击
        pass

    sp = []
    for tmp in support:
        sp.append(int(tmp is not None))

    thd = 0.9
    if analyze(sh, end, thd):  # 设定为只刷新一次
        # 读取文件遍历一遍，看是否有低优先级合适的，没有的话再二次更新
        print('already check all ....')
        # press refresh button
        psn = PSN()
        psn.SUPPREF()
        if refresh:
            print('Can not find the support...')
            exit()
        else:
            refresh = True

    sizea = [support_sel_size_1, support_sel_size_2]

    for size in sizea:
        match = match_support(size, support)
        f = open(tmp_support, 'a+')
        f.writelines(str(match) + '\n')
        f.close()

        if operator.eq(sp, match[:3]):
            tap(match[3], match[4])
            return True

    x0 = support_swipe_parm[0]
    y0 = support_swipe_parm[1]
    x1 = support_swipe_parm[2]
    y1 = support_swipe_parm[3]
    d0 = support_swipe_parm[4]
    swipe(x0, y0, x1, y1, d0)
