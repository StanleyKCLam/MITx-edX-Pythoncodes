# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 23:24:41 2017

@author: stanl
"""

import math
def polysum(n,s):
    """
    n: the number of sides of polygon, +ve int
    s: the length of each side
    return: sum of the area and square of the perimeter,
            rounded to 4 decimal places.
    """
    area=(0.25*n*s**2)/math.tan(math.pi/n)
    perimeter=n*s
    return round(area+perimeter**2,4)