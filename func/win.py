import cv2
from util.default import *
from util.ats import random_tap
from util.ats import picture_tap
from util.ats import analyze
from util.global0 import *






def judge():
    sh = cv2.imread(screenshot_path, 0)
    tmp = cv2.imread(win_path + '/material.png', 0)
    thd = 0.85
    if analyze(sh, tmp, thd):
        # run_materials++ if needed
        set_run_num = eval(rd_global('set_run_parm'))
        cur_run_num = eval(rd_global('run_parm'))

        if set_run_num[1] != -1:
            cur_run_num[1] += 1
            wt_global('run_parm', cur_run_num)
            # print(rd_global('run_parm'))

        if cur_run_num[1] >= set_run_num[1]:
            wt_global('RUN_FLAG', 'False')


def win_and_next(scene):

    set_run_num = eval(rd_global('set_run_parm'))
    if scene == 'win2' and set_run_num[1] != -1:
        judge()

    # thd = 0.85
    if picture_tap(win_path + '/next.png'):
        pass
    else:
        # win0/1/2/3/4
        random_tap()
