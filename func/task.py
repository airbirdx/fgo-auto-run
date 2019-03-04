
from util.default import task_path
from util.ats import picture_tap
from util.initmp import init_tmp

def task_select():
    # thd = 0.85
    picture_tap(task_path + '/task.png')
    init_tmp()



