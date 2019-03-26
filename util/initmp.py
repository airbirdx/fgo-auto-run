import os
import shutil
from util.scene import png_lst
from util.global0 import *


# 循环迭代删除路径文件夹下的所有文件
def clean(path):
    ls = os.listdir(path)
    for i in ls:
        c_path = os.path.join(path, i)
        # print(c_path)
        if os.path.isdir(c_path):
            clean(c_path)
        else:
            os.remove(c_path)


# 循环迭代删除路径文件夹下的所有含有目标字符串的文件
def clean_str_file(path, string):
    ls = os.listdir(path)
    for i in ls:
        c_path = os.path.join(path, i)
        # print(c_path)
        if os.path.isdir(c_path):
            clean_str_file(c_path, string)
        elif string in c_path:
            # print(c_path)
            os.remove(c_path)



# 创建空白的 tmp 文件
# support.txt -> 助战选择界面下记录助战从者、技能、以及礼装的属性列表
# global.txt  -> 脚本运行全局变量
def create(path):
    file_lst = [
        'support.txt',
        'global.txt'
    ]
    for file in file_lst:
        f = open(path + '/' + file, 'w')
        f.close()


# 将 cfg 中需要拷贝的文件，拷贝到想对应的路径下
# task , material , support , craft , skill
def cpcfg2lib():
    lst = png_lst(cfg_path)
    support = eval(rd_global('set_default_support'))

    # copy support to the support_path
    flg = [0] * 3
    # for comp in support:
    for i in range(3):
        comp = support[i]
        for file in lst:
            name, ext = os.path.splitext(file)
            if comp is not '' and comp in name:
                shutil.copyfile(cfg_path + f'/{file}', support_path + f'/{file}')
                flg[i] = 1
    # 根据图片调整设定的support选项
    for i in range(3):
        if not flg[i]:
            support[i] = ''
    wt_global('set_default_support', support)

    for file in lst:
        name, ext = os.path.splitext(file)
        if name == 'task':
            shutil.copyfile(cfg_path + f'/{file}', task_path + f'/{file}')
            shutil.copyfile(cfg_path + f'/{file}', scenes_path + f'/{file}')
        elif name == 'material':
            shutil.copyfile(cfg_path + f'/{file}', win_path + f'/{file}')


# 初始化, 清空 tmp 文件夹, 并创建临时 txt 文件
def init_tmp():
    clean(tmp_path)

    clean(task_path)

    clean_str_file(support_path, 'servant')
    clean_str_file(support_path, 'skill')
    clean_str_file(support_path, 'craft')
    clean_str_file(win_path, 'material')

    create(tmp_path)

    init_global()

    cpcfg2lib()




