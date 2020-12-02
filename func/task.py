
from util.ats import picture_tap
from util.default import *
from util.global0 import *
from util.log import *


def judge_parm_num():
    '''
    判断当前刷新副本此时是否已经到达设定值
    :return:
    '''
    if rd_tmp_ini('run', 'parm') == 'apples':
        config_num = int(get_cfg('run', rd_tmp_ini('run', 'parm')).split(',')[-1])
    else:
        config_num = int(get_cfg('run', rd_tmp_ini('run', 'parm')))
    current_num = int(rd_tmp_ini('run', 'num'))

    sys_log('run_parm_num --> %s@%s' % (rd_tmp_ini('run', 'parm'), current_num))
    
    if current_num >= config_num:
        wt_tmp_ini('run', 'flag', 'False')
        sys_log('「 DONE 」 RUN TIMES')
        return 1
    else:
        rm_tmp_ini(sec='battle')
        return 0
    


def task_select():
    '''
    判断是否已经完成所设定操作，如果未完成，继续点击任务，持续攻略
    :return:
    '''
    if not judge_parm_num():
        picture_tap(task_path + '/task.png')
