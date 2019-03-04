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


def select_support(servant=None, skill=None, craft=None):

    # 先看是不是 start 界面
    support = [servant, skill, craft]
    sh = cv2.imread(screenshot_path, 0)
    # start = cv2.imread(support_path + '/start.png', 0)
    end = cv2.imread(support_path + '/end.png', 0)
    refresh = False

    # if analyze(sh, start, 0.85):
    #     ps = position(sh, start, 0.85)
    #     tap(ps[0][0], ps[0][1])

    if servant is None and craft is None and skill is None:
        # 直接随便选择一个
        pass
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






# # support.txt
# # servant, skill, craft,
# def support_select(servant=None, skill=None, craft=None):
#     flg_lst = [0, 0, 0]
#
#     flg_lst[0] = int(servant is not None)
#     flg_lst[1] = int(skill is not None)
#     flg_lst[2] = int(craft is not None)
#
#     input_lst = [servant, skill, craft]  # , craft] # craft0 未能满破######
#
#     # print('servant = ', servant)
#     # print('craft = ', craft)
#     # print('skill = ', skill)
#
#     sh = cv2.imread(screenshot_path, 0)
#     #         height, width
#     im1 = sh[250:590, 50:1820]  # zhuzhan 1
#     im2 = sh[560:890, 50:1820]  # zhuzhan 2
#
#     end = cv2.imread('./lib/support_select/sel_bar_end.png', 0)
#
#     flg = False
#
#     if servant is None and craft is None and skill is None:
#         # 直接随便选择一个
#         pass
#         return True
#
#     if analyze(sh, end, 0.9):
#         # 读取文件遍历一遍，看是否有低优先级合适的，没有的话再二次更新
#         print('already check all ....')
#         # basic_tap(1260, 200)
#         # time.sleep(3)
#         # basic_tap(1260, 200)
#         # time.sleep(3)
#         return False
#
#     for i in range(2):
#
#         match_lst = [0, 0, 0]  # , 0] # servant, skill, craft1, craft2
#
#         if i == 0:
#             imx = im1
#         else:
#             imx = im2
#
#         for pic_file in file_lst:
#             name, extension = os.path.splitext(pic_file)
#             if extension == '.png':
#                 tmp = cv2.imread(f'./lib/support_select/{pic_file}', 0)
#                 thd = 0.85
#
#                 if analyze(imx, tmp, thd):
#
#                     w, h = tmp.shape[::-1]
#                     ps = get_filtered(imx, tmp, thd)
#
#                     if i == 0:
#                         px = 50 + ps[0][0]
#                         py = 250 + ps[0][1]
#                     else:
#                         px = 50 + ps[0][0]
#                         py = 560 + ps[0][1]
#
#                     px = px + w // 2
#                     py = py + h // 2
#
#                     print('i = ', i)
#                     print('cmp pass /', pic_file)
#                     print('name ', name)
#
#                     for j in range(len(input_lst)):
#                         if input_lst[j] is not None:  # 名字/技能/满破礼装/礼装 对了
#                             if input_lst[j] in name:  # 加if保证改变后面的时候，前面已经更改过的的不变
#                                 match_lst[j] = int(input_lst[j] in name)
#
#                                 # 这里加上servant的坐标信息
#                                 if j == 0:
#                                     match_lst.append(px)
#                                     match_lst.append(py)
#
#         # 写入match_lst
#         f = open('./tmp/support_select.txt', 'a+')
#         f.writelines(str(match_lst) + '\n')
#         f.close()
#
#         if operator.eq(flg_lst, match_lst[:3]):
#             # if sum(match_lst[0:len(match_lst)]) >= 3:
#             pass
#
#             basic_tap(match_lst[3], match_lst[4])
#             # genjui
#             # 然后再找一遍头像的position位置
#
#             # 直接选中
#             # 点击对应的助战
#             return True
#
#     if flg:
#         return True
#     else:
#         # 没找到，滑动
#         swipe(1024, 800, 1022, 800 - 538, 2000)
#         pass
#         # 然后再截图进入循环

