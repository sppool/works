# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
'''
完全數的計算  完全數: 一個數字的 "所有因數和sum" 為該數字
例如 6 = 1 + 2 + 3
Ans : [6,28,496,8128,33550336]
'''
num = int(input('尋找輸入數字以下的"完全數" : '))
for x in range(4, num + 1):
    in_list = [1]
    for i in range(2, (x // 2) + 1):
        if x % i == 0:
            in_list.append(i)
            if sum(in_list) == x and i == x // 2:
                print(x)
else:
    print('END')
