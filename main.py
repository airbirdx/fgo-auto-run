import time
import os
import sys
from util.global0 import *
from func.operation import scene_operation
from util.ats import screenshot
from util.initmp import init_tmp
from util.log import *


def tst():
    from func.battle import attack
    init_log()
    init_tmp()
    attack()

    # from util.global0 import toast
    # toast('You can see me now.')
    # return True


def main():

    dbg_shoot = int(bool(len(sys.argv) > 1))

    script_path = os.path.abspath(sys.argv[0])
    script_name = os.path.basename(sys.argv[0]).split('.')[0] + '.py'
    folder_path = script_path.replace(script_name, '')
    os.chdir(folder_path)

    init_log()

    sys_log('//-------------------------------------------------//')
    sys_log('//------------  S  T  A  R  T  --------------------//')
    sys_log('//-------------------------------------------------//')

    if dbg_shoot:
        screenshot()
        exit()

    init_tmp()
    while rd_global('RUN_FLAG') == 'True':
        screenshot()
        scene_operation()

    sys_log('//-------------------------------------------------//')
    sys_log('//------------  D  O  N  E     --------------------//')
    sys_log('//-------------------------------------------------//')

    toast('ALL DONE...')

    return True


if __name__ == '__main__':
    main()
    # tst()
