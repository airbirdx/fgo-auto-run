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
    return match


def select_support():
    sup_rank = rd_global('set_default_support_rank')
    tmp_sup_rank = eval(rd_global('tmp_sup_rank'))  # rank, flag
    rank, flag = tmp_sup_rank

    if flag == 1:       # 说明当前的扫描完了，需要切换下一个
        # 判断一下是不是最后一个了
        # 如果是，直接退出选择以及脚本
        if list(sup_rank).index(rank) == len(sup_rank) - 1:
            print('NONONONONO SUPPORT~~~!!!')
            toast('NONONONONO SUPPORT~~~!!!')
            exit()
        # 如果不是，那么自动向后选择一个新的rank
        else:
            new_rank = sup_rank[list(sup_rank).index(rank) + 1]
            new_flag = 0

            psn = PSN()
            eval('psn.ZHIJIE%s()' % new_rank)

            wt_global('tmp_sup_rank', [new_rank, new_flag])
            return True
    # 如果当前是第一个 rank
    elif list(sup_rank).index(rank) == 0:
        psn = PSN()
        eval('psn.ZHIJIE%s()' % rank)
        pass
    else: # 当前的没扫描完
        pass









    # 如果当前的 rank 小于所有的rank
    if list(sup_rank).index(rank) < len(sup_rank):
        # 如果是第一个rank
        if list(sup_rank).index(rank) == 0:






    # if list(sup_rank).index(tmp_sup_rank[10]) < len(sup_rank) - 1:
    #     if not tmp_sup_rank[1]:
    #         psn = PSN()
    #         eval('psn.ZHIJIE%s()' % tmp_sup_rank[0])
    #         return True
    # elif list(sup_rank).index(tmp_sup_rank[10]) == len(sup_rank) - 1:
    #     if not tmp_sup_rank[1]:
    #         if tmp_sup_rank[1] != '0':
    #             psn = PSN()
    #             eval('psn.ZHIJIE%s()' % tmp_sup_rank[0])
    #         return True
    #     else:


    select_support0()


def select_support0():
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

        if set_sup_mod > 1:   # 如果模式设定为 3 / 4
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
        elif set_sup_mod == 3:   # 最后一次刷新，模式3需要选择第一张卡，那么点击第一个助战从者
            w, h = sh.shape[::-1]
            tap(w // 2, int(h * 0.4))  # choose the first one
            return True
        else:
            print('No suitable [SUPPORT] option in this rank')
            tmp_sup_rank = eval(rd_global('tmp_sup_rank'))  # rank, flag
            tmp_sup_rank[1] = 1
            wt_global('tmp_sup_rank', tmp_sup_rank)
            return False

    sizea = [support_sel_size_1, support_sel_size_2]

    for size in sizea:
        match = match_support(size, support)
        f = open(tmp_support, 'a+')
        f.writelines(str(match) + '\n')
        f.close()

        if operator.eq(sp, match[:3]):
            if set_sup_mod > 0:     # ( 1/2/3 都可以触发，只要有满破礼装)
                if len(match) > 5:  # 满破礼装，len=6
                    tap(match[3], match[4])
                    return True
            # elif set_sup_mod == 1:
            #     tap(match[3], match[4])
            #     return True

    x0, y0, x1, y1, d0 = support_swipe_parm
    swipe(x0, y0, x1, y1, d0)
