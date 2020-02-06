# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 17:43:36 2018

@author: Pool
"""

import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

pp = pd.read_csv('People107.csv')
pcol = list(pp.columns[7:])
pp['縣市'] = pp['區域別'].str[0:3]
pp['鄉鎮區'] = pp['區域別'].str[3:]
pp = pd.DataFrame(pp, columns=['縣市', '鄉鎮區', '村里'] + pcol)
pp = pp.set_index(['縣市', '鄉鎮區', '村里'])
pp.columns = pp.columns.str.split('歲').str[0]
pp = pp.T
pp.index = pp.index.astype(int)
pp.index.name = 'age'
pp['sex'] = ['M', 'F']*101
pp = pp.set_index(['sex', pp.index,])
pp = pp.sort_index()
pp = pp.unstack(level=0)
pp['decade'] = ((pp.index//10)*10).astype(str) + 's'
pp = pp.set_index(['decade', pp.index,])
pp = pp.T






# =============================================================================
# plt.plot(xx.values[:, 1], label='M')
# plt.plot(xx.values[:, 0], '--', label='F')
# plt.title('TW population')
# plt.xlim(0, 102)
# plt.ylim(0,)
# plt.ylabel('unmber')
# plt.xlabel('age')
# plt.legend()
# =============================================================================












