import time
import os
import sys
from util.global0 import *
from func.operation import *
from util.ats import screenshot
from util.initmp import init_env
from util.log import *



def help_info():
    # TODO: if enter NONE or just Enter, then show help info to remind ???
    print('+----------------------------------------------+')
    print('| python main.py <x>')
    s = """\
+----------------------------------------------+
| x                                            |
+----------------------------------------------+
| 0 - AUTO-BATTLE                              |
| 1 - Friendship point                         |
| 2 - Auto CRAFT experience                    |
| 3 - Friendship & CRAFT experience (3 times)  |
| h - help                                     |
| q - quit                                     |
| ? - get current screenshot (for debug)       |
+----------------------------------------------+
"""
    print(s)






def auto_battle():
    while rd_tmp_ini('run', 'flag') == 'True':
        # sys_log('**')
        screenshot()
        # sys_log('@@')
        scene_operation()
        time.sleep(1)  # @TODO:random 0.3-0.5s
        # exit()


from func.case import pypoint
from func.case import craftexp
from func.case import py_craft


def hash_cmd(cmd):

    cmd = str.lower(str(cmd))
    if cmd == '':
        help_info()
    elif cmd == '0':
        os.system('cp ./template.ini ./config.ini')
        auto_battle()
    elif cmd == '1':
        pypoint()
    elif cmd =='2':
        craftexp()
    elif cmd == '3':
        py_craft
    elif cmd =='h':
        help()
    elif cmd =='q':
        exit()
    else:
        screenshot()
        from util.scene import current_scene
        scene = current_scene()
        # print(scene)



def main():
    dbg_shoot = int(bool(len(sys.argv) > 1))

    # script_path = os.path.abspath(sys.argv[0])
    # script_name = os.path.basename(sys.argv[0]).split('.')[0] + '.py'
    # folder_path = script_path.replace(script_name, '')
    # os.chdir(folder_path)

    init_env()

    sys_log('//-------------------------------------------------//')
    sys_log('//------------  S  T  A  R  T  --------------------//')
    sys_log('//-------------------------------------------------//')

    if len(sys.argv) == 1: # for example,  sf b, just backup and quit, don't keep while 1
        os.system('cp ./template.ini ./config.ini')
        auto_battle()

    elif len(sys.argv) == 2: # for example,  sf b, just backup and quit, don't keep while 1
        cmd = sys.argv[1]
        hash_cmd(cmd)
        # hash_cmd('q')

        while 1:
            help_info()
            # print('==================================')
            # print('Please input the function below...')
            print('========================================')
            print('Please input the function below...')
            cmd = str.lower(input('#> '))
            if ',' in cmd:
                for x in cmd.split(','):
                    hash_cmd(x)
                    time.sleep(1)
            hash_cmd(cmd)

    sys_log('//-------------------------------------------------//')
    sys_log('//------------  D  O  N  E     --------------------//')
    sys_log('//-------------------------------------------------//')

    toast('SCRIPT DONE !!!')


if __name__ == '__main__':
    main()












