import time
import os
import sys
from util.global0 import *
from func.operation import scene_operation
from util.ats import screenshot
from util.initmp import init_env
from util.log import *

from func.battle import split_in_battle

def tst():
    from func.case import pypoint
    from func.case import infinity_pool
    # pypoint()
    infinity_pool()


def main():
    dbg_shoot = int(bool(len(sys.argv) > 1))

    script_path = os.path.abspath(sys.argv[0])
    script_name = os.path.basename(sys.argv[0]).split('.')[0] + '.py'
    folder_path = script_path.replace(script_name, '')
    os.chdir(folder_path)

    init_env()

    sys_log('//-------------------------------------------------//')
    sys_log('//------------  S  T  A  R  T  --------------------//')
    sys_log('//-------------------------------------------------//')

    if dbg_shoot:
        screenshot()
        exit()

    while rd_tmp_ini('run', 'flag') == 'True':
        screenshot()
        scene_operation()
        time.sleep(0.5)  # @TODO:random 0.3-0.5s
        # exit()

    sys_log('//-------------------------------------------------//')
    sys_log('//------------  D  O  N  E     --------------------//')
    sys_log('//-------------------------------------------------//')

    toast('SCRIPT DONE !!!')


if __name__ == '__main__':
    main()
    # tst()