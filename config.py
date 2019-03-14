# for debug use
dbg_shoot = 0
dbg_train = 0

# rotation if needed
default_rotation = 0   # range : 0/1/2/3, 1 for meizu phone

run_times = 5                            # How many times do you want to run
# run_materials = 5                        # How many materials do you want to get
# run_apples = ['Cu', 1]                   # How many apple do you want to eat, only support 'Au' and 'Ag' apple
# default_servant_priority = [0, 1, 3, 2]  # servant priority # high(left) -> low(right)
default_color_priority = 'RBG'           # R -> Blaster, G -> Quick, B -> Arts # high(left) -> low(right)
default_skill = '(1)bck(2)ijo(3)qy33'   # skill _seq & final # (n) means for turn n # abc / ijk / opq / xyz / s
default_final = '(1)axx(2)bxx(3)cxx'     # a/b/c for final card... BaoJu(Pinyin)
default_final_unit = 'turn'             # round(default) / turn
# 这里考虑一下 round 结束后怎么处理下 final 这个参数，不然下一次还会宝具，但是这里已经没有宝具了，skill最好同理
default_chain = 1
default_support = [   # example # default support information # servant # skill # craft
    '',         # meilin
    '',      # skill_310
    'event'      # bao shi weng
]
