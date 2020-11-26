import platform
import configparser
from util.default import *
from config import *
from util.log import *


def speed():
    return 1;


def toast(information):
    '''
    广播消息
    :param information:
    :return:
    '''
    string = '『 TOAST 』 ' + information
    sys_log(string)

    if platform.system() == 'Windows':
        from win10toast import ToastNotifier
        toaster = ToastNotifier()
        toaster.show_toast('fgo-auto-run', string, duration=10)

    elif platform.system() == 'Darwin':
        from subprocess import call
        cmd = 'display notification \"' + \
              string + '\" with title \"fgo-auto-run\"'
        call(['osascript', '-e', cmd])


def rd_ini(file, sec, key):
    """
    获取 ini 中内容
    :param file:
    :param sec:
    :param key:
    :return:
    """
    cf = configparser.ConfigParser()
    cf.read(file)
    secs = cf.sections()
    if sec not in secs:
        dbg_log('WARNING! dont have section:%s in file:%s' % (sec, file))
        return False
    options = cf.options(sec)
    if key not in options:
        dbg_log('WARNING! dont have key:%s in section:%s' % (key, sec))
        return False
    tmp = cf.get(sec, key)
    return tmp.split(';')[0].strip()


def wt_ini(file, sec, key, value):
    """
    写入内容到 ini 文件中
    :param file:
    :param sec:
    :param key:
    :param value:
    :return:
    """
    if not os.path.exists(file):
        f = open(file, 'w')
        f.close()
    cf = configparser.ConfigParser()
    cf.read(file, encoding="utf-8")
    secs = cf.sections()
    if sec not in secs:
        cf.add_section(sec)
    cf.set(sec, key, str(value))
    cf.write(open(file, "w", encoding="utf-8"))


def rd_tmp_ini(sec, key):
    """
    获取 tmp.ini 中内容
    :param sec:
    :param key:
    :return:
    """
    return rd_ini(f'{tmp_path}/tmp.ini', sec, key)




def rm_tmp_ini(sec=None, key=None):
    file = f'{tmp_path}/tmp.ini'
    if not os.path.exists(file):
        f = open(file, 'w')
        f.close()
    cf = configparser.ConfigParser()
    cf.read(file, encoding="utf-8")

    secs = cf.sections()
    dbg_log(secs)
    if sec is not None and key is not None:
        secs = cf.sections()
        if sec not in secs:
            dbg_log('WARNING! dont have section:%s in file:%s' % (sec, file))
            return False
        options = cf.options(sec)
        if key not in options:
            dbg_log('WARNING! dont have key:%s in section:%s' % (key, sec))
            return False
        cf.remove_option(sec, key)
    elif sec is not None and key is None:
        secs = cf.sections()
        if sec not in secs:
            dbg_log('WARNING! dont have section:%s in file:%s' % (sec, file))
            return False
        cf.remove_section(sec)
    cf.write(open(file, "w", encoding="utf-8"))
    
    


def wt_tmp_ini(sec, key, value):
    """
    获取 tmp.ini 中内容
    :param sec:
    :param key:
    :return:
    """
    wt_ini(f'{tmp_path}/tmp.ini', sec, key, value)


def get_cfg(sec, key):
    """
    获取 config.ini 中内容
    :param sec:
    :param key:
    :return:
    """
    return rd_ini('./config.ini', sec, key)


def demo_1():
    a = get_cfg('run', 'times')
    print(a, type(a))
    wt_tmp_ini('global', 'times', 1)
    a = rd_tmp_ini('global', 'times')
    print(a, type(a))


def ini_cfg_rd_demo():
    cf = configparser.ConfigParser()
    cf.read('./config.ini')  # 读取配置文件，如果写文件的绝对路径，就可以不用os模块
    
    secs = cf.sections()        # 获取文件中所有的section(一个配置文件中可以有多个配置，如数据库相关的配置，邮箱相关的配置，每个section由[]包裹，即[section])，并以列表的形式返回
    print(secs)
    for sec in secs:
        print(sec)
        options = cf.options(sec)  # 获取某个section名为Mysql-Database所对应的键
        print(options)
        items = cf.items(sec)  # 获取section名为Mysql-Database所对应的全部键值对
        print(items)
    
    tmp = cf.get("addap", "en_apple")  # 获取[apple]中type对应的值
    vlu = tmp.split(';')[0].strip() # 去除注释
    print(vlu)

