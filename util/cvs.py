import cv2
import numpy as np


def analyze(sh, tmp, thd):
    res = cv2.matchTemplate(sh, tmp, cv2.TM_CCOEFF_NORMED)
    if (res >= thd).any():
        return 1


def location(sh, tmp, thd):
    res = cv2.matchTemplate(sh, tmp, cv2.TM_CCOEFF_NORMED)
    pos = []
    loc = np.where(res >= thd)
    for pt in zip(*loc[::-1]):
        pos.append(pt)
    return pos


def aline(tmp, ary):
    ret = []
    w, h = tmp.shape[::-1]
    # print(ary)
    for ps in ary:
        psl = []
        psl.append(ps[0] + w // 2)
        psl.append(ps[1] + h // 2)
        # psl[1] = ps[1] + h // 2
        ret.append(psl)
    return ret


# a filtered method
def position(sh, tmp, thd):
    ary = location(sh, tmp, thd)
    ary.sort()
    for i in range(len(ary)):
        for p in range(1, len(ary) - i):
            for k in range(-5, 5):
                for l in range(-5, 5):
                    if ((ary[i][0] + k) == ary[i + p][0]) and ((ary[i][1] + l) == ary[i + p][1]):
                        ary[i + p] = [0, 0]
    while ary.count([0, 0]) >= 1:
        ary.remove([0, 0])
    # return ary
    return aline(tmp, ary)






