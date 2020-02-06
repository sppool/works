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

ar = np.arange(100).reshape(10, 10)
df = pd.DataFrame(ar, index=list('ABCDEFGHIJ'), columns=list('1234567890'))
