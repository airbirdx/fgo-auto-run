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


# 创建空白的 tmp 文件
# support.txt -> 助战选择界面下记录助战从者、技能、以及礼装的属性列表
#             -> 具体可以在 support 相关功能界面了解
# battle.txt  -> 记录战斗中当前回合数
# runtime.txt -> 记录当前 task 运行次数
# apple.txt   -> 记录已经消耗的苹果数目
def create(path):
    file_lst = [
        'support.txt',
        'global.txt'
        # 'runtime.txt',
        # 'apple.txt'
    ]
    for file in file_lst:
        f = open(path + '/' + file, 'w')
        # if file is not 'support.txt':
        # if file != 'support.txt':
        #     f.write('0')
        f.close()


def cpcfg2lib():
    lst = png_lst(cfg_path)
    svt_priority = eval(rd_global('set_servant_priority'))
    for file in lst:
        name, ext = os.path.splitext(file)
        if name == 'task':
            shutil.copyfile(cfg_path + f'/{file}', task_path + f'/{file}')
            shutil.copyfile(cfg_path + f'/{file}', scenes_path + f'/{file}')
        elif name == 'material':
            shutil.copyfile(cfg_path + f'/{file}', win_path + f'/{file}')


# 初始化, 清空 tmp 文件夹, 并创建临时 txt 文件
def init_tmp():
    cpcfg2lib()
    clean(tmp_path)
    create(tmp_path)
    init_global()


