import traceback
import os
import sys
import datetime
# from util.global0 import *
from util.default import *

# datetime.datetime.now().strftime('%y%m%d_%H%M%S%p')

global init_time
try:
    init_time
    print('exist,,,,', init_time)
except NameError:
    init_time = datetime.datetime.now().strftime('%y%m%d_%H%M%S%p')
    # print('<><><><><><>...', init_time)
else:
    pass



def init_log():
    '''
    清空并初始化 log 文件
    :return:
    '''
    # if not os.path.exists(f'{tmp_path}/log.log'):
    logfn     = f'{log_path}/log_{init_time}.log'

    if not os.path.exists(log_path):
        os.mkdir(log_path)

    if not os.path.exists(logfn):
        f = open(logfn, 'w')
        f.close()





def sys_log(*objects, sep=' ', end='\n', file=sys.stdout, flush=False, debug=True):
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

    logfn     = f'{log_path}/log_{init_time}.log'

    logf = open(logfn, 'a+')
    # ts_func = '[TIME] %s , [FUNC] %-20s , [INFO]' % (curr_t, func_n)
    ts_func = '%s , %-20s , ' % (curr_t, func_n)
    if debug:
        # print('[TIME] %s , [FUNC] %-20s , [INFO]' % (curr_t, func_n), *objects, sep=sep, end=end, file=file, flush=flush)
        print('%s'  % ts_func, *objects, sep=sep, end=end, file=file, flush=flush)
    # print('[TIME] %s , [FUNC] %-20s , [INFO]' % (curr_t, func_n), *objects, sep=sep, end=end, file=logf, flush=flush)
    print('%s'  % ts_func, *objects, sep=sep, end=end, file=logf, flush=flush)
    logf.close()



def dbg_log(*objects, sep=' ', end='\n', file=sys.stdout, flush=False, debug=True):
    sys_log(*objects, sep=' ', end='\n', file=sys.stdout, flush=False, debug=debug)
    '''
    将 debug 信息导入 log 文件中, 并 show 出来
    :param objects:
    :param sep:
    :param end:
    :param file:
    :param flush:
    :return:
    '''
    pass


# MUST keep below item, do not remove
init_log()




