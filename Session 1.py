# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 13:55:11 2020

@author: CGQU
"""

import sys
import numpy as np
from scipy.signal import find_peaks


sys.path.append('C:\\Users\CGQU\Desktop\cowi python course')

print(sys.path)

a = np.arange(-2, 2, 0.5)
b = np.arange(2,-2,-0.5)

c = np.append(a,b)

find_peaks(c)

