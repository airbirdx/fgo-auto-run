
from util.ats import picture_tap
from util.default import *
from util.global0 import *
from util.log import *


# 判断当前刷新副本此时是否已经到达设定值
def judge():
    set_run_num = eval(rd_global('set_run_parm'))
    cur_run_num = eval(rd_global('run_parm'))
    for i in range(len(set_run_num)):
        set_parm = set_run_num[i]
        run_parm = cur_run_num[i]
        if set_parm != -1 and isinstance(set_parm, int):
            if run_parm >= set_parm:
                wt_global('RUN_FLAG', 'False')
                sys_log('「 DONE 」 RUN TIMES')
                return 1
    return 0


def task_select():

    if judge():
        return False

    # thd = 0.85
    picture_tap(task_path + '/task.png')

    # 给 rank 和 refresh 临时变量，并赋初值
    wt_global('tmp_sup_rank', ['', 1])
    wt_global('tmp_sup_rfh', 0)




