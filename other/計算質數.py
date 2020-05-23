# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#計算質數
maxnum = int(input('請輸入一個整數 計算小於這個整數的數是否為質數:'))
for num in range(1,maxnum+1):
    if num == 1: # 1 無定義
        pass
    elif num <= 3: # 2.3為質數
        print(num,'是質數')
    else:
        for i in range(2,int(num**0.5)+1): # 計算到開根號取整數
            if num % i == 0:
                print(num,'不是質數,','被',i,'整除.')
                break
            else :
                if i == int(num**0.5):        
                    print(num,'是質數')
                    break
                else:
                    continue