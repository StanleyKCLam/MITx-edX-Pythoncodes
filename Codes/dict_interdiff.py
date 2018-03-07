# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 09:49:40 2017

@author: stanl
"""

def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    r1 = {}
    r2 = {}
    for e in d1:
        if d2.get(e) != None:
            r1[e] = f(d1[e], d2[e])
#        v2 = d2.get(e, 0)
#        if v2 != 0:
#            r1[e] = f(d1[e], d2[e])
#            if 'int' not in str(type(d1[e])): a = 0
#            else: a = d1[e]
#            if 'int' not in str(type(d2[e])): b = 0
#            else: b = d2[e]
#            r1[e] = f(a, b)
#            r1[e] = d1[e] + v2
#            r1[e] = d1[e] > d2[e]
#    k = []
#    for e in d1:
#        if e not in d2: k = k + [e]
#    for e in d2:
#        if e not in d1: k = k + [e]
#    k.sort()
#    for e in k:
#        if d1.get(e, 0) == 0: r2[e] = d2[e]
#        else: r2[e] = d1[e]
    for e in d1:
        if e not in d2: r2[e] = d1[e]
    for e in d2:
        if e not in d1: r2[e] = d2[e]
    return (r1, r2)

def f(a, b):
    return a+b