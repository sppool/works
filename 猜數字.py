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
ans = items[0:4]
while True:
    num = input('猜數字? 請輸入4個不同的數字(0 ~ 9):')
    if num == 'ans':
        print('作弊模式 Ans:', ans)
        continue
    try:
        int(num)  # 輸入非數字!!
    except:
        print('輸入格式錯了')
        continue

    if len(num) != 4:  # 數量不為4
        print('輸入格式錯了')
        continue
    elif len(set(num)) != 4:  # 數字重複
        print('有數字重複了')
        continue
    '''
    以上判斷輸入格式是否正確
    以下猜數字回饋
    '''
    num = list(num)
    i = 0
    for numlist in num:  # 把str格式 改成int格式
        num[i] = int(numlist)
        i += 1
    a = 0
    for j, k in zip(ans, num):  # 計算幾個 A
        if j == k:
            a += 1
    if a == 4:  # 4 A 勝利條件達成
        print(num, '  4 A 0 B         U WIN')
        break
    else:  # 計算幾個 B
        b = 8 - len(set(ans + num)) - a
        print(num, ' ', a, 'A', b, 'B')
        continue
