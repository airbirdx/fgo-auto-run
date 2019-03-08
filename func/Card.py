
__metaclass__ = type

import os
import cv2
from PIL import Image
from util.cvs import *
from util.default import *
from util.global0 import *
from util.scene import png_lst
from func.similar.similar import *


class Card:

    def __init__(self):
        self.__card = -1   # ok
        self.idx = -1      # ok
        self.servant = -1  # ok
        self.color = ''    # ok
        self.buff = 0      # ok
        self.crit = -1     # ok
        self.px = -1       # ok
        self.py = -1       # ok

    def analyze(self):
        if self.idx == -1:
            print('ERROR IN CLASS CARD')
        else:
            self.get_servant()
            self.get_color_and_psn()
            self.get_buff()
            self.get_crit()

    def set_idx(self, n):
        self.idx = n
        self.__card = cv2.imread(tmp_path + f'/card_{n}.png', 0)

    def get_servant(self):  # servant and position
        card = self.__card
        for i in range(self.servant_num()):
            servant = cv2.imread(cfg_path + f'/servant_{i}.png', 0)
            thd = 0.85
            if analyze(card, servant, thd):
                self.servant = i

    def get_color_and_psn(self):
        card = self.__card
        tmpR = cv2.imread(battle_path + '/buster.png', 0)
        tmpG = cv2.imread(battle_path + '/quick.png', 0)
        tmpB = cv2.imread(battle_path + '/arts.png', 0)
        tRGB = [tmpR, tmpG, tmpB]
        sRGB = ['R', 'G', 'B']
        for i in range(3):
            thd = 0.85
            if analyze(card, tRGB[i], thd):
                self.color = sRGB[i]
                ps = position(card, tRGB[i], thd)
                sh = cv2.imread(screenshot_path, 0)
                w, h = sh.shape[::-1]
                self.px = ps[0][0] + w // 5 * self.idx
                self.py = ps[0][1] + h // 2
                break

    def get_buff(self):
        card = self.__card
        tmp_buff    = cv2.imread(battle_path + '/restraint.png', 0)
        tmp_debuff  = cv2.imread(battle_path + '/resistance.png', 0)
        tmp_vertigo = cv2.imread(battle_path + '/vertigo.png', 0)
        thd = 0.85
        if analyze(card, tmp_buff, thd):
            self.buff = 1
        elif analyze(card, tmp_debuff, thd):
            self.buff = -1
        elif analyze(card, tmp_vertigo, thd):
            self.buff = -2
        else:
            self.buff = 0

    def get_crit(self):
        card = self.__card
        self.crit = 0
        crit_100 = cv2.imread(crit_path + '/100.png', 0)
        thd = 0.75 # ####### tst
        if analyze(card, crit_100, thd):
            self.crit = 100
        else:
            for i in range(1, 10):
                crit_x = cv2.imread(crit_path + f'/{i}0.png', 0)
                thd = 0.75
                if analyze(card, crit_x, thd):
                    self.crit = i * 10

    # Get the current servant number under cfg_path
    # Used in analyzing the screenshot before auto-run
    def servant_num(self):
        num = 0

        lst = png_lst(cfg_path)  # list all files in this folder
        lst.sort()

        for pic_file in lst:
            name, extension = os.path.splitext(pic_file)
            num += int('servant' in name)

        # print('servant num = ', num)
        return num

    def show(self):
        # print('CARD - INDEX   = %d' % self.idx)
        # print('CARD - SERVANT = %d' % self.servant)
        # print('CARD - COLOR   = %s' % self.color)
        # print('CARD - BUFF    = %d' % self.buff)
        # print('CARD - CRIT    = %d' % self.crit)
        # print('CARD - PX      = %d' % self.px)
        # print('CARD - PY      = %d' % self.py)
        # print('+-----+---------+-------+------+------+-----------+')
        # print('| IDX | SERVANT | COLOR | BUFF | CRIT |  POSITION |')
        print('| %2d  | %3d     | %2s    | %-3d  | %-4d | %4d, %-4d|' % (self.idx, self.servant, self.color, self.buff, self.crit, self.px, self.py))
        # print('+-----+---------+-------+------+------+-----------+')

    # Get the current servant logo under cfg_path
    # Used in analyzing the screenshot before auto-run
    def servant_logo(self):
        for i in range(5):
            if not self.servant_num():
                res = cv2.imread(tmp_path + '/tmp_servant_0.png')
                cv2.imwrite(cfg_path + '/servant_0.png', res)
            else:
                flg = 0
                for j in range(self.servant_num()):
                    file1 = tmp_path + f'/tmp_servant_{i}.png'
                    file2 = cfg_path + f'/servant_{j}.png'
                    # im1 = cv2.imread(tmp_path + f'/tmp_servant_{i}.png', 0)
                    # im2 = cv2.imread(cfg_path + f'/servant_{j}.png', 0)
                    flg += int(similar_image2(file1, file2))
                if not flg:
                    new = cv2.imread(tmp_path + f'/tmp_servant_{i}.png')
                    cv2.imwrite(cfg_path + f'/servant_{j+1}.png', new)


