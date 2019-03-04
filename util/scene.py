import cv2
import os
# import numpy as np
# import random
# from PIL import Image
# import operator
# import time

from util.cvs import analyze
from util.default import scenes_path
from util.default import screenshot_path


def curr_png_lst(path):
    png_lst = []
    file_lst = os.listdir(path)  # list all files in this folder
    file_lst.sort()
    # print(file_lst)
    sh = cv2.imread(screenshot_path, 0)
    for file in file_lst:
        name, extension = os.path.splitext(file)
        if extension == '.png':
            png_lst.append(file)
    return png_lst


def current_scene():
    png_lst = curr_png_lst(scenes_path)
    # print(png_lst)
    sh = cv2.imread(screenshot_path, 0)
    for file in png_lst:
        tmp = cv2.imread(scenes_path + '/' + file, 0)
        thd = 0.85
        if analyze(sh, tmp, thd):
            name, extension = os.path.splitext(file)
            return name
    return 'PROCESS'






#
# def scene_operation():
#     scene = current_scene()
#     print(scene)
#     if 'addap' in scene:
#         pass
#     elif 'attack' in scene:
#         pass
#     elif 'fail' in scene:
#         pass
#     elif 'friend' in scene:
#         pass
#     elif 'loading' in scene:
#         pass
#     elif 'support' in scene:
#         # select_support()
#         select_support(servant='meilin', skill='310')
#         pass
#     elif 'task' in scene:
#         pass
#     elif 'win' in scene:
#         pass
#     else:
#         pass












def cmd_lut(scene):
    if scene == 'support_select':
        return support_select(person='meilin', skill='310', lizhuang = 'lizhuang_manpo') # person -> servent
        # return support_select('meilin')
        # function here
        pass
    elif scene == 'team_confirm':
        # function here
        team_confirm()
        pass
    elif scene == 'task_select':
        # function here
        task_select()
        pass
    elif scene == 'loading':
        # function here
        x = random.randint(1920/5,1920/5*4)
        y = random.randint(1080/5,1080/5*4)
        time.sleep(0.5)
        basic_tap(x, y)
        pass
    elif scene == 'bond' or scene == 'experience':
        # function here
        pass
        basic_tap(960, 500)
        # 羁绊页面
        # 经验值页面
    elif scene == 'trophy':
        # function
        trophy()
        pass
        # 找到下一步按钮的中心，并点击
    elif scene == 'award':
        # functin
        basic_tap(960, 500)
        pass
        # 随机点击画面
    elif scene == 'attack':
        attack_yanzuo_shougao(1)              ################1 turn start
        pass
    elif scene == 'add_ap':
        return add_ap(3) #一个金色苹果
    elif scene == 'new_friend':
        new_friend()
    elif scene == 'task_failed' or scene == 'pullout':
        task_failed()
    else:
        pass

    return False