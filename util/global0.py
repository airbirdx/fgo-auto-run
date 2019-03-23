import platform
from util.default import *
from config import *


def wt_parm_basic():
    wt_global('RUN_FLAG', 'True')  # --> RUN_FLAG

    # --> set and curr run_times parm
    if defined_var('run_times'):
        run_t = run_times
    else:
        run_t = -1

    if defined_var('run_materials'):
        run_m = run_materials
    else:
        run_m = -1

    if defined_var('run_apples'):
        run_a = run_apples
        crun_a = [''] * 2
        crun_a[0] = run_apples[0]
        crun_a[1] = 0
    else:
        run_a = -1
        crun_a = 0

    set_run_parm = [run_t, run_m, run_a]
    curr_run_parm = [0, 0, crun_a]

    wt_global('set_run_parm', set_run_parm)
    wt_global('run_parm', curr_run_parm)


def wt_parm_battle():
    wt_global('round', 0)  # --> round in battle
    wt_global('turn', 0)  # --> turn in battle
    # --> default_color_priority, used in select cards in one turn.
    if defined_var('default_color_priority'):
        wt_global('set_color_priority', default_color_priority)
    else:
        wt_global('set_color_priority', 'RBG')

    # --> apple_priority, set this for run_times and run_materials
    apple_priority = ['Cu', 'Ag', 'Au']
    wt_global('set_apple_priority', apple_priority)

    # --> default_servant_priority, used in select cards in one turn.
    if defined_var('default_servant_priority'):
        set_servant_priority = default_servant_priority
    else:
        set_servant_priority = []

    wt_global('set_servant_priority', set_servant_priority)

    # --> default_chain, used in select cards in one turn.
    if defined_var('default_chain'):
        set_default_chain = default_chain
    else:
        set_default_chain = 0

    wt_global('set_default_chain', set_default_chain)

    # --> default_skill
    if defined_var('default_skill'):
        set_default_skill = default_skill
    else:
        set_default_skill = ''

    wt_global('set_default_skill', set_default_skill)

    # --> default_final
    if defined_var('default_final'):
        set_default_final = default_final
    else:
        set_default_final = ''

    wt_global('set_default_final', set_default_final)

    # --> default_final_unit
    if defined_var('default_final_unit'):
        if default_final_unit == 'round' or default_final_unit == 'turn':
            set_default_final_unit = default_final_unit
        else:
            set_default_final_unit = 'round'
    else:
        set_default_final_unit = 'round'

    wt_global('set_default_final_unit', set_default_final_unit)


def wt_parm_support():
    # --> default_final
    if defined_var('default_support_mode'):
        set_default_support = ['support', 'skill', 'craft']
        set_default_support_mode = default_support_mode
    else:
        set_default_support = ['', '', '']
        set_default_support_mode = 0

    wt_global('set_default_support', set_default_support)
    wt_global('set_default_support_mode', set_default_support_mode)


    # --> default_support_rank
    if defined_var('default_support_rank'):
        set_default_support_rank = str(default_support_rank)
    else:
        set_default_support_rank = ''

    wt_global('set_default_support_rank', set_default_support_rank)


    # --> default_support_rank
    if defined_var('default_support_refresh'):
        set_default_support_refresh = default_support_refresh
    else:
        set_default_support_refresh = 1

    wt_global('set_default_support_refresh', default_support_refresh)


def init_global():
    wt_parm_basic()
    wt_parm_battle()
    wt_parm_support()


def rd_global(parm):
    f = open(tmp_global, 'r')
    lines = f.readlines()
    f.close()
    for line in lines:
        # print('line -->', line)
        string = line
        string = string.replace('\n', '')
        string = string.replace(' ', '')
        idx = string.find('=')
        if idx != -1 and string[:idx] == parm:
            res = string[idx + 1:]
            return res
    return False


def wt_global(parm, value):
    print('--> wt parm @ %-30s, value @ %-30s' % (parm, str(value)))
    if rd_global(parm):
        f = open(tmp_global, 'r')
        lines = f.readlines()
        f.close()
        f = open(tmp_global, 'w')
        for line in lines:
            # print('line,,,', line)
            string = line
            string = string.replace('\n', '')
            string = string.replace(' ', '')
            wts = string
            idx = string.find('=')
            if idx != -1 and string[:idx] == parm:
                wts = string[:idx] + '=' + str(value)
            wts = wts.replace('\n', '')
            f.writelines(wts + '\n')
        f.close()
    else:
        f = open(tmp_global, 'a+')
        wts = parm + '=' + str(value)
        f.writelines(wts + '\n')
        f.close()


def defined_var(var):
    try:
        eval(var)
    except NameError:
        return False
    else:
        return True


def speed():
    if defined_var('speed_ratio'):
        spd = 1 / speed_ratio
    else:
        spd = 1
    # print(spd)
    return spd


def toast(information):
    string = '『 NOTE 』 ' + information
    if platform.system() == 'Windows':
        from win10toast import ToastNotifier
        toaster = ToastNotifier()
        toaster.show_toast('fgo-auto-run', string, duration=10)

    elif platform.system() == 'Darwin':
        from subprocess import call
        cmd = 'display notification \"' + \
              string + '\" with title \"fgo-auto-run\"'
        call(['osascript', '-e', cmd])



# def wt_parm_var(init_var, from_var):
#     if defined_var(from_var):
#         tmp = eval(from_var)
#     else:
#         tmp = 0
#     wt_global(init_var, tmp)
