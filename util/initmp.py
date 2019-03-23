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
    support = eval(rd_global('set_default_support'))

    # copy support to the support_path
    support_wt = []
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
    # print(support)
    wt_global('set_default_support', support)

    # 如果 cfg 路径下没有礼装文件，就是说不筛选礼装的情况下
    if support[2] == '':
        wt_global('set_default_craft_manpo', 0)

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

    create(tmp_path)

    init_global()

    cpcfg2lib()




