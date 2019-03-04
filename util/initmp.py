import os
from util.default import tmp_path


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
        'battle.txt',
        'runtime.txt',
        'apple.txt'
    ]
    for file in file_lst:
        f = open(path + '/' + file, 'w')
        f.close()


# 初始化, 清空 tmp 文件夹, 并创建临时 txt 文件
def init_tmp():
    clean(tmp_path)
    create(tmp_path)


