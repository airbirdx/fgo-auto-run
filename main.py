import time
import os
import sys
from util.global0 import *
from func.operation import scene_operation
from util.ats import screenshot
from util.initmp import init_tmp


def tst():
    from util.global0 import toast
    toast('You can see me now.')
    return True


def main():

    dbg_shoot = int(bool(len(sys.argv) > 1))

    script_path = os.path.abspath(sys.argv[0])
    script_name = os.path.basename(sys.argv[0]).split('.')[0] + '.py'
    folder_path = script_path.replace(script_name, '')
    os.chdir(folder_path)

    if dbg_shoot:
        screenshot()
        exit()

    init_tmp()
    while rd_global('RUN_FLAG') == 'True':
        screenshot()
        scene_operation()

    print('//-------------------------------------------------//')
    print('//------------   D  O  N  E    --------------------//')
    print('//-------------------------------------------------//')

    toast('All scripts done!')

    return True


if __name__ == '__main__':
    main()
    # tst()
