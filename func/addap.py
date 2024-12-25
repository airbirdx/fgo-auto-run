import cv2, time
from util.ats import picture_tap
from util.cvs import *
from util.ats import screenshot
from util.ats import swipe
from util.default import *
from util.global0 import *
from util.log import *


def addap0():
    """
    使用[苹果]或者[圣晶石]增加体力 AP 数值
    :return:
    """
    # set_clr_lst
    # if rd_tmp_ini('run', 'parm') == 'apples':
    #     config_num = int(get_cfg('run', rd_tmp_ini('run', 'parm')).split(',')[-1])
    # else:
    #     config_num = int(get_cfg('run', rd_tmp_ini('run', 'parm')))
    current_num = int(rd_tmp_ini('run', 'num'))
    
    if rd_tmp_ini('run', 'parm') == 'apples':
        current_num += 1
        wt_tmp_ini('run', 'num', str(current_num))
        
        color = get_cfg('run', rd_tmp_ini('run', 'parm')).split(',')[0]
        sys_log('addap,,, color:%s' % color)


        # if color != 'Cu':
        if color == 'Xu' or color == 'Cu':
            x0, y0, x1, y1, d0 = addap_swipe_parm
            swipe(x0, y0, x1, y1, d0)
            screenshot()

            # exit()##### debug
        # print('color is %s' % color)
        picture_tap(addap_path + f'/apple{color}.png')
        screenshot()
        if not pic_in_sh(addap_path + '/confirm.png'):
            sys_log('@@run out of apples/stones...1')
            # exit() # for debug

    elif rd_tmp_ini('run', 'parm') == 'stones':
        current_num += 1
        wt_tmp_ini('run', 'num', str(current_num))
        picture_tap(addap_path + '/stone.png')
        screenshot()
        if not pic_in_sh(addap_path + '/confirm.png'):
            sys_log('@@run out of apples/stones...2')
            exit()
            
    elif int(get_cfg('addap', 'en_apple')) or int(get_cfg('addap', 'en_stone')):
        if int(get_cfg('addap', 'en_apple')):
            tmp0 = ['appleAg.png', 'appleAu.png']
        else:
            tmp0 = []
            
        if int(get_cfg('addap', 'en_stone')):
            tmp1 = ['stone.png']
        else:
            tmp1 = []
            
        auto_eat = tmp0 + tmp1
        for item in auto_eat:
            picture_tap(addap_path + '/' + item)
            screenshot()
            if pic_in_sh(addap_path + '/confirm.png'):
                break
        if not pic_in_sh(addap_path + '/confirm.png'):
            sys_log('@@run out of apples/stones...3')
            exit()

    # thd = 0.85
    if picture_tap(addap_path + '/confirm.png'):
        pass
    
    time.sleep(3)  # just in case....
    screenshot()   # 这里加一个截图，放置直接点击，然后选择了助战
    # thd = 0.85
    if picture_tap(addap_path + '/close.png'):
        pass

