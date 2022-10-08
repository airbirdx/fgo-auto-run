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
from util.log import *

# split the sh picture when it is under battle
def split_in_battle(file):
    # im = Image.open("./tmp/123.png")
    cut_ratio = [0.3, 0.9] # in direction Y
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

        up    = int(0.52 * h)
        down  = int(0.62 * h)
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


def turn_attribute(color_priority=None):
    res = []
    split_in_battle(screenshot_path)
    # sys_log('color_priority : %s' % color_priority)
    crd = Card(color_priority=color_priority)        # ####################
    crd.servant_logo()  # ####################

    for i in range(5):
        crd = Card(color_priority=color_priority)
        crd.set_idx(i)
        crd.analyze()
        res.append(crd)
    return res


def extra_chain(crd_lst, show=1):
    # 首先，将 support 从者的 card.servant += issup * 10
    # update card_list
    # 根据 issup 更新 servant ... 这里是 +=
    update_lst = []
    for card in crd_lst:
        crd = Card()
        crd.copy(card)
        if crd.servant != -1:
            crd.servant += crd.issup * 10
        update_lst.append(crd)
    crd_lst = update_lst

    # 如果有，返回chain的list，如果没有，返回-1
    # 如果不能识别的时候，输出false，默认使用color chain
    # 如果有 extra 的 chain, 输出 servant 编号
    # 然后与第一位 判断 该 servant 的从者优先级，注意仅仅判断从者优先级，如果从者优先级 >=，那么可以使用此，chain
    # 之后只需要把这一个 从者 的所有卡选出来即可

    # 获取最大的card.servant
    lst_servant_num = []
    for card in crd_lst:
        lst_servant_num.append(card.servant)

    tmp = [0] * (max(lst_servant_num)+1)

    for card in crd_lst:
        if card.servant != -1:
            tmp[card.servant] += 1

    extra_svt = -1

    for i in range(len(tmp)):
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

    # 根据 issup 更新 servant ... 这里是 -=
    update_lst = []
    for card in tmp_lst:
        crd = Card()
        crd.copy(card)
        if crd.servant != -1:
            crd.servant -= crd.issup * 10
        update_lst.append(crd)
    tmp_lst = update_lst

    # 如果 chain 中 从者的优先级比 list 中第一个低的话
    # 那么就不执行这个 chain
    # 直接考虑 color chain 或者 平砍 三 张卡
    if tmp_lst[0].servant_priority() == -1:
        tmpchn_prior = tmp_lst[0].buff_priority()   # tmp chain
        sortop_prior = crd_lst[0].buff_priority()   # sort top
    else:
        tmpchn_prior = tmp_lst[0].servant_priority()
        sortop_prior = crd_lst[0].servant_priority()

    if tmpchn_prior < sortop_prior:
        return -1
    else:
        show_cards(tmp_lst, '@SORT/ EXTRA CHAIN', show=show)
        return tmp_lst


def color_chain(crd_lst, show=1):
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
    if tmp_lst[0].servant_priority() == -1:
        tmpchn_prior = tmp_lst[0].buff_priority()   # tmp chain
        sortop_prior = crd_lst[0].buff_priority()   # sort top
    else:
        tmpchn_prior = tmp_lst[0].servant_priority()
        sortop_prior = crd_lst[0].servant_priority()

    if tmpchn_prior < sortop_prior:
        return -1
    else:
        show_cards(tmp_lst, '@SORT/ COLOR CHAIN', show=show)
        return tmp_lst


def turn_sorted(turn_card):

    show_cards(turn_card, '@INFO/ ORIGINAL')

    sort_cards = []
    sort_cards.append(turn_card[0])  # 第一张卡先放到list中

    for curr_card in turn_card[1:]:
        for i in range(len(sort_cards)):
            comp_card = sort_cards[i]
            if curr_card.weight > comp_card.weight:
                sort_cards.insert(i, curr_card)
                break
            elif i == len(sort_cards) - 1:
                sort_cards.append(curr_card)
                break
            else:
                pass

    show_cards(sort_cards, '@SORT/ INITIAL')

    if int(get_cfg('priority', 'chain')):

        chain_mode = int(get_cfg('priority', 'chain'))

        if chain_mode == 1 and extra_chain(sort_cards, show=0) != -1:
            sort_cards = extra_chain(sort_cards)
        elif chain_mode == 1 and color_chain(sort_cards, show=0) != -1:
            sort_cards = color_chain(sort_cards)
        elif chain_mode == 2 and extra_chain(sort_cards, show=0) != -1:
            sort_cards = extra_chain(sort_cards)
        elif chain_mode == 3 and color_chain(sort_cards, show=0) != -1:
            sort_cards = color_chain(sort_cards)

    # 将不能移动的移动到最后，特殊情况
    # 如果chain中有，也是不能够正常启动 chain的
    lst_normal = []
    lst_cantmove = []
    for i in range(len(sort_cards)):
        if sort_cards[i].buff == -2:
            lst_cantmove.append(sort_cards[i])
        else:
            lst_normal.append(sort_cards[i])

    sort_cards = lst_normal + lst_cantmove
    show_cards(sort_cards, '@SORT/ MODIFY BUFF')

    return sort_cards


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

    show_cards(tap_cards, '@SORT/ FINALLY / TAP CARDS')

    return tap_cards


def show_cards(cards, info, show=1):
    if not show:
        return 0
    sys_log(info)
    sys_log('|----|---------|-------|------|------|-----------|-----|--------|')
    sys_log('| ID | SERVANT | COLOR | BUFF | CRIT | POSITION  | SUP | WEIGHT |')
    for card in cards:
        card.show()
    sys_log('|----|---------|-------|------|------|-----------|-----|--------|')



# 返回当前 round, 如果没有识别到，返回-1
def curr_round():
    sh = cv2.imread(screenshot_path, 0)
    for i in range(3):
        tmp = cv2.imread(round_path + f'/round{i+1}.png', 0)
        thd = 0.85
        if analyze(sh, tmp, thd):
            wt_tmp_ini('battle', 'round', i + 1)
            return i + 1

    # 两次校验，防止某些图，一种方法不能采集成功
    for i in range(3):
        tmp = cv2.imread(round_path + f'/twice/round{i + 1}.png', 0)
        thd = 0.85
        if analyze(sh, tmp, thd):
            wt_tmp_ini('battle', 'round', i + 1)
            return i + 1

    return -1

def attack12132314():
    time.sleep(10)
    pass



def get_color_priority(td_idx):
    color_priority = get_cfg('priority', 'color')
    skill_list = cfgstr2lst(skill_string_trans(get_cfg('skill', 'value'), color=1))  # unit:round/turn
    color_list = []

    for skill in skill_list:
        if   'R' in skill:
            color_list.append('R')
        elif 'G' in skill:
            color_list.append('G')
        elif 'B' in skill:
            color_list.append('B')
        else:
            color_list.append('')

    color = color_list[td_idx - 1]  ###
    if not color:
        color_priority = None
        return color_priority

    elif color in 'RGB':
        color_priority = color_priority.replace(color, '')
        color_priority = color + color_priority
        return color_priority

    else:
        sys_log('ERROR! EXIT, get_color_priority')
        exit()


def attack():
    
    if not rd_tmp_ini('battle', 'round'):
        wt_tmp_ini('battle', 'round', 0)
    
    if not rd_tmp_ini('battle', 'turn'):
        wt_tmp_ini('battle', 'turn', 0)

    lst = png_lst(cfg_path)
    svt_priority = get_cfg('priority', 'servant')
    for file in lst:
        # name, ext = os.path.splitext(file)
        if 'servant' in file and not svt_priority:
            os.remove(cfg_path + '/' + file)

    # 获取 skill 和 final ..并转换为新的变量
    if not rd_tmp_ini('battle', 'skill_list'):
        wt_tmp_ini('battle', 'skill_list', cfgstr2lst(skill_string_trans(get_cfg('skill', 'value'))))
    if not rd_tmp_ini('battle', 'ultimate_list'):
        wt_tmp_ini('battle', 'ultimate_list', cfgstr2lst(get_cfg('ultimate', 'value')))

    
    psn = PSN()

    # 获取当前 round 数
    round0 = curr_round()

    # 获取当前回合数，并更新， +=1 是因为文件内是从 0 开始计算的，需要转换一下
    turn = int(rd_tmp_ini('battle', 'turn'))
    turn += 1
    wt_tmp_ini('battle', 'turn', turn)

    sys_log('current @ round : %1d, turn : %-2d' % (round0, turn))

    # 获取 turn / round 参数
    op_unit = get_cfg('skill', 'unit')  # round / turn
    if op_unit == 'round':
        td_idx = round0  # turn_round_idx
    else:
        td_idx = turn

    # 获取设定某些回合技能输入 20201117
    skill_lst = eval(rd_tmp_ini('battle', 'skill_list'))
    if td_idx <= len(skill_lst):
        turn_skill(skill_lst[td_idx - 1])
        skill_lst[td_idx - 1] = ''
        wt_tmp_ini('battle', 'skill_list', skill_lst)

    # 点击 ATTACK 按钮，更新截图
    psn.ATK()
    time.sleep(2)
    screenshot()
    
    # for _ in range(5):
    #     time.sleep(1)
    #     screenshot()
    #     if pic_in_sh(f'{battle_path}/speed.png'):
    #         break
    
    # 获取指令卡色优先级
    color_priority = get_color_priority(td_idx)
    sys_log('color_priority : %s' % color_priority)
    cards_attr = turn_attribute(color_priority=color_priority)   ### 2022-08-19

    # 获取指令卡属性
    # cards_attr = turn_attribute()

    # sort card
    cards_sort = turn_sorted(cards_attr)

    # 这里可以控制前面的输出来进行简化
    ultimate_list = eval(rd_tmp_ini('battle', 'ultimate_list'))
    if td_idx <= len(ultimate_list):
        ins = ultimate_list[td_idx - 1].upper()
    else:
        ins = ''

    if td_idx <= len(ultimate_list) and ins != 'XXX' and ins != '':
        lst = tap_crd(cards_sort, 2)
        idx = 0
        for char in ins:
            if char == 'X':
                crd = lst[idx]
                tap(crd.px, crd.py)
                # time.sleep(1)   # 2022-08-17, for speed-up
                time.sleep(0.1)   # 2022-08-17, for speed-up
                idx += 1
            else:
                eval('psn.E%s()' % char)
                ultimate_list[td_idx - 1] = ''
                wt_tmp_ini('battle', 'ultimate_list', ultimate_list)
    else:
        lst = tap_crd(cards_sort, 3)
        for crd in lst:
            tap(crd.px, crd.py)
            # time.sleep(1)    # 2022-08-17, for speed-up
            # time.sleep(0.1)  # 2022-08-17, for speed-up


