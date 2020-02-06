# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 12:40:39 2017

@author: Pool
"""
# 畢氏三元數
from numpy import sqrt
a = []
i = 0
nummax = int(input("求斜邊???以下的所有畢氏三元數(比例),輸入正整數"))
for side_a in range(5, nummax + 1):
    for side_b in range(1, int(side_a / sqrt(2)) + 1):
        x = (side_a**2 - side_b**2)
        if int(sqrt(x))**2 == x and (side_a / side_b) not in a:
            side_c = int(sqrt(x))
            a.append(side_a / side_b)
            i += 1
            print(i, ' 斜邊:', side_a, ' ', side_c, ' ', side_b)
        else:
            pass
a = []
i = 0
