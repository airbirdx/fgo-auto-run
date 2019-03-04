def color_num(crd_attr):
    from config import crd_color_priority
    clr_read = crd_color_priority.upper()
    rgb = []
    for char in clr_read:
        if char == 'R':
            tmp = crd_attr[2]
        elif char == 'G':
            tmp = crd_attr[3]
        elif char == 'B':
            tmp = crd_attr[4]
        rgb.append(tmp)
    return rgb[0] * 100 + rgb[1] * 10 + rgb[2]




def servent_priority(crd_attr):
    # servent_priority = [1, 0, 2]
    # servant_priority = [1, 0, 2]
    n = crd_attr[1]
    from config import servant_priority
    for i in range(len(servant_priority)):
        if n == servant_priority[i]:
            return 5 - i  # 优先级 5>4>3>2>1...

    return -1  # 从者优先级一样

#

def turn_sorted(turn_attr):
    from config import crd_color_priority

    # turn_attr = turn_attribute()

    turn_sort = []

    # print('---------------------------------------')
    # for i in range(len(turn_attr)):
    #     print(curr_crd_attr)

    for i in range(len(turn_attr)):
        
        curr_crd_attr = turn_attr[i]

        if i == 0:
            turn_sort.append(curr_crd_attr)
        else:
            for j in range(len(turn_sort)):

                sort_crd_attr = turn_sort[j]

                if servent_priority(curr_crd_attr) > servent_priority(sort_crd_attr):
                    # 当前卡优先级高，插入到所比较排序的前面去，否则在最后append
                    print('A (i = crd)/ i = %d, j = %d' % (i, j))
                    turn_sort.insert(j, curr_crd_attr)
                    break
                elif servent_priority(curr_crd_attr) == servent_priority(sort_crd_attr):

                    if color_num(curr_crd_attr) >= color_num(sort_crd_attr):
                        print('B (i = crd)/ i = %d, j = %d' % (i, j))
                        turn_sort.insert(j, curr_crd_attr)
                        break
                    else:
                        print('C (i = crd)/ i = %d, j = %d' % (i, j))
                        turn_sort.insert(j + 1, curr_crd_attr)
                        break
                elif j == len(turn_sort) - 1:
                    print('D (i = crd)/ i = %d, j = %d' % (i, j))
                    turn_sort.append(curr_crd_attr)
                    break
                else:
                    pass

    print('*************************************')
    for i in range(len(turn_sort)):
        print(turn_sort[i])

    lst_normal = []
    lst_cantmove = []
    for i in range(len(turn_sort)):
        if turn_sort[i][5] == -2:
            lst_cantmove.append(turn_sort[i])
        else:
            lst_normal.append(turn_sort[i])

    lst_sorted = lst_normal + lst_cantmove

    print('---------------------------------------')
    for i in range(len(lst_sorted)):
        print(lst_sorted[i])

    # new add parts
    new_tap_lst = lst_sorted[n - 5 - 1::-1]  # 前n个逆序排列

    # tmp_new_tap_lst = lst_sorted[::-1] # 前n个逆序排列
    # new_tap_lst = tmp_new_tap_lst[:n]

    if n == 3:
        sum_r = 0
        for iii in range(3):
            sum_r += new_tap_lst[iii][2]
        if sum_r > 0 and new_tap_lst[0][2] == 0:

            if new_tap_lst[1][2] > 0:
                tmp_swap_lst = new_tap_lst.pop(1)
            else:  # new_tap_lst[2][2] > 0:
                tmp_swap_lst = new_tap_lst.pop(2)
            new_tap_lst.insert(0, tmp_swap_lst)

    for i in range(n):
        basic_tap(new_tap_lst[i][7], new_tap_lst[i][8])
        time.sleep(1.5)
