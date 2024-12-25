import os
import shutil
import datetime
from util.scene import png_lst
from util.global0 import *
from util.log import *


def clean_path(path):
    """
    循环迭代删除路径文件夹下的所有文件
    :param path:
    :return:
    """
    ls = os.listdir(path)
    for i in ls:
        c_path = os.path.join(path, i)
        # print(c_path)
        if os.path.isdir(c_path):
            clean_path(c_path)
        else:
            os.remove(c_path)


def rm_file_in_path(path, string):
    """
    循环迭代删除路径文件夹下的所有含有目标字符串的文件
    :param path:
    :param string:
    :return:
    """
    if os.path.exists(path):
        ls = os.listdir(path)
        for i in ls:
            c_path = os.path.join(path, i)
            # print(c_path)
            if os.path.isdir(c_path):
                rm_file_in_path(c_path, string)
            elif string in c_path:
                # print('remove', c_path)
                if string in os.path.basename(c_path):
                    # print('remove', c_path)
                    os.remove(c_path)
    else:
        os.mkdir(path)


def cp_cfg_2_lib():
    """
    将 cfg 中 task/material/support/craft/skill 等需要拷贝的文件，拷贝到对应的路径
    :return:
    """
    # TODO:add servant,craft,skill to lib
    # supportx.png/craftx.png -> support_path
    lst = png_lst(cfg_path)
    for file in lst:
        name, ext = os.path.splitext(file)
        if 'task' in name:
            shutil.copyfile(cfg_path + f'/{file}', task_path + f'/{file}')
            shutil.copyfile(cfg_path + f'/{file}', scenes_path + f'/{file}')
        elif 'material' in name:
            shutil.copyfile(cfg_path + f'/{file}', win_path + f'/{file}')
        elif 'support' in name or 'skill' in name or 'craft' in name or 'manpo' in name:
            shutil.copyfile(cfg_path + f'/{file}', support_path + f'/{file}')


def init_tmp_ini():
    wt_tmp_ini('run', 'flag', 'True')
    
    set_run_times = int(get_cfg('run', 'times'))
    set_run_materials = int(get_cfg('run', 'materials'))
    set_run_apple = get_cfg('run', 'apples').split(',')
    set_run_stones = int(get_cfg('run', 'stones'))
    if set_run_times >= 0:
        wt_tmp_ini('run', 'parm', 'times')
    elif set_run_materials >= 0:
        wt_tmp_ini('run', 'parm', 'materials')
    elif set_run_apple[0] in ['Au', 'Ag', 'Cu', 'Xu'] and int(set_run_apple[1]) >= 0:
        wt_tmp_ini('run', 'parm', 'apples')
    elif set_run_stones >= 0:
        wt_tmp_ini('run', 'parm', 'stones')
    else:
        sys_log('RUN PARAMETER ERROR !!! please check config.ini')
        toast('ERROR!!! EXIT SCRIPT!!!')
        exit()
        
    wt_tmp_ini('run', 'num', 0)

    wt_tmp_ini('run', 'total', 0)   # for total counter


    init_time = datetime.datetime.now().strftime('%y%m%d_%H%M%S%p')
    wt_tmp_ini('date', 'time', init_time)



def init_env():
    """
    初始化脚本的运行环境
    :return:
    """

    script_path = os.path.abspath(sys.argv[0])
    script_name = os.path.basename(sys.argv[0]).split('.')[0] + '.py'
    folder_path = script_path.replace(script_name, '')
    os.chdir(folder_path)

    clean_path(tmp_path)
    init_tmp_ini()
    init_log()
    
    rm_file_in_path(task_path, 'task')
    rm_file_in_path(scenes_path, 'task')

    rm_file_in_path(support_path, 'support')
    rm_file_in_path(support_path, 'skill')
    rm_file_in_path(support_path, 'craft')

    rm_file_in_path(win_path, 'material')
    
    cp_cfg_2_lib()
    # init_tmp_ini()


# def init_basement():
#     init_tmp_ini()
#     init_log()
    
    


