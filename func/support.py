import os
import operator
import cv2
import math
import time
from util.ats import tap
from util.ats import swipe
from util.cvs import analyze
from util.cvs import position
from util.ats import picture_tap
from util.global0 import *
from util.scene import png_lst
from util.default import *
from psn.PSN import *


def update_match(match, name, support, px, py, flg):
    for i in range(len(support)):
        # 加if保证改变后面的时候，前面已经更改过的的不变
        if support[i] is not '' and support[i] in name:
            match[i] = int(support[i] in name)
            # if i == 0:
            #     match.append(px)
            #     match.append(py)
    match.append(px)
    match.append(py)

    if flg is not None:
        match.append(flg)

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
        thd = 0.9
        if analyze(im, tmp, thd):
            ps = position(im, tmp, thd)

            # px = ps[0][0] + x1
            # py = ps[0][1] + y1
            px = (x1 + x2) // 2  # 点击位置点为中心区域
            py = (y1 + y2) // 2

            set_sup_mod = None
            if 'craft' in name:
                w, h = tmp.shape[::-1]
                craft_im = sh[y1+int(0.6*(y2-y1)):y2, x1:x2]
                manpo_im = cv2.imread(support_path + '/manpo/manpo.png', 0)
                if analyze(craft_im, manpo_im, 0.85):
                    set_sup_mod = 1

            match = update_match(match, name, support, px, py, set_sup_mod)
    # match = ['servant', 'skill', 'craft', 'px', 'py']
    return match


def select_support():
    # para 1/2/3 in support -> servant/skill/craft
    support = eval(rd_global('set_default_support'))
    sh = cv2.imread(screenshot_path, 0)
    end = cv2.imread(support_path + '/end.png', 0)

    set_sup_mod = eval(rd_global('set_default_support_mode'))

    if not set_sup_mod or support[0] + support[1] + support[2] == '':
        w, h = sh.shape[::-1]
        tap(w // 2, int(h * 0.4))  # choose the first one
        return True

    # thd = 0.85
    if picture_tap(support_path + '/confirm.png'):    # 如果有确认刷新按键，点击
        time.sleep(2)   # 这里加上是为了防止出现加载中再次点击引起的误触发选择从者，不能删
        return False

    sp = []
    for tmp in support:
        sp.append(int(tmp != ''))

    thd = 0.9
    if analyze(sh, end, thd):  # 设定为只刷新一次
        # 读取文件遍历一遍，看是否有低优先级合适的，没有的话再二次更新

        swipe(1860, 1045, 1860, 120, 1500)  # 滑动到最上面

        if set_sup_mod >= 3:   # 如果模式设定为 3 / 4
            # swipe(1860, 1045, 1860, 120, 1500)   # 滑动到最上面
            f = open(tmp_support, 'r')
            lines = f.readlines()
            f.close()
            # line_num = 0
            for i in range(len(lines)):
                line = lines[i]
                line.replace('\n', '')
                # print(line)
                line_match = eval(line)
                if operator.eq(sp, line_match[:3]):
                    if line_match[2]:
                        line_num = i + 1

                        # 点击非满破卡
                        for n in range(math.ceil(line_num / 2) - 1):
                            x0, y0, x1, y1, d0 = support_swipe_parm
                            swipe(x0, y0, x1, y1, d0)
                            time.sleep(0.1)

                        if line_num % 2:
                            y1, y2, x1, x2 = support_sel_size_1
                        else:
                            y1, y2, x1, x2 = support_sel_size_2

                        px = (x1 + x2) // 2  # 点击位置点为中心区域
                        py = (y1 + y2) // 2

                        tap(px, py)

                        return True

        curr_refresh_num = eval(rd_global('tmp_sup_rfh'))
        set_refresh_num = eval(rd_global('set_default_support_refresh'))

        if curr_refresh_num < set_refresh_num:
            print('support list one has been checked... now refresh it...')
            # press refresh button
            psn = PSN()
            psn.SUPPREF()
            wt_global('tmp_sup_rfh', curr_refresh_num + 1)
            return False
        elif set_sup_mod == 4:   # 最后一次刷新，点击第一个助战从者
            w, h = sh.shape[::-1]
            tap(w // 2, int(h * 0.4))  # choose the first one
            return True
        else:
            print('No suitable [SUPPORT] option')
            toast('- No suitable [SUPPORT] option')
            exit()

    sizea = [support_sel_size_1, support_sel_size_2]

    for size in sizea:
        match = match_support(size, support)
        f = open(tmp_support, 'a+')
        f.writelines(str(match) + '\n')
        f.close()

        if operator.eq(sp, match[:3]):
            if set_sup_mod > 1:     # ( 2 / 3 / 4 都可以触发)
                if len(match) > 5:  # 满破礼装，len=6
                    tap(match[3], match[4])
                    return True
            elif set_sup_mod == 1:
                tap(match[3], match[4])
                return True

    x0, y0, x1, y1, d0 = support_swipe_parm
    swipe(x0, y0, x1, y1, d0)
