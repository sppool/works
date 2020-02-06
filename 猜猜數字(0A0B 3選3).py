# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 16:27:23 2017
@author: Pool
"""
'''
猜數字 猜四個數字
 A : 位置數字全對
 B : 數字對 位置不對
'''
import random  # 隨機模組
items = [x for x in range(10)]
random.shuffle(items)  # 洗牌函式
ans = items[0:4]  # 出題答案


def chk_A(ans_list, num_list):  # 計算幾個 A
    a, i = 0, 0
    for x in ans_list:
        if x == num_list[i]:
            a += 1
        i += 1
    return a


def chk_B(ans_list, num_list, a_int):  # 計算幾個 B
    return 8 - len(set(ans_list + num_list)) - a_int


def win():
    print('%5d' % gs_time, num, ans, '  4 A 0 B    U WIN')


gs_time = 0  # 猜題次數
while True:
    gs_time += 1
    random.shuffle(items)  # 電腦計算隨機猜題序列
    num = items[0:4]
    a = chk_A(ans, num)  # 計算幾個 A
    if a == 4:  # 4 A 勝利條件達成
        win()
        break
    else:  # 計算幾個 B
        b = chk_B(ans, num, a)
        if a + b == 0:
            print('%5d' % gs_time, num, ans, ' ',
                  a, 'A', b, 'B', ' Key guess ')
            break  # 確定items[0,4]都錯 0A0B
        else:
            print('%5d' % gs_time, num, ans, ' ', a, 'A', b, 'B')

kick = []  # 要剔除的數字 2/6
num4 = []  # 第4個數字
for y in items[4:10]:  # 剩餘的 6 個數字
    gs_time += 1
    num = items[0:3] + [y]
    a = chk_A(ans, num)  # 計算幾個 A
    b = chk_B(ans, num, a)  # 計算幾個 B
    if a + b == 0:  # 要剔除的數字 設為串列
        kick.append(y)  # 需要剔除的數字 "兩個"
        print('%5d' % gs_time, num, ans, ' ', a, 'A', b, 'B', ' Kick guess ')
    elif a == 1:  # 獲得第4個數字
        num4 = [y]  # 出現A 第四個數字
        print('%5d' % gs_time, num, ans, ' ', a, 'A', b, 'B', ' Num4 get ')
    else:
        print('%5d' % gs_time, num, ans, ' ', a, 'A', b, 'B')
    if len(num4) + len(kick) == 3:  # 取得剔除和第4個數字可跳出迴圈
        break

items = list(set(items[4:10]) - set(kick) - set(num4))
while True:
    gs_time += 1
    random.shuffle(items)  # 電腦計算隨機猜題序列
    num = items + num4  # 隨機三位  加上  num4
    a = chk_A(ans, num)  # 計算幾個 A
    if a == 4:  # 4 A 勝利條件達成
        win()
        break
    else:  # 計算幾個 B
        b = chk_B(ans, num, a)  # 計算幾個 B
        print('%5d' % gs_time, num, ans, ' ', a, 'A', b, 'B')
