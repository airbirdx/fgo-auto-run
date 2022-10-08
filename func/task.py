
import time
from util.ats import picture_tap, screenshot
from util.default import *
from util.global0 import *
from util.log import *
from util.scene import current_scene


def judge_parm_num():
    '''
    判断当前刷新副本此时是否已经到达设定值
    :return:
    '''
    # config_apple_num = 0
    # if rd_tmp_ini('run', 'parm') == 'apples':
    #     config_apple_num = int(get_cfg('run', rd_tmp_ini('run', 'parm')).split(',')[-1])
    
    # if config_apple_num > 0:
    #     config_num = config_apple_num
    if rd_tmp_ini('run', 'parm') == 'apples':
        config_num = int(get_cfg('run', rd_tmp_ini('run', 'parm')).split(',')[-1])
    else:
        config_num = int(get_cfg('run', rd_tmp_ini('run', 'parm')))
    current_num = int(rd_tmp_ini('run', 'num'))

    sys_log('run_parm_num --> %s@%s' % (rd_tmp_ini('run', 'parm'), current_num))
    sys_log('cfg_parm_num --> %s@%s' % (rd_tmp_ini('run', 'parm'), config_num))
    
    flag = 0    # flag for finish
    if current_num >= config_num:
        if rd_tmp_ini('run', 'parm') == 'apples':
            picture_tap(task_path + '/task.png')
            time.sleep(1)
            screenshot()
            # sys_log('debug, hit task, addap??')
            scene = current_scene()
            # sys_log('current_scene....%s' % scene)

            if 'addap' in scene:
                flag = 1
            # exit()
        else:
            flag = 1

    if flag:
        wt_tmp_ini('run', 'flag', 'False')
        sys_log('「 DONE 」 RUN TIMES')
    else:
        rm_tmp_ini(sec='battle')
        sys_log('「 CONTINUE 」 task')
    
    return flag


def task_select():
    '''
    判断是否已经完成所设定操作，如果未完成，继续点击任务，持续攻略
    :return:
    '''
    if not judge_parm_num():
        picture_tap(task_path + '/task.png')
