import time
import os
import sys
from util.global0 import *
from func.operation import scene_operation
from util.ats import screenshot
from util.initmp import init_tmp





# from func.battle import tst_class_Card
# from psn.psfunc import cfgstr2lst
# tst_class_Card()








dbg_shoot = int(bool(len(sys.argv) > 1))

script_path = os.path.abspath(sys.argv[0])
script_name = os.path.basename(sys.argv[0]).split('.')[0] + '.py'
folder_path = script_path.replace(script_name, '')
os.chdir(folder_path)

if dbg_shoot:
    screenshot()
    exit()

# if dbg_train:
#     training()
#     exit()

init_tmp()
while rd_global('RUN_FLAG') == 'True':
    screenshot()
    scene_operation()
    time.sleep(1)

print('//-------------------------------------------------//')
print('//------------   D  O  N  E    --------------------//')
print('//-------------------------------------------------//')

