# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 15:43:08 2017

@author: Pool
"""
'''
Enigma machine
3 / 5 roller (I II III IV V)
1 transform

use 'for loop' variable name : locals()['roll{0}'.format(x)]
import random
for x in range(1,6):
    locals()['roll{0}'.format(x)] = \
    ''.join(random.sample('ABCDEFGHIJKLMNOPQRSTUVWXYZ',26))
    ''.join(串列) 把'串列字元' 結合成'字串'
trsf(x) last roller
'''


def roll(i, j):  # i:轉盤編號 j:轉盤位置
    '''隨機產生五個轉盤'''
    roller = ['VSFETDKBYJIRNOXCHUMAGQPLWZ', 'FRDAQHNSCVJGIPTXYEWLBUZOKM',
              'HYCQWFDMKIEPRBUXSAZLOVJTNG', 'KXMUARVFBGNODTLHZEPYCSWJQI',
              'FMWSPZNGVDBXIQHCUTJAROKLEY']
    return roller[i - 1][j:] + roller[i - 1][:j]


def trsf(word, aa=0, bb=0, cc=0, i=1, j=2, k=3):
    code = []
    s = 0
    inout_pin = 'FTKAGHCJDZMVEIRLQPYONWXSBU'  # 進出電盤'字母位置列表'
    for x in word:
        if x in letter:
            a = (aa + s % 26) % 26  # 第一轉輸位置
            b = (bb + (s // 26) % 26) % 26
            c = (cc + (s // 676) % 26) % 26
            g1 = inout_pin.find(x)  # 進出電盤輸入位置
            g2 = roll(i, a).find(letter[g1])  # 第一轉輸入位置
            g3 = roll(j, b).find(letter[g2])  # 第二轉輸入位置
            g4 = roll(k, c).find(letter[g3])  # 第三轉輸入位置
            b1 = (25 - g4)  # 轉換 第三轉輸出位置
            b2 = letter.find(roll(k, c)[b1])  # 第二轉輸出位置
            b3 = letter.find(roll(j, b)[b2])  # 第一轉輸出位置
            b4 = letter.find(roll(i, a)[b3])  # 進出電盤輸出位置
            code.append(inout_pin[b4])  # 進出電盤輸出位置轉換字母
        else:
            code.append(x)
        s += 1
    code = ''.join(code)
    return code


'''
func up
'''
letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'  # 將隨意排列的子母轉成26個位置()
i = int(input('選用第一轉盤(1~5):'))
j = int(input('選用第二轉盤(1~5):'))
k = int(input('選用第三轉盤(1~5):'))
aa = letter.find(input('第一轉盤原始位置(A~Z):').upper())
bb = letter.find(input('第二轉盤原始位置(A~Z):').upper())
cc = letter.find(input('第三轉盤原始位置(A~Z):').upper())
word = input('請輸入明碼(大小寫皆可):').upper()  # 全部轉換大寫
code = trsf(word, aa, bb, cc, i, j, k)
print(code)

code_file = open('code.txt', 'a')
code_file.write('第一轉盤:' + '%d' % i + ' 原始位置:' + letter[aa] + '\n')
code_file.write('第二轉盤:' + '%d' % j + ' 原始位置:' + letter[bb] + '\n')
code_file.write('第三轉盤:' + '%d' % k + ' 原始位置:' + letter[cc] + '\n')
code_file.write('明碼:' + word + '\n')
code_file.write('暗碼:' + code + '\n')
code_file.close()
