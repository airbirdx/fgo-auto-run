
from util.ats import picture_tap
from util.default import *
from util.global0 import *


def judge():
    set_run_num = eval(rd_global('set_run_parm'))
    cur_run_num = eval(rd_global('run_parm'))
    for i in range(len(set_run_num)):
        set_parm = set_run_num[i]
        run_parm = cur_run_num[i]
        if set_parm != -1 and isinstance(set_parm, int):
            if run_parm >= set_parm:
                wt_global('RUN_FLAG', 'False')
                print('/---/ DONE --> RUN TIMES')
                exit()


def task_select():
    judge()
    # thd = 0.85
    picture_tap(task_path + '/task.png')

    # 获取 rank 和 refresh ..并转换为新的变量
    tmp_sup_rank = rd_global('set_default_support_rank')
    wt_global('tmp_sup_rank', tmp_sup_rank)

    tmp_sup_rfh = rd_global('set_default_support_refresh')
    wt_global('tmp_sup_rfh', 0)



