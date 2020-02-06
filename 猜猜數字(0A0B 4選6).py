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
gs_time = 0
while True:
    gs_time += 1
    random.shuffle(items)  # 電腦計算隨機猜題序列
    num = items[0:4]
    a, i = 0, 0
    for x in ans:  # 計算幾個 A
        if x == num[i]:
            a += 1
        i += 1
    if a == 4:  # 4 A 勝利條件達成
        print('%5d' % gs_time, num, ans, '  4 A 0 B         U WIN')
        break
    else:  # 計算幾個 B
        b = 8 - len(set(ans + num)) - a
        if a + b == 0:
            print('%5d' % gs_time, num, ans, ' ',
                  a, 'A', b, 'B', ' key guess ')
            break
        else:
            print('%5d' % gs_time, num, ans, ' ', a, 'A', b, 'B')
            continue
items = items[4:10]
while True:
    gs_time += 1
    random.shuffle(items)  # 電腦計算隨機猜題序列
    num = items[0:4]
    a, i = 0, 0
    for x in ans:  # 計算幾個 A
        if x == num[i]:
            a += 1
        i += 1
    if a == 4:  # 4 A 勝利條件達成
        print('%5d' % gs_time, num, ans, '  4 A 0 B         U WIN')
        break
    else:  # 計算幾個 B
        b = 8 - len(set(ans + num)) - a
        print('%5d' % gs_time, num, ans, ' ', a, 'A', b, 'B')
        continue
