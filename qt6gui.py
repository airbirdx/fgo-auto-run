# python lib
import sys
import os
import time
import shutil
import threading

# PySide6/PyQt6
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *

# ui Frame
import ui_fgo

# self function
from util.global0 import *
from util.scene import png_lst, folder_lst
from util.log import *
from util.initmp import init_env

##################################################
# pyside6-uic fgo.ui -o ui_fgo.py
##################################################

#TODO 卖从者，需要再加筛选的一些选项
#DONE 在获得战利品界面，把其保存下来到 log 文件夹下，这样方便后续统一获取材料图片


##################################################
### LOG FILE
global logfn_last_end_location, logfn_curr_end_location
logfn = f'{log_path}/log_{init_time}.log'
logfn_last_end_location = 0
logfn_curr_end_location = 0
##################################################
# 停止进程
import inspect
import ctypes
def _async_raise(tid, exctype):
    """raises the exception, performs cleanup if needed"""
    tid = ctypes.c_long(tid)
    if not inspect.isclass(exctype):
        exctype = type(exctype)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        # """if it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect"""
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")
def stop_thread(thread):
    _async_raise(thread.ident, SystemExit)
##################################################


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = ui_fgo.Ui_Form()
        self.ui.setupUi(self)

        self.get_combobox_items()
        self.ui.label_log_fn.setText(logfn)
        self.threading = None
        
        self.btn_group = [
            self.ui.pushButton_stop,

            self.ui.pushButton_adbconnect,
            self.ui.pushButton_screenshot,

            self.ui.pushButton_loadcfg,
            self.ui.pushButton_savecfg,

            self.ui.pushButton_autobattle,

            self.ui.pushButton_pypoint,
            self.ui.pushButton_craftexp,
            self.ui.pushButton_py_craft,
        ]

        self.timer=QTimer()
        self.timer.timeout.connect(self.auto_polling)#这个通过调用槽函数来刷新时间
        self.timer.start(1000)#每隔一秒刷新一次，这里设置为1000ms
        # self.timer.stop()

        self.ui.pushButton_stop.clicked.connect(lambda: self.actived_btn(self.ui.pushButton_stop))

        self.ui.pushButton_adbconnect.clicked.connect(lambda: self.actived_btn(self.ui.pushButton_adbconnect))
        self.ui.pushButton_screenshot.clicked.connect(lambda: self.actived_btn(self.ui.pushButton_screenshot))

        self.ui.pushButton_loadcfg.clicked.connect(lambda: self.actived_btn(self.ui.pushButton_loadcfg))
        self.ui.pushButton_savecfg.clicked.connect(lambda: self.actived_btn(self.ui.pushButton_savecfg))

        self.ui.pushButton_autobattle.clicked.connect(lambda: self.actived_btn(self.ui.pushButton_autobattle))

        self.ui.pushButton_pypoint.clicked.connect(lambda: self.actived_btn(self.ui.pushButton_pypoint))
        self.ui.pushButton_craftexp.clicked.connect(lambda: self.actived_btn(self.ui.pushButton_craftexp))
        self.ui.pushButton_py_craft.clicked.connect(lambda: self.actived_btn(self.ui.pushButton_py_craft))

        self.ui.pushButton_task_refresh.clicked.connect(self.get_combobox_items)

        self.ui.textBrowser_cfg.setFont(QtGui.QFont("SF Mono"))
        self.ui.textBrowser_log.setFont(QtGui.QFont("SF Mono", 12))
        
        self.load_cfg_from_file(file='./cfg/last.ini')
    

    def get_combobox_items(self):
        '''
        函数：
        自动读取当前数据库里的助战从者和礼装
        自动读取 task 列表
        '''

        # self.ui.comboBox_servant.clear()
        # self.ui.comboBox_servant.addItem('无')
        # path = './db/b-supports'
        # self.ui.comboBox_servant.setIconSize(QSize(50, 40))
        # folder_all = folder_lst(f'{path}')
        # for folder in folder_all:
        #     figure_list = png_lst(f'{path}/{folder}')
        #     for filename in figure_list:
        #         if 'support' in filename:
        #             self.ui.comboBox_servant.addItem(QIcon(f'{path}/{folder}/{filename}'), folder)
        #             break

        # self.ui.comboBox_craft.clear()
        # self.ui.comboBox_craft.addItem('无')
        # path = './db/c-crafts'
        # self.ui.comboBox_craft.setIconSize(QSize(80, 30))
        # figure_list = png_lst(f'{path}')
        # for filename in figure_list:
        #     self.ui.comboBox_craft.addItem(QIcon(f'{path}/{filename}'), filename)

        self.refresh_comboBox_servant()
        self.refresh_comboBox_craft()
        self.refresh_comboBox_task()


    def refresh_comboBox_servant(self):
        '''
        刷新助战从者
        '''
        flag = False
        if self.ui.comboBox_servant.count() != 0:
            flag = True
            current_text = self.ui.comboBox_servant.currentText()

        self.ui.comboBox_servant.clear()
        self.ui.comboBox_servant.addItem('无')
        path = './db/b-supports'
        self.ui.comboBox_servant.setIconSize(QSize(50, 40))
        folder_all = folder_lst(f'{path}')
        for folder in folder_all:
            figure_list = png_lst(f'{path}/{folder}')
            for filename in figure_list:
                if 'support' in filename:
                    self.ui.comboBox_servant.addItem(QIcon(f'{path}/{folder}/{filename}'), folder)
                    break
        
        if flag:
            self.ui.comboBox_servant.setCurrentText(current_text)


    def refresh_comboBox_craft(self):
        '''
        刷新助战礼装
        '''
        flag = False
        if self.ui.comboBox_craft.count() != 0:
            flag = True
            current_text = self.ui.comboBox_craft.currentText()

        self.ui.comboBox_craft.clear()
        self.ui.comboBox_craft.addItem('无')
        path = './db/c-crafts'
        self.ui.comboBox_craft.setIconSize(QSize(80, 30))
        figure_list = png_lst(f'{path}')
        for filename in figure_list:
            self.ui.comboBox_craft.addItem(QIcon(f'{path}/{filename}'), filename)
        
        if flag:
            self.ui.comboBox_craft.setCurrentText(current_text)


    def refresh_comboBox_task(self):
        '''
        刷新任务
        '''
        pass
        flag = False
        if self.ui.comboBox_run_task.count() != 0:
            flag = True
            current_text = self.ui.comboBox_run_task.currentText()

        self.ui.comboBox_run_task.clear()

        path = './db/a-tasks'
        # self.ui.comboBox_craft.clear()
        # self.ui.comboBox_craft.addItems(png_lst(path))
        self.ui.comboBox_run_task.setIconSize(QSize(80, 30))
        figure_list = png_lst(f'{path}')

        if os.path.exists('./cfg/task.png'):
            self.ui.comboBox_run_task.addItem(QIcon('./cfg/task.png'), '自定义')

        for filename in figure_list:
            self.ui.comboBox_run_task.addItem(QIcon(f'{path}/{filename}'), filename)

        if flag:
            self.ui.comboBox_run_task.setCurrentText(current_text)



    def get_current_cfg(self):
        '''
        函数：
        获取当前界面配置
        '''
        os.system('cp ./template.ini ./config.ini')
        pass
        
        # --- run setup
        if self.ui.comboBox_type.currentText() == '基础':
            wt_cfg('run', 'times', self.ui.lineEdit_run_times.text())

            wt_cfg('run', 'stones', -1)
            wt_cfg('run', 'materials', -1)
            wt_cfg('run', 'apples', '%s,%s' % ('Au', -1))
        elif self.ui.comboBox_type.currentText() == '材料':
            wt_cfg('run', 'materials', self.ui.lineEdit_run_times.text())

            wt_cfg('run', 'times', -1)
            wt_cfg('run', 'stones', -1)
            wt_cfg('run', 'apples', '%s,%s' % ('Au', -1))
        elif self.ui.comboBox_type.currentText() == '苹果':
            if self.ui.comboBox_subtype.currentText() == '金':
                apple_type = 'Au'
            elif self.ui.comboBox_subtype.currentText() == '银':
                apple_type = 'Ag'
            elif self.ui.comboBox_subtype.currentText() == '铜':
                apple_type = 'Cu'
            elif self.ui.comboBox_subtype.currentText() == '青铜':
                apple_type = 'Xu'
            apple_num = self.ui.lineEdit_run_times.text()
            wt_cfg('run', 'apples', '%s,%s' % (apple_type, apple_num))

            wt_cfg('run', 'times', -1)
            wt_cfg('run', 'materials', -1)
            wt_cfg('run', 'stones', -1)
        elif self.ui.comboBox_type.currentText() == '圣晶石':
            wt_cfg('run', 'stones', self.ui.lineEdit_run_times.text())

            wt_cfg('run', 'times', -1)
            wt_cfg('run', 'materials', -1)
            wt_cfg('run', 'apples', '%s,%s' % ('Au', -1))


        # --- addap
        if self.ui.radioButton_apple_on.isChecked():
            wt_cfg('addap', 'en_apple', 1)
        else:
            wt_cfg('addap', 'en_apple', 0)

        if self.ui.radioButton_stone_on.isChecked():
            wt_cfg('addap', 'en_stone', 1)
        else:
            wt_cfg('addap', 'en_stone', 0)

        # --- support
        rank = ''
        if self.ui.checkBox_rank_0.isChecked():
            rank += '0'
        if self.ui.checkBox_rank_1.isChecked():
            rank += '1'
        if self.ui.checkBox_rank_2.isChecked():
            rank += '2'
        if self.ui.checkBox_rank_3.isChecked():
            rank += '3'
        if self.ui.checkBox_rank_4.isChecked():
            rank += '4'
        if self.ui.checkBox_rank_5.isChecked():
            rank += '5'
        if self.ui.checkBox_rank_6.isChecked():
            rank += '6'
        if self.ui.checkBox_rank_7.isChecked():
            rank += '7'
        if self.ui.checkBox_rank_8.isChecked():
            rank += '8'
        if self.ui.checkBox_rank_9.isChecked():
            rank += '9'
        wt_cfg('support', 'rank', rank)

# [support]           ; option for support servant from friends
# mode    = 0         ; please see wiki for details

        if self.ui.checkBox_manpo.isChecked():
            wt_cfg('support', 'manpo', 1)
        else:
            wt_cfg('support', 'manpo', 0)

        # print(self.ui.comboBox_refresh.currentText())
        wt_cfg('support', 'refresh', self.ui.comboBox_refresh.currentText())

        # print(self.ui.comboBox_keepgo.currentText())
        if self.ui.comboBox_keepgo.currentText() == '继续':
            wt_cfg('support', 'keepgo', 1)
        else:
            wt_cfg('support', 'keepgo', 0)

        # --- skill
        wt_cfg('skill', 'value', self.ui.lineEdit_skill.text())
        wt_cfg('ultimate', 'value', self.ui.lineEdit_ultimate.text())

        wt_cfg('skill', 'unit', str.lower(self.ui.comboBox_skill_unit.currentText()))
        wt_cfg('ultimate', 'unit', str.lower(self.ui.comboBox_ultimate_unit.currentText()))

        # --- priority
        wt_cfg('priority', 'color', str.upper(self.ui.lineEdit_color.text()))
        chain = 0
        if self.ui.comboBox_chain_mode.currentText() == '无':
            chain = 0
        elif self.ui.comboBox_chain_mode.currentText() == '自动':
            chain = 3
        elif self.ui.comboBox_chain_mode.currentText() == '额外攻击':
            chain = 1
        elif self.ui.comboBox_chain_mode.currentText() == '色卡连携':
            chain = 2
        wt_cfg('priority', 'chain', chain)


        # ## XJBD
        if self.ui.checkBox_XJBD.isChecked():
            wt_cfg('skill', 'value', '')
            wt_cfg('ultimate', 'value', '')
            wt_cfg('priority', 'color', 'RBG')
            wt_cfg('priority', 'chain', 3)

        # ## support mode
        if self.ui.comboBox_craft.currentText() == '无' and self.ui.comboBox_servant.currentText() == '无':
            wt_cfg('support', 'mode', 0)
        else:
            wt_cfg('support', 'mode', 1)

        # f = open('./config.ini')
        # s = f.read()
        # f.close()
        s = ini_cfg_rd_demo()
        return s



    def uu_10s(self):
        for i in range(10):
            time.sleep(1)
            print(i)

    @QtCore.Slot()
    def actived_btn(self, btn):
        from func.case import pypoint
        from func.case import craftexp
        from func.case import py_craft
        from main import auto_battle
        from util.ats import screenshot
        

        self.disable_all_btn_except(btn=self.ui.pushButton_stop)
        
        if not btn == self.ui.pushButton_stop:
            init_env()

        if btn == self.ui.pushButton_autobattle:

            self.save_cfg_to_file('./cfg/last.ini')

            from util.initmp import rm_file_in_path
            rm_file_in_path(cfg_path, 'material')
            rm_file_in_path(cfg_path, 'support')
            rm_file_in_path(cfg_path, 'craft')
            rm_file_in_path(cfg_path, 'skill')
            # rm_file_in_path(cfg_path, 'task')

            if self.ui.comboBox_type.currentText() == '材料':
                path = './db/d-materials'
                file = f'{path}/%s' % self.ui.comboBox_subtype.currentText()
                os.system(f'cp {file} ./cfg/material.png')

            if self.ui.comboBox_servant.currentIndex() != 0:
                path = './db/b-supports'
                file = f'{path}/%s/*.png' % self.ui.comboBox_servant.currentText()
                os.system(f'cp {file} ./cfg')

            if self.ui.comboBox_craft.currentIndex() != 0:
                path = './db/c-crafts'
                file = f'{path}/%s' % self.ui.comboBox_craft.currentText()
                os.system(f'cp {file} ./cfg/craft.png')
            
            if self.ui.comboBox_run_task.count() != 0:
                if self.ui.comboBox_run_task.currentText() != '自定义':
                    path = './db/a-tasks'
                    file = f'{path}/%s' % self.ui.comboBox_run_task.currentText()
                    os.system(f'cp {file} ./cfg/task.png')
                
            init_env()   # re-do it after cp files
            # self.ui.textBrowser_cfg.setText(self.get_current_cfg())
            # QtWidgets.QApplication.processEvents()
            self.threading = threading.Thread(target=auto_battle, args=())
            # self.threading = threading.Thread(target=self.uu_10s, args=())
            self.threading.start()
        elif btn == self.ui.pushButton_screenshot:
            self.threading = threading.Thread(target=screenshot, args=())
            self.threading.start()
            # screenshot()
            # self.actived_btn(self.ui.pushButton_stop)
        elif btn == self.ui.pushButton_adbconnect:
            os.system('adb kill-server; sleep 1; adb start-server; sleep 2; adb connect 127.0.0.1')
            sys_log('adb connect done, please check')
        elif btn == self.ui.pushButton_pypoint:
            self.threading = threading.Thread(target=pypoint, args=())
            self.threading.start()
        elif btn == self.ui.pushButton_craftexp:
            self.threading = threading.Thread(target=craftexp, args=())
            self.threading.start()
        elif btn == self.ui.pushButton_py_craft:
            self.threading = threading.Thread(target=py_craft, args=())
            self.threading.start()
        elif btn == self.ui.pushButton_savecfg:
            self.save_cfg()
            self.actived_btn(self.ui.pushButton_stop)
        elif btn == self.ui.pushButton_loadcfg:
            self.load_cfg()
            self.actived_btn(self.ui.pushButton_stop)
        elif btn == self.ui.pushButton_stop:
            print('x')
            self.enable_all_btn_except(btn=self.ui.pushButton_stop)
            if type(self.threading) == threading.Thread:
                if self.threading.is_alive():
                    stop_thread(self.threading)
                self.threading = None
            else:
                print('just keep it...')



    




    def save_cfg_to_file(self, file='./cfg/last.ini'):
        '''
        保存 cfg 文件
        并显示出来
        '''
        cfg = self.get_current_cfg()
        self.ui.textBrowser_cfg.setText(cfg)

        os.system(f'cp ./config.ini ./qtconfig.ini')
        if self.ui.comboBox_type.currentText() == '材料':
            wt_ini('./qtconfig.ini', 'gui', 'material', self.ui.comboBox_subtype.currentText())
        if self.ui.comboBox_servant.currentText() != '无':
            wt_ini('./qtconfig.ini', 'gui', 'servant', self.ui.comboBox_servant.currentText())
        if self.ui.comboBox_craft.currentText() != '无':
            wt_ini('./qtconfig.ini', 'gui', 'craft', self.ui.comboBox_craft.currentText())

        wt_ini('./qtconfig.ini', 'gui', 'xjbd', int(self.ui.checkBox_XJBD.isChecked()))
        if self.ui.comboBox_run_task.currentIndex() != 0:
            wt_ini('./qtconfig.ini', 'gui', 'task', self.ui.comboBox_run_task.currentText())


        qt_gui_cfg = ini_cfg_rd_demo(file='./qtconfig.ini')

        if file.strip() != '':

            # if self.ui.comboBox_type.currentText() == '材料':
            #     os.mkdir('./cfg')

            f = open(file, 'w', encoding='utf8')
            f.write(qt_gui_cfg)
            f.close()
        
        os.system('rm ./qtconfig.ini')




    def save_cfg(self):
        '''
        窗口，保存 cfg 文件
        并显示出来
        '''
        file_path, _ = QFileDialog.getSaveFileName(
            self,  # 父窗口对象
            "save config",  # 标题
            r"./cfg",  # 起始目录
            "ini类型 (*.ini)"  # 选择类型过滤项，过滤内容在括号中
        )

        # print(repr(file_path))
        self.save_cfg_to_file(file_path)



    def load_cfg(self):
        '''
        窗口，选择 cfg 文件
        并显示出来
        '''
        file_path, _ = QFileDialog.getOpenFileName(
            self,  # 父窗口对象
            "open config",  # 标题
            r"./cfg",  # 起始目录
            "ini类型 (*.ini)"  # 选择类型过滤项，过滤内容在括号中
        )
        # print('>>>1', file_path)
        # print('>>>2', _)
        self.load_cfg_from_file(file=file_path)
        


    def load_cfg_from_file(self, file='./template.cfg'):
        '''
        加载 cfg 文件
        并反映到 GUI
        '''
        pass
        # file = './cfg/qq.ini'
        # print(file)

        if not os.path.exists(file):
            file = './template.ini'

        # sys_log(file)
        # os.system(f'cp {file} ./config.ini')    # 不可以有空格
        shutil.copyfile(f'{file}', './config.ini')   # 可以有空格
        # exit()
        # sys_log(file)

        apple_setting = get_cfg('run', 'apples').split(',')

        if int(get_cfg('run', 'times')) >= 0:
            # 0-基础，1-材料， 2-苹果， 3-圣晶石
            self.ui.comboBox_type.setCurrentIndex(0)
            self.ui.lineEdit_run_times.setText(get_cfg('run', 'times'))
        elif int(get_cfg('run', 'materials')) >= 0:
            self.ui.comboBox_type.setCurrentIndex(1)
            self.ui.comboBox_subtype.setCurrentText(get_cfg('gui', 'material'))
            self.ui.lineEdit_run_times.setText(get_cfg('run', 'materials'))
        elif int(apple_setting[-1]) >= 0:
        # elif int(get_cfg('run', 'apple')) > 0:
            self.ui.comboBox_type.setCurrentIndex(2)
            if apple_setting[0] == 'Cu':
                self.ui.comboBox_subtype.setCurrentText('铜')
            elif apple_setting[0] == 'Ag':
                self.ui.comboBox_subtype.setCurrentText('银')
            elif apple_setting[0] == 'Au':
                self.ui.comboBox_subtype.setCurrentText('金')
            elif apple_setting[0] == 'Xu':
                self.ui.comboBox_subtype.setCurrentText('青铜')
            self.ui.lineEdit_run_times.setText(apple_setting[-1])
        elif int(get_cfg('run', 'stones')) >= 0:
            self.ui.comboBox_type.setCurrentIndex(3)   
            self.ui.lineEdit_run_times.setText(get_cfg('run', 'stones'))

        if int(get_cfg('addap', 'en_apple')) > 0:
            self.ui.radioButton_apple_on.setChecked(True)
        else:
            self.ui.radioButton_apple_off.setChecked(True)

        if int(get_cfg('addap', 'en_stone')) > 0:
            self.ui.radioButton_stone_on.setChecked(True)
        else:
            self.ui.radioButton_stone_off.setChecked(True)

        support_rank = sorted(list(set(get_cfg('support', 'rank'))))
        for rank in range(10):
            # 0-9
            if str(rank) in support_rank:
                eval('self.ui.checkBox_rank_%s.setChecked(True)' % rank)
            else:
                eval('self.ui.checkBox_rank_%s.setChecked(False)' % rank)

        # if int(get_cfg('support', 'refresh')):
        self.ui.comboBox_refresh.setCurrentIndex(int(get_cfg('support', 'refresh')))
        if int(get_cfg('support', 'manpo')):
            self.ui.checkBox_manpo.setChecked(True)
        else:
            self.ui.checkBox_manpo.setChecked(False)
        
        if int(get_cfg('support', 'keepgo')):
            self.ui.comboBox_keepgo.setCurrentIndex(0)  # 继续
        else:
            self.ui.comboBox_keepgo.setCurrentIndex(1)  # 等待

        if get_cfg('gui', 'servant'):
            self.ui.comboBox_servant.setCurrentText(get_cfg('gui', 'servant'))
        
        if get_cfg('gui', 'craft'):
            self.ui.comboBox_craft.setCurrentText(get_cfg('gui', 'craft'))

        if get_cfg('gui', 'xjbd'):
            self.ui.checkBox_XJBD.setChecked(bool(int(get_cfg('gui', 'xjbd'))))

        if get_cfg('gui', 'task'):
            self.ui.comboBox_run_task.setCurrentText(get_cfg('gui', 'task'))

        self.ui.lineEdit_skill.setText(get_cfg('skill', 'value'))
        self.ui.comboBox_skill_unit.setCurrentText(str.title(get_cfg('skill', 'unit')))
        self.ui.lineEdit_ultimate.setText(get_cfg('ultimate', 'value'))
        self.ui.comboBox_ultimate_unit.setCurrentText(str.title(get_cfg('ultimate', 'unit')))
        # self.ui.lineEdit_ultimate.setText(get_cfg('ultimate', 'value'))

        self.ui.lineEdit_color.setText(get_cfg('priority', 'color'))
        chain = int(get_cfg('priority', 'chain'))
        if chain == 0:
            self.ui.comboBox_chain_mode.setCurrentText('无')
        elif chain == 3:
            self.ui.comboBox_chain_mode.setCurrentText('自动')
        elif chain == 1:
            self.ui.comboBox_chain_mode.setCurrentText('额外攻击')
        elif chain == 2:
            self.ui.comboBox_chain_mode.setCurrentText('色卡连携')

        cfg = self.get_current_cfg()
        self.ui.textBrowser_cfg.setText(cfg)


    @QtCore.Slot()
    def auto_polling(self):
        '''
        每秒刷新，打印 log 文件最新的内容
        槽函数：
        '''
        # time=QDateTime.currentDateTime()#获取当前时间
        # timedisplay=time.toString("yyyy-MM-dd hh:mm:ss dddd")#格式化一下时间
        # print(timedisplay)
        # self.lable.setText(timedisplay)
        global logfn_last_end_location, logfn_curr_end_location
        # print('last:', logfn_last_end_location)
        # print('curr:', logfn_curr_end_location)
        # print()
        f = open(logfn, 'r')
        f.seek(logfn_last_end_location, 0)
        s = f.read()
        logfn_curr_end_location = f.tell()
        if logfn_curr_end_location > logfn_last_end_location:
            if s[-1] == '\n':
                ss = s[:-1]
            else:
                ss = s
            self.ui.textBrowser_log.append(ss)
            logfn_last_end_location = logfn_curr_end_location
        f.close()


        if type(self.threading) == threading.Thread:
            if self.threading.is_alive():
                pass
                # print('still alive...')
            else:
                self.actived_btn(self.ui.pushButton_stop)
                toast('D-O-N-E')


    @QtCore.Slot()
    def cstm_ckebox_skill_xjbd(self):
        '''
        槽函数：
        是否勾选 XJBD
        '''
        if self.ui.checkBox_XJBD.isChecked():
            self.ui.lineEdit_skill.setDisabled(True)
            self.ui.lineEdit_ultimate.setDisabled(True)
            self.ui.comboBox_skill_unit.setDisabled(True)
            self.ui.comboBox_ultimate_unit.setDisabled(True)
        else:
            self.ui.lineEdit_skill.setEnabled(True)
            self.ui.lineEdit_ultimate.setEnabled(True)
            self.ui.comboBox_skill_unit.setEnabled(True)
            self.ui.comboBox_ultimate_unit.setEnabled(True)


    @QtCore.Slot()
    def cstm_cbobox_support_servant(self):
        '''
        槽函数：
        是否满破礼装
        '''
        if self.ui.comboBox_servant.currentText() != '无':
            # self.ui.checkBox_skill_310.setEnabled(True)
            pass
        else:
            self.ui.checkBox_skill_310.setDisabled(True)


    @QtCore.Slot()
    def cstm_cbobox_support_craft(self):
        '''
        槽函数：
        是否满破礼装
        '''
        if self.ui.comboBox_craft.currentText() != '无':
            self.ui.checkBox_manpo.setEnabled(True)
        else:
            self.ui.checkBox_manpo.setDisabled(True)

    @QtCore.Slot()
    def cstm_cbobox_run_param(self):
        '''
        槽函数：
        每次选中 [run] 参数时，切换子参数
        '''
        if self.ui.comboBox_type.currentText() in ['基础', '圣晶石']:
            self.ui.comboBox_subtype.setDisabled(True)
            self.ui.comboBox_subtype.clear()
        elif self.ui.comboBox_type.currentText() == '材料':
            self.ui.comboBox_subtype.clear()
            self.ui.comboBox_subtype.setIconSize(QSize(50, 50))
            path = './db/d-materials'
            material_lst = png_lst(f'{path}')
            for filename in material_lst:
                self.ui.comboBox_subtype.addItem(QIcon(f'./db/d-materials/{filename}'), filename)
            # self.ui.comboBox_subtype.addItems(material_lst)
            self.ui.comboBox_subtype.setEnabled(True)
        elif self.ui.comboBox_type.currentText() == '苹果':
            self.ui.comboBox_subtype.clear()
            self.ui.comboBox_subtype.setIconSize(QSize(50, 50))
            # self.ui.comboBox_subtype.addItems(['金', '银', '铜'])
            self.ui.comboBox_subtype.addItem(QIcon(f'./lib/addap/appleCu'), '铜')
            self.ui.comboBox_subtype.addItem(QIcon(f'./lib/addap/appleAg'), '银')
            self.ui.comboBox_subtype.addItem(QIcon(f'./lib/addap/appleAu'), '金')
            self.ui.comboBox_subtype.addItem(QIcon(f'./lib/addap/appleXu'), '青铜')
            self.ui.comboBox_subtype.setEnabled(True)



    def enable_all_btn_except(self, btn):
        for button in self.btn_group:
            button.setEnabled(True)
        
        btn.setDisabled(True)


    def disable_all_btn_except(self, btn):
        for button in self.btn_group:
            button.setDisabled(True)
        
        btn.setEnabled(True)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    widget = MyWidget()
    widget.show()
    app.exec()
    # print('uhiuqweiuhdkjahnksjn')
    if type(widget.threading) is threading.Thread:
        stop_thread(widget.threading)   ## just make sure
    # sys.exit(app.exec())
    sys.exit()