import cv2
from util.default import *
from util.ats import random_tap
from util.ats import picture_tap
from util.ats import analyze
from util.global0 import *
from util.log import *
from util.scene import current_scene
from psn.PSN import *
from util.ats import screenshot

def pypoint():

    psn = PSN()

    path = './lib/func/pypoint'

    pyp = cv2.imread(f'{path}/pypoint.png', 0)
    callx10 = cv2.imread(f'{path}/call_next.png', 0)
    call_notice = cv2.imread(f'{path}/call_notice.png', 0)
    call_confirm = cv2.imread(f'{path}/call_confirm.png', 0)
    call_next = cv2.imread(f'{path}/call_next.png', 0)
    full = cv2.imread(f'{path}/full.png', 0)

    while 1:
        screenshot()
        sh = cv2.imread(screenshot_path, 0)
        thd = 0.85

        if analyze(sh, full, thd):
            sys_log('PYPOINT FULL !')
            break

        if analyze(sh, pyp, thd):

            sys_log('Current scene : PY POINT')
            if picture_tap(f'{path}/callx10.png'):

                for idx in range(5):

                    screenshot()
                    time.sleep(0.2)
                    # sh = cv2.imread(screenshot_path, 0)
                    # if analyze(sh, call_notice, thd):
                    #     picture_tap(f'{path}/call_confirm.png')
                    if picture_tap(f'{path}/call_confirm.png'):

                        for i in range(100):
                            psn.PYPONT()
                            screenshot()
                            time.sleep(0.2)
                            if picture_tap(f'{path}/call_next.png'):
                                time.sleep(1.5)
                                break

                        break
                    else:
                        pass

                    if idx == 4:
                        sys_log('ERROR IN PYPOINT...')
                        break


        else:
            sys_log('NOT IN PYPOINT SCENE @@')



def craftexp():
    psn = PSN()

    path = './lib/func/craftexp'

    strscene = cv2.imread(f'{path}/strscene.png', 0)
    zoom2x2 = cv2.imread(f'{path}/zoom2x2.png', 0)
    zoom3x3 = cv2.imread(f'{path}/zoom3x3.png', 0)
    zoom4x4 = cv2.imread(f'{path}/zoom4x4.png', 0)
    decide = cv2.imread(f'{path}/decide.png', 0)
    confirm = cv2.imread(f'{path}/confirm.png', 0)
    strengthen = cv2.imread(f'{path}/strengthen.png', 0)

    cx, cy = [210, 380]  # craft one
    all_pos = []
    for row in range(3):
        for col in range(7):
            px = cx + col * 200
            py = cy + row * 214
            all_pos.append([px, py])

    while 1:
        screenshot()
        sh = cv2.imread(screenshot_path, 0)
        thd = 0.85

        # if analyze(sh, full, thd):
        #     sys_log('PYPOINT FULL !')
        #     break

        if analyze(sh, strscene, thd):

            sys_log('Current scene : strengthen')
            psn.STRSELECT()

            time.sleep(1)
            screenshot()
            if picture_tap(f'{path}/zoom2x2.png', thd=0.9):
                time.sleep(1)
                screenshot()

            time.sleep(1)
            screenshot()
            if picture_tap(f'{path}/zoom3x3.png', thd=0.9):
                time.sleep(1)
                screenshot()

            sh = cv2.imread(screenshot_path, 0)
            if analyze(sh, zoom4x4, thd):

                for tmp_pos in all_pos:
                    px, py = tmp_pos
                    tap(px, py, 20)
                    time.sleep(0.1)

                time.sleep(1)
                screenshot()
                if picture_tap(f'{path}/decide.png'):
                    time.sleep(3)
                    screenshot()
                else:
                    sys_log('ERROR - A1')

                ##############################
                if picture_tap(f'{path}/decide.png'):
                    sys_log('END THIS AAAA')
                    exit()
                ##############################

                tap(1655, 1020, 20)
                time.sleep(1)
                screenshot()

                if picture_tap(f'{path}/confirm.png'):
                    time.sleep(3)
                    screenshot()
                else:
                    sys_log('ERROR - A3')

                for i in range(100):
                    psn.PYPONT()
                    screenshot()
                    sh = cv2.imread(screenshot_path, 0)
                    time.sleep(0.2)
                    if analyze(sh, strscene, thd):
                        time.sleep(1.5)
                        break
        else:
            sys_log('DDDDDDONEEEEEE @@')
