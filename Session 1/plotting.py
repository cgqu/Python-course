# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 13:55:11 2020

@author: CGQU
"""

def annotate_points(points_to_annotate, **kwargs):
    '''
    Annotate points with corresponding text.
    
    Parameters
    ----------
    points_to_annoate : dict
        Dictionary with desired annotation text as keys and the (x, y)-
        coordinates of the annotation as values.
    **kwargs : keyword arguments
        Arguments to be forwarded to the ax.annotate call.    
    '''
    
    # Loop through x- and y-coordiantes of all points
    for text, (xp, yp) in points_to_annotate.items():

        # Annotate point
        ax.annotate(s=text, xy=(xp, yp), **kwargs)
        
    



