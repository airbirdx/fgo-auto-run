
from util.default import scenes_path
from util.scene import png_lst
from util.ats import picture_tap
from util.ats import random_tap

def login0():
    lst = png_lst(scenes_path)
    for file in lst:
        if 'fgo_login_pypoint' in file:
            random_tap()
        elif 'fgo_' in file:
            # thd = 0.85
            picture_tap(scenes_path + '/' + file)


