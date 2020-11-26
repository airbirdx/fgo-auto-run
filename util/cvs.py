import cv2
import numpy as np
from util.default import *


def analyze(a, b, thd=0.85):
    """
    判断图像[a]中是否含有图像[b]
    :param a:cv2.imread 图像
    :param b:cv2.imread 图像
    :param thd:阈值
    :return:
    """
    res = cv2.matchTemplate(a, b, cv2.TM_CCOEFF_NORMED)
    if (res >= thd).any():
        return 1


def pic_in_sh(pic, thd=0.85):
    """
    图片[pic]是否在截图中
    :param pic:图片路径
    :param thd:阈值
    :return:
    """
    img = cv2.imread(pic, 0)
    return img_in_sh(img, thd)


def img_in_sh(img, thd=0.85):
    """
    图像[img]是否在截图中
    :param img:cv2.imread 图像
    :param thd:阈值
    :return:
    """
    sh = cv2.imread(screenshot_path, 0)
    return analyze(sh, img, thd)


def location(a, b, thd):
    """
    图像[b]在图像[a]中出现的位置，左上角坐标
    :param a:cv2.imread 图像
    :param b:cv2.imread 图像
    :param thd:阈值
    :return:图像[b]出现的位置
    """
    res = cv2.matchTemplate(a, b, cv2.TM_CCOEFF_NORMED)
    pos = []
    loc = np.where(res >= thd)
    for pt in zip(*loc[::-1]):
        pos.append(pt)
    return pos


def position(img, tmp, thd):
    """
    图像[tmp]在图像[img]中出现的位置，中心坐标
    :param img:cv2.imread 图像
    :param tmp:cv2.imread 图像
    :param thd:阈值
    :return:图像[tmp]出现的位置
    """
    ary = location(img, tmp, thd)
    ary.sort()
    # 以下部分类似于中心滤波
    for i in range(len(ary)):
        for p in range(1, len(ary) - i):
            for k in range(-5, 5):
                for l in range(-5, 5):
                    if ((ary[i][0] + k) == ary[i + p][0]) and ((ary[i][1] + l) == ary[i + p][1]):
                        ary[i + p] = [0, 0]
    while ary.count([0, 0]) >= 1:
        ary.remove([0, 0])
    # return ary
    res = [] # [[x0,y0],[x1,y1], ...]
    w, h = tmp.shape[::-1]
    # print(ary)
    for ps in ary:
        psl = []
        psl.append(ps[0] + w // 2)
        psl.append(ps[1] + h // 2)
        # psl[1] = ps[1] + h // 2
        res.append(psl)
    return res






