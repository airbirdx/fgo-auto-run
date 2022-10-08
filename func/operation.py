import time
import random
from func.support import select_support
from func.team import team_confirm
from util.log import sys_log
from util.cvs import pic_in_sh
from util.scene import current_scene
from func.win import win_and_next
from util.ats import picture_tap, random_tap, screenshot
from func.friend import make_friend
from func.fail import withdrawn
from func.task import task_select
from func.battle import attack
from func.addap import addap0
from func.login import login0

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
    if 'fgo' in scene:
        login0()
    if 'addap' in scene:
        addap0()
    elif 'task' in scene:        ######
        task_select()
    elif 'support' in scene:     ######
        select_support()
    elif 'team' in scene:        #####
        # exit()
        team_confirm()
    elif 'loading' in scene:     #####
        pass
        # random_tap()
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


def return_home_page():
    path = './lib/menu'
    btn_open  = f'{path}/open.png'                    # 菜单按钮
    btn_close = f'{path}/close.png'                   # 菜单按钮
    btn_back  = f'{path}/back.png'                   # 菜单按钮
    btn_back2 = f'{path}/back2.png'                   # 菜单按钮

    btn_team       = f'{path}/team.png'
    btn_strengthen = f'{path}/strengthen.png'
    btn_call       = f'{path}/call.png'
    btn_store      = f'{path}/store.png'
    btn_friend     = f'{path}/friend.png'
    btn_space      = f'{path}/space.png'
    btn_home       = f'{path}/home.png'

    # sce_team       = f'{path}/x_team.png'
    # sce_strengthen = f'{path}/x_strengthen.png'
    # sce_call       = f'{path}/x_call.png'
    # sce_store      = f'{path}/x_store.png'
    # sce_friend     = f'{path}/x_friend.png'
    # sce_space      = f'{path}/x_space.png'
    
    # sces = [sce_team, sce_strengthen, sce_call, sce_store, sce_friend, sce_space]
    while 1:
        screenshot()
        scene = current_scene(path=f'{path}/scene')
        # if scene != 'none' and (pic_in_sh(btn_open) or pic_in_sh(btn_close)):
        if (pic_in_sh(btn_open) or pic_in_sh(btn_close)):
            break
        else:
            if pic_in_sh(btn_back):
                picture_tap(btn_back)
            elif pic_in_sh(btn_back2):
                picture_tap(btn_back2)
            else:
                sys_log('NOT found BACK Button...')
                
    
    while 1:
        screenshot()
        scene = current_scene()

        if 'home' in scene:
            sys_log('Already under HOME page...')
            break

        elif pic_in_sh(btn_open):
            picture_tap(btn_open)
        
        elif pic_in_sh(btn_home):
            picture_tap(btn_home)
