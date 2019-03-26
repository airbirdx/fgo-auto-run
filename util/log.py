import traceback
import os
import sys
import datetime
from util.default import *


def init_log():
    # if not os.path.exists(f'{tmp_path}/log.log'):
    f = open(f'{tmp_path}/log.log', 'w')
    f.close()


def sys_log(*objects, sep=' ', end='\n', file=sys.stdout, flush=False):

    tmp = traceback.extract_stack()
    func_n = tmp[-2][2]
    curr_t = datetime.datetime.now().strftime('%m/%d %H:%M:%S %p')

    if not os.path.exists(f'{tmp_path}/log.log'):
        f = open(f'{tmp_path}/log.log', 'w')
        f.close()

    logf = open(f'{tmp_path}/log.log', 'a+')
    print('[TIME] %s , [FUNC] %-15s , [INFO]' % (curr_t, func_n), *objects, sep=sep, end=end, file=file, flush=flush)
    print('[TIME] %s , [FUNC] %-15s , [INFO]' % (curr_t, func_n), *objects, sep=sep, end=end, file=logf, flush=flush)
    logf.close()

# def tet_func_name():
#     sys_log('Hello %s' % 'World', '123')
#
# def tet_func_name0():
#     tet_func_name()
#
# tet_func_name()
