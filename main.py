from util.ats import screenshot
from util.initmp import init_tmp
from util.global0 import *
from func.operation import *
from func.battle import *
from config import *

if dbg_shoot:
    screenshot()
    exit()

if dbg_train:
    training()
    exit()

init_tmp()
while rd_global('RUN_FLAG') == 'True':
    screenshot()
    scene_operation()
    time.sleep(1)


print('//-------------------------------------------------//')
print('//------------   D  O  N  E    --------------------//')
print('//-------------------------------------------------//')

