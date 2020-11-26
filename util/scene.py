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


def current_scene():
    """
    判断当前处于哪种场景
    :return:
    """
    scenes = png_lst(scenes_path)
    sh = cv2.imread(screenshot_path, 0)
    for file in scenes:
        tmp = cv2.imread(scenes_path + f'/{file}', 0)
        thd = 0.85
        if analyze(sh, tmp, thd):
            name, extension = os.path.splitext(file)
            sys_log('「 CURRENT SCENE 」', name)
            return name
    dbg_log('「 CURRENT SCENE 」 %s' % 'N/A')
    return 'none'

