import os
import time
from psn.PSN import *
from util.global0 import defined_var

# convert the config skill string to list
# in  : string : (1)abc(2)opq31(4)ijk
# out : list   : ['abc', 'opq31', '', 'ijk']
def cfgstr2lst(string):

    string = string.replace(' ', '')

    if string == '':
        seq = ['']
        return seq

    tmp_str = string.split('(')
    tmp_str.remove('')
    
    max_idx = 0
    for skill in tmp_str:
        tmp_idx = int(skill[:skill.find(')')])
        if tmp_idx > max_idx:
            max_idx = tmp_idx

    seq = [''] * max_idx

    for skill in tmp_str:
        tmp_idx = int(skill[:skill.find(')')])
        # print(tmp_idx)
        seq[tmp_idx - 1] = skill[skill.find(')') + 1:]

    return seq


# convert the skill string to skill param
# in  : string : 'abc31'
# out : list   : ['a', 'b', 'c31']
def split_turn_seq(string=None):
    lst = []
    tmp = ''
    for char in string.upper():
        # if char >= 'A' and char <= 'Z':
        if char.isalpha():
            if tmp != '':
                lst.append(tmp)
                tmp = ''
            tmp += char
        else:
            tmp += char
    lst.append(tmp)
    return lst


# s for switch servant
# abc, ijk, opq, xyz, s
# psn means position
# skill('a') -> psn.A()
def skill(parm, duration=None):
    psn = PSN()
    lst = list(parm.upper())

    nlst = []      # 去除非技能参数，增加鲁棒性
    for char in lst:
        if char in 'ABCIJKOPQXYZS0123456':
            nlst.append(char)
    lst = nlst

    if lst == []:
        # print('No skill in this turn...')
        return False

    # switch servant
    if lst[0] == 'S':
        if len(lst) == 3:
            psn.MS()
            psn.Z()
            eval('psn.S%s()' % lst[1])
            eval('psn.S%s()' % lst[2])
            psn.S0()
            time.sleep(10)
        else:
            print('error-----')
        return True

    if '0' in lst:      # 对敌人释放技能
        lst.remove('0')
        eval('psn.DR%s()' % lst[1])
        lst.pop(1)   # 只保留一个技能字母

    # if lst[0] == 'X' or lst[0] == 'Y' or lst[0] == 'Z':
    if lst[0] in 'XYZ':
        psn.MS()

    if len(lst) == 3:
        eval('psn.%s()' % lst[0])
        eval('psn.SEL%s%s()' % (lst[1], lst[2]))
    elif len(lst) == 1:
        eval('psn.%s()' % lst[0])
    else:
        print('skill input format error')
        pass


def turn_skill(string=None):
    lst = split_turn_seq(string)
    for skl in lst:
        skill(skl)


