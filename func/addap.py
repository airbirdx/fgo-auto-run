import time
from util.ats import picture_tap
from util.ats import screenshot
from util.ats import swipe
from util.default import *
from util.global0 import *

def addap0():
    # set_clr_lst
    set_run_num = eval(rd_global('set_run_parm'))
    cur_run_num = eval(rd_global('run_parm'))
    set_clr_lst = eval(rd_global('set_apple_priority'))

    if set_run_num[2] != -1:
        color = set_run_num[2][0]
    else:
        color = set_clr_lst[0]

    swipe(1920 // 2, 780, 1920 // 2, 200, 1000)
    screenshot()
    time.sleep(1)

    # print('set_run_num', set_run_num, type(set_run_num))
    # print('cur_run_num', cur_run_num, type(cur_run_num))
    # print('set_clr_lst', set_clr_lst)
    # print(color)

    if set_run_num[2] != -1:
        set_num = set_run_num[2][1]
        run_num = cur_run_num[2][1]
        if run_num < set_num:
            pass
        else:
            wt_global('RUN_FLAG', 'False')
            print('/---/ DONE --> USE APPLE ')
            exit()

    # thd = 0.85
    if picture_tap(addap_path + '/apple' + color + '.png'):

        # print('!@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        # print('set_run_num', set_run_num)
        # 根据点击苹果，进行自加
        if set_run_num[2] != -1:
            cur_run_num[2][1] += 1
            # print(cur_run_num)
            wt_global('g_cur_run_parm', cur_run_num)

        # 点击苹果，1s后获取截图
        time.sleep(1)
        screenshot()

        # 如果还能点击苹果，说明此颜色苹果已经消耗完
        # ！！！以下部分需要调试！！！
        if picture_tap(addap_path + '/apple' + color + '.png'):
            # 如果是配置了刷一定量颜色的苹果，那么已经无法再继续进行
            if set_run_num[2] != -1:
                print('There are no %s apple you can use' % color)
                wt_global('RUN_FLAG', 'False')
            # 如果是其他两种刷多少次或者多少个材料的形式，当前优先级颜色 pop 出 list ，顺位查找下一个优先级
            else:
                set_clr_lst.pop(0)
                print('set_clr_lst', set_clr_lst)
                # 如果已经全部出栈，表示已经没有可以选择的，退出执行
                if not set_clr_lst:
                    wt_global('RUN_FLAG', 'False')
                else:
                    wt_global('set_apple_priority', set_clr_lst)
                return True
        else:
            pass




    # thd = 0.85
    if picture_tap(addap_path + '/confirm.png'):
        pass

    # thd = 0.85
    if picture_tap(addap_path + '/close.png'):
        pass

