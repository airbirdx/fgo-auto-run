import os
from tkinter import *
import tkinter.messagebox as messagebox
from tkinter import ttk
from tkinter import filedialog

from util.global0 import *
from util.scene import png_lst

# class TkDemo():
#     def __init__(self):

#         self.init_parm()

#         # --------------------------------------------------------- #

#         self.master = Tk()
#         self.master.title('FGO-AUTO-RUN')

#         # --------------------------------------------------------- #
#         text = '基于 Python3 + ADB 的国服 FGO 脚本'
#         title = Label(self.master, text=text, font='15', bg='white', fg='red')
#         title.pack(fill=X)

#         # --------------------------------------------------------- #

#         # frame = Frame(self.master)
#         # frame.grid(row=0, col=0)

#         # self.name = StringVar()

#         self.run_mode = IntVar()
#         self.run_apple = 'X'
#         self.run_material = 'X'
#         self.run_parm = StringVar()

#         # self.support_servant = 'X'
#         # self.support_skill = 'X'
#         # self.support_craft = 'X'
#         # self.support_servant_rank = []
#         # self.support_craft_mode = 'X'
#         # self.support_refresh = StringVar()

#         # self.battle_skill = StringVar()
#         # self.battle_final = StringVar()
#         # self.battle_unit = IntVar()
#         # self.battle_chain = StringVar()
#         # self.battle_speed = '1'

#         # self.support_refresh_entry = []

#         # --------------------------------------------------------- #

#         self.fme_boundary()
#         self.fme_text('运行模式')
#         self.fme_runparm()

#         # self.fme_boundary(self.master)
#         # self.fme_text(self.master, '助战选择')
#         # self.fme_support0(self.master)
#         # self.fme_support1(self.master)
#         # self.fme_support2(self.master)

#         # self.fme_boundary(self.master)
#         # self.fme_text(self.master, '战斗选项')
#         # self.fme_battle0(self.master)  # 技能说明
#         # self.fme_battle1(self.master)  # 技能 + 宝具
#         # self.fme_battle2(self.master)  # 单位 + chain

#         # self.fme_boundary(self.master)
#         # self.fme_btnfunc(self.master)

#         # self.fme_boundary(self.master)

#         # --------------------------------------------------------- #

#         self.master.mainloop()

#     def get_battle_unit(self):
#         res = self.battle_unit.get()
#         self.parm3_unit = res
#         print('BATTLE UNIT :', res, type(res))

#     def get_battle_chain(self):
#         res = self.battle_chain.get()
#         self.parm3_chain = res
#         print('BATTLE CHAIN :', res, type(res))

#     def init_parm(self):

#         lst = png_lst('./db/d-materials/')
#         self.items_parm1_materials = []
#         for file in lst:
#             name, ext = os.path.splitext(file)
#             self.items_parm1_materials.append(name)
#         self.items_parm1_materials.sort()
#         # print(self.items_parm1_materials)
#         # exit()


#         # 菜单选项
#         self.items_parm1_mode = [
#             ('普通', 0),
#             ('材料', 1),
#             ('苹果', 2),
#         ]

#         self.items_parm1_apple = ['金苹果', '银苹果']

#         self.items_parm2_servant = ['跳过', '自定义', '孔明', '梅林']
#         self.items_parm2_skill = ['跳过', '自定义']
#         self.items_parm2_craft = ['跳过', '自定义', '午餐']
#         self.items_parm2_craft_mode = ['满破', '满破/未满破', '满破/未满破/无']

#         self.items_parm3_unit = [
#             ('ROUND', 0),
#             ('TURN', 1)
#         ]

#         # 1 运行模式
#         # 2 助战选择
#         # 3 战斗选择

#         # 默认值
#         self.parm1_mode = 0
#         self.parm1_apple = '银苹果'
#         self.parm1_times = 1

#         self.parm2_servant = '跳过'
#         self.parm2_skill = '跳过'
#         self.parm2_craft = '跳过'
#         self.parm2_craft_mode = '满破/未满破/无'
#         self.parm2_refresh = 1
#         self.parm2_rank = '0'

#         self.parm3_skill = ''
#         self.parm3_final = ''
#         self.parm3_unit = 'round'
#         self.parm3_chain = '1'
#         self.parm3_speed = 1


#     def load_config(self):
#         file_path = filedialog.askopenfilename(title='加载配置文件', filetypes=[('txt', '*.txt'), ('All Files', '*')])
#         print(file_path)  # 打印文件的路径
#         print('Load config done !')


#     def save_config(self):
#         pass
#         print('Save config done !')



#     def fme_runparm(self):
#         frame = Frame(self.master)
#         frame.pack(fill=X, side=TOP)

#         # 单选框
#         items = self.items_parm1_mode

#         for i in range(len(items)):
#             text, num = items[i]
#             # 改变前面的小圆点为按钮形式
#             button = Radiobutton(frame, text=text, variable=self.run_mode, value=num, indicatoron=False, command=self.get_run_mode)
#             button.grid(row=i, column=0)

#         self.add_gui_text(' → ', frame, row=2, col=2)

#         # 材料选择
#         items = self.items_parm1_materials
#         #################
#         # 创建下拉菜单
#         self.run_material = ttk.Combobox(frame, values=items, width=6, state='disable')
#         self.run_material.grid(row=1, column=3)
#         self.run_material.current(0)
#         self.run_material.bind("<<ComboboxSelected>>", self.get_run_material)

#         # 苹果选择
#         items = self.items_parm1_apple

#         # 创建下拉菜单
#         self.run_apple = ttk.Combobox(frame, values=items, width=6, state='disable')
#         self.run_apple.grid(row=2, column=3)
#         self.run_apple.current(1)
#         self.run_apple.bind("<<ComboboxSelected>>", self.get_run_apple)

#         for i in range(3):
#             self.add_gui_text(' | ', frame, row=i, col=4)

#         # 文本说明
#         self.add_gui_text('设定数字', frame, row=0, col=5)
#         self.add_gui_text('   ↓   ', frame, row=1, col=5)

#         # 输入框(Entry)，设定初始值为 1
#         parm = Entry(frame, textvariable=self.run_parm, width=6)
#         self.run_parm.set('1')
#         parm.grid(row=2, column=5)

#     def fme_support0(self, self.master):
#         frame = Frame(self.master)
#         frame.pack(fill=X)

#         self.add_gui_text('从者 ', frame, row=0, col=0)
#         items = self.items_parm2_servant
#         self.support_servant = ttk.Combobox(frame, values=items, width=6)
#         self.support_servant.grid(row=0, column=1)
#         self.support_servant.current(0)
#         self.support_servant.bind("<<ComboboxSelected>>", self.get_support_servant)

#         self.add_gui_text('→ 技能 ', frame, row=0, col=2)
#         items = self.items_parm2_skill
#         self.support_skill = ttk.Combobox(frame, values=items, width=6)
#         self.support_skill.grid(row=0, column=3)
#         self.support_skill.current(0)
#         self.support_skill.bind("<<ComboboxSelected>>", self.get_support_skill)

#         self.add_gui_text('→ 礼装 ', frame, row=0, col=4)
#         items = self.items_parm2_craft
#         self.support_craft = ttk.Combobox(frame, values=items, width=6)
#         self.support_craft.grid(row=0, column=5)
#         self.support_craft.current(0)
#         self.support_craft.bind("<<ComboboxSelected>>", self.get_support_craft)

#     def fme_support1(self, self.master):
#         frame = Frame(self.master)
#         frame.pack(fill=X)

#         text = '职阶  ↓              '
#         self.add_gui_text(text, frame, row=0, col=1)

#         text = '刷新次数'
#         self.add_gui_text(text, frame, row=0, col=2)
#         # 输入框(Entry)，设定初始值为 1
#         self.support_refresh_entry = Entry(frame, textvariable=self.support_refresh, width=4, state='disable')
#         self.support_refresh.set('1')
#         # self.support_refresh_entry['state'] = 'normal'
#         self.support_refresh_entry.grid(row=0, column=3)

#         self.add_gui_text('            模式 ', frame, row=0, col=4)
#         items = self.items_parm2_craft_mode
#         self.support_craft_mode = ttk.Combobox(frame, values=items, width=12, state='disable')
#         self.support_craft_mode.grid(row=0, column=5)
#         self.support_craft_mode.current(2)
#         self.support_craft_mode.bind("<<ComboboxSelected>>", self.get_support_craft_mode)  #########

#     def fme_support2(self, self.master):
#         pass
#         frame = Frame(self.master)
#         frame.pack(fill=X)

#         items = [
#             ('剑', '1'),
#             ('弓', '2'),
#             ('枪', '3'),
#             ('骑', '4'),
#             ('术', '5'),
#             ('杀', '6'),
#             ('狂', '7'),
#             ('全', '8'),
#             ('特殊', '9'),
#         ]

#         for i in range(len(items)):
#             rank = StringVar()
#             rank.set('0')
#             self.support_servant_rank.append(rank)

#         for i in range(len(items)):
#             name, index = items[i]
#             if i == len(items)-1:
#                 text = name
#             else:
#                 text = name + ' |'
#             # 产生选择按钮###################
#             ckbtn = Checkbutton(frame, text=text, variable=self.support_servant_rank[i], \
#                                 onvalue=index, offvalue='0', command=self.get_support_rank)
#             ckbtn.grid(row=0, column=i)

#     def fme_battle0(self, self.master):
#         frame = Frame(self.master)
#         frame.pack(fill=X)

#         item0 = [
#             '',
#             '|', '从者 1',
#             '|', '从者 2',
#             '|', '从者 3',
#             '|', '礼装',
#             '|', '换人',
#             '|', '敌人'
#         ]

#         item1 = [
#             '技能代码',
#             '|', 'a b c',
#             '|', 'i j k',
#             '|', 'o p q',
#             '|', 'x y z',
#             '|', 's',
#             '|', 'v'
#         ]

#         for i in range(len(item0)):
#             text = item0[i]
#             self.add_gui_text(text, frame, row=0, col=i)

#         for i in range(len(item1)):
#             text = item1[i]
#             self.add_gui_text(text, frame, row=1, col=i)

#     def fme_battle1(self, self.master):
#         frame = Frame(self.master)
#         frame.pack(fill=X)

#         text = '技能 →   '
#         self.add_gui_text(text, frame, row=0, col=1)
#         skill_entry = Entry(frame, textvariable=self.battle_skill, width=40)
#         self.battle_skill.set('')
#         skill_entry.grid(row=0, column=2)

#         text = '宝具 →   '
#         self.add_gui_text(text, frame, row=1, col=1)
#         skill_entry = Entry(frame, textvariable=self.battle_final, width=40)
#         self.battle_final.set('')
#         skill_entry.grid(row=1, column=2)

#     def fme_battle2(self, self.master):
#         frame = Frame(self.master)
#         frame.pack(fill=X)

#         text = '单位 '
#         self.add_gui_text(text, frame, row=0, col=1)

#         # 单选框
#         items = self.items_parm3_unit

#         for i in range(len(items)):
#             text, num = items[i]
#             # 改变前面的小圆点为按钮形式
#             button = Radiobutton(frame, text=text, variable=self.battle_unit, value=num, indicatoron=False,
#                                  command=self.get_battle_unit)
#             button.grid(row=0, column=i+2)

#         text = ' | '
#         self.add_gui_text(text, frame, row=0, col=4)

#         text = 'CHAIN'
#         self.battle_chain.set('1')
#         ckbtn = Checkbutton(frame, text=text, variable=self.battle_chain, \
#                             onvalue='1', offvalue='0', command=self.get_battle_chain)
#         ckbtn.grid(row=0, column=5)

#     def fme_btnfunc(self, self.master):
#         frame = Frame(self.master)
#         frame.pack(fill=X)

#         btn = Button(frame, text='< 单次截图 >', command=self.get_all_parm)
#         btn.grid(row=0, column=1)


#         text = '|'
#         self.add_gui_text(text, frame, row=0, col=2)

#         btn = Button(frame, text='< 加载配置 >', command=self.load_config)
#         btn.grid(row=0, column=3)

#         self.add_gui_text(text, frame, row=0, col=4)

#         btn = Button(frame, text='< 保存配置 >', command=self.save_config)
#         btn.grid(row=0, column=5)

#         self.add_gui_text(text, frame, row=0, col=6)

#         btn = Button(frame, text='< 开始运行 >', command=self.run_fgo_script)
#         btn.grid(row=0, column=7)

#     def run_fgo_script(self):
#         pass

#     # def fme_loadconfig(self, self.master):
#     #     frame = Frame(self.master)
#     #     frame.pack(fill=X)
#     #     dbg = Button(frame, text='加载配置', command=self.load_config)
#     #     dbg.grid(row=1, column=0)
#     #
#     # def fme_screenshoot(self, self.master):
#     #     frame = Frame(self.master)
#     #     frame.pack(fill=X)
#     #     dbg = Button(frame, text='单次截图', command=self.get_all_parm)
#     #     dbg.grid(row=1, column=0)

#     def fme_boundary(self):
#         frame = Frame(self.master)
#         frame.pack(fill=X)
#         text='- ' * 40
#         self.add_gui_text(text, frame, row=0, col=0)

#     def fme_text(self, text):
#         frame = Frame(self.master)
#         frame.pack(fill=X, side=TOP)
#         self.add_gui_text('「 %s 」' % text, frame, row=0, col=0, fg='red', sticky=W)

#     def add_gui_text(self, text, frame, row, col, fg=None, sticky=None):
#         label = Label(frame, text=text, fg=fg)
#         label.grid(row=row, column=col, sticky=sticky)

#     def get_run_material(self, event):
#         res = self.run_apple.get()
#         self.parm1_apple = res
#         print('RUN APPLE :', res, type(res))

#     def get_run_apple(self, event):
#         res = self.run_apple.get()
#         self.parm1_apple = res
#         print('RUN APPLE :', res, type(res))

#     def get_run_mode(self):
#         res = self.run_mode.get()
#         self.parm1_mode = res
#         print('RUN MODE :', res, type(res))

#         if res == 1:
#             self.run_material.state(['!disabled', 'selected'])
#         else:
#             self.run_material.state(['!selected', 'disabled'])

#         if res == 2:
#             self.run_apple.state(['!disabled', 'selected'])
#         else:
#             self.run_apple.state(['!selected', 'disabled'])



#     def get_battle_skill(self):
#         res = self.battle_skill.get()
#         self.parm3_skill = res
#         print('BATTLE SKILL :', res, type(res))

#     def get_battle_final(self):
#         res = self.battle_final.get()
#         self.parm3_final = res
#         print('BATTLE FINAL :', res, type(res))

#     def get_run_parm(self):
#         res = self.run_parm.get()
#         self.parm1_times = res
#         print('RUN PARM :', res, type(res))

#     def get_support_refresh(self):
#         res = self.support_refresh.get()
#         self.parm2_refresh = res
#         print('SUPPORT REFRESH :', res, type(res))

#     def change_status_parm2_refresh(self):
#         print('@!@!@!@')
#         if self.parm2_servant == '跳过' and self.parm2_skill == '跳过' and self.parm2_craft == '跳过':
#             self.support_refresh_entry['state'] = 'disable'
#         else:
#             self.support_refresh_entry['state'] = 'normal'

#     def get_support_servant(self, event):
#         res = self.support_servant.get()
#         self.parm2_servant = res
#         self.change_status_parm2_refresh()
#         print('SUPPORT SERVANT :', res, type(res))

#     def get_support_skill(self, event):
#         res = self.support_skill.get()
#         self.parm2_skill = res
#         self.change_status_parm2_refresh()
#         print('SUPPORT SKILL :', res, type(res))

#     def get_support_craft(self, event):
#         res = self.support_craft.get()
#         self.parm2_craft = res
#         self.change_status_parm2_refresh()

#         if res != '跳过':
#             self.support_craft_mode.state(['!disabled', 'selected'])
#         else:
#             self.support_craft_mode.state(['!selected', 'disabled'])

#         print('SUPPORT CRAFT :', res, type(res))

#     def get_support_craft_mode(self, event):
#         res = self.support_craft_mode.get()
#         self.parm2_craft_mode = res
#         print('SUPPORT CRAFT MODE :', res, type(res))

#     def get_support_rank(self):
#         res = ''
#         for rank in self.support_servant_rank:
#             res += rank.get()
#         self.parm2_rank = res
#         print('SUPPORT RANK :', res, type(res))

#     def get_all_parm(self):

#         self.get_run_parm()

#         self.get_support_refresh()

#         self.get_battle_skill()
#         self.get_battle_final()

#         print('----------------------------------------------------')

#         n = 25

#         print(f'%-{n}s' % 'self.parm1_mode', self.parm1_mode)
#         print(f'%-{n}s' % 'self.parm1_apple', self.parm1_apple)
#         print(f'%-{n}s' % 'self.parm1_times', self.parm1_times)

#         print('----------------------------------------------------')

#         print(f'%-{n}s' % 'self.parm2_servant', self.parm2_servant)
#         print(f'%-{n}s' % 'self.parm2_skill', self.parm2_skill)
#         print(f'%-{n}s' % 'self.parm2_craft', self.parm2_craft)
#         print(f'%-{n}s' % 'self.parm2_craft_mode', self.parm2_craft_mode)
#         print(f'%-{n}s' % 'self.parm2_refresh', self.parm2_refresh)
#         print(f'%-{n}s' % 'self.parm2_rank', self.parm2_rank)

#         print('----------------------------------------------------')

#         print(f'%-{n}s' % 'self.parm3_skill', self.parm3_skill)
#         print(f'%-{n}s' % 'self.parm3_final', self.parm3_final)
#         print(f'%-{n}s' % 'self.parm3_unit', self.parm3_unit)
#         print(f'%-{n}s' % 'self.parm3_chain', self.parm3_chain)
#         print(f'%-{n}s' % 'self.parm3_speed', self.parm3_speed)

#         print('----------------------------------------------------')


    
# # tkd = TkDemo()
# # tkd.get_all_parm()








# master = Tk()
# master.title('TITLE')

# fme = Frame(master)
# fme.grid(row=0, column=0, sticky=(E,W))


# fme_top = Frame(fme)
# # fme_top.pack(fill=X)
# fme_top.grid(row=0, column=0, columnspan=2)


# fme_left = Frame(fme)
# # fme_left.pack(side=LEFT)
# fme_left.grid(row=1, column=0)


# fme_right= Frame(fme)
# # fme_right.pack(side=RIGHT)
# fme_right.grid(row=1, column=1)


# fme_btm = Frame(fme)
# # fme_btm.pack(fill=X, side=BOTTOM)
# fme_btm.grid(row=2, column=0, columnspan=2)#, sticky=(E,W))

# # text = '基于 Python3 + ADB 的国服 FGO 脚本'
# # title = Label(fme_right, text=text, font='15', bg='white', fg='red')
# # title.pack(fill=X)



# text = '12324324546534'
# title = Label(fme_top, text=text, font='15', bg='white', fg='red')
# # title.pack(fill=X)
# title.grid(row=0, column=0, sticky=(E,W))


# text = '324324343'
# title = Label(fme_btm, text=text, font='15', bg='white', fg='red')
# title.grid(row=0, column=0, sticky=(E,W))
# # title.pack(fill=X)


# text = '111'
# title = Label(fme_left, text=text, font='15', bg='white', fg='red')
# title.grid(row=0, column=0)

# text = '222'
# title = Label(fme_left, text=text, font='15', bg='white', fg='red')
# title.grid(row=1, column=0)

# text = '333'
# title = Label(fme_left, text=text, font='15', bg='white', fg='red')
# title.grid(row=1, column=1)


# cfg = Text(fme_right, height = 10,width = 60)
# cfg.grid(row=0, column=0)
# # cfg.pack(fill=BOTH)
# cfg.insert(END,'python\n\n\n\n')
# cfg.insert(INSERT,'Tkinter')



# # frame = Frame(master)
# # frame.pack(fill=X)
# # text='- ' * 40
# # label = Label(frame, text=text)
# # label.grid(row=0, column=0, sticky=None)


# # # frame = Frame(root)
# # # frame.pack(fill=X)
# # # # skill_entry.grid(row=0, column=1, sticky=None)

# # xx=StringVar()
# # skill_entry = Entry(frame, textvariable=xx, width=40)
# # # self.battle_skill.set('')
# # skill_entry.grid(row=0, column=2)
# # # skill_entry.grid(row=0, column=1, sticky=None)







# mainloop()












# from tkinter import *
# from tkinter import ttk

# root = Tk()
# s = ttk.Style()
# s.configure('1.TFrame',background='red',width=16)
# s.configure('1.TButton',width=3)





# main = ttk.Frame(root,style='1.TFrame')
# ety = ttk.Entry(main,width=17)
# btn_add = ttk.Button(main,text=' + ',style='1.TButton')
# btn_ac = ttk.Button(main,text="AC",style='1.TButton')
# btn_del = ttk.Button(main,text="Del",style='1.TButton')
# btn_mol = ttk.Button(main,text=" % ",style="1.TButton")
# btn_div = ttk.Button(main,text=' ÷ ',style="1.TButton")
# btn_7 = ttk.Button(main,text=" 7 ",style='1.TButton')
# btn_8 = ttk.Button(main,text=" 8 ",style='1.TButton')
# btn_9 = ttk.Button(main,text=" 9 ",style="1.TButton")
# btn_times = ttk.Button(main,text=' × ',style="1.TButton")
# btn_4 = ttk.Button(main,text=" 4 ",style='1.TButton')
# btn_5 = ttk.Button(main,text=" 5 ",style='1.TButton')
# btn_6 = ttk.Button(main,text=" 6 ",style="1.TButton")
# btn_minus = ttk.Button(main,text=' - ',style="1.TButton")
# btn_1 = ttk.Button(main,text=" 1 ",style='1.TButton')
# btn_2 = ttk.Button(main,text=" 2 ",style='1.TButton')
# btn_3 = ttk.Button(main,text=" 3 ",style="1.TButton")
# btn_add = ttk.Button(main,text=' + ',style="1.TButton")
# btn_dot = ttk.Button(main,text=" . ", style="1.TButton")
# btn_0 = ttk.Button(main,text=" 0 ",style="1.TButton")
# btn_eq = ttk.Button(main,text=" + ",width=7)


# ety.grid(column=0,row=0,columnspan=4,sticky=(E,W))
# btn_ac.grid(row=1,column=0,sticky=(E,W))
# btn_del.grid(row=1,column=1,sticky=(E,W))
# btn_mol.grid(row=1,column=2,sticky=(E,W))
# btn_div.grid(row=1,column=3,sticky=(E,W))
# btn_7.grid(row=2,column=0,sticky=(E,W))
# btn_8.grid(row=2,column=1,sticky=(E,W))
# btn_9.grid(row=2,column=2,sticky=(E,W))
# btn_times.grid(row=2,column=3,sticky=(E,W))
# btn_4.grid(row=3,column=0,sticky=(E,W))
# btn_5.grid(row=3,column=1,sticky=(E,W))
# btn_6.grid(row=3,column=2,sticky=(E,W))
# btn_minus.grid(row=3,column=3,sticky=(E,W))
# btn_1.grid(row=4,column=0,sticky=(E,W))
# btn_2.grid(row=4,column=1,sticky=(E,W))
# btn_3.grid(row=4,column=2,sticky=(E,W))
# btn_add.grid(row=4,column=3,sticky=(E,W))
# btn_dot.grid(row=5,column=0,sticky=(E,W))
# btn_0.grid(row=5,column=1,sticky=(E,W))
# btn_eq.grid(row=5,column=2,columnspan=2,sticky=(E,W,N,S))
# main.grid(column=0,row=0,sticky=(E,W,N,S))
# main.columnconfigure(0,weight=1)
# main.columnconfigure(1,weight=1)
# main.columnconfigure(2,weight=1)
# main.columnconfigure(3,weight=1)
# root.rowconfigure(0,weight=1)
# root.columnconfigure(0,weight=1)

# root.mainloop()









from tkinter import *
from tkinter import ttk

root = Tk()
s = ttk.Style()
s.configure('1.TFrame',background='red',width=16)
# s.configure('1.TButton',width=8)
s.configure('1.TButton')
# s.configure('1.TLabel', bg='white', fg='red')
s.configure("1.TLabel", foreground="red", background='#000fff000', font=('Times', '24', 'bold italic'))






main = ttk.Frame(root,style='1.TFrame')
main.grid(column=0,row=0,sticky=(E,W,N,S))

# Main
fme_top = ttk.Frame(main,style='1.TFrame')
fme_lft = ttk.Frame(main,style='1.TFrame')
fme_rgt = ttk.Frame(main,style='1.TFrame')
fme_btm = ttk.Frame(main,style='1.TFrame')

fme_top.grid(row=0, column=0, columnspan=2)
fme_lft.grid(row=1, column=0)
fme_rgt.grid(row=1, column=1)
fme_btm.grid(row=2, column=0, columnspan=2)

# Left
fme_lft_run     = ttk.Frame(fme_lft,style='1.TFrame')
fme_lft_addap   = ttk.Frame(fme_lft,style='1.TFrame')
fme_lft_support = ttk.Frame(fme_lft,style='1.TFrame')
fme_lft_battle  = ttk.Frame(fme_lft,style='1.TFrame')

fme_lft_run.grid(row=0, column=0)
fme_lft_addap.grid(row=0, column=1)
fme_lft_support.grid(row=1, column=0, columnspan=2)
fme_lft_battle.grid(row=2, column=0, columnspan=2)

# Bottom
fme_btm_run = ttk.Frame(fme_btm,style='1.TFrame')
fme_btm_cfg = ttk.Frame(fme_btm,style='1.TFrame')
fme_btm_fun = ttk.Frame(fme_btm,style='1.TFrame')

fme_btm_run.grid(row=0, column=0)
fme_btm_cfg.grid(row=0, column=1)
fme_btm_fun.grid(row=0, column=2)


# --- Top
text = 'ENTER [TITLE] HERE' ###
title = Label(
    fme_top,
    text=text, 
    # style='1.TFrame',
    )
title.grid(row=0, column=0, sticky=(E,W,N,S))

# --- Right
cfg = Text(
    fme_rgt,
    # style='1.TButton',
    )
cfg.grid(row=0, column=0, sticky=(E,W,N,S))


# --- Bottom
btn_screenshoot = ttk.Button(
    fme_btm_run,
    text='截图',
    style='1.TButton',
    )

btn_run = ttk.Button(
    fme_btm_run,
    text='刷图',
    style='1.TButton',
    )

btn_adbconnect = ttk.Button(
    fme_btm_run,
    text='连接',
    style='1.TButton',
    )

btn_screenshoot.grid(row=0, column=0, sticky=(E,W,N,S))
btn_run.grid(row=1, column=0, sticky=(E,W,N,S))
btn_adbconnect.grid(row=0, column=2, sticky=(E,W,N,S))


btn_load = ttk.Button(
    fme_btm_cfg,
    text='加载配置',
    style='1.TButton',
    )

btn_save = ttk.Button(
    fme_btm_cfg,
    text='保存配置',
    style='1.TButton',
    )

btn_load.grid(row=0, column=0, sticky=(E,W,N,S))
btn_save.grid(row=1, column=0, sticky=(E,W,N,S))


btn_pypoint = ttk.Button(
    fme_btm_fun,
    text='友情点',
    style='1.TButton',
    )

btn_craft = ttk.Button(
    fme_btm_fun,
    text='搓丸子',
    style='1.TButton',
    )

btn_py_craft = ttk.Button(
    fme_btm_fun,
    text='友情点+搓丸子',
    style='1.TButton',
    )

btn_pypoint.grid(row=0, column=0, sticky=(E,W,N,S))
btn_craft.grid(row=1, column=0, sticky=(E,W,N,S))
btn_py_craft.grid(row=0, column=1, sticky=(E,W,N,S))




# --- LEFT

ety_title_times = ttk.Label(
    fme_lft_run,
    text='「 %s 」' % '攻略次数',
    style='1.TLabel',
)

ety_title_addap = ttk.Label(
    fme_lft_addap,
    text='「 %s 」' % '增加体力',
    # style='1.TLabel',
)

ety_title_support = ttk.Label(
    fme_lft_support,
    text='「 %s 」' % '助战选择',
    style='1.TLabel',
)

ety_title_skill = ttk.Label(
    fme_lft_battle,
    text='「 %s 」' % '技能宝具',
    style='1.TLabel',
)

fme_lft_run.columnconfigure(0,weight=1)
fme_lft_addap.columnconfigure(0,weight=1)
fme_lft_battle.columnconfigure(0,weight=1)
fme_lft_support.columnconfigure(0,weight=1)

fme_lft_run.rowconfigure(0,weight=1)
fme_lft_addap.rowconfigure(0,weight=1)
fme_lft_battle.rowconfigure(0,weight=1)
fme_lft_support.rowconfigure(0,weight=1)
# fme_lft_run.rowconfigure(0,weight=1)

ety_title_times.grid(row=0, column=0, sticky=W)
ety_title_addap.grid(row=0, column=0, sticky=W)
ety_title_support.grid(row=0, column=0, sticky=W)
ety_title_skill.grid(row=0, column=0, sticky=W)





root.mainloop()
