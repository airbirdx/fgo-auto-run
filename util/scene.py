import cv2
import os

from util.cvs import analyze
from util.default import *
from util.log import *


def png_lst(path):
    """
    获取路径[path]下 png 格式图片列表
    :param path:
    :return:
    """
    res = []
    file_lst = os.listdir(path)  # list all files in this folder
    file_lst.sort()
    for file in file_lst:
        name, ext = os.path.splitext(file)
        if ext == '.png':
            res.append(file)
    return res

##
def folder_lst(path):
    """
    获取路径[path]下 folder 格式图片列表
    :param path:
    :return:
    """
    res = []
    file_lst = os.listdir(path)  # list all files in this folder
    file_lst.sort()
    # print(file_lst)
    cwd_0 = os.getcwd()
    # print(cwd_0)

    os.chdir(path)
    
    cwd_1 = os.getcwd()
    # print(cwd_1)
    os.chdir(cwd_0)

    for file in file_lst:
        # print(file, os.path.isdir(f'{cwd_1}/{file}'))
        if os.path.isdir(f'{cwd_1}/{file}'):
            res.append(file)
    return res


def current_scene(path=None):
    """
    判断当前处于哪种场景
    :return:
    """
    path_default = scenes_path
    if path is not None:
        path_default = path

    scenes = png_lst(path_default)
    sh = cv2.imread(screenshot_path, 0)
    for file in scenes:
        tmp = cv2.imread(path_default + f'/{file}', 0)
        # thd = 0.65
        thd = 0.85
        # print(file)
        if analyze(sh, tmp, thd):
            name, extension = os.path.splitext(file)
            sys_log('「 CURRENT SCENE 」', name)
            return name
    dbg_log('「 CURRENT SCENE 」 %s' % 'N/A')
    return 'none'





# folder_lst('../db/b-supports')
# folder_lst('../')