import cv2
import os

from util.cvs import analyze
from util.default import *


def png_lst(path):
    res = []
    file_lst = os.listdir(path)  # list all files in this folder
    file_lst.sort()
    for file in file_lst:
        name, ext = os.path.splitext(file)
        if ext == '.png':
            res.append(file)
    return res


def current_scene():
    scenes = png_lst(scenes_path)
    sh = cv2.imread(screenshot_path, 0)
    for file in scenes:
        tmp = cv2.imread(scenes_path + f'/{file}', 0)
        thd = 0.85
        if analyze(sh, tmp, thd):
            name, extension = os.path.splitext(file)
            print('「 CURRENT SCENE 」', name)
            return name
    return 'none'

