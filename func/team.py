import os

from util.default import team_path
from util.default import cfg_path
from util.scene import png_lst
from util.ats import picture_tap
from util.global0 import *
from psn.psfunc import cfgstr2lst


def team_confirm():
    
    # if rd_tmp_ini('run', 'parm') == 'apples':
    #     config_num = int(get_cfg('run', rd_tmp_ini('run', 'parm')).split(',')[-1])
    # else:
    #     config_num = int(get_cfg('run', rd_tmp_ini('run', 'parm')))
    current_num = int(rd_tmp_ini('run', 'num'))

    if rd_tmp_ini('run', 'parm') == 'times':
        current_num += 1
        wt_tmp_ini('run', 'num', str(current_num))

    dbg_log('run_parm_num --> %s@%s' % (rd_tmp_ini('run', 'parm'), current_num))

    # thd = 0.85
    picture_tap(team_path + '/start.png')


def team_confirm0():

    # thd = 0.85
    picture_tap(team_path + '/start.png')

    