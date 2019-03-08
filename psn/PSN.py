
__metaclass__ = type

import time
from util.ats import tap


class PSN:
    def __init__(self):
        pass

    def A(self, duration=None):
        if duration is None:
            duration = 3.0
        tap(102, 865)
        time.sleep(duration)

    def B(self, duration=None):
        if duration is None:
            duration = 3.0
        tap(245, 865)
        time.sleep(duration)

    def C(self, duration=None):
        if duration is None:
            duration = 3.0
        tap(392, 865)
        time.sleep(duration)

    def I(self, duration=None):
        if duration is None:
            duration = 3.0
        tap(585, 865)
        time.sleep(duration)

    def J(self, duration=None):
        if duration is None:
            duration = 3.0
        tap(725, 865)
        time.sleep(duration)

    def K(self, duration=None):
        if duration is None:
            duration = 3.0
        tap(875, 865)
        time.sleep(duration)

    def O(self, duration=None):
        if duration is None:
            duration = 3.0
        tap(1063, 865)
        time.sleep(duration)

    def P(self, duration=None):
        if duration is None:
            duration = 3.0
        tap(1203, 865)
        time.sleep(duration)

    def Q(self, duration=None):
        if duration is None:
            duration = 3.0
        tap(1347, 865)
        time.sleep(duration)

    def P1(self, duration=None):
        if duration is None:
            duration = 0.5
        tap(200, 800)
        time.sleep(duration)

    def P2(self, duration=None):
        if duration is None:
            duration = 0.5
        tap(580, 800)
        time.sleep(duration)

    def P3(self, duration=None):
        if duration is None:
            duration = 0.5
        tap(960, 800)
        time.sleep(duration)

    def P4(self, duration=None):
        if duration is None:
            duration = 0.5
        tap(1340, 800)
        time.sleep(duration)

    def P5(self, duration=None):
        if duration is None:
            duration = 0.5
        tap(1720, 800)
        time.sleep(duration)

    def EA(self, duration=None):
        if duration is None:
            duration = 1.0
        tap(620, 340)
        time.sleep(duration)

    def EB(self, duration=None):
        if duration is None:
            duration = 1.0
        tap(960, 340)
        time.sleep(duration)

    def EC(self, duration=None):
        if duration is None:
            duration = 1.0
        tap(1300, 340)
        time.sleep(duration)

    def MS(self, duration=None):
        if duration is None:
            duration = 2.0
        tap(1795, 480)
        time.sleep(duration)

    def X(self, duration=None):
        if duration is None:
            duration = 3.0
        tap(1360, 465)
        time.sleep(duration)

    def Y(self, duration=None):
        if duration is None:
            duration = 3.0
        tap(1495, 465)
        time.sleep(duration)

    def Z(self, duration=None):
        if duration is None:
            duration = 3.0
        tap(1630, 465)
        time.sleep(duration)

    def DR1(self, duration=None):
        if duration is None:
            duration = 1.0
        tap(70, 60)
        time.sleep(duration)

    def DR2(self, duration=None):
        if duration is None:
            duration = 1.0
        tap(435, 60)
        time.sleep(duration)

    def DR3(self, duration=None):
        if duration is None:
            duration = 1.0
        tap(800, 60)
        time.sleep(duration)

    def SEL0(self, duration=None):
        if duration is None:
            duration = 1.0
        tap(1649, 225)
        time.sleep(duration)

    def SEL31(self, duration=None):
        if duration is None:
            duration = 5.0
        tap(482, 720)
        time.sleep(duration)

    def SEL32(self, duration=None):
        if duration is None:
            duration = 5.0
        tap(992, 720)
        time.sleep(duration)

    def SEL33(self, duration=None):
        if duration is None:
            duration = 5.0
        tap(1446, 720)
        time.sleep(duration)

    def SEL21(self, duration=None):
        if duration is None:
            duration = 5.0
        tap(0, 0)
        time.sleep(duration)

    def SEL22(self, duration=None):
        if duration is None:
            duration = 5.0
        tap(0, 0)
        time.sleep(duration)

    def SEL11(self, duration=None):
        if duration is None:
            duration = 5.0
        tap(0, 0)
        time.sleep(duration)

    def S0(self, duration=None):
        if duration is None:
            duration = 1.0
        tap(963, 936)
        time.sleep(duration)

    def S1(self, duration=None):
        if duration is None:
            duration = 1.0
        tap(220, 520)
        time.sleep(duration)

    def S2(self, duration=None):
        if duration is None:
            duration = 1.0
        tap(520, 520)
        time.sleep(duration)

    def S3(self, duration=None):
        if duration is None:
            duration = 1.0
        tap(820, 520)
        time.sleep(duration)

    def S4(self, duration=None):
        if duration is None:
            duration = 1.0
        tap(1120, 520)
        time.sleep(duration)

    def S5(self, duration=None):
        if duration is None:
            duration = 1.0
        tap(1420, 520)
        time.sleep(duration)

    def S6(self, duration=None):
        if duration is None:
            duration = 1.0
        tap(1720, 520)
        time.sleep(duration)

    def ATK(self, duration=None):
        if duration is None:
            duration = 2.0
        tap(1700, 900)
        time.sleep(duration)

    def START(self, duration=None):
        if duration is None:
            duration = 30.0
        tap(1780, 1010)
        time.sleep(duration)

    def NEXT(self, duration=None):
        if duration is None:
            duration = 1.0
        tap(1660, 1010)
        time.sleep(duration)

    def INFI0(self, duration=None):
        if duration is None:
            duration = 0.2
        tap(584, 647)
        time.sleep(duration)

    def INFI1(self, duration=None):
        if duration is None:
            duration = 2.0
        tap(1710, 365)
        time.sleep(duration)

    def INFI2(self, duration=None):
        if duration is None:
            duration = 3.0
        tap(1255, 840)
        time.sleep(duration)

    def INFI3(self, duration=None):
        if duration is None:
            duration = 2.0
        tap(960, 840)
        time.sleep(duration)

    def DTASK(self, duration=None):
        if duration is None:
            duration = 3.0
        tap(1050, 345)
        time.sleep(duration)

    def DZHUZHAN(self, duration=None):
        if duration is None:
            duration = 3.0
        tap(240, 465)
        time.sleep(duration)

    def P_AP50(self, duration=None):
        if duration is None:
            duration = 1.0
        tap(335, 1040)
        time.sleep(duration)

    def SUPPREF(self, duration=None):
        if duration is None:
            duration = 1.0
        tap(1255, 193)
        time.sleep(duration)

    def ZHIJIE0(self, duration=None):
        if duration is None:
            duration = 1.0
        tap(150, 193)
        time.sleep(duration)

    def ZHIJIE1(self, duration=None):
        if duration is None:
            duration = 1.0
        tap(250, 193)
        time.sleep(duration)

    def ZHIJIE2(self, duration=None):
        if duration is None:
            duration = 1.0
        tap(350, 193)
        time.sleep(duration)

    def ZHIJIE3(self, duration=None):
        if duration is None:
            duration = 1.0
        tap(450, 193)
        time.sleep(duration)

    def ZHIJIE4(self, duration=None):
        if duration is None:
            duration = 1.0
        tap(550, 193)
        time.sleep(duration)

    def ZHIJIE5(self, duration=None):
        if duration is None:
            duration = 1.0
        tap(650, 193)
        time.sleep(duration)

    def ZHIJIE6(self, duration=None):
        if duration is None:
            duration = 1.0
        tap(750, 193)
        time.sleep(duration)

    def ZHIJIE7(self, duration=None):
        if duration is None:
            duration = 1.0
        tap(850, 193)
        time.sleep(duration)

    def ZHIJIE8(self, duration=None):
        if duration is None:
            duration = 1.0
        tap(950, 193)
        time.sleep(duration)

    def SKIPS(self, duration=None):
        if duration is None:
            duration = 2.0
        tap(1770, 60)
        time.sleep(duration)

    def SKIPN(self, duration=None):
        if duration is None:
            duration = 2.0
        tap(680, 840)
        time.sleep(duration)

    def SKIPY(self, duration=None):
        if duration is None:
            duration = 2.0
        tap(1240, 840)
        time.sleep(duration)

    def ADDAP(self, duration=None):
        if duration is None:
            duration = 2.0
        tap(250, 1040)
        time.sleep(duration)

    def AuAPPLE(self, duration=None):
        if duration is None:
            duration = 2.0
        tap(670, 475)
        time.sleep(duration)

    def CONFIRM(self, duration=None):
        if duration is None:
            duration = 2.0
        tap(1260, 840)
        time.sleep(duration)

    def CANCLE(self, duration=None):
        if duration is None:
            duration = 2.0
        tap(660, 840)
        time.sleep(duration)

