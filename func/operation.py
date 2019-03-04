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

def scene_operation():
    # config = load_config()
    print(scene)
    if 'addap' in scene:
        pass
    elif 'task' in scene:
        task_select()
    elif 'support' in scene:
        # select_support()
        select_support(servant='meilin', skill='310')
    elif 'team' in scene:
        team_confirm()
    elif 'loading' in scene:
        random_tap()
    elif 'attack' in scene:
        pass
    elif 'win' in scene:
        win_and_next()
    elif 'fail' in scene:
        withdrawn()
    elif 'friend' in scene:
        make_friend()
    else:
        print('「 ONLY GET SCREENSHOT 」')
        pass
