import os

from util.default import team_path
from util.default import cfg_path
from util.scene import png_lst
from util.ats import picture_tap
from util.global0 import *
from psn.psfunc import cfgstr2lst


def team_confirm():
    # run_times++ if needed
    set_run_num = eval(rd_global('set_run_parm'))
    cur_run_num = eval(rd_global('run_parm'))

    if set_run_num[0] != -1:
        cur_run_num[0] += 1
        wt_global('run_parm', cur_run_num)

    # thd = 0.85
    picture_tap(team_path + '/start.png')

    wt_global('round', 0)
    wt_global('turn', 0)

    lst = png_lst(cfg_path)
    svt_priority = eval(rd_global('set_servant_priority'))
    for file in lst:
        # name, ext = os.path.splitext(file)
        if 'servant' in file and not svt_priority:
            os.remove(cfg_path + '/' + file)

    # 获取 skill 和 final ..并转换为新的变量
    # tmp = rd_global('set_default_skill')
    # skill_lst = cfgstr2lst(tmp)
    # wt_global('tmp_skl_lst', skill_lst)
    #
    # tmp = rd_global('set_default_final')
    # final_lst = cfgstr2lst(tmp)
    # wt_global('tmp_fnl_lst', final_lst)
    wt_global('tmp_skl_lst', cfgstr2lst(rd_global('set_default_skill')))
    wt_global('tmp_fnl_lst', cfgstr2lst(rd_global('set_default_final')))

