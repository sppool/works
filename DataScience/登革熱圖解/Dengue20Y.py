# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 17:43:36 2018

@author: Pool
"""

import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import sklearn

# ar = np.arange(100).reshape(10,10)
# df = pd.DataFrame(ar, index=list('ABCDEFGHIJ'), columns=list('1234567890'))

den = pd.read_csv('Dengue_20y.csv')
lst = ['year', 'month', 'day']
for n in range(3):
    den[lst[n]] = den['發病日'].str.split('/').str[n]
    den[lst[n]] = den[lst[n]].astype(int)
    den['call_' + lst[n]] = den['通報日'].str.split('/').str[n]
    den['call_' + lst[n]] = den['call_' + lst[n]].astype(int)
del lst
den['發病日'] = pd.to_datetime(10000 * den.year + 100 * den.month + den.day,
   format='%Y%m%d')
den['通報日'] = pd.to_datetime(10000 * den.call_year + 100 * den.call_month + den.call_day,
   format='%Y%m%d')
den['是否境外移入'] = (den['是否境外移入'] == '是').astype(int)
d2 = den[['year', 'month', 'day', '發病日', '通報日', 'call_day','性別'
          , '年齡層', '居住縣市', '是否境外移入', '確定病例數']]
d2 = d2[d2['年齡層'].str.len() > 1]
d2 = d2[d2['性別'] != 'None']
d2 = d2[d2['確定病例數'] == 1]



# =============================================================================
# d2.pivot_table('確定病例數', index='year', columns='性別', aggfunc='count', margins=True, fill_value=0)
#
#
# births = pd.read_csv('data/births.csv')
#
# quartiles = np.percentile(births['births'], [25, 50, 75])
# mu = quartiles[1]
# sig = 0.74 * (quartiles[2] - quartiles[0])
#
# births = births.query('(births > @mu - 5 * @sig) & (births < @mu + 5 * @sig)')
#
# births['day'] = births['day'].astype(int)
#
# births.index = pd.to_datetime(10000 * births.year +
#                               100 * births.month +
#                               births.day, format='%Y%m%d')
#
# births['dayofweek'] = births.index.dayofweek
#
# births_by_date = births.pivot_table('births',
#                                     [births.index.month, births.index.day])
# =============================================================================
