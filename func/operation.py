import os
# import operator
# from util.default import support_path
# from util.default import screenshot_path
# from util.scene import curr_png_lst
# from util.default import tmp_support
# from util.ats import tap
# from util.ats import swipe
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

def scene_operation():
    scene = current_scene()

    print('「 CURRENT SCENE 」', scene)

    if 'addap' in scene:
        addap0()
    elif 'task' in scene:
        task_select()
    elif 'support' in scene:
        select_support()
    elif 'team' in scene:
        team_confirm()
    elif 'loading' in scene:
        random_tap()
    elif 'attack' in scene:
        attack()
    elif 'win' in scene:
        win_and_next(scene)
    elif 'fail' in scene:
        withdrawn()
    elif 'friend' in scene:
        make_friend()
    else:
        print('「 ONLY GET SCREEN SHOT 」')
        pass
