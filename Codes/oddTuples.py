# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 09:26:30 2017

@author: stanl
"""

def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    odd = ()
    for e in range(len(aTup)):
        if e%2 == 0:
            odd += (aTup[e],)
    return odd

print(oddTuples((20,21, 23, 24, 25, "a", "b")))