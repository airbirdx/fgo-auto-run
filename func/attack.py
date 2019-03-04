import os
import cv2
from PIL import Image

from util.default import screenshot_path
from util.default import tmp_path
from util.default import config_path
from util.default import attack_path
from util.scene import curr_png_lst
from util.cvs import position
from util.cvs import analyze
from util.ats import tap
from util.ats import random_tap


def classfiy_histogram(image1, image2, size=(256, 256)):
    ''' 'image1' and 'image2' is a Image Object.
    You can build it by 'Image.open(path)'.
    'Size' is parameter what the image will resize to it.It's 256 * 256 when it default.
    This function return the similarity rate betweene 'image1' and 'image2'
    '''
    image1 = image1.resize(size).convert("RGB")
    g = image1.histogram()

    image2 = image2.resize(size).convert("RGB")
    s = image2.histogram()

    assert len(g) == len(s), "error"

    data = []

    for index in range(0, len(g)):
        if g[index] != s[index]:
            data.append(1 - abs(g[index] - s[index]) / max(g[index], s[index]))
        else:
            data.append(1)

    return sum(data) / len(g)


# 获取5个从者的卡
def split():
    cut_y_ratio = [0.5, 0.9]
    # im = Image.open("./bufferpic/1.png")
    im = Image.open(screenshot_path)
    img_size = im.size
    px = img_size[0]
    py = img_size[1]

    interval = px // 5

    up   = py * cut_y_ratio[0]
    down = py * cut_y_ratio[1]

    for i in range(5):
        left = interval * i
        right = interval * (i + 1)
        if right > px:
            right = px
        region = im.crop((left, up, right, down))
        region.save(tmp_path + f'/card_{i}.png')

    for i in range(5):
        im = Image.open(tmp_path + f'/card_{i}.png')
        w, h = im.size

        up = int(0.3 * h)
        down = (0.24 + 0.2) * h
        left = w // 2 - 0.1 * w
        right = w // 2 + 0.1 * w
        region = im.crop((left, up, right, down))
        region.save(tmp_path + f'/tmp_servant_{i}.png')


# 自学习的时候使用
# 获取当前 config 目录下的 servant 数目
def servent_num():
    num = 0

    file_lst = os.listdir('./config')  # list all files in this folder
    file_lst.sort()

    for pic_file in file_lst:
        name, extension = os.path.splitext(pic_file)
        num += (extension == '.png' and 'servant' in name)
    # print('servant num = ', num)
    return num


# 自学习的时候使用
def servant_logo():
    for i in range(5):
        if not servent_num():
            res = cv2.imread(tmp_path + '/tmp_servant_0.png')
            cv2.imwrite(config_path + '/servant_0.png', res)
        else:
            flg = 0
            for j in range(servent_num()):
                tmp = Image.open(tmp_path + f'/tmp_servent_{i}.png')
                ser = Image.open(config_path + '/servant_{j}.png')
                res = classfiy_histogram(tmp, ser)
                thd = 0.5
                if res > thd:
                    flg += 1
            if not flg:
                new = cv2.imread(tmp_path + f'/tmp_servent_{i}.png')
                cv2.imwrite(config_path + f'/servant_{j+1}.png', new)

def gen_servant_logo():
    pass





def get_card_attribute():
    if not os.path.exists('./tmp/card_attribute.txt'):
        f = open('./tmp/card_attribute.txt', 'w')
        f.write('')
        f.close()

    ## 每一回合都要清空 一下才好
    f = open('./tmp/card_attribute.txt', 'w')
    f.write('')
    f.close()

    for i in range(5):
        card_attribute = [0] * 9
        # servent no, R,G,B, X(+1/0/-1),baoji, RGB x, y
        card = cv2.imread(f"./tmp/card_{i}.png", 0)

        for j in range(servent_num()):
            servent = cv2.imread(f"./config/servent_{j}.png", 0)
            thd = 0.85
            if analyze(card, servent, thd):
                # print('i = %d, servent = %d' % (i, j))
                card_attribute[0] = j

        tmp_R = cv2.imread(f"./lib/battle/buster.png", 0)
        tmp_G = cv2.imread(f"./lib/battle/quick.png", 0)
        tmp_B = cv2.imread(f"./lib/battle/arts.png", 0)
        RGB = [tmp_R, tmp_G, tmp_B]
        for j in range(3):
            thd = 0.85
            if analyze(card, RGB[j], thd):
                # print('i = %d, servent = %d' % (i, j))

                ps = get_filtered(card, RGB[j], thd)

                w, h = RGB[j].shape[::-1]
                px = ps[0][0] + w // 2
                py = ps[0][1] + h // 2

                card_attribute[j + 1] = 1
                card_attribute[6] = px + 1920 // 5 * i
                card_attribute[7] = py + 1080 // 2

        tmp_buff = cv2.imread(f"./lib/battle/restraint.png", 0)
        tmp_debuff = cv2.imread(f"./lib/battle/resistance.png", 0)
        tmp_vertigo = cv2.imread(f"./lib/battle/vertigo.png", 0)  #### warning
        thd = 0.85

        if analyze(card, tmp_buff, thd):
            card_attribute[4] = 1
        if analyze(card, tmp_debuff, thd):
            card_attribute[4] = -1
        if analyze(card, tmp_vertigo, thd):
            card_attribute[4] = -2
        else:
            card_attribute[4] = 9

        # 暴击
        card_attribute[5] = 0

        card_attribute.insert(0, i)

        # txt = ' '.join([str(x) for x in card_attribute])

        print(card_attribute)
        f = open('./tmp/card_attribute.txt', 'a+')
        # f.writelines((txt) + '\n')
        f.writelines(str(card_attribute) + '\n')


def get_servent_priority(n):
    servent_priority = [1, 0, 2]

    for i in range(len(servent_priority)):
        if n == servent_priority[i]:
            return 5 - i  # 优先级 5>4>3>2>1...

    return -1  # 从者优先级一样


def get_crd_sorted_taped(n):
    crd_attr = [];
    f = open('./tmp/card_attribute.txt', 'r')
    lines = f.readlines()
    # print(type(lines))
    for line in lines:
        crd_attr.append(eval(line))
    f.close()

    crd_sort_lst = []

    print('---------------------------------------')
    for i in range(len(crd_attr)):
        print(crd_attr[i])

    for i in range(len(crd_attr)):

        if i == 0:
            crd_sort_lst.append(crd_attr[i])
        else:

            for j in range(len(crd_sort_lst)):
                if get_servent_priority(crd_attr[i][1]) > get_servent_priority(crd_sort_lst[j][1]):
                    # 当前卡优先级高，插入到所比较排序的前面去，否则在最后append
                    print('A (i = crd)/ i = %d, j = %d' % (i, j))
                    crd_sort_lst.insert(j, crd_attr[i])
                    # print('----------------------------------------------------')
                    # for k in range(len(crd_sort_lst)):
                    #     print(crd_sort_lst[k])
                    break
                elif get_servent_priority(crd_attr[i][1]) == get_servent_priority(crd_sort_lst[j][1]):
                    # 判断卡颜色234 - RGB

                    tmp_rgb_var_crd = crd_attr[i][2] * 100 + crd_attr[i][3] * 10 + crd_attr[i][4]
                    tmp_rgb_var_sort = crd_sort_lst[j][2] * 100 + crd_sort_lst[j][3] * 10 + crd_sort_lst[j][4]

                    if tmp_rgb_var_crd >= tmp_rgb_var_sort:
                        print('B (i = crd)/ i = %d, j = %d' % (i, j))
                        crd_sort_lst.insert(j, crd_attr[i])
                        # print('----------------------------------------------------')
                        # for k in range(len(crd_sort_lst)):
                        #     print(crd_sort_lst[k])
                        break
                    else:
                        print('C (i = crd)/ i = %d, j = %d' % (i, j))
                        crd_sort_lst.insert(j + 1, crd_attr[i])
                        # print('----------------------------------------------------')
                        # for k in range(len(crd_sort_lst)):
                        #     print(crd_sort_lst[k])
                        break
                elif j == len(crd_sort_lst) - 1:
                    print('D (i = crd)/ i = %d, j = %d' % (i, j))
                    crd_sort_lst.append(crd_attr[i])
                    # print('----------------------------------------------------')
                    # for k in range(len(crd_sort_lst)):
                    #     print(crd_sort_lst[k])
                    break
                else:
                    pass

    print('*************************************')
    for i in range(len(crd_sort_lst)):
        print(crd_sort_lst[i])

    lst_normal = []
    lst_cantmove = []
    for i in range(len(crd_sort_lst)):
        if crd_sort_lst[i][5] == -2:
            lst_cantmove.append(crd_sort_lst[i])
        else:
            lst_normal.append(crd_sort_lst[i])

    lst_sorted = lst_normal + lst_cantmove

    print('---------------------------------------')

    for i in range(len(lst_sorted)):
        print(lst_sorted[i])

    # new add parts
    new_tap_lst = lst_sorted[n - 5 - 1::-1]  # 前n个逆序排列

    # tmp_new_tap_lst = lst_sorted[::-1] # 前n个逆序排列
    # new_tap_lst = tmp_new_tap_lst[:n]

    if n == 3:
        sum_r = 0
        for iii in range(3):
            sum_r += new_tap_lst[iii][2]
        if sum_r > 0 and new_tap_lst[0][2] == 0:

            if new_tap_lst[1][2] > 0:
                tmp_swap_lst = new_tap_lst.pop(1)
            else:  # new_tap_lst[2][2] > 0:
                tmp_swap_lst = new_tap_lst.pop(2)
            new_tap_lst.insert(0, tmp_swap_lst)

    for i in range(n):
        basic_tap(new_tap_lst[i][7], new_tap_lst[i][8])
        time.sleep(1.5)


def att_0224(n):
    split()
    get_card_attribute()
    get_crd_sorted_taped(n)

