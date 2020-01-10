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
#
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

def extrema_indices(x):
        ''' Return indices of all local extrema in `y`. 
    
    Parameters
    ----------
    y : 1D numpy array
        Array of values to search for local extrema.
        
    Returns
    -------
    1D numpy array
        Array of indices for local extrema.
    
    '''
# =============================================================================
# Alternative way  
#    
#     # Find local maxima
#     idx_max, _ = find_peaks(y)
#     
#     # Find local minima
#     idx_min, _ = find_peaks(-y)
#     
#     # Combine the two index arrays to one array and return it
#     return np.append(idx_max, idx_min)
# =============================================================================
    
    z=[] 
    w=[]
    z.append(x[find_peaks(x)[0]])
    w.append(x[find_peaks(-x)[0]])
    
    return np.append(z,w)

def arrays_todict(x_arr, y_arr):
    ''' 
    Return a dictionary with y-values in string form as keys 
    and x- and y-values as values. 
    
    Parameters
    ----------
    x_arr : 1D numpy array
        Array of x-values
    y_arr : 1D numpy array
        Array of y-values
        
    Returns
    -------
    dict
        Dictionary of the form 
        {'y1': (x1, y1), 'y2': (x2, y2), ..., 'yn': (xn, yn)}
    '''
    return {f'{y:.2f}': (x, y) for x, y in zip(x_arr, y_arr)}
