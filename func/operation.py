import time
import random
from func.support import select_support
from func.team import team_confirm
from util.scene import current_scene
from func.win import win_and_next
from util.ats import random_tap
from func.friend import make_friend
from func.fail import withdrawn
from func.task import task_select
from func.battle import attack
from func.addap import addap0
from func.disconnect import retry_connection
from func.continuebat import close_continue

def scene_operation():
    '''
    判断当前场景，根据场景进行下一步操作
    :return:
    '''
    scene = current_scene()
    # print(scene)
    # exit()
    
    if 'addap' in scene:
        addap0()
    elif 'task' in scene:        ######
        task_select()
    elif 'support' in scene:     ######
        select_support()
    elif 'team' in scene:        #####
        team_confirm()
    elif 'loading' in scene:     #####
        random_tap()
    elif 'attack' in scene:
        attack()
    elif 'win' in scene:         #####
        win_and_next(scene)
    elif 'fail' in scene:        #####
        withdrawn()
    elif 'friend' in scene:      #####qqq
        make_friend()
    elif 'disconnect' in scene:
        retry_connection()
    elif 'continue' in scene:   #####
        close_continue()
    else:
        pass
    
    # time.sleep(random.random())   # [0,1)
