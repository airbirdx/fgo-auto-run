import cv2
import os
import numpy as np
import random
from PIL import Image
import operator
import time

screenshot_path = 'sh.png'
# basic_scenes = [cv2.imread(f"./lib/basic/{basic_scene}.png", 0) for basic_scene in basic_scenes]
turn = 0




def classfiy_histogram(image1,image2,size = (256,256)):
	''' 'image1' and 'image2' is a Image Object.
	You can build it by 'Image.open(path)'.
	'Size' is parameter what the image will resize to it.It's 256 * 256 when it default.  
	This function return the similarity rate betweene 'image1' and 'image2'
	'''
	image1 = image1.resize(size).convert("RGB")
	g = image1.histogram()

	image2 = image2.resize(size).convert("RGB")
	s = image2.histogram()

	assert len(g) == len(s),"error"

	data = []

	for index in range(0,len(g)):
		if g[index] != s[index]:
			data.append(1 - abs(g[index] - s[index])/max(g[index],s[index]) )
		else:
			data.append(1)
	
	return sum(data)/len(g)




def screenshot(rotation = 0): # inv-clockwise dir
    os.system('adb shell screencap -p /sdcard/tst.png')
    os.system('adb pull /sdcard/tst.png ./sh.png')

    if rotation:
        img = cv2.imread(screenshot_path, 1) # 1 is color, 0 is gray
        
        for i in range(rotation):
            img = np.rot90(img)

        cv2.imwrite('sh.png', img)
    
    return screenshot_path # can be ##


# 模拟点击与滑动
def tap(x0, y0):
    cmdTap = 'adb shell input tap {x1} {y1}'.format(
        x1=x0,
        y1=y0
    )
    print(cmdTap)
    os.system(cmdTap)


def swipe(x0, y0, x1, y1, delay0):
    cmdSwipe = 'adb shell input swipe {x2} {y2} {x3} {y3} {delay1}'.format(
        x2=x0,
        y2=y0,
        x3=x1,
        y3=y1,
        delay1=delay0
    )
    print(cmdSwipe)
    os.system(cmdSwipe)


def long_tap(x, y):  # random length tap
    delay = random.randrange(5, 100)
    x0 = x + random.randrange(-10, 10)
    y0 = y + random.randrange(-10, 10)
    swipe(x, y, x0, y0, delay)


def tap_card(x, y):  # tap on random location of the card
    x0 = x + random.uniform(0, 75)
    y0 = y + random.uniform(-90, 0)
    x0 = int(x0)
    y0 = int(y0)
    tap(x0, y0)


def basic_tap(x, y):  # tap on random location of the button
    x0 = x + random.uniform(-10, 10)
    y0 = y + random.uniform(-10, 10)
    x0 = int(x0)
    y0 = int(y0)
    tap(x0, y0)


def del_file(path):
    ls = os.listdir(path)
    for i in ls:
        c_path = os.path.join(path, i)
        if os.path.isdir(c_path):
            del_file(c_path)
        else:
            os.remove(c_path)



def analyze(sh, tmp, thd):
    res = cv2.matchTemplate(sh, tmp, cv2.TM_CCOEFF_NORMED)
    if (res >= thd).any():
        return 1


def current_scene():
    file_lst = os.listdir('./lib/basic')       # list all files in this folder
    file_lst.sort()

    print(file_lst)

    sh = cv2.imread(screenshot_path, 0)

    for pic_file in file_lst:
        name, extension = os.path.splitext(pic_file)
        if extension == '.png':
            tmp = cv2.imread(f'./lib/basic/{pic_file}', 0)
            thd = 0.85
            if analyze(sh, tmp, thd):
                return name

def position(sh, tmp, thd):
    res = cv2.matchTemplate(sh, tmp, cv2.TM_CCOEFF_NORMED)
    pos = []
    loc = np.where(res >= thd)
    for pt in zip(*loc[::-1]):
        pos.append(pt)
    return pos

def get_filtered(sh, tmp, thd):
    ary = position(sh, tmp, thd)
    ary.sort()
    for i in range(len(ary)):
        for p in range(1, len(ary) - i):
            for k in range(-5, 5):
                for l in range(-5, 5):
                    if ((ary[i][0] + k) == ary[i + p][0]) and ((ary[i][1] + l) == ary[i + p][1]):
                        ary[i + p] = [0, 0]
    while ary.count([0, 0]) >= 1:
        ary.remove([0, 0])
    return ary

def support_select(person=None, skill=None, lizhuang = None):

    flg_lst = [0,0,0]#,0]
    
    flg_lst[0] = int(person is not None)
    flg_lst[1] = int(skill is not None)
    flg_lst[2] = int(lizhuang is not None)
    # flg_lst[3] = int(lizhuang is not None)

    if not os.path.exists('./tmp/support_select.txt'):
        f = open('./tmp/support_select.txt', 'w')
        f.close()
    
    input_lst = [person, skill, lizhuang]#, lizhuang] # lizhuang0 未能满破######
    
    # print('person = ', person)
    # print('lizhuang = ', lizhuang)
    # print('skill = ', skill)
    
    file_lst = os.listdir('./lib/support_select')       # list all files in this folder
    file_lst.sort()

    sh  = cv2.imread(screenshot_path, 0)
    #         height, width
    im1 = sh[250:590, 50:1820] # zhuzhan 1
    im2 = sh[560:890, 50:1820] # zhuzhan 2

    end = cv2.imread('./lib/support_select/sel_bar_end.png', 0)
    

    # cv2.namedWindow('Detected',0)
    # cv2.startWindowThread()
    # cv2.imshow('Detected',im2)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    flg = False


    if person is None and lizhuang is None and skill is None:
        # 直接随便选择一个
        pass
        return True

    search_flg = False

    if analyze(sh, end, 0.9):
        # 读取文件遍历一遍，看是否有低优先级合适的，没有的话再二次更新
        print('already check all ....')
        basic_tap(1260, 200)
        time.sleep(3)
        basic_tap(1260, 200)
        time.sleep(3)
        return False
    
    for i in range(2):

        match_lst = [0, 0, 0]#, 0] # person, skill, lizhuang1, lizhuang2

        if i == 0:
            imx = im1
        else:
            imx = im2

        for pic_file in file_lst:
            name, extension = os.path.splitext(pic_file)
            if extension == '.png':
                tmp = cv2.imread(f'./lib/support_select/{pic_file}', 0)
                thd = 0.85

                if analyze(imx, tmp, thd):

                    w, h = tmp.shape[::-1]
                    ps = get_filtered(imx, tmp, thd)

                    if i == 0:
                        px = 50 + ps[0][0]
                        py = 250 + ps[0][1]
                    else:
                        px = 50 + ps[0][0]
                        py = 560 + ps[0][1]

                    px = px + w // 2
                    py = py + h // 2
                    
                    print('i = ', i)
                    print('cmp pass /', pic_file)
                    print('name ', name)

                    for j in range(len(input_lst)):
                        if input_lst[j] is not None:# 名字/技能/满破礼装/礼装 对了
                            if input_lst[j] in name: # 加if保证改变后面的时候，前面已经更改过的的不变
                                match_lst[j] = int(input_lst[j] in name)

                                # 这里加上person的坐标信息
                                if j == 0:
                                    match_lst.append(px)
                                    match_lst.append(py)
                          
        # 写入match_lst
        f = open('./tmp/support_select.txt', 'a+')
        f.writelines(str(match_lst) + '\n')
        f.close()


        if operator.eq(flg_lst, match_lst[:3]):
        # if sum(match_lst[0:len(match_lst)]) >= 3:
            pass

            basic_tap(match_lst[3], match_lst[4])
            # genjui
            # 然后再找一遍头像的position位置


            #直接选中
            #点击对应的助战
            return True
        
    if flg:
        return True
    else:
        # 没找到，滑动
        swipe(1024, 800, 1022, 800-538, 2000)
        pass
        # 然后再截图进入循环

                   


def task_select():

    sh  = cv2.imread(screenshot_path, 0)
    # #         height, width
    # im1 = sh[250:590, 50:1820] # zhuzhan 1
    # im2 = sh[560:890, 50:1820] # zhuzhan 2

    task = cv2.imread('./lib/task_select/task_select.png', 0)
    thd = 0.85
    ps = get_filtered(sh, task, thd)

    basic_tap(ps[0][0], ps[0][1])

    del_file('./tmp/')

def team_confirm():
    
    sh  = cv2.imread(screenshot_path, 0)
    # #         height, width
    # im1 = sh[250:590, 50:1820] # zhuzhan 1
    # im2 = sh[560:890, 50:1820] # zhuzhan 2

    tmp = cv2.imread('./lib/team_confirm/team_confirm.png', 0)
    thd = 0.85
    ps = get_filtered(sh, tmp, thd)

    w, h = tmp.shape[::-1]
    px = ps[0][0] + w // 2
    py = ps[0][1] + h // 2

    basic_tap(px, py)





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
        left  = interval * i
        right = interval * (i + 1)
        if right > px:
            right = px
        region = im.crop((left, up, right, down))
        region.save(f"./tmp/card_{i}.png")

    for i in range(5):
        im = Image.open(f"./tmp/card_{i}.png")
        w, h = im.size
        
        up = int(0.3 * h)
        down = (0.24 + 0.2) * h
        left = w // 2 - 0.1 * w
        right = w // 2 + 0.1 * w
        region = im.crop((left, up, right, down))
        region.save(f"./tmp/tmp_servent_{i}.png")
        




def attack_yanzuo_shougao(start=1):


    if not os.path.exists('./tmp/battle.txt'):
        f = open('./tmp/battle.txt', 'w')
        f.write('0')
        f.close()
    # else:
        
    #     f = open('./tmp/battle.txt', 'w')
    #     f.write('0')
    #     f.close()


    f = open('./tmp/battle.txt', 'r')
    turn = int(f.read())
    f.close()

    turn = turn + start - 1

    turn += 1
    print('123 - - - curr turn is : %d' % turn)

    time.sleep(1)

    if turn == 1:

        basic_tap(392,865)
        time.sleep(4)

        basic_tap(1203,865)
        time.sleep(4)

        basic_tap(1347,865)
        time.sleep(4)

        basic_tap(1700,900)
        time.sleep(3)

        basic_tap(620,340)
        time.sleep(2)

        basic_tap(580,800)
        time.sleep(2)

        basic_tap(960,800)
        time.sleep(2)


    elif turn == 2:

        basic_tap(1063,865)
        time.sleep(4)
        basic_tap(482,720)
        time.sleep(6)

        basic_tap(1795,480)
        time.sleep(3)
        basic_tap(1630,465)
        time.sleep(4)
        basic_tap(820,520)
        time.sleep(2)
        basic_tap(1120,520)
        time.sleep(2)
        basic_tap(963,936)
        time.sleep(15)

        basic_tap(1063,865)
        time.sleep(4)

        basic_tap(1203,865)
        time.sleep(4)

        

        basic_tap(392,865)
        time.sleep(4)

        basic_tap(1700,900)
        time.sleep(3)

        basic_tap(580,800)
        time.sleep(2)

        basic_tap(960,800)
        time.sleep(2)

        basic_tap(620,340)
        time.sleep(2)

    elif turn==3:

        basic_tap(585,865)
        time.sleep(4)
	    
        basic_tap(1347,865)
        time.sleep(4)

        basic_tap(992,720)
        time.sleep(6)

        basic_tap(725,865)
        time.sleep(4)

        basic_tap(875,865)
        time.sleep(4)

        basic_tap(1795,480)
        time.sleep(3)
        basic_tap(1360,465)
        time.sleep(4)

        basic_tap(435,60)
        time.sleep(3)
        basic_tap(1795,480)
        time.sleep(3)
        basic_tap(1495,465)
        time.sleep(4)

        basic_tap(1700,900)
        time.sleep(4)

        # get screenshot
        screenshot()

        basic_tap(960,340)
        time.sleep(2)

        att_0224(2)

    elif turn==4:

        basic_tap(245,865)
        time.sleep(4)

        basic_tap(1700,900)
        time.sleep(4)

        # get screenshot
        screenshot()

        att_0224(3)

    else:

        basic_tap(1700,900)
        time.sleep(3)

        # get screenshot
        screenshot()

        att_0224(3)


    f = open('./tmp/battle.txt', 'w')
    f.write(str(turn))
    f.close()


def trophy(): #zhan li pin
    
    sh  = cv2.imread(screenshot_path, 0)
    # #         height, width
    # im1 = sh[250:590, 50:1820] # zhuzhan 1
    # im2 = sh[560:890, 50:1820] # zhuzhan 2

    tmp = cv2.imread('./lib/trophy/next.png', 0)
    thd = 0.85

    if get_filtered(sh, tmp, thd):
        ps = get_filtered(sh, tmp, thd)

        w, h = tmp.shape[::-1]
        px = ps[0][0] + w // 2
        py = ps[0][1] + h // 2

        basic_tap(px, py)

    

def cmd_lut(var):
    if var == 'support_select':
        return support_select(person='meilin', skill='310', lizhuang = 'lizhuang_manpo') # person -> servent
        # return support_select('meilin')
        # function here
        pass
    elif var == 'team_confirm':
        # function here
        team_confirm()
        pass
    elif var == 'task_select':
        # function here
        task_select()
        pass
    elif var == 'loading':
        # function here
        x = random.randint(1920/5,1920/5*4)
        y = random.randint(1080/5,1080/5*4)
        time.sleep(0.5)
        basic_tap(x, y)
        pass
    elif var == 'bond' or var == 'experience':
        # function here
        pass
        basic_tap(960, 500)
        # 羁绊页面
        # 经验值页面
    elif var == 'trophy':
        # function
        trophy()
        pass
        # 找到下一步按钮的中心，并点击
    elif var == 'award':
        # functin
        basic_tap(960, 500)
        pass
        # 随机点击画面
    elif var == 'attack':
        attack_yanzuo_shougao(1)              ################1 turn start
        pass
    elif var == 'add_ap':
        return add_ap(3) #一个金色苹果 
    elif var == 'new_friend':
        new_friend()
    elif var == 'task_failed' or var == 'pullout':
        task_failed()
    else:
        pass

    return False


def task_failed():

    sh  = cv2.imread(screenshot_path, 0)

    tmp = cv2.imread('./lib/task_failed/back.png', 0)
    thd = 0.85

    if analyze(sh, tmp, thd):
        ps = get_filtered(sh, tmp, thd)


        w, h = tmp.shape[::-1]
        px = ps[0][0] + w // 2
        py = ps[0][1] + h // 2

        basic_tap(px, py)
        time.sleep(0.1)

    tmp = cv2.imread('./lib/task_failed/confirm.png', 0)
    thd = 0.85

    if analyze(sh, tmp, thd):
        ps = get_filtered(sh, tmp, thd)

        w, h = tmp.shape[::-1]
        px = ps[0][0] + w // 2
        py = ps[0][1] + h // 2

        basic_tap(px, py)
        time.sleep(0.1)

    tmp = cv2.imread('./lib/task_failed/close.png', 0)
    thd = 0.85

    if analyze(sh, tmp, thd):
        ps = get_filtered(sh, tmp, thd)

        w, h = tmp.shape[::-1]
        px = ps[0][0] + w // 2
        py = ps[0][1] + h // 2

        basic_tap(px, py)
        time.sleep(0.1)

def new_friend():

    sh  = cv2.imread(screenshot_path, 0)

    tmp = cv2.imread('./lib/new_friend/no.png', 0)
    thd = 0.85

    if analyze(sh, tmp, thd):
        ps = get_filtered(sh, tmp, thd)

        w, h = tmp.shape[::-1]
        px = ps[0][0] + w // 2
        py = ps[0][1] + h // 2

        basic_tap(px, py)
        time.sleep(0.1)

    tmp = cv2.imread('./lib/new_friend/no.png', 0)
    thd = 0.85

    if analyze(sh, tmp, thd):
        ps = get_filtered(sh, tmp, thd)

        w, h = tmp.shape[::-1]
        px = ps[0][0] + w // 2
        py = ps[0][1] + h // 2

        basic_tap(px, py)
        time.sleep(0.1)

def add_ap(n):

    if not os.path.exists('./add_ap.txt'):
        f = open('./add_ap.txt', 'w')
        f.write('0')
        f.close()

    f = open('./add_ap.txt', 'r')
    apple_num = int(f.read())
    f.close()

    if apple_num < n:

        


        sh  = cv2.imread(screenshot_path, 0)

        tmp = cv2.imread('./lib/add_ap/appleAu.png', 0)
        thd = 0.85

        if analyze(sh, tmp, thd):
            ps = get_filtered(sh, tmp, thd)


            w, h = tmp.shape[::-1]
            px = ps[0][0] + w // 2
            py = ps[0][1] + h // 2

            basic_tap(px, py)

        
        tmp = cv2.imread('./lib/add_ap/confirm.png', 0)
        thd = 0.85
        if analyze(sh, tmp, thd):
            ps = get_filtered(sh, tmp, thd)

            w, h = tmp.shape[::-1]
            px = ps[0][0] + w // 2
            py = ps[0][1] + h // 2

            basic_tap(px, py)

            apple_num += 1
            f = open('./add_ap.txt', 'w')
            f.write(str(apple_num))
            f.close()

            time.sleep(5)

        return 1

    else:
        return 999




def servent_num():
    num = 0

    file_lst = os.listdir('./config')       # list all files in this folder
    file_lst.sort()

    for pic_file in file_lst:
        name, extension = os.path.splitext(pic_file)
        num += (extension == '.png' and 'servent' in name)
    # print('servent num = ', num)
    return num



def gen_servent_logo():

    for i in range(5):

        if not servent_num():
            res = cv2.imread(f"./tmp/tmp_servent_0.png")
            cv2.imwrite(f"./config/servent_0.png", res)
        else:
            flg = 0

            for j in range(servent_num()):

                tmp = Image.open(f"./tmp/tmp_servent_{i}.png")
                ser = Image.open(f"./config/servent_{j}.png")

                res = classfiy_histogram(tmp, ser)
                # print('i = %d, j = %d, sim_res = %f' % (i, j, res))

                thd = 0.5
                if res > 0.5:

                    flg += 1
            if not flg:
                new = cv2.imread(f"./tmp/tmp_servent_{i}.png")
                cv2.imwrite(f"./config/servent_{j+1}.png", new)
    



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

                card_attribute[j+1] = 1
                card_attribute[6] = px + 1920 // 5 * i
                card_attribute[7] = py + 1080 // 2



      
        tmp_buff    = cv2.imread(f"./lib/battle/restraint.png", 0)
        tmp_debuff  = cv2.imread(f"./lib/battle/resistance.png", 0)
        tmp_vertigo = cv2.imread(f"./lib/battle/vertigo.png", 0) #### warning
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
            return 5-i # 优先级 5>4>3>2>1...

    return -1 #从者优先级一样



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
                    #当前卡优先级高，插入到所比较排序的前面去，否则在最后append
                    print('A (i = crd)/ i = %d, j = %d' %(i, j))
                    crd_sort_lst.insert(j, crd_attr[i])
                    # print('----------------------------------------------------')
                    # for k in range(len(crd_sort_lst)):
                    #     print(crd_sort_lst[k])
                    break
                elif get_servent_priority(crd_attr[i][1]) == get_servent_priority(crd_sort_lst[j][1]):
                    #判断卡颜色234 - RGB
                    
                    tmp_rgb_var_crd = crd_attr[i][2] * 100 + crd_attr[i][3] * 10 + crd_attr[i][4]
                    tmp_rgb_var_sort = crd_sort_lst[j][2] * 100 + crd_sort_lst[j][3] * 10 + crd_sort_lst[j][4]

                    if tmp_rgb_var_crd >= tmp_rgb_var_sort:
                        print('B (i = crd)/ i = %d, j = %d' %(i, j))
                        crd_sort_lst.insert(j, crd_attr[i])
                        # print('----------------------------------------------------')
                        # for k in range(len(crd_sort_lst)):
                        #     print(crd_sort_lst[k])
                        break
                    else:
                        print('C (i = crd)/ i = %d, j = %d' %(i, j))
                        crd_sort_lst.insert(j+1, crd_attr[i])
                        # print('----------------------------------------------------')
                        # for k in range(len(crd_sort_lst)):
                        #     print(crd_sort_lst[k])
                        break
                elif j == len(crd_sort_lst) - 1:
                    print('D (i = crd)/ i = %d, j = %d' %(i, j))
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
    new_tap_lst = lst_sorted[n-5-1::-1] # 前n个逆序排列

    # tmp_new_tap_lst = lst_sorted[::-1] # 前n个逆序排列
    # new_tap_lst = tmp_new_tap_lst[:n]
    
    if n==3:
        sum_r = 0
        for iii in range(3):
            sum_r += new_tap_lst[iii][2]
        if sum_r > 0 and new_tap_lst[0][2] == 0:

            if new_tap_lst[1][2] > 0:
                tmp_swap_lst = new_tap_lst.pop(1)
            else: # new_tap_lst[2][2] > 0:
                tmp_swap_lst = new_tap_lst.pop(2)
            new_tap_lst.insert(0, tmp_swap_lst)

    for i in range(n):
        basic_tap(new_tap_lst[i][7], new_tap_lst[i][8])
        time.sleep(1.5)



def att_0224(n):
    split()
    get_card_attribute()
    get_crd_sorted_taped(n)



screenshot(rotation = 0) # meizu 1
# # # att_0224(3)
#
#
# del_file('./tmp/')
#
# if os.path.exists('./add_ap.txt'):
#     os.remove('./add_ap.txt')
#
# screenshot(rotation = 0)
#
#
# while(True):
#
#     time.sleep(1)
#
#     screenshot(rotation = 0) # meizu 1
#
#     sh = cv2.imread(screenshot_path, 0)
#
#     last_sh = 'None'
#
#     var = current_scene()
#     print('! - current sence = ', var)
#
#
#     # cmd_lut(var)
#     if cmd_lut(var) == 999:
#         break
#
#
# print('//-------------------------------------------------//')
# print('//-------   D  O  N  E    -------------------------//')
# print('//-------------------------------------------------//')
# print('//-------------------------------------------------//')




        
