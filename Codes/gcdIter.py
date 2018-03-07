# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 17:27:12 2017

@author: stanl
"""

def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if a>b:
        g=b
    else:
        g=a
    while g>1 and (a%g!=0 or b%g!=0):
            g-=1
    return g
print(gcdIter(9,48))
        
            