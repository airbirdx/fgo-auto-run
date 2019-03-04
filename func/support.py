import os
import operator
import cv2
from util.default import support_path
from util.default import screenshot_path
from util.scene import curr_png_lst
from util.default import tmp_support
from util.ats import tap
from util.ats import swipe
from util.cvs import analyze
from util.cvs import position


def update_match(match, name, support, px, py):
    for i in range(len(support)):
        if support[i] is not None and support[i] in name:  # 加if保证改变后面的时候，前面已经更改过的的不变
            match[i] = int(support[i] in name)
            if i == 0:
                match.append(px)
                match.append(py)
    return match


# size = x1, x2, y1, y2
# im = sh[250:590, 50:1820]  # support 1
# size = 50, 1820, 250, 590
def match_support(size, support):
    sh = cv2.imread(screenshot_path, 0)
    x1, x2, y1, y2 = size
    im = sh[y1:y2, x1:x2]
    match = [0] * len(support)
    png_lst = curr_png_lst(support_path)
    for file in png_lst:
        name, extension = os.path.splitext(file)
        tmp = cv2.imread(support_path + '/' + file, 0)
        thd = 0.85
        if analyze(im, tmp, thd):
            ps = position(im, tmp, thd)
            px = ps[0][0] + x1
            py = ps[0][1] + y1
            match = update_match(match, name, support, px, py)
    return match


def select_support():

    try:
        default_support
    except NameError:
        servant = ''
        skill = ''
        craft = ''
    else:
        servant = default_support[0]
        skill = default_support[1]
        craft = default_support[2]

    support = [servant, skill, craft]
    sh = cv2.imread(screenshot_path, 0)
    end = cv2.imread(support_path + '/end.png', 0)
    refresh = False

    if servant is '' and craft is '' and skill is '':
        w, h = sh.shape[::-1]
        tap(w // 2, int(h * 0.4))  # choose the first one
        return True

    sp = []
    for tmp in support:
        sp.append(int(tmp is not None))

    if analyze(sh, end, 0.9):  # 设定为只刷新一次
        # 读取文件遍历一遍，看是否有低优先级合适的，没有的话再二次更新
        print('already check all ....')
        # press refresh button
        pass
        if refresh:
            return False
        else:
            refresh = True

    size1 = [50, 1820, 250, 590]
    size2 = [50, 1820, 560, 890]

    sizea = [size1, size2]

    for size in sizea:
        match = match_support(size, support)
        f = open(tmp_support, 'a+')
        f.writelines(str(match) + '\n')
        f.close()

        if operator.eq(sp, match[:3]):
            tap(match[3], match[4])
            return True
    swipe(1024, 800, 1022, 800 - 538, 2000) ##############这里写成固定形式，或者调用函数，参数用txt传参
