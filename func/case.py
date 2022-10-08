from enum import Flag
import re
import cv2
from util.default import *
from util.ats import random_tap
from util.ats import picture_tap
from util.cvs import *
from util.global0 import *
from util.log import *
from util.scene import current_scene
from psn.PSN import *
from util.ats import screenshot
from util.scene import png_lst
from func.operation import *




def py_craft(loop=3):
    for _ in range(loop):
        pypoint()
        craftexp()




def pypoint():

    psn = PSN()
    
    path = './lib/menu'
    menu_open  = f'{path}/open.png'                    # 菜单按钮
    menu_close = f'{path}/close.png'                   # 菜单按钮
    menu_call  = f'{path}/call.png'                   # 菜单按钮

    call_scene  = f'{path}/scene/x_call.png'        # 召唤场景
    call_scene0 = f'{path}/call/x_stone.png'         # 补充-召唤场景
    call_scene1 = f'{path}/call/x_point.png'         # 补充-召唤场景
    call_scene2 = f'{path}/call/x_detail.png'        # 补充-召唤场景

    pyp          = f'{path}/call/pypoint0.png'        # 友情点界面
    pyp1         = f'{path}/call/pypoint1.png'        # 友情点界面
    callx10      = f'{path}/call/callx10.png'         # 召唤 x10 按钮
    callx10_0    = f'{path}/call/callx10_0.png'         # 免费召唤 x10 按钮
    call_notice  = f'{path}/call/call_notice.png'     # 召唤提示
    call_confirm = f'{path}/call/call_confirm.png'    # 召唤确认
    call_next    = f'{path}/call/call_next.png'       # 继续十连召唤
    full0        = f'{path}/call/full0.png'            # 召唤已经满了
    full1        = f'{path}/call/full1.png'            # 召唤已经满了
    close0       = f'{path}/call/close0.png'            # 召唤已经满了，点击关闭
    close1       = f'{path}/call/close1.png'            # 召唤已经满了，点击关闭


    def is_call_scene():
        if pic_in_sh(call_scene):
            return True
        if pic_in_sh(call_scene0) and pic_in_sh(call_scene1) and pic_in_sh(call_scene2):
            return True
        else:
            return False

    def is_pypoint_scenc():
        if pic_in_sh(pyp) or pic_in_sh(pyp1):
            return True
        else:
            return False


    sys_log('start pypoint...')

    if not is_call_scene():
        return_home_page()

    # 进入召唤界面
    while 1:
        screenshot()
        if is_call_scene():
            sys_log('Current scene -> CALL')
            picture_tap(call_scene)
            picture_tap(call_scene)
            picture_tap(call_scene)
            break

        if pic_in_sh(menu_open):
            picture_tap(menu_open)
            sys_log('Open menu')
        
        if pic_in_sh(menu_close):
            picture_tap(menu_call)
            sys_log('click call in menu')


    

    # 进入友情池界面
    while 1:
        screenshot()
        if is_pypoint_scenc():
            sys_log('Now under pypoint poll successfully')
            break
        else:
            sys_log('not pypoint poll')
            psn.CALL_PREVIOUS()
            sys_log('check previous poll next')

    # 开抽
    num = 0
    flag = 0
    while 1:
        screenshot()

        if flag == 0 and (pic_in_sh(full0) or pic_in_sh(full1)):
            sys_log('PY POINT MUSTER FULL !')
            flag = 1
        elif pic_in_sh(call_confirm):
            num += 1
            sys_log('PY POINT MUSTER CONFIRM @ %s' % num)
            sys_log('USED PY POINT: %s' % format(num*2000,',') )
            picture_tap(call_confirm)
        elif pic_in_sh(call_next):
            sys_log('PY POINT MASTER CONTINUE')
            picture_tap(call_next)
        # elif pic_in_sh(pyp) or pic_in_sh(pyp1):
        elif is_pypoint_scenc():
            sys_log('Current scene -> PY POINT')
            if pic_in_sh(callx10):
                picture_tap(callx10)
            elif pic_in_sh(callx10_0):
                picture_tap(callx10_0)
            # psn.CALL_x10()
        elif pic_in_sh(close0):
            sys_log('stop pypoint, set flag')
            picture_tap(close0)
            if flag:
                toast('PY POINT MUSTER FULL !')
                break
        # elif flag and pic_in_sh(close1):
        #     picture_tap(close1)
        #     sys_log('stop pypoint')

        else:
            dbg_log('tap screen to speed up')
            psn.PYPONT()
            psn.PYPONT()
            psn.PYPONT()
            # time.sleep(0.2)
    
    # return_home_page()
    pass


def infinity_pool():
    
    psn = PSN()
    path = './lib/func/infinity_pool'
    
    psn.INFI_M1()
    time.sleep(1)
    lst = png_lst(path)
    
    while 1:
        screenshot()
        for file in lst:
            # thd = 0.85
            flg = picture_tap(path + '/' + file)
            if flg == 1:
                print(file)
                break

def zoom_to_4x4():
    path = './lib/menu/craftexp'
    zoom2x2      = f'{path}/zoom2x2.png'
    zoom3x3      = f'{path}/zoom3x3.png'
    zoom4x4      = f'{path}/zoom4x4.png'
    while 1:
        screenshot()
        if pic_in_sh(zoom4x4):
            pass
            break
        elif pic_in_sh(zoom2x2):
            picture_tap(zoom2x2)
        elif pic_in_sh(zoom3x3):
            picture_tap(zoom3x3)
        time.sleep(0.3)

def craftexp():
    # 搓丸子
    psn = PSN()

    path = './lib/menu/craftexp'

    strscene     = f'{path}/strscene.png'
    
    decide       = f'{path}/decide.png'
    confirm      = f'{path}/confirm.png'
    strengthen   = f'{path}/strengthen.png'
    select_scene = f'{path}/select_scene.png'
    select_base  = f'{path}/select_base.png'
    select_board = f'{path}/select_board.png'
    sort_ascend  = f'{path}/sort_ascend.png'
    sort_descend = f'{path}/sort_descend.png'
    sub_menu     = f'{path}/sub_menu_craft.png'

    flg_screen_base = 0
    flg_screen_food = 0
    flg_no_available_craft = 0

    cx, cy = [210, 380]  # craft one under zoom 4x4
    all_pos = []
    for row in range(4):
        for col in range(7):
            px = cx + col * 200
            py = cy + row * 214
            all_pos.append([px, py])

    def get_default_screen_sort():
        psn.CRAFT_SCREEN()
        psn.CRAFT_SCREEN_DEFAULT()
        psn.CRAFT_SCREEN_x2()
        psn.CRAFT_SCREEN_x1()
        psn.CRAFT_SCREEN_CONFIRM()

        psn.CRAFT_SORT()
        psn.CRAFT_SORT_LEVEL()
        psn.CRAFT_SORT_CONFIRM()

        screenshot()
        if pic_in_sh(sort_ascend):
            # picture_tap(sort_ascend)
            psn.CRAFT_SORT_ASCEND_DESCEND()


    def select_craft(type=None):
        time.sleep(1)
        # type = base, 被强化的礼装
        # type = None or 'food', 狗粮
        for tmp_pos in all_pos[:24]:
            px, py = tmp_pos
            tap(px, py, 20)
            # time.sleep(0.1)
            if type == 'base':
                time.sleep(1)
                screenshot()
                time.sleep(1)
                if pic_in_sh(strscene):
                    sys_log('Select CRAFT BASE done...')
                    break
    

    def enter_sub_menu():
        # 进入召唤界面
        path = './lib/menu'
        menu_open  = f'{path}/open.png'                    # 菜单按钮
        menu_close = f'{path}/close.png'                   # 菜单按钮
        menu_stren = f'{path}/strengthen.png'                   # 按钮

        strengthen_scene = f'{path}/scene/x_strengthen.png'
        while 1:
            screenshot()
            time.sleep(0.3)
            if pic_in_sh(strengthen_scene):
                sys_log('Current scene -> strengthen')
                picture_tap(strengthen_scene)
                picture_tap(strengthen_scene)
                if pic_in_sh(sub_menu):
                    picture_tap(sub_menu)
                break

            if pic_in_sh(menu_open):
                picture_tap(menu_open)
                sys_log('Open menu')
            
            if pic_in_sh(menu_close):
                picture_tap(menu_stren)
                sys_log('click stren in menu')

    sys_log('start craft exp auto-eat.')

    return_home_page()
    enter_sub_menu()
    time.sleep(1)

    while 1:
        # select base craft
        screenshot()
        if pic_in_sh(select_base) and pic_in_sh(strscene):
            picture_tap(select_base)

            if not flg_screen_base:
                zoom_to_4x4()
                get_default_screen_sort()
                flg_screen_base = 1

            select_craft(type='base')
            flg_no_available_craft = 0

        elif pic_in_sh(select_board) and pic_in_sh(strscene):
            picture_tap(select_board)
        
            if not flg_screen_food:
                zoom_to_4x4()
                get_default_screen_sort()
                flg_screen_food = 1

            select_craft()
            psn.CRAFT_SELECT_CONFIRM()

        screenshot()
        if pic_in_sh(select_scene):
            sys_log('No available selection craft for food...')
            flg_no_available_craft += 1
            if flg_no_available_craft == 2: # suppose no any craft food.
                sys_log('Out of craft food...')
                break
            else:
                continue

        if pic_in_sh(strscene):
            psn.CRAFT_STRENGTHEN()
            screenshot()
            if pic_in_sh(confirm):
                picture_tap(confirm)

        sys_log('Running craft strengthen...')
        for _ in range(100):
            for xxx in range(3):
                psn.PYPONT()
                time.sleep(0.3)
            screenshot()
            if pic_in_sh(strscene):
                break

        # if flg_no_available_craft == 2: # suppose no any craft food.
        #     sys_log('Out of craft food...2')
        #     break

    #return_home_page()
    pass
    

def sell_servant(type='craft'):
    # 卖 1*, 2* 从者

    def enter_sub_menu():
        # 进入召唤界面
        path = './lib/menu'
        menu_open  = f'{path}/open.png'                    # 菜单按钮
        menu_close = f'{path}/close.png'                   # 菜单按钮
        menu_stren = f'{path}/store.png'                   # 按钮

        menu_scene = f'{path}/scene/x_store.png'
        btn_sub_menu = f'{path}/sell_servant/sub_menu_cell.png'
        while 1:
            screenshot()
            if pic_in_sh(menu_scene):
                sys_log('Current scene -> strengthen')
                picture_tap(menu_scene)
                picture_tap(menu_scene)
                if pic_in_sh(btn_sub_menu):
                    picture_tap(btn_sub_menu)
                break

            if pic_in_sh(menu_open):
                picture_tap(menu_open)
                sys_log('Open menu')
            
            if pic_in_sh(menu_close):
                picture_tap(menu_stren)
                sys_log('click call in menu')

    return_home_page()
    enter_sub_menu()
    time.sleep(1)
