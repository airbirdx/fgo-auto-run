import os
import operator
import cv2
import math
import time
from util.ats import tap
from util.ats import swipe
from util.cvs import *
# from util.cvs import position
from util.ats import picture_tap
from util.global0 import *
from util.scene import png_lst
from util.default import *
from psn.PSN import *
from util.log import *
from util.ats import screenshot


# 0 - 无特殊指定，选择第一个
# 1 - 选择指定[从者]/[礼装]作为助战，并根据是否有[技能]图片和[满破]图片进行模糊选择
# 2 - 选择指定[从者]/[礼装]作为助战，并根据是否有[技能]图片和[满破]图片进行精确选择


def tap_support(num):
    """
    点击助战， 1/2(正数第一第二) and 8/9（倒数第二第一）
    :param num:
    :return:
    """
    sh = cv2.imread(screenshot_path, 0)
    w, h = sh.shape[::-1]
    if num == 1:
        tap(w // 2, int(h * 0.4))  # choose the first one
    elif num == 2:
        tap(w // 2, int(h * 0.65))  # choose the 2 one
    elif num == 8:
        tap(w // 2, int(h * 0.5))  # choose the 2 one
    elif num == 9:
        tap(w // 2, int(h * 0.8))  # choose the 2 one
    return True


def match_item(img, item):
    # item = 'support'
    lst = png_lst(support_path)
    
    res = 0
    for file in lst:
        if item in file:
            fimg = cv2.imread(f'{support_path}/{file}', 0)
            if analyze(img, fimg):
                res = 1
    
    return res


def get_support_item(img):
    res = []
    servant = match_item(img, 'support')
    skill = match_item(img, 'skill')
    craft = match_item(img, 'craft')

    w, h = img.shape[::-1]
    tmp = img[h*2//3:h-1, 0:w-1]
    manpo = match_item(tmp, 'manpo')
    
    if servant == 0:
        skill = 0
    if craft == 0:
        manpo = 0
    
    res = [servant, skill, craft, manpo]
    return res


def judge_support(mode):
    set_rank = get_cfg('support', 'rank')
    if not set_rank:
        set_rank = '0'
    
    if mode == '1':
        factor_servant = 10
        factor_craft = 1
    elif mode == '2':
        factor_servant = 1
        factor_craft = 10
    elif mode == '3':
        factor_servant = 10
        factor_craft = 10
    
    set_refresh = get_cfg('support', 'refresh')
    if not set_refresh:
        set_refresh = 0
    else:
        set_refresh = int(set_refresh)
    if set_refresh < 0:
        set_refresh = 0
    for i in range(set_refresh + 1):
        
        sup = []
        # print(set_rank)
        for rank in set_rank:
            psn = PSN()
            eval('psn.ZHIJIE%s()' % rank)
            screenshot()
            while not pic_in_sh(support_path + '/lastlogin.png'):
                time.sleep(1)
                screenshot()
            index = 0
            
            if pic_in_sh(support_path + '/top1.png') or pic_in_sh(support_path + '/top2.png'):
                # 存在助战数目 > 2
                while not pic_in_sh(support_path + '/end.png'):
                    sh = cv2.imread(screenshot_path, 0)
                    for region in [support_sel_size_1, support_sel_size_2]:
                        index += 1
                        x1, y1, x2, y2 = region
                        tmp = get_support_item(sh[y1:y2, x1:x2])
                        # dbg_log([rank, index] + tmp) ###########
                        dbg_log('rank=%s, index=%-2s, servant=%s, skill=%s, craft=%s, manpo=%s' % \
                                (rank, index, tmp[0], tmp[1], tmp[2], tmp[3]))
                        sup.append([rank, index] + tmp)
                    x0, y0, x1, y1, d0 = support_swipe_parm
                    swipe(x0, y0, x1, y1, d0)
                    screenshot()
                
                index = 90
                sh = cv2.imread(screenshot_path, 0)
                for region in [support_sel_size_8, support_sel_size_9]:
                    index += 1
                    x1, y1, x2, y2 = region
                    tmp = get_support_item(sh[y1:y2, x1:x2])
                    # print([rank, index] + tmp)
                    # dbg_log([rank, index] + tmp)  ###########
                    dbg_log('rank=%s, index=%-2s, servant=%s, skill=%s, craft=%s, manpo=%s' % \
                            (rank, index, tmp[0], tmp[1], tmp[2], tmp[3]))
                    sup.append([rank, index] + tmp)
                    screenshot()
                
                swipe(1860, 1045, 1860, 120, 1500)  # 滑动到最上面
            else:
                # 存在助战数目 <=2
                sh = cv2.imread(screenshot_path, 0)
                for region in [support_sel_size_1, support_sel_size_2]:
                    index += 1
                    x1, y1, x2, y2 = region
                    tmp = get_support_item(sh[y1:y2, x1:x2])
                    # dbg_log([rank, index] + tmp)  ###########
                    dbg_log('rank=%s, index=%-2s, servant=%s, skill=%s, craft=%s, manpo=%s' % \
                            (rank, index, tmp[0], tmp[1], tmp[2], tmp[3]))
                    sup.append([rank, index] + tmp)
                    # screenshot()
            
            weight = []
            for tmp in sup:
                weight.append(factor_servant * sum(tmp[2:4]) + factor_craft * sum(tmp[4:]))

            # 当前 rank 没有符合条件的助战
            # 继续下一个 rank
            if max(weight) < 10:
                continue
            
            # 选出当前 rank 助战中最合适的一个
            for i in range(len(weight)):
                if weight[i] == max(weight):
                    rank, index = sup[i][:2]
                    psn = PSN()
                    eval('psn.ZHIJIE%s()' % rank)
                    if index >= 90:
                        swipe(1860, 280, 1860, 1060, 1500)  # 滑动到最下面
                        tap_support(9 - (index % 2))
                    else:
                        for i in range((index - 1) // 2):
                            x0, y0, x1, y1, d0 = support_swipe_parm
                            swipe(x0, y0, x1, y1, d0)
                        tap_support(2 - (index % 2))
                    sys_log('select the support')
                    sys_log('rank=%s, index=%-2s, servant=%s, skill=%s, craft=%s, manpo=%s' % \
                            (sup[i][0], sup[i][1], sup[i][2], sup[i][3], sup[i][4], sup[i][5]))
                    return True
        
        # 如果所有 rank 都没有合适的助战
        # 进行刷新操作
        if max(weight) < 10 and i != set_refresh:
            sys_log('refresh support')
            picture_tap(support_path + '/refresh.png')
            screenshot()
            picture_tap(support_path + '/confirm.png')
            time.sleep(2)
            continue
    
    # 如果选择不到合适的助战，根据 keepgo 进行后续操作
    if int(get_cfg('support', 'keepgo')):
        tap_support(1)
    else:
        toast('select support fail')
        exit()


def select_support():
    """
    根据 ini 设定选择相应的助战
    :return:
    """
    
    # 如果还没有刷新出来助战，直接返回，继续截图
    if not pic_in_sh(support_path + '/lastlogin.png'):
        return 0
    
    # 已经刷新出来助战了
    mode = get_cfg(sec='support', key='mode')
    if mode == '0':
        tap_support(1)
    elif mode == '1' or mode == '2':
        judge_support(mode)