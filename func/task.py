
from util.ats import picture_tap
from util.default import *
from util.global0 import *


def task_select():
    judge()
    # thd = 0.85
    picture_tap(task_path + '/task.png')


def judge():
    set_run_num = eval(rd_global('set_run_parm'))
    cur_run_num = eval(rd_global('run_parm'))
    for i in range(len(set_run_num)):
        set_parm = set_run_num[i]
        run_parm = cur_run_num[i]
        if set_parm != -1 and isinstance(set_parm, int):
            if run_parm >= set_parm:
                wt_global('RUN_FLAG', 'False')
                print('?????? RUN TIMES DONE IN TASK')
                exit()
