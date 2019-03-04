
from util.default import win_path
from util.ats import random_tap
from util.ats import picture_tap

def win_and_next():
    # thd = 0.85
    if picture_tap(win_path + '/next.png'):
        pass
    else:
        # win0, win1, win2
        random_tap()
