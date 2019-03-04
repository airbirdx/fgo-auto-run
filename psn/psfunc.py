import os
import time
from psn.PSN import *


# s for switch servant
# abc, ijk, opq, xyz, s
# psn <-> position
def skill(parm, duration=None):
    psn = PSN()
    lst = list(parm.upper())

    if lst == []:
        print('No skill in this turn...')
        return False

    # switch servant
    if lst[0] == 'S':
        if len(lst) == 3:
            psn.MS()
            psn.Z()
            eval('psn.S%s(duration)' % lst[1])
            eval('psn.S%s(duration)' % lst[2])
            psn.S0()
            time.sleep(10)
        else:
            print('error-----')

    if lst[0] == 'X' or lst[0] == 'Y' or lst[0] == 'Z':
        psn.MS()

    if len(lst) == 3:
        eval('psn.%s(duration)' % lst[0])
        eval('psn.SEL%s%s(duration)' % (lst[1], lst[2]))
    elif len(lst) == 1:
        eval('psn.%s(duration)' % lst[0])
    else:
        print('skill input format error')
        pass


def skill_seq(parm=None):
    seq = split_seq(parm)
    for tmp in seq:
        skill(tmp)


def split_seq(parm=None):
    parm_seq = []
    parm_tmp = ''
    for char in parm.upper():
        # if char >= 'A' and char <= 'Z':
        if char.isalpha():
            if parm_tmp != '':
                parm_seq.append(parm_tmp)
                parm_tmp = ''
            parm_tmp += char
        else:
            parm_tmp += char
    parm_seq.append(parm_tmp)
    return parm_seq

