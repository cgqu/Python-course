# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 13:55:11 2020

@author: CGQU
"""

import sys
import numpy as np
from scipy.signal import find_peaks


def extract_interval(x, x_bounds):
    '''  
    Return the indices of `x` that are within `x_bounds` with both of values 
    `x_bounds` being inclusive.

    Parameters
    ----------
    x : 1D numpy array
        x-coordinates sorted in ascending order.
    x_bounds : tuple
        A two-element tuple defining the interval within which to extract x-indices.

    Returns
    -------
    1D numpy array
        Array of indices for `x`-values that reside within `x_bounds`.
'''
# =============================================================================
# Alternative way
#     # Create boolean array with values indicating if each element is in interval
#     a_bool = (x >= x_bounds[0]) & (x <= x_bounds[1])
#     
#     # Extract indices where condition is True into array
#     idx = np.where(a_bool)
#     
#     # Take first element since this is only 1D and return
#     return idx[0]
# =============================================================================
    
    z=0
    idx1=[]
    for i in x:
        if i >= x_bounds[0] and i<= x_bounds[1]:
            idx1.append(z)
        z += 1
    return idx1

x2 = np.arange(-0.6, 3.8, 0.4)
x_bounds2=(-0.3, 1.5)

x1 = np.arange(0, 10)
x_bounds1=(3, 7)

extract_interval(x2, x_bounds2)
extract_interval(x1, x_bounds1)
        
    



