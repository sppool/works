# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 00:52:09 2017

@author: Pool
"""


def trsf(in_wrd, lvl):
    wM = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    wm = 'abcdefghijklmnopqrstuvwxyz'
    wM_t = wM[lvl:] + wM[:lvl]
    wm_t = wm[lvl:] + wm[:lvl]
    out_wrd = ''
    for x in in_wrd:
        if x in wm:
            out_wrd = out_wrd + (wm_t[wm.index(x)])
        elif x in wM:
            out_wrd = out_wrd + (wM_t[wM.index(x)])
        else:
            out_wrd = out_wrd + x
    return out_wrd


'''
func up
'''
in_wrd = input('請輸入要轉譯的文字\n')
lvl = int(input('請輸入轉譯推移量\n'))
lvl = lvl % 26
out_wrd = trsf(in_wrd, lvl)
print(out_wrd)
