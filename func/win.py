import cv2
from util.default import *
from util.ats import random_tap
from util.ats import picture_tap
from util.cvs import *
from util.global0 import *
from util.log import *


def win_judge():
    """
    判断是否了 times 或者 material 设定，并写入当前脚本已经跑了的次数
    :return:
    """
    if rd_tmp_ini('run', 'parm') == 'apples':
        config_num = int(get_cfg('run', rd_tmp_ini('run', 'parm')).split(',')[-1])
    else:
        config_num = int(get_cfg('run', rd_tmp_ini('run', 'parm')))
    current_num = int(rd_tmp_ini('run', 'num'))
    
    if rd_tmp_ini('run', 'parm') == 'materials' and pic_in_sh(win_path + '/material.png'):
        current_num += 1
    
    wt_tmp_ini('run', 'num', str(current_num))
    
    dbg_log('run_parm_num --> %s@%s' % (rd_tmp_ini('run', 'parm'), current_num))


def win_and_next(scene):
    """
    获胜并进行下一步
    :param scene:
    :return:
    """
    if scene == 'win2':
        os.system('cp ./sh.png ./log/sh_win2_%s.png' % datetime.datetime.now().strftime('%y%m%d_%H%M%S%p'))
        win_judge()

    # thd = 0.85
    if picture_tap(win_path + '/next.png'):
        pass
    else:
        # win0/1/2/3/4
        random_tap()
