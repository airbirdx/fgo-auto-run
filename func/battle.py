import cv2
from PIL import Image

from config import *
from util.default import *
from util.scene import png_lst
from util.cvs import position
from util.cvs import analyze
from util.global0 import *
from util.ats import screenshot
from psn.psfunc import *
from psn.PSN import *
from func.Card import *


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


def training():
    lst = png_lst(cfg_path)
    for file in lst:
        name, ext = os.path.splitext(file)
        if 'train' in name:
            split_in_battle(cfg_path + f'/{file}')
            crd = Card()
            crd.servant_logo()


def turn_attribute():
    res = []
    split_in_battle(screenshot_path)

    crd = Card()        # ####################
    crd.servant_logo()  # ####################

    for i in range(5):
        # print(i)
        crd = Card()
        crd.set_idx(i)
        crd.analyze()
        # crd.show()
        # attr = [crd.idx, crd.servant, crd.color, crd.buff, crd.crit, crd.px, crd.py]
        # res.append(attr)
        res.append(crd)
    # for i in range(5):
    #     crd = res[i]
    #     print([crd.idx, crd.servant, crd.color, crd.buff, crd.crit, crd.px, crd.py])
    return res


def card_priority(crd):
    a = servant_priority(crd)  # 十进制：1位
    b = buff_priority(crd)     # 十进制：1位
    c = color_priority(crd)    # 十进制：1位
    d = crit_priority(crd)     # 十进制：2位
    # 几个参数中优先级，a > b > c > d
    #       servant > buff > color > crit
    res = a * 1e4 + b * 1e3 + c * 1e2 + d
    return res


def servant_priority(crd):
    svt_prior = eval(rd_global('set_servant_priority'))
    # 输出，优先级从高到低，5/4/3/2/1/0
    for i in range(len(svt_prior)):
        if crd.servant == svt_prior[i]:
            return 5 - i

    # 如果定义为空，一样的返回 -1
    return -1


def color_priority(crd):
    clr_prior = rd_global('set_color_priority')
    clr_prior = clr_prior.upper()
    for i in range(3):
        if clr_prior[i] == crd.color:
            return 3-i
        else:
            pass

    return -1


def crit_priority(crd):
    return crd.crit // 10


def buff_priority(crd):
    return crd.buff


def extra_chain(crd_lst):
    # 如果有，返回chain的list，如果没有，返回-1
    # 如果不能识别的时候，输出false，默认使用color chain
    # 如果有 extra 的 chain, 输出 servant 编号
    # 然后与第一位 判断 该 servant 的从者优先级，注意仅仅判断从者优先级，如果从者优先级 >=，那么可以使用此，chain
    # 之后只需要把这一个 从者 的所有卡选出来即可
    tmp = [0] * 6
    for card in crd_lst:
        if card.servant == -1:
           pass
        else:
            tmp[card.servant] += 1
    # i = servant number
    extra_svt = -1
    for i in tmp:
        if tmp[i] >= 3:
            extra_svt = i
            break

    if extra_svt == -1:
        return -1

    tmp_lst0 = []
    tmp_lst1 = []
    for card in crd_lst:
        if card.servant == extra_svt:
            tmp_lst0.append(card)
        else:
            tmp_lst1.append(card)
    tmp_lst = tmp_lst0 + tmp_lst1
    # 如果 chain 中 从者的优先级比 list 中第一个低的话
    # 那么就不执行这个 chain
    # 直接考虑 color chain 或者 平砍 三 张卡
    if servant_priority(tmp_lst[0]) == -1:
        tmpchn_prior = buff_priority(tmp_lst[0])   # tmp chain
        sortop_prior = buff_priority(crd_lst[0])   # sort top
    else:
        tmpchn_prior = servant_priority(tmp_lst[0])
        sortop_prior = servant_priority(crd_lst[0])

    if tmpchn_prior < sortop_prior:
        return -1
    else:
        return tmp_lst


def color_chain(crd_lst):
    # 返回颜色的字符，如果没有，返回-1
    rgb = 'RGB'
    lst = [0] * 3
    for i in range(3):
        char = rgb[i]
        for card in crd_lst:
            if char == card.color:
                lst[i] += 1

        chain_clr = -1
    for i in range(3):
        if lst[i] >= 3:
            chain_clr = rgb[i]

    if chain_clr == -1:
        return -1

    # 已知 color

    tmp_lst0 = []
    tmp_lst1 = []
    for card in crd_lst:
        if card.color == chain_clr:
            tmp_lst0.append(card)
        else:
            tmp_lst1.append(card)
    tmp_lst = tmp_lst0 + tmp_lst1
    # 如果 chain 中 从者的优先级比 list 中第一个低的话
    # 那么就不执行这个 chain
    # 直接考虑 color chain 或者 平砍 三 张卡
    if servant_priority(tmp_lst[0]) == -1:
        tmpchn_prior = buff_priority(tmp_lst[0])   # tmp chain
        sortop_prior = buff_priority(crd_lst[0])   # sort top
    else:
        tmpchn_prior = servant_priority(tmp_lst[0])
        sortop_prior = servant_priority(crd_lst[0])

    if tmpchn_prior < sortop_prior:
        return -1
    else:
        return tmp_lst


def turn_sorted(turn_card):

    print('**@**@**@**@**@**@**@**@**@**@**@**@**@**[ X ] ORIGINAL CARD')
    for card in turn_card:
        card.show()

    sort_card = []
    sort_card.append(turn_card[0])  # 第一张卡先放到list中

    for curr_card in turn_card[1:]:
        # print('curr_card', curr_card)
        for i in range(len(sort_card)):
            comp_card = turn_card[i]
            if card_priority(curr_card) > card_priority(comp_card):
                sort_card.insert(i, curr_card)
                break
            elif i == len(sort_card) - 1:
                sort_card.append(curr_card)
                break
            else:
                pass

    print('**@**@**@**@**@**@**@**@**@**@**@**@**@**[ X ] SORT A')
    for card in sort_card:
        card.show()

    if eval(rd_global('set_default_chain')):

        if extra_chain(sort_card) != -1:
            sort_card = extra_chain(sort_card)

            print('**@**@**@**@**@**@**@**@**@**@**@**@**@**[ X ] SORT B (EXTRA CHAIN)')
            for card in sort_card:
                card.show()

        elif color_chain(sort_card) != -1:
            sort_card = color_chain(sort_card)

            print('**@**@**@**@**@**@**@**@**@**@**@**@**@**[ X ] SORT C (COLOR CHAIN)')
            for card in sort_card:
                card.show()

        else:
            pass


    # 将不能移动的移动到最后，特殊情况
    # 如果chain中有，也是不能够正常启动 chain的
    lst_normal = []
    lst_cantmove = []
    for i in range(len(sort_card)):
        if sort_card[i].buff == -2:
            lst_cantmove.append(sort_card[i])
        else:
            lst_normal.append(sort_card[i])

    sort_card = lst_normal + lst_cantmove


    print('**@**@**@**@**@**@**@**@**@**@**@**@**@**[ X ] SORT D (CHANGE BUFF = -2)')
    for card in sort_card:
        card.show()

    return sort_card


def tap_crd(cards, n):
    tap_cards = cards[n - 5 - 1::-1]  # 前n个逆序排列
    if n == 3:
        sum = 0
        for card in tap_cards:
            sum += int(card.color == 'R')
        if sum >0 and tap_cards[0].color != 'R':
            if tap_cards[1].color == 'R':
                swap_card = tap_cards.pop(1)
            else:
                swap_card = tap_cards.pop(2)
            tap_cards.insert(0, swap_card)

    return tap_cards


# 返回当前 round, 如果没有识别到，返回-1
def curr_round():
    sh = cv2.imread(screenshot_path, 0)
    for i in range(3):
        tmp = cv2.imread(round_path + f'/round{i+1}.png', 0)
        thd = 0.85
        if analyze(sh, tmp, thd):
            wt_global('round', i + 1)
            return i+1
    return -1






def attack():
    psn = PSN()

    # 获取当前 round 数
    round = curr_round()
    # print('round', round)


    # 获取当前回合数，并更新， +=1 是因为文件内是从 0 开始计算的，需要转换一下
    turn = eval(rd_global('turn'))
    turn += 1
    wt_global('turn', turn)

    # 获取设定某些回合技能输入
    default_skill = rd_global('set_default_skill')
    skill_lst = cfgstr2lst(default_skill)
    if turn <= len(skill_lst):
        turn_skill(skill_lst[turn - 1])

    # 点击 ATTACK 按钮，更新截图
    psn.ATK()
    time.sleep(1)
    screenshot()

    # 获取指令卡属性
    cards_attr = turn_attribute()
    cards_sort = turn_sorted(cards_attr)
    # cards_tap  = tap_crd(cards_sort, n) #####

    default_final = rd_global('set_default_final')
    final_lst = cfgstr2lst(default_final)


    # 这里有段重复，应该可以后期简化
    # 这里可以控制前面的输出来进行简化

    final_unit = rd_global('set_default_final_unit') # round / turn
    if final_unit == 'round':
        td_idx = round  # turn_round_idx
    else:
        td_idx = turn


    if td_idx <= len(final_lst):
        ins = final_lst[td_idx-1].upper()

        if ins != 'XXX' and ins != '':
        #     lst = tap_lst(turn_sort, 3)
        #     for crd in lst:
        #         tap(crd[7], crd[8])
        #         time.sleep(1)
        # else: #说明有一张是宝具
            lst = tap_crd(cards_sort, 2)
            idx = 0
            for char in ins:
                if char == 'X':
                    crd = lst[idx]
                    tap(crd.px, crd.py)
                    time.sleep(1)
                    idx += 1
                else:
                    eval('psn.E%s()' % char)
        else:
            lst = tap_crd(cards_sort, 3)
            for crd in lst:
                tap(crd.px, crd.py)
                time.sleep(1)
    else:
        lst = tap_crd(cards_sort, 3)
        for crd in lst:
            tap(crd.px, crd.py)
            time.sleep(1)









def tst_class_Card():
    from func.similar.similar import similar_image2

    for i in range(5):
        for j in range(5):
            if i < j:
                file1 = f'./cfg/servant_{i}.png'
                file2 = f'./cfg/servant_{j}.png'
                print('i = %d, j = %d' % (i, j), end = ' -->')
                print(bool(similar_image2(file1, file2)))

                # im1 = Image.open(f'./cfg/servant_{i}.png')
                # im2 = Image.open(f'./cfg/servant_{j}.png')
                # print('i = %d, j = %d' % (i, j), simliar_image(im1, im2))


