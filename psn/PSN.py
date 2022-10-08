
__metaclass__ = type

import time
from util.ats import tap
from util.global0 import speed


class PSN:
    def __init__(self):
        pass

    def A(self, duration=None, skill_speedup=False):
        if duration is None:
            duration = 3.0
        duration = duration * speed()
        tap(102, 865)
        if skill_speedup:
            self.SKILL_SPEEDUP()
        time.sleep(duration)

    def B(self, duration=None, skill_speedup=False):
        if duration is None:
            duration = 3.0
        duration = duration * speed()
        tap(245, 865)
        if skill_speedup:
            self.SKILL_SPEEDUP()
        time.sleep(duration)

    def C(self, duration=None, skill_speedup=False):
        if duration is None:
            duration = 3.0
        duration = duration * speed()
        tap(392, 865)
        if skill_speedup:
            self.SKILL_SPEEDUP()
        time.sleep(duration)

    def I(self, duration=None, skill_speedup=False):
        if duration is None:
            duration = 3.0
        duration = duration * speed()
        tap(585, 865)
        if skill_speedup:
            self.SKILL_SPEEDUP()
        time.sleep(duration)

    def J(self, duration=None, skill_speedup=False):
        if duration is None:
            duration = 3.0
        duration = duration * speed()
        tap(725, 865)
        if skill_speedup:
            self.SKILL_SPEEDUP()
        time.sleep(duration)

    def K(self, duration=None, skill_speedup=False):
        if duration is None:
            duration = 3.0
        duration = duration * speed()
        tap(875, 865)
        if skill_speedup:
            self.SKILL_SPEEDUP()
        time.sleep(duration)

    def O(self, duration=None, skill_speedup=False):
        if duration is None:
            duration = 3.0
        duration = duration * speed()
        tap(1063, 865)
        if skill_speedup:
            self.SKILL_SPEEDUP()
        time.sleep(duration)

    def P(self, duration=None, skill_speedup=False):
        if duration is None:
            duration = 3.0
        duration = duration * speed()
        tap(1203, 865)
        if skill_speedup:
            self.SKILL_SPEEDUP()
        time.sleep(duration)

    def Q(self, duration=None, skill_speedup=False):
        if duration is None:
            duration = 3.0
        duration = duration * speed()
        tap(1347, 865)
        if skill_speedup:
            self.SKILL_SPEEDUP()
        time.sleep(duration)

    def P1(self, duration=None, skill_speedup=False):
        if duration is None:
            duration = 0.5
        duration = duration * speed()
        tap(200, 800)
        if skill_speedup:
            self.SKILL_SPEEDUP()
        time.sleep(duration)

    def P2(self, duration=None, skill_speedup=False):
        if duration is None:
            duration = 0.5
        duration = duration * speed()
        tap(580, 800)
        if skill_speedup:
            self.SKILL_SPEEDUP()
        time.sleep(duration)

    def P3(self, duration=None, skill_speedup=False):
        if duration is None:
            duration = 0.5
        duration = duration * speed()
        tap(960, 800)
        if skill_speedup:
            self.SKILL_SPEEDUP()
        time.sleep(duration)

    def P4(self, duration=None, skill_speedup=False):
        if duration is None:
            duration = 0.5
        duration = duration * speed()
        tap(1340, 800)
        if skill_speedup:
            self.SKILL_SPEEDUP()
        time.sleep(duration)

    def P5(self, duration=None, skill_speedup=False):
        if duration is None:
            duration = 0.5
        duration = duration * speed()
        tap(1720, 800)
        if skill_speedup:
            self.SKILL_SPEEDUP()
        time.sleep(duration)

    def EA(self, duration=None, skill_speedup=False):
        if duration is None:
            duration = 1.0
        duration = duration * speed()
        tap(620, 340)
        if skill_speedup:
            self.SKILL_SPEEDUP()
        time.sleep(duration)

    def EB(self, duration=None, skill_speedup=False):
        if duration is None:
            duration = 1.0
        duration = duration * speed()
        tap(960, 340)
        if skill_speedup:
            self.SKILL_SPEEDUP()
        time.sleep(duration)

    def EC(self, duration=None, skill_speedup=False):
        if duration is None:
            duration = 1.0
        duration = duration * speed()
        tap(1300, 340)
        if skill_speedup:
            self.SKILL_SPEEDUP()
        time.sleep(duration)

    def SKILL_SPEEDUP(self, duration=None, skill_speedup=False):
        if duration is None:
            duration = 0.0
        duration = duration * speed()
        tap(958, 290)
        if skill_speedup:
            self.SKILL_SPEEDUP()
        time.sleep(duration)

    def MS(self, duration=None, skill_speedup=False):
        if duration is None:
            duration = 2.0
        duration = duration * speed()
        tap(1795, 480)
        if skill_speedup:
            self.SKILL_SPEEDUP()
        time.sleep(duration)

    def X(self, duration=None, skill_speedup=False):
        if duration is None:
            duration = 3.0
        duration = duration * speed()
        tap(1360, 465)
        if skill_speedup:
            self.SKILL_SPEEDUP()
        time.sleep(duration)

    def Y(self, duration=None, skill_speedup=False):
        if duration is None:
            duration = 3.0
        duration = duration * speed()
        tap(1495, 465)
        if skill_speedup:
            self.SKILL_SPEEDUP()
        time.sleep(duration)

    def Z(self, duration=None, skill_speedup=False):
        if duration is None:
            duration = 3.0
        duration = duration * speed()
        tap(1630, 465)
        if skill_speedup:
            self.SKILL_SPEEDUP()
        time.sleep(duration)

    def DR1(self, duration=None, skill_speedup=False):
        if duration is None:
            duration = 1.0
        duration = duration * speed()
        tap(800, 60)
        if skill_speedup:
            self.SKILL_SPEEDUP()
        time.sleep(duration)

    def DR2(self, duration=None, skill_speedup=False):
        if duration is None:
            duration = 1.0
        duration = duration * speed()
        tap(435, 60)
        if skill_speedup:
            self.SKILL_SPEEDUP()
        time.sleep(duration)

    def DR3(self, duration=None, skill_speedup=False):
        if duration is None:
            duration = 1.0
        duration = duration * speed()
        tap(70, 60)
        if skill_speedup:
            self.SKILL_SPEEDUP()
        time.sleep(duration)

    def SEL0(self, duration=None, skill_speedup=False):
        if duration is None:
            duration = 1.0
        duration = duration * speed()
        tap(1649, 225)
        if skill_speedup:
            self.SKILL_SPEEDUP()
        time.sleep(duration)

    def SEL31(self, duration=None, skill_speedup=False):
        if duration is None:
            duration = 5.0
        duration = duration * speed()
        tap(482, 720)
        if skill_speedup:
            self.SKILL_SPEEDUP()
        time.sleep(duration)

    def SEL32(self, duration=None, skill_speedup=False):
        if duration is None:
            duration = 5.0
        duration = duration * speed()
        tap(992, 720)
        if skill_speedup:
            self.SKILL_SPEEDUP()
        time.sleep(duration)

    def SEL33(self, duration=None, skill_speedup=False):
        if duration is None:
            duration = 5.0
        duration = duration * speed()
        tap(1446, 720)
        if skill_speedup:
            self.SKILL_SPEEDUP()
        time.sleep(duration)

    def SEL21(self, duration=None, skill_speedup=False):
        if duration is None:
            duration = 5.0
        duration = duration * speed()
        tap(737, 720)
        if skill_speedup:
            self.SKILL_SPEEDUP()
        time.sleep(duration)

    def SEL22(self, duration=None, skill_speedup=False):
        if duration is None:
            duration = 5.0
        duration = duration * speed()
        tap(1219, 720)
        if skill_speedup:
            self.SKILL_SPEEDUP()
        time.sleep(duration)

    def SEL11(self, duration=None, skill_speedup=False):
        if duration is None:
            duration = 5.0
        duration = duration * speed()
        tap(992, 720)
        if skill_speedup:
            self.SKILL_SPEEDUP()
        time.sleep(duration)

    def S0(self, duration=None, skill_speedup=False):
        if duration is None:
            duration = 1.0
        duration = duration * speed()
        tap(963, 936)
        if skill_speedup:
            self.SKILL_SPEEDUP()
        time.sleep(duration)

    def S1(self, duration=None, skill_speedup=False):
        if duration is None:
            duration = 1.0
        duration = duration * speed()
        tap(220, 520)
        if skill_speedup:
            self.SKILL_SPEEDUP()
        time.sleep(duration)

    def S2(self, duration=None, skill_speedup=False):
        if duration is None:
            duration = 1.0
        duration = duration * speed()
        tap(520, 520)
        if skill_speedup:
            self.SKILL_SPEEDUP()
        time.sleep(duration)

    def S3(self, duration=None, skill_speedup=False):
        if duration is None:
            duration = 1.0
        duration = duration * speed()
        tap(820, 520)
        if skill_speedup:
            self.SKILL_SPEEDUP()
        time.sleep(duration)

    def S4(self, duration=None, skill_speedup=False):
        if duration is None:
            duration = 1.0
        duration = duration * speed()
        tap(1120, 520)
        if skill_speedup:
            self.SKILL_SPEEDUP()
        time.sleep(duration)

    def S5(self, duration=None, skill_speedup=False):
        if duration is None:
            duration = 1.0
        duration = duration * speed()
        tap(1420, 520)
        if skill_speedup:
            self.SKILL_SPEEDUP()
        time.sleep(duration)

    def S6(self, duration=None, skill_speedup=False):
        if duration is None:
            duration = 1.0
        duration = duration * speed()
        tap(1720, 520)
        if skill_speedup:
            self.SKILL_SPEEDUP()
        time.sleep(duration)

    def ATK(self, duration=None, skill_speedup=False):
        if duration is None:
            duration = 2.0
        duration = duration * speed()
        tap(1700, 900)
        if skill_speedup:
            self.SKILL_SPEEDUP()
        time.sleep(duration)

    def START(self, duration=None, skill_speedup=False):
        if duration is None:
            duration = 30.0
        duration = duration * speed()
        tap(1780, 1010)
        if skill_speedup:
            self.SKILL_SPEEDUP()
        time.sleep(duration)

    def NEXT(self, duration=None, skill_speedup=False):
        if duration is None:
            duration = 1.0
        duration = duration * speed()
        tap(1660, 1010)
        if skill_speedup:
            self.SKILL_SPEEDUP()
        time.sleep(duration)

    def INFI0(self, duration=None, skill_speedup=False):
        if duration is None:
            duration = 0.2
        duration = duration * speed()
        tap(584, 647)
        if skill_speedup:
            self.SKILL_SPEEDUP()
        time.sleep(duration)

    def INFI1(self, duration=None, skill_speedup=False):
        if duration is None:
            duration = 2.0
        duration = duration * speed()
        tap(1710, 365)
        if skill_speedup:
            self.SKILL_SPEEDUP()
        time.sleep(duration)

    def INFI2(self, duration=None, skill_speedup=False):
        if duration is None:
            duration = 3.0
        duration = duration * speed()
        tap(1255, 840)
        if skill_speedup:
            self.SKILL_SPEEDUP()
        time.sleep(duration)

    def INFI3(self, duration=None, skill_speedup=False):
        if duration is None:
            duration = 2.0
        duration = duration * speed()
        tap(960, 840)
        if skill_speedup:
            self.SKILL_SPEEDUP()
        time.sleep(duration)

    def DTASK(self, duration=None, skill_speedup=False):
        if duration is None:
            duration = 3.0
        duration = duration * speed()
        tap(1050, 345)
        if skill_speedup:
            self.SKILL_SPEEDUP()
        time.sleep(duration)

    def DZHUZHAN(self, duration=None, skill_speedup=False):
        if duration is None:
            duration = 3.0
        duration = duration * speed()
        tap(240, 465)
        if skill_speedup:
            self.SKILL_SPEEDUP()
        time.sleep(duration)

    def P_AP50(self, duration=None, skill_speedup=False):
        if duration is None:
            duration = 1.0
        duration = duration * speed()
        tap(335, 1040)
        if skill_speedup:
            self.SKILL_SPEEDUP()
        time.sleep(duration)

    def SUPPREF(self, duration=None, skill_speedup=False):
        if duration is None:
            duration = 1.0
        duration = duration * speed()
        tap(1277, 193)
        if skill_speedup:
            self.SKILL_SPEEDUP()
        time.sleep(duration)

    def ZHIJIE0(self, duration=None, skill_speedup=False):
        if duration is None:
            duration = 1.0
        duration = duration * speed()
        tap(140, 195)
        if skill_speedup:
            self.SKILL_SPEEDUP()
        time.sleep(duration)

    def ZHIJIE1(self, duration=None, skill_speedup=False):
        if duration is None:
            duration = 1.0
        duration = duration * speed()
        tap(241, 195)
        if skill_speedup:
            self.SKILL_SPEEDUP()
        time.sleep(duration)

    def ZHIJIE2(self, duration=None, skill_speedup=False):
        if duration is None:
            duration = 1.0
        duration = duration * speed()
        tap(342, 195)
        if skill_speedup:
            self.SKILL_SPEEDUP()
        time.sleep(duration)

    def ZHIJIE3(self, duration=None, skill_speedup=False):
        if duration is None:
            duration = 1.0
        duration = duration * speed()
        tap(443, 195)
        if skill_speedup:
            self.SKILL_SPEEDUP()
        time.sleep(duration)

    def ZHIJIE4(self, duration=None, skill_speedup=False):
        if duration is None:
            duration = 1.0
        duration = duration * speed()
        tap(544, 195)
        if skill_speedup:
            self.SKILL_SPEEDUP()
        time.sleep(duration)

    def ZHIJIE5(self, duration=None, skill_speedup=False):
        if duration is None:
            duration = 1.0
        duration = duration * speed()
        tap(645, 195)
        if skill_speedup:
            self.SKILL_SPEEDUP()
        time.sleep(duration)

    def ZHIJIE6(self, duration=None, skill_speedup=False):
        if duration is None:
            duration = 1.0
        duration = duration * speed()
        tap(746, 195)
        if skill_speedup:
            self.SKILL_SPEEDUP()
        time.sleep(duration)

    def ZHIJIE7(self, duration=None, skill_speedup=False):
        if duration is None:
            duration = 1.0
        duration = duration * speed()
        tap(847, 195)
        if skill_speedup:
            self.SKILL_SPEEDUP()
        time.sleep(duration)

    def ZHIJIE8(self, duration=None, skill_speedup=False):
        if duration is None:
            duration = 1.0
        duration = duration * speed()
        tap(948, 195)
        if skill_speedup:
            self.SKILL_SPEEDUP()
        time.sleep(duration)

    def ZHIJIE9(self, duration=None, skill_speedup=False):
        if duration is None:
            duration = 1.0
        duration = duration * speed()
        tap(1049, 195)
        if skill_speedup:
            self.SKILL_SPEEDUP()
        time.sleep(duration)

    def SKIPS(self, duration=None, skill_speedup=False):
        if duration is None:
            duration = 2.0
        duration = duration * speed()
        tap(1770, 60)
        if skill_speedup:
            self.SKILL_SPEEDUP()
        time.sleep(duration)

    def SKIPN(self, duration=None, skill_speedup=False):
        if duration is None:
            duration = 2.0
        duration = duration * speed()
        tap(680, 840)
        if skill_speedup:
            self.SKILL_SPEEDUP()
        time.sleep(duration)

    def SKIPY(self, duration=None, skill_speedup=False):
        if duration is None:
            duration = 2.0
        duration = duration * speed()
        tap(1240, 840)
        if skill_speedup:
            self.SKILL_SPEEDUP()
        time.sleep(duration)

    def ADDAP(self, duration=None, skill_speedup=False):
        if duration is None:
            duration = 2.0
        duration = duration * speed()
        tap(250, 1040)
        if skill_speedup:
            self.SKILL_SPEEDUP()
        time.sleep(duration)

    def AuAPPLE(self, duration=None, skill_speedup=False):
        if duration is None:
            duration = 2.0
        duration = duration * speed()
        tap(670, 475)
        if skill_speedup:
            self.SKILL_SPEEDUP()
        time.sleep(duration)

    def CONFIRM(self, duration=None, skill_speedup=False):
        if duration is None:
            duration = 2.0
        duration = duration * speed()
        tap(1260, 840)
        if skill_speedup:
            self.SKILL_SPEEDUP()
        time.sleep(duration)

    def CANCLE(self, duration=None, skill_speedup=False):
        if duration is None:
            duration = 2.0
        duration = duration * speed()
        tap(660, 840)
        if skill_speedup:
            self.SKILL_SPEEDUP()
        time.sleep(duration)

    def PYPONT(self, duration=None, skill_speedup=False):
        if duration is None:
            duration = 1.0
        duration = duration * speed()
        tap(1500, 100)
        if skill_speedup:
            self.SKILL_SPEEDUP()
        time.sleep(duration)

    def ZOOM(self, duration=None, skill_speedup=False):
        if duration is None:
            duration = 1.0
        duration = duration * speed()
        tap(40, 1015)
        if skill_speedup:
            self.SKILL_SPEEDUP()
        time.sleep(duration)

    def STRSELECT(self, duration=None, skill_speedup=False):
        if duration is None:
            duration = 1.0
        duration = duration * speed()
        tap(650, 350)
        if skill_speedup:
            self.SKILL_SPEEDUP()
        time.sleep(duration)

    def CRAFTONE(self, duration=None, skill_speedup=False):
        if duration is None:
            duration = 1.0
        duration = duration * speed()
        tap(210, 380)
        if skill_speedup:
            self.SKILL_SPEEDUP()
        time.sleep(duration)

    def A_SELECT(self, duration=None, skill_speedup=False):
        if duration is None:
            duration = 1.0
        duration = duration * speed()
        tap(1465, 192)
        if skill_speedup:
            self.SKILL_SPEEDUP()
        time.sleep(duration)

    def A_SORT(self, duration=None, skill_speedup=False):
        if duration is None:
            duration = 1.0
        duration = duration * speed()
        tap(1690, 192)
        if skill_speedup:
            self.SKILL_SPEEDUP()
        time.sleep(duration)

    def A_JUEDING(self, duration=None, skill_speedup=False):
        if duration is None:
            duration = 1.0
        duration = duration * speed()
        tap(1730, 1010)
        if skill_speedup:
            self.SKILL_SPEEDUP()
        time.sleep(duration)

    def A_1ST_ONE(self, duration=None, skill_speedup=False):
        if duration is None:
            duration = 1.0
        duration = duration * speed()
        tap(210, 380)
        if skill_speedup:
            self.SKILL_SPEEDUP()
        time.sleep(duration)

    def A_xBACK(self, duration=None, skill_speedup=False):
        if duration is None:
            duration = 1.0
        duration = duration * speed()
        tap(660, 660)
        if skill_speedup:
            self.SKILL_SPEEDUP()
        time.sleep(duration)

    def CRAFT_SCREEN(self, duration=None, skill_speedup=False):
        if duration is None:
            duration = 1.0
        duration = duration * speed()
        tap(1465, 192)
        if skill_speedup:
            self.SKILL_SPEEDUP()
        time.sleep(duration)

    def CRAFT_SCREEN_x2(self, duration=None, skill_speedup=False):
        if duration is None:
            duration = 1.0
        duration = duration * speed()
        tap(1240, 352)
        if skill_speedup:
            self.SKILL_SPEEDUP()
        time.sleep(duration)

    def CRAFT_SCREEN_x1(self, duration=None, skill_speedup=False):
        if duration is None:
            duration = 1.0
        duration = duration * speed()
        tap(1530, 352)
        if skill_speedup:
            self.SKILL_SPEEDUP()
        time.sleep(duration)

    def CRAFT_SCREEN_DEFAULT(self, duration=None, skill_speedup=False):
        if duration is None:
            duration = 1.0
        duration = duration * speed()
        tap(340, 955)
        if skill_speedup:
            self.SKILL_SPEEDUP()
        time.sleep(duration)

    def CRAFT_SCREEN_CONFIRM(self, duration=None, skill_speedup=False):
        if duration is None:
            duration = 1.0
        duration = duration * speed()
        tap(1584, 955)
        if skill_speedup:
            self.SKILL_SPEEDUP()
        time.sleep(duration)

    def CRAFT_SORT(self, duration=None, skill_speedup=False):
        if duration is None:
            duration = 1.0
        duration = duration * speed()
        tap(1688, 192)
        if skill_speedup:
            self.SKILL_SPEEDUP()
        time.sleep(duration)

    def CRAFT_SORT_LEVEL(self, duration=None, skill_speedup=False):
        if duration is None:
            duration = 1.0
        duration = duration * speed()
        tap(481, 350)
        if skill_speedup:
            self.SKILL_SPEEDUP()
        time.sleep(duration)

    def CRAFT_SORT_CONFIRM(self, duration=None, skill_speedup=False):
        if duration is None:
            duration = 1.0
        duration = duration * speed()
        tap(1282, 954)
        if skill_speedup:
            self.SKILL_SPEEDUP()
        time.sleep(duration)

    def CRAFT_SORT_ASCEND_DESCEND(self, duration=None, skill_speedup=False):
        if duration is None:
            duration = 1.0
        duration = duration * speed()
        tap(1870, 194)
        if skill_speedup:
            self.SKILL_SPEEDUP()
        time.sleep(duration)

    def CRAFT_SELECT_CONFIRM(self, duration=None, skill_speedup=False):
        if duration is None:
            duration = 1.0
        duration = duration * speed()
        tap(1731, 1011)
        if skill_speedup:
            self.SKILL_SPEEDUP()
        time.sleep(duration)

    def CRAFT_STRENGTHEN(self, duration=None, skill_speedup=False):
        if duration is None:
            duration = 1.0
        duration = duration * speed()
        tap(1650, 1020)
        if skill_speedup:
            self.SKILL_SPEEDUP()
        time.sleep(duration)

    def INFI_M1(self, duration=None, skill_speedup=False):
        if duration is None:
            duration = 1.0
        duration = duration * speed()
        tap(1120, 210)
        if skill_speedup:
            self.SKILL_SPEEDUP()
        time.sleep(duration)

    def INFI_M2(self, duration=None, skill_speedup=False):
        if duration is None:
            duration = 1.0
        duration = duration * speed()
        tap(1675, 210)
        if skill_speedup:
            self.SKILL_SPEEDUP()
        time.sleep(duration)

    def INFI_BTN(self, duration=None, skill_speedup=False):
        if duration is None:
            duration = 1.0
        duration = duration * speed()
        tap(627, 210)
        if skill_speedup:
            self.SKILL_SPEEDUP()
        time.sleep(duration)

    def CALL_PREVIOUS(self, duration=None, skill_speedup=False):
        if duration is None:
            duration = 1.0
        duration = duration * speed()
        tap(65, 540)
        if skill_speedup:
            self.SKILL_SPEEDUP()
        time.sleep(duration)

    def CALL_NEXT(self, duration=None, skill_speedup=False):
        if duration is None:
            duration = 1.0
        duration = duration * speed()
        tap(1860, 540)
        if skill_speedup:
            self.SKILL_SPEEDUP()
        time.sleep(duration)

    def CALL_x10(self, duration=None, skill_speedup=False):
        if duration is None:
            duration = 1.0
        duration = duration * speed()
        tap(1225, 800)
        if skill_speedup:
            self.SKILL_SPEEDUP()
        time.sleep(duration)

