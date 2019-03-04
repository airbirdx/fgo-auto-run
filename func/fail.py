
from util.default import fail_path
from util.scene import curr_png_lst
from util.ats import picture_tap

def withdrawn():
    lst = curr_png_lst(fail_path)
    for file in lst:
        # thd = 0.85
        picture_tap(file)


