import cv2, time
from util.ats import picture_tap
from util.cvs import analyze
from util.ats import screenshot
from util.ats import swipe
from util.default import *
from util.global0 import *
from util.log import *


def addap0():
    '''
    使用[苹果]或者[圣晶石]增加体力 AP 数值
    :return:
    '''
    # set_clr_lst
    set_run_num = eval(rd_global('set_run_parm'))
    cur_run_num = eval(rd_global('run_parm'))
    set_clr_lst = eval(rd_global('set_apple_priority'))

    if set_run_num[2] != -1:
        color = set_run_num[2][0]
    else:
        color = set_clr_lst[0]

    if set_run_num[2] != -1:
        set_num = set_run_num[2][1]
        run_num = cur_run_num[2][1]
        if run_num >= set_num:
            wt_global('RUN_FLAG', 'False')
            sys_log('「 DONE 」, RUN APPLES ')
            return False

    swipe(1920 // 2, 780, 1920 // 2, 200, 1000)
    time.sleep(1)
    screenshot()

    # thd = 0.85
    if picture_tap(f'{addap_path}/apple{color}.png'):

        # 根据点击苹果，进行自加
        if set_run_num[2] != -1:
            cur_run_num[2][1] += 1
            wt_global('g_cur_run_parm', cur_run_num)

        # 点击苹果了之后，1s后获取截图
        time.sleep(1)
        screenshot()

        sh = cv2.imread(screenshot_path, 0)
        tmp = cv2.imread(f'{addap_path}/apple{color}.png', 0)
        thd = 0.85
        # 如果仍然在苹果界面

        if analyze(sh, tmp, thd):
            # 如果是配置了刷一定量颜色的苹果，那么已经无法再继续进行
            if set_run_num[2] != -1:
                sys_log('run out of %s color apple.' % color)
                wt_global('RUN_FLAG', 'False')
                return False
            else:
                set_clr_lst.pop(0)
                sys_log('current apple color priority =', set_clr_lst)
                # 如果已经全部出栈，表示已经没有可以选择的，退出执行
                if not set_clr_lst:
                    wt_global('RUN_FLAG', 'False')
                else:
                    wt_global('set_apple_priority', set_clr_lst)

    # thd = 0.85
    if picture_tap(addap_path + '/confirm.png'):
        pass

    # thd = 0.85
    if picture_tap(addap_path + '/close.png'):
        pass

