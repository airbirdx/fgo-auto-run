import re
import os


# s for switch servant
# abc, ijk, opq, xyz, s
# psn <-> position
def skill(parm, duration=None):
    # psn = PSN()
    lst = list(parm.upper())

    if lst == []:
        print('No skill in this turn...')
        return False

    # switch servant
    if lst[0] == 'S':
        if len(lst) == 3:
            pass
            # psn.MS()
            # psn.Z()
            # eval('psn.S%s(duration)' % lst[1])
            # eval('psn.S%s(duration)' % lst[2])
            # psn.S0()
            # time.sleep(10)
        else:
            print('error-----')

    if lst[0] == 'X' or lst[0] == 'Y' or lst[0] == 'Z':
        pass
        # psn.MS()

    if len(lst) == 3:
        pass
        # eval('psn.%s(duration)' % lst[0])
        # eval('psn.SEL%s%s(duration)' % (lst[1], lst[2]))
    elif len(lst) == 1:
        pass
        # eval('psn.%s(duration)' % lst[0])
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


def str2seq(string):
    # string = '(1)abc(2)opq31(3)ijk'
    # string = '(3)ijk(11)opq(9)abc'
    # string = ''

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
        print(tmp_idx)
        seq[tmp_idx - 1] = skill[skill.find(')') + 1:]

    return seq


aa = str2seq('(1)abc(2)opq31(4)ijk')
print(aa)

# split_seq(aa[0])
