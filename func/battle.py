import cv2
from PIL import Image

from config import *

from util.default import *
from util.scene import curr_png_lst
from util.cvs import position
from util.cvs import analyze

from util.ats import screenshot

from psn.psfunc import *
from psn.PSN import *


# compare the two picture to find whether simlar
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


# split the sh picture when it is under battle
def split_in_battle(file):
    # im = Image.open("./bufferpic/1.png")
    cut_ratio = [0.5, 0.9] # in direction Y
    im = Image.open(file)
    img_size = im.size
    px = img_size[0]
    py = img_size[1]

    interval = px // 5

    up   = py * cut_ratio[0]
    down = py * cut_ratio[1]

    for i in range(5):
        left  = interval * i
        right = interval * (i + 1)
        if right > px:
            right = px
        region = im.crop((left, up, right, down))
        region.save(tmp_path + f'/card_{i}.png')

    for i in range(5):
        im = Image.open(tmp_path + f'/card_{i}.png')
        w, h = im.size

        up    = int(0.3 * h)
        down  = (0.24 + 0.2) * h
        left  = w // 2 - 0.1 * w
        right = w // 2 + 0.1 * w
        region = im.crop((left, up, right, down))
        region.save(tmp_path + f'/tmp_servant_{i}.png')


# Get the current servant number under cfg_path
# Used in analyzing the screenshot before auto-run
def servent_num():
    num = 0

    lst = curr_png_lst(cfg_path)  # list all files in this folder
    lst.sort()

    for pic_file in lst:
        name, extension = os.path.splitext(pic_file)
        num += int('servant' in name)

    # print('servant num = ', num)
    return num


# Get the current servant logo under cfg_path
# Used in analyzing the screenshot before auto-run
def servant_logo():
    for i in range(5):
        if not servent_num():
            res = cv2.imread(tmp_path + '/tmp_servant_0.png')
            cv2.imwrite(cfg_path + '/servant_0.png', res)
        else:
            flg = 0
            for j in range(servent_num()):
                tmp = Image.open(tmp_path + f'/tmp_servant_{i}.png')
                ser = Image.open(cfg_path + f'/servant_{j}.png')
                res = classfiy_histogram(tmp, ser)
                thd = 0.5
                if res > thd:
                    flg += 1
            if not flg:
                new = cv2.imread(tmp_path + f'/tmp_servant_{i}.png')
                cv2.imwrite(cfg_path + f'/servant_{j+1}.png', new)


def training():
    lst = curr_png_lst(cfg_path)
    for file in lst:
        name, ext = os.path.splitext(file)
        if 'train' in name:
            split_in_battle(cfg_path + f'/{file}')
            servant_logo()


def card_attribute(n):
    crd_attr = [0] * 8
    # card idx, servant idx, R, G, B, X(+1/0/-1), baoji, px, py
    # card idx -> use list.insert(0, i) in the end
    # px, py is the position of the card
    card = cv2.imread(tmp_path + f'/card_{n}.png', 0)

    crd_attr[0] = 9 # use 9 as default for servant in cfg is null
    # j indicate servant x under cfg file

    for j in range(servent_num()):
        servant = cv2.imread(cfg_path + f'/servant_{j}.png', 0)
        thd = 0.85
        if analyze(card, servant, thd):
            crd_attr[0] = j     # CARD ATTR : SERVANT INDEX

    tmp_R = cv2.imread(battle_path + f'/buster.png', 0)
    tmp_G = cv2.imread(battle_path + f'/quick.png', 0)
    tmp_B = cv2.imread(battle_path + f'/arts.png', 0)
    RGB = [tmp_R, tmp_G, tmp_B]
    for j in range(3):
        thd = 0.85
        if analyze(card, RGB[j], thd):
            # print('i = %d, servent = %d' % (i, j))
            # Get the position in split picture
            ps = position(card, RGB[j], thd)

            sh =  cv2.imread(screenshot_path, 0)
            w, h = sh.shape[::-1]

            crd_attr[j + 1] = 1                  # CARD ATTR : R / G / B = 0/1
            # Calibra the position to axis of screenshot
            crd_attr[6] = ps[0][0] + w // 5 * n  # CARD ATTR : PX
            crd_attr[7] = ps[0][1] + h // 2      # CARD ATTR : PY

    tmp_buff    = cv2.imread(battle_path + '/restraint.png', 0)
    tmp_debuff  = cv2.imread(battle_path + '/resistance.png', 0)
    tmp_vertigo = cv2.imread(battle_path + '/vertigo.png', 0)
    thd = 0.85

    if analyze(card, tmp_buff, thd):    # CARD ATTR : BUFF : 1 / -1 / -2 / 9
        crd_attr[4] = 1
    elif analyze(card, tmp_debuff, thd):
        crd_attr[4] = -1
    elif analyze(card, tmp_vertigo, thd):
        crd_attr[4] = -2
    else:
        crd_attr[4] = 9

    crd_attr[5] = 0         # CARD ATTR : CRIT RATIO : 10 / 20 / .. / 100

    crd_attr.insert(0, n)   # CARD ATTR : CARD INDEX : [0..4]

    return crd_attr


def turn_attribute():
    turn_attr = []
    for i in range(5):
        crd_attr = card_attribute(i)
        turn_attr.append(crd_attr)
    return turn_attr


def color_num(crd_attr):

    clr_read = crd_color_priority.upper()
    rgb = []
    for char in clr_read:
        if char == 'R':
            tmp = crd_attr[2]
        elif char == 'G':
            tmp = crd_attr[3]
        elif char == 'B':
            tmp = crd_attr[4]
        rgb.append(tmp)
    return rgb[0] * 100 + rgb[1] * 10 + rgb[2]


def svt_priority(crd_attr):

    n = crd_attr[1]

    try:
        servant_priority
    except NameError:
        svt_prior = []
    else:
        svt_prior = servant_priority
        pass

    for i in range(len(svt_prior)):
        if n == svt_prior[i]:
            return 5 - i  # 优先级 5>4>3>2>1...

    return -1  # 从者优先级一样


def turn_sorted(turn_attr):
    # turn_attr = turn_attribute()
    turn_sort = []

    for i in range(len(turn_attr)):

        curr_crd_attr = turn_attr[i]

        if i == 0:
            turn_sort.append(curr_crd_attr)
        else:
            for j in range(len(turn_sort)):

                sort_crd_attr = turn_sort[j]

                if svt_priority(curr_crd_attr) > svt_priority(sort_crd_attr):
                    # 当前卡优先级高，插入到所比较排序的前面去，否则在最后append
                    turn_sort.insert(j, curr_crd_attr)
                    break
                elif svt_priority(curr_crd_attr) == svt_priority(sort_crd_attr):

                    if color_num(curr_crd_attr) >= color_num(sort_crd_attr):
                        turn_sort.insert(j, curr_crd_attr)
                        break
                    else:
                        turn_sort.insert(j + 1, curr_crd_attr)
                        break
                elif j == len(turn_sort) - 1:
                    turn_sort.append(curr_crd_attr)
                    break
                else:
                    pass

    print('*************************************')
    for i in range(len(turn_sort)):
        print(turn_sort[i])

    lst_normal = []
    lst_cantmove = []
    for i in range(len(turn_sort)):
        if turn_sort[i][5] == -2:
            lst_cantmove.append(turn_sort[i])
        else:
            lst_normal.append(turn_sort[i])

    lst_sorted = lst_normal + lst_cantmove

    print('---------------------------------------')
    for i in range(len(lst_sorted)):
        print(lst_sorted[i])

    return lst_sorted

def tap_lst(lst, n):
    # 红色卡置顶
    # n = 3
    tap_lst = lst[n - 5 - 1::-1]  # 前n个逆序排列

    if n == 3:
        sum_r = 0
        for i in range(3):
            sum_r += tap_lst[i][2]
        if sum_r > 0 and tap_lst[0][2] == 0:
            if tap_lst[1][2] > 0:
                swap_crd = tap_lst.pop(1)
            else:  # new_tap_lst[2][2] > 0:
                swap_crd = tap_lst.pop(2)
            tap_lst.insert(0, swap_crd)

    return tap_lst


def attack():
    psn = PSN()

    f = open(tmp_battle, 'r')
    turn = int(f.read())
    f.close()

    turn += 1
    print('{-}{-}{-}{-}{-}curr turn is : %d' % turn)

    skill_lst = cfgstr2lst(default_skill)

    if turn <= len(skill_lst):
        turn_skill(skill_lst[turn - 1])

    psn.ATK()
    time.sleep(1)
    screenshot()

    split_in_battle(screenshot_path)
    turn_attr = turn_attribute()
    # for i in turn_attr:
    #     print(i)
    turn_sort = turn_sorted(turn_attr)
    # for i in tap_lst:
    #     print('--> ', i)

    final_lst = cfgstr2lst(default_final)
    if turn <= len(final_lst):
        ins = final_lst[turn-1].upper()

        if ins != 'XXX' and ins != '':
        #     lst = tap_lst(turn_sort, 3)
        #     for crd in lst:
        #         tap(crd[7], crd[8])
        #         time.sleep(1)
        # else: #说明有一张是宝具
            lst = tap_lst(turn_sort, 2)
            idx = 0
            for char in ins:
                if char == 'X':
                    crd = lst[idx]
                    tap(crd[7], crd[8])
                    time.sleep(1)
                    idx += 1
                else:
                    eval('psn.E%s()' % char)
    else:
        lst = tap_lst(turn_sort, 3)
        for crd in lst:
            tap(crd[7], crd[8])
            time.sleep(1)

    f = open(tmp_battle, 'w')
    f.write(str(turn))
    f.close()
