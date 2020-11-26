import traceback
import os
import sys
import datetime
from util.default import *


def init_log():
    '''
    清空并初始化 log 文件
    :return:
    '''
    # if not os.path.exists(f'{tmp_path}/log.log'):
    f = open(f'{tmp_path}/log.log', 'w')
    f.close()


def sys_log(*objects, sep=' ', end='\n', file=sys.stdout, flush=False):
    '''
    将信息导入 log 文件中
    :param objects:
    :param sep:
    :param end:
    :param file:
    :param flush:
    :return:
    '''
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



def dbg_log(*objects, sep=' ', end='\n', file=sys.stdout, flush=False):
    '''
    显示 dbg info
    :param objects:
    :param sep:
    :param end:
    :param file:
    :param flush:
    :return:
    '''
    debug = 0
    tmp = traceback.extract_stack()
    func_n = tmp[-2][2]
    curr_t = datetime.datetime.now().strftime('%m/%d %H:%M:%S %p')
    if debug:
        print('[TIME] %s , [FUNC] %-15s , [DBG>]' % (curr_t, func_n), *objects, sep=sep, end=end, file=file, flush=flush)


