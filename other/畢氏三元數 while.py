# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 17:03:07 2017

@author: Pool
"""
# 畢氏三元數
from numpy import sqrt
nummax = int(input("求斜邊???以下的所有畢氏三元數,輸入正整數"))
side_a = 5
while side_a < nummax+1:
    side_b = 1
    while side_b < int(side_a/sqrt(2))+1:
        x = (side_a**2-side_b**2)
        if int(sqrt(x))**2 == x:
            side_c = int(sqrt(x))
            print('斜邊:',side_a,' ',side_c,' ',side_b)
        else:
            pass
        side_b += 1
    side_a += 1