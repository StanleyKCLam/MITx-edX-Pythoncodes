# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 09:02:52 2017

@author: stanl
"""

def is_list_permutation(L1, L2):
    '''
    L1 and L2: lists containing integers and strings
    Returns False if L1 and L2 are not permutations of each other. 
            If they are permutations of each other, returns a 
            tuple of 3 items in this order: 
            the element occurring most, how many times it occurs, and its type
    '''
    if L1 == [] and L2 == []: return (None, None, None)
    dL1 = {}
    for e in L1:
        g = dL1.get(e, 0)
        if g != 0: dL1[e] += 1
        else: dL1[e] = 1
    dL2 = {}
    for e in L2:
        g = dL2.get(e, 0)
        if g != 0: dL2[e] += 1
        else: dL2[e] = 1

    if dL1 != dL2: return False
    v=list(dL1.values())
    k=list(dL1.keys())
    return (k[v.index(max(v))], max(v), type(k[v.index(max(v))]))